# Diagnostic de passation — stratégie bootstrap et backlog

Document public, sans corpus ni contenu d'entretien. Date de référence : 7 novembre 2026. Tête vérifiée : `dev` = `d29882b`, `main` = `74a6354` (commit de base, inchangé).

## 1. Stratégie bootstrap telle qu'elle a été exécutée

| Principe | Mise en œuvre observée |
|---|---|
| Isolement | Sous-projet `diagnostic-complet/` ; aucun changement de template ou de mode global ; aucune promotion `main`. |
| Découpage | 4 phases, 8 epics, 72 microtickets (DC-001 à DC-072), 5 sprints. Chaque ticket a entrées, sorties, acceptation, dépendances, `write_scope` et condition d'arrêt. |
| Traçabilité | `board.json` (72/72 `verified`), un reçu JSON par ticket, `coverage.json`, issues GitHub liées. |
| Reprise | Capsule `runs/bootstrap/RESUME.md`, paquet ciblé `context.py`, checkpoint avec empreintes SHA-256 et contrôle de fraîcheur. |
| Intégration | Commits `[skip ci]`, avance fast-forward de `dev`, sans force, sans PR ni `workflow_dispatch`. |
| Réparation | Deux corrections maximum par cause, puis `BLOCKED` avec travail indépendant. |
| Preuve de reprise | Revue indépendante (DC-036) : la capsule et le paquet suffisent à identifier la prochaine action, les interdits et les gates humains. |

Cette stratégie est solide pour un prototype : chaque affirmation pointe vers un fichier, un commit ou un test, et les limites sont écrites dans `docs/LIMITS.md`.

## 2. Diagnostic

### Forces

- **Séparation des étapes** conforme à `AGENTS.md` : recherche, preuve, scaffold, narration et rendu restent des modules distincts (`context.py`, `runtime.py`, `writing.py`, `render.py`).
- **Aucun fait promu automatiquement** : l'import produit des `supplied_claim` ; les tests vérifient qu'une relation ou un fait qualifié exige une revue déclarée.
- **Reprise testée**, pas seulement décrite.
- **Vérifications locales reproductibles** : 105 tests (18 contexte, 21 KB, 17 loopback, 4 catalogue de relations, 9 rendu, 20 runtime, 16 écriture), tous verts à `d29882b`.

### Faiblesses et écarts mesurés

1. **Board R2 désynchronisé.** `runs/r2/board.json` marque les 16 tickets `planned`, alors que `writing.py`, `loopback.py`, `kb.py` et le catalogue de relations sont livrés et testés dans `d29882b`. Aucun reçu R2 n'existe. Le board ne reflète pas l'état du code. Détail des statuts proposés : `runs/handover/R2-RECONCILIATION.md`.
2. **La CI n'a jamais validé le code de passation.** Les commits `40d7e5f` et `d29882b` portent `[skip ci]`, et aucun run n'a pour head ces SHA (vérifié via l'API Actions). Le « vert » de `dev` est donc uniquement local. Le gate local équivalent est documenté dans `docs/LOCAL-GATE.md` et a été exécuté.
3. **Changement de contrat racine sans CI** (`d29882b`). `contracts/claims-graph-light.schema.json` passe de 8 à 12 valeurs d'`edges.type`, `contracts/relation-types.json` est ajouté, `references/workflow.md` et `scripts/validate_contracts.py` sont modifiés. L'ajout est compatible : le seul consommateur est le validateur et ses tests. Mais le fichier schéma a été entièrement reformaté (réindentation), ce qui gonfle la revue et masque le delta réel. Audit : `runs/handover/CONTRACT-AUDIT.md`.
4. **Une empreinte de reçu est périmée, pour une raison légitime.** 71 empreintes sur 72 concordent. DC-002 pointe `AGENTS.md`, modifié par le mandat R2. Conformément à `R2-SCOPE.md`, le reçu ancien n'est pas réécrit ; le delta est tracé dans `runs/handover/freshness.json`.
5. **Chiffres de tests datés.** `DELIVERY.md` annonce 47 tests ; l'état actuel est 105. Tout chiffre de test doit désormais être daté par un SHA.
6. **Pré-requis CI non reproduits localement par défaut.** `python -m unittest discover -s tests` échoue sans le module `markdown`, installé par le workflow via `renderers/pedagogical/requirements.txt`. Échec préexistant au commit de base, non lié aux changements de passation. Résolu avec un venv hors dépôt.
7. **QA visuelle précédemment bloquée, désormais effectuée** sur le fixture synthétique uniquement : rendu sans erreur JavaScript, sans débordement horizontal à 1280 px ni à 390 px, sans ressource externe. Capture : `runs/handover/qa/study-desktop.png`. Ce contrôle ne vaut ni pour un contenu réel ni pour l'approbation éditoriale.
8. **Dépôt source Sri Lanka non relu dans cette session.** Le scope GitHub de la session ne couvre que ce dépôt ; le transfert est accepté tel que documenté dans `SOURCE-TRANSFER.md`.
9. **Question de confidentialité à trancher.** Aucun nom de corpus privé ni contenu d'entretien n'apparaît dans les fichiers versionnés (vérifié par recherche). Restent des mentions de la « voix Sarah » dans `SOURCE-TRANSFER.md` et `WRITING-WORKFLOWS.md`, qui décrivent une signature d'auteur de la source. À confirmer avant toute diffusion du dépôt.
10. **Concurrence.** Codex continue d'écrire sur `dev`. Toute intégration doit donc repartir de `origin/dev` ; un push refusé se traite par nouvelle récupération, jamais par force.
11. **Gate humain toujours ouvert** : HITL-258 (piliers, trame, side stories). Aucun test ne le remplace.

## 3. Stratégie adaptée à la suite

Règles de la passe H (`runs/handover/board.json`) :

- Un micro-ticket = un artefact + un contrôle exécuté + un reçu + un commit. Pas de ticket fermé sans contrôle.
- Chaque commit de chaque push porte `[skip ci]` (le head du push est celui qui compte, on les met tous par sécurité).
- Intégration uniquement en fast-forward sur `dev` : `git fetch origin dev`, rebase de mes seuls commits non publiés sur `origin/dev` si nécessaire, puis `git push origin HEAD:dev` sans `--force`.
- Pas de PR, pas de `workflow_dispatch`, pas de modification des workflows.
- Après push : vérifier que `origin/dev` pointe sur le SHA attendu, et qu'aucun run Actions n'existe pour ce `head_sha`.
- Gate local avant chaque intégration : validateur racine et, si le ticket touche au renderer ou aux contrats pédagogiques, les tests `test_pedagogical*` avec le navigateur préinstallé.

## 4. Backlog résiduel (non exécuté dans cette passe)

| Ticket R2 | Situation | Blocage |
|---|---|---|
| R2-02 Rapatrier matériaux | Partiellement fait en privé (`INTAKE-POLICY.md`) | Stockage privé à désigner ; transcript R1 non récupéré. |
| R2-04 Révision itérative | Tests présents dans `test_writing.py` | Reçu à produire par un ticket de revue. |
| R2-07 / R2-08 Skills atomiques | Non commencé dans le dépôt | Hors dépôt par mandat ; environnement personnel. |
| R2-09 Formats sources | `kb.py` existe, conversions PDF/DOCX non vérifiées | Dépendances de conversion à valider. |
| R2-11 Collecte corporate | `crawl.py` absent | Accès réseau sortant et `robots.txt` à vérifier ; à confirmer avec Codex avant de démarrer pour éviter le conflit d'écriture. |
| R2-12 à R2-14 Graphe et Graph1 | Dépendants | Dépôt Graph1 hors scope GitHub actuel. |
| HITL-258 | Décision humaine | François. |

Recommandation : prochaine unité = R2-11 (collecte corporate), après accord de Codex sur la répartition d'écriture.
