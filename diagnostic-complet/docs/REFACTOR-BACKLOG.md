# Registre des tickets de refactor — séparation build / run et terminologie

Document public : méthode et état du code uniquement. Aucun contenu de corpus. Chaque ticket a une preuve de clôture mécanique (test) ou un statut humain explicite. Convention : `RF-nn`, règles dans `AGENTS.md` (M1–M11, P5).

## Clôturés dans ce changement (9 novembre 2026)

| ID | Constat initial | Action | Preuve de clôture |
|---|---|---|---|
| RF-01 | `kb.py` embarquait `ENTITY_LEXICON` et `PILLAR_LEXICON` (GreenYellow, VisioSense, PV, onduleur…) | Lexiques déplacés dans `profiles/greenyellow.profile.json` (identiques, version 1.0.0). `kb.py` lit un profil passé en argument, défaut `neutral` | `test_golden_greenyellow_classification_is_unchanged` ; `test_core_code_contains_no_run_vocabulary` |
| RF-02 | `project.py` avait `DEFAULT_NAMESPACE = knowledge/business/greenyellow` | Défaut supprimé. Namespace exigé par argument ou par `projection.namespace` du profil | `test_projection_requires_a_namespace` ; tests `test_project.py` sur `knowledge/business/fixture-run` |
| RF-03 | Trois vocabulaires de statut sans correspondance (claims, `evidence_basis`, `knowledge_status`) | `ontology/terminology.json` unique. `evidence_basis` retirée de l'ontologie (facette jamais produite). Ontologie 0.5.0 | `TerminologyTests` ; `ontology.validate_referential` refuse toute divergence |
| RF-04 | `PRIMARY_KINDS` incluait `primary_vendor` et `primary_corporate` : une auto-déclaration pouvait valider un `verified_fact` | Tier explicite, sinon mapping legacy (`primary_vendor`→T2, `primary_corporate`→T1). Seuls T3 et T4 sont éligibles, plus `qualified: true` | `VerifiedTierRegressionTests` |
| RF-05 | Aucun second profil : la généricité n'était pas prouvée | `profiles/synthetic-logistics.profile.json` (fictif) ; isolation et exclusivité des termes testées | `test_synthetic_profile_is_isolated_from_greenyellow` |

## Ouverts

| ID | Sujet | Statut | Décideur | Note |
|---|---|---|---|---|
| RF-06 | Migrer les index KB sans `profile_id` (produits avant ce changement) vers un profil déclaré | open | coordinateur | Refus explicite aujourd'hui. Le corpus privé n'est pas présent dans ce conteneur |
| RF-07 | Projection Graph1 : passer `--profile` ou `--namespace` explicitement à chaque lot ; ajouter `profile_id` au MANIFEST | open | coordinateur + rédacteur business | Lien avec le lot R2-14 déjà publié : ne rien rejouer sans reçu |
| RF-08 | Entité `microsoft` dans le profil GreenYellow | closed | D33 | Conservée : la suite Microsoft (Copilot et Copilot Studio, Power Platform, Fabric, Azure) couvre les gammes IA et données de l'intégration GreenYellow. Sous-produits au lexique = version 1.1.0 + migration RF-06, à décider à part |
| RF-09 | 9 faux positifs `directive` dans le corpus (phrases descriptives à l'infinitif, « il faut ») | open, HITL | humain | Corriger l'heuristique de `kb.py` demande une nouvelle version de lexique et un reçu |
| RF-10 | Un `attributed_claim` n'exige pas aujourd'hui de source de tier T1 à T3 | open | — | Règle à ajouter dans `runtime.py` avec fixture de non-régression |
| RF-11 | Skill `reinforce-kb-loopback` : intégration dans le dépôt | closed dans le dépôt (D31) ; installation personnelle restante | humain | Versionnée dans `operational-skills/`, copies `.claude/` et `.agents/`, dépendances mappées (`dependencies.json`), test d'identité |
| RF-12 | Calibrer la cadence HIL (D18) | open, backlog | humain | Plusieurs cycles mesurés requis ; aucun seuil avant `decision_ref` |
| RF-13 | Revue sémantique du catalogue des 12 relations avant tout passage sur `main` | open | humain | L'écart 8 → 12 est clos : `contracts/claims-graph-light.schema.json` déclare les 12 relations depuis `d29882b`. Reste à valider le sens de chacune, surtout `causes` (preuve obligatoire) et `answers`, `enables`. Voir issue #272 |
| RF-14 | Migrer les études JSON existantes de `kind` vers `tier` | open, basse priorité | — | Le mapping legacy garde la compatibilité ; la migration est cosmétique |
| RF-15 | Plafond d'une modification de type par cycle | closed | D32 | Plafond retiré du contrat, de `loopback.py` et de `reinforce.py`. Preuves : `test_no_cap_on_candidates_and_repair_loop_still_bounded`, `test_every_proposal_is_listed_and_none_is_applied` |
| RF-16 | Évaluation de la skill : le groupe témoin « sans skill » et le jugement LLM n'ont pas été exécutés ; les cas de refus sont vérifiés sur des réponses rédigées pour le test | open | humain | Relancer avec un juge indépendant avant de déclarer la skill validée |
| RF-17 | Chaque proposition doit porter la liste explicite de ses nœuds et arêtes visés (aujourd'hui seulement un échantillon dans `observation`) | open | — | Nécessaire pour regrouper par emplacement, comme demandé ; à faire dans `loopback.py` avec test |
| RF-18 | Emplacement du profil GreenYellow : `RUN-BUILD-BOUNDARY.md` range la connaissance sur l'entreprise côté run, alors que `profiles/greenyellow.profile.json` est dans le dépôt public | open | humain | Options : garder (vocabulaire public, faible risque) ou déplacer vers le namespace Graph1 et ne garder dans le dépôt que le schéma. Décision à prendre avant tout nouveau lot |
| RF-19 | PR #285 (dev → main, présentée comme brouillon de promotion) a été mergée dans `main` (commit `92e9fc9`) | open | humain | Aucun agent de ce dépôt n'a mergé cette PR. À confirmer, ou à annuler si ce n'était pas voulu |
| RF-20 | `origin/dev` a été réécrit de force (reflog : `forced-update` de `1713ca4` vers `ca67c1e`), ce qui a retiré deux commits de ce travail | closed (récupéré) | — | Récupéré par rebase sans force puis fast-forward. Règle : fetch et rebase avant chaque commit. Preuve : `origin/dev` contient les commits, 286 tests OK |
| RF-21 | Une fusion `main → dev` (01384d3) a remplacé le AGENTS.md riche de `dev` par une version plus lourde, perdant les mandats éditoriaux | closed (restauré) | D34 | Restauré et protégé par `test_agents_keeps_its_mandates` |
