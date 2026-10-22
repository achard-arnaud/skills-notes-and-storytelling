# GitHub Actions/Webhooks / vault local — integration proposal

**Aucune de ces intégrations n'est actuellement livrée dans Decision Notes & Storytelling.** L'état cible sépare GitHub (code, contrats, revue), PC Obsidian (données de recherche et édition), moteur local (états de runs), et objets de sortie.

## Topologie recommandée

**V0 : local-first / pull-based** (le plus sûr) : React UI sur `127.0.0.1`, agent local explicitement installé sur le PC, dossier vault choisi par François, GitHub App token à privilèges limités, polling GitHub sur les runs connus ou `workflow_dispatch` autorisé. Aucun serveur public ni tunnel permanent; aucun secret GitHub/API dans le navigateur. Le service local est l'unique processus pouvant écrire dans le vault.

**V1 : cloud webhook optionnel** après pilote : GitHub → HTTPS ingress contrôlé avec vérification HMAC `X-Hub-Signature-256` sur octets bruts → journal de delivery `X-GitHub-Delivery` en contrainte UNIQUE → queue de commandes typées → worker → stockage artefact *non sensible*. L'agent PC **tire** les événements autorisés (outbound TLS) et vérifie session/tenant/consentement; le webhook ne monte jamais un chemin PC ni ne passe du raw texte non fiable comme commande shell. GitHub ne peut pas toucher un PC local à lui seul.

## Branch / PR / Actions lifecycle

1. `RUN_PLANNED` obtient `subject_slug, template_id, date, run_uuid` ; crée `research/YYYY-MM-DD/<subject>/<template>-<short-id>` sur base épinglée `dev` ou `main` selon politique explicite. En cas de même sujet, ID stable unique. Ne réutilise jamais une ancienne branche comme base.
2. Un ticket/run stocke `remote_repo, branch, base_sha, head_sha, event_id, actor, permissions`.
3. Chaque étape peut publier **uniquement** manifest de recherche anonymisé/autorisations+résultats approuvés; raw secrets, contacts, données clients et caches ne sont jamais poussés par défaut.
4. `workflow_dispatch` ou PR déclenche tests de schéma, épistémologie, absence de fuite, NRT ciblées, renderer layout si changement document.
5. Distinction `branch_created`, `commit_saved`, `PR_opened`, `CI_passed`, `candidate_approved`, `merged`, `delivered`. Aucun statut inféré de la seule existence d'un artefact. Merge sous intervention humaine et seulement après consentement / autorisations.
6. Suppression/archivage branche uniquement avec HEAD attendu (optimistic locking), merge vérifié et lien permanent vers manifest; pas de suppression automatique d'une branche non intégrée.
7. Retenter `create branch` ou `dispatch` avec idempotency key; si collision, comparer HEAD et l'objet attendu, sinon demander arbitrage.

### Sécurité GitHub

- Validation HMAC-SHA256 constant-time, corps de requête non parsé avant validation; parse seulement événements allowlist : `push, pull_request, workflow_run, check_suite, issue_comment` si chacun a un usage justifié.
- `X-GitHub-Delivery` UNIQUE + hash corps + repo ID + SHA; replay = no-op, mismatch même ID = alerte. Webhooks délivrés hors ordre : état monotone par événements + réconciliation REST.
- Utiliser GitHub App installation tokens expiring et permissions minimales sur repos explicitement allowlistés; secrets exclusivement côté service/secret store, jamais logs/token dans issue/CI artifact.
- `issue_comment` est non fiable : seul un bot/acteur allowlisté peut émettre des actions structurées pré-approuvées; pas d'exécution arbitraire sous `pull_request_target` d'une PR non fiable.
- Receipts de chaque action `requested→attempted→remote-confirmed|failed`; `200` webhook ≠ merge réussi. CI Actions `contents:read` par défaut, écriture dans un job dédié sous approval.
- Test adversarial : signature absente/fausse, replay, ordre inverse, PR hors repo, chemin vault traversal, action non autorisée, token expiré, conflit de HEAD et event/branch duplicate.

## Obsidian : permissions et synchronisation

- Configuration **sur PC**, non sur Git : chemin vault, dossier cible, consentement de lecture/écriture, liste des dossiers autorisés. Normaliser et vérifier realpath, symlinks, Windows UNC, traversée `../`, verrou exclusif et atomic rename.
- L'agent écrit `.md` à frontmatter schema validé, liens Obsidian (Wikilinks) vers source/claim/question/run, et un `manifest` avec hash. La projection graph-light est régénérée; Obsidian n'est pas une base de vérité externe vérifiée.
- Si utilisateur modifie une note : compare `base_hash`, diff, provenance; conflit ⇒ `REVIEW_REQUIRED`, ne jamais last-write-wins. Idempotence par `source_id/claim_id`.
- Sauvegarde locale : snapshots versionnés, journal d'événements, politique de rétention et export/restore; rollback ne perd pas notes créées entre temps. Vérification du hash des *octets* capturés et statut `capture_kind`, pas hash d'une URL.
- Reprise entre conversations LLM : importer uniquement checkpoint, sous-graphe top claims et stage actifs, jamais toute la vault; secrets/raw captures sont des données, non instructions.
- Scope multi-comptes : future isolation par `workspace_id`, pas répertoires partagés ni autorisation fondée sur l'URL transmise par client.

## Contrat Search et Deepsearch

- Fingerprint : normalized entity identifier, company aliases ou produit + éditeur, analysis dimensions, question, cutoff/date d'observation, source classes, language et store snapshot. Lookup exact puis similarité candidate bornée/validée.
- `REUSE`: sources fraîches/qualifiées, référence hash, aucune réaffirmation de faits temporaires.
- `REFRESH`: sélectionner uniquement sources périmées ou questions affectées, conserver anciennes assertions avec superseded/contradicts.
- `NEW`: création d'un nouveau périmètre d'étude sans dupliquer un sujet par faute d'alias.
- `SEARCH`: requêtes pertinentes / corroboration, arrêt si questions couvertes.
- `DEEPSEARCH`: decomposer en sous-questions, résultats multi-fournisseurs, counter-evidence, quotas `source_limit, token_limit, concurrency_limit, wall_budget`, budget pré-approuvé, checkpoints périodiques. Aucune prétention d'exhaustivité sans couverture mesurée.
- Le backend exploite des connecteurs autorisés par rôle; refus explicite si une source requiert une authentification non disponible. Aucune collecte opaque de données privées.

## Livrables minimum d'un test V1

Fixture synthétique : annonce d'une entreprise fictive, une fiche produit fictive, une source périmée, une contradiction, une PR de deux commits, trois webhook deliveries dont un doublon, modification vault concurrente, workflow CI vert mais QA sémantique `needs_human`. Tous les événements et erreurs produisent un reçu traçable.
