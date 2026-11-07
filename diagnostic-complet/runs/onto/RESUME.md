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

## Proposition S8 — réalisable sans intervention

1. Appliquer `reinforce.py` à un graphe **synthétique plus grand** (génération déterministe), pour mesurer le temps et la stabilité du reçu, sans conclusion sur la KB réelle.
2. Ajouter un contrôle d'idempotence : deux exécutions identiques donnent un reçu identique (hors horodatage absent).
3. Documenter la frontière reinforce / challenge-a1 (diagnostic sans mutation) dans le contrat.
4. Préparer le schéma de reçu en JSON Schema, validé par un test.

Ne pas faire sans décision : calibrer un seuil, approuver un candidat, fusionner un alias, toucher au catalogue racine pour `main`.

## Prochaine action immédiate

Pousser le board et cette capsule (S7 clôturé), puis lancer S8 sur les points 1 à 4.
