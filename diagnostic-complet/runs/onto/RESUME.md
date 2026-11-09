# Reprise — sprints ONTO-S6 et ONTO-S7 (renforcement KB par ontologie)

Date : 7 novembre 2026. Board : `runs/onto/board.json` (20 tickets, tous `verified`). Mode : fast-forward sur `dev`, `[skip ci]`, sans PR, sans dispatch, sans modification de `runs/r2/board.json` ni de `runs/bootstrap/`, aucune promotion `main`.

## Livré et vérifié mécaniquement

- Référentiel `ontology/ontology-v1.json` v0.1.0 (proposé) : 5 classes, 10 types, 16 règles d'arêtes, densité sémantique, déclencheurs sans cible, politique d'alias en lecture seule, chemin de calibration humain.
- `ontology.py` : validateur, classification, contrôle domaine/codomaine et preuve, couverture des règles, journal de cadence sans seuil.
- `loopback.py` : section `ontology` additive ; **vocabulaire d'arêtes dérivé du référentiel** (correction d'un défaut trouvé en S7 : 9 relations canoniques absentes de la liste codée, faux `type_review`).
- `reinforce.py` : reçu unique, loopback + ontologie, au plus trois actions, `automatic_mutations`, `automatic_promotion` et `candidate_approval` toujours à false.
- Fixtures : positive, négative, négative-structure, relations-all ; `expected.json` ; couverture 16/16.
- Décisions D13 à D18 (`docs/ONTOLOGY.md`) ; contrat de skill (`docs/REINFORCE-KB-SKILL-CONTRACT.md`) ; protocole de calibration (`docs/CADENCE-CALIBRATION-PROTOCOL.md`).
- Suite : 145 tests locaux ; gate racine et renderer pédagogique rejoués.

## Chiffres (fixtures synthétiques, aucune mesure de la KB réelle)

- Baseline synthétique : densité historique inchangée (0,059) ; densité sémantique 0 (aucune arête entre nœuds sémantiques).
- Titres : 4 classés `structure.heading`, hors densité sémantique.
- Négatif-structure : 4 violations, 1 hors ontologie, 3 non classés, déclencheur `directive_in_material`.
- Relations-all : 0 violation ; décision `no_change` (après correction D17).

## Ce qui reste bloqué, décision humaine requise

- Calibration de la cadence HIL : aucun seuil. Corpus réel requis, puis décision consignée (D18).
- Validation métier des règles `answers` et `causes` (preuve explicite obligatoire).
- Revue sémantique du delta du catalogue racine (8 vers 12 relations) avant toute promotion `main`.
- Accès au corpus privé Graph1 pour appliquer l'ontologie à la KB réelle.
- Coordination avec Codex sur l'écriture de `dev` (R2-11 notamment).
- HITL-258 : piliers, trame et side stories.

## S8 et S9 réalisés (sans intervention humaine)

- S8 : générateur synthétique déterministe (`synth.py`), idempotence du reçu, schéma minimal du reçu, mesure d'échelle indicative (jusqu'à 3 105 nœuds), frontière avec run-loopback et challenge-a1.
- S9 : diff entre versions du référentiel (`ontology.py diff`), reçu agrégé sur lot (`reinforce.py --batch`), runbook du cycle humain (`docs/RUNBOOK-KB-REINFORCEMENT.md`).
- Suite : 157 tests locaux. Board : 29 tickets, tous `verified`.

## S10 réalisé (sans intervention humaine)

- Graph1 ajouté en lecture seule (clone, SHA `ad4bf02`). Graphe gelé conforme : empreinte `dd784af7…`, 877 nœuds, 1 282 arêtes. Namespace `knowledge/business/greenyellow` absent de `dev`, `main` et de la branche de transport `bootstrap/transport-graph1-v1` : le transfert de Codex n'est pas publié. Aucune écriture dans Graph1 (`runs/onto/graph1-precheck.json`).
- Facette `knowledge_status` alignée sur le vocabulaire de Graph1 (référentiel v0.2.0). Règle : `HUMAN_ADJUDICATED` exige `decision_ref`. Décision D19.
- Suite : 163 tests locaux. Board : 33 tickets, tous `verified`.

## Ce qui reste hors portée sans décision humaine

- Calibrer un seuil de cadence (corpus réel, décision D18).
- Valider métier `answers` et `causes`.
- Revue du delta racine (8 vers 12 relations) avant `main`.
- Accès au corpus Graph1 pour appliquer l'ontologie à la KB réelle.
- Coordination avec Codex sur l'écriture de `dev` (R2-11).
- HITL-258 : piliers, trame et side stories.

## Prochaine action

Aucune action sans décision ci-dessus, ou sans publication du namespace business par Codex. Si Codex publie `knowledge/business/greenyellow` sur un dépôt Graph1 `dev` : relire le namespace au SHA livré (R2-14), vérifier que le graphe gelé n'a pas bougé, et seulement ensuite appliquer `reinforce.py` en lecture seule.
