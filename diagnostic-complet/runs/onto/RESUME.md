# Reprise — sprint ONTO-S6 (renforcement KB par ontologie)

Date : 7 novembre 2026. Base de passation : `dev` `b86fd10`. Board : `runs/onto/board.json`. Mode : fast-forward sur `dev`, `[skip ci]`, sans PR, sans dispatch, sans modification de `runs/r2/board.json` ni de `runs/bootstrap/`.

## Ce qui est livré et vérifié mécaniquement

- Référentiel `ontology/ontology-v1.json` (v0.1.0, statut proposé) : 5 classes, 10 types, 16 règles d'arêtes, densité sémantique, déclencheurs sans cible, politique d'alias en lecture seule.
- Validateur `ontology.py check` : refuse un référentiel incohérent (type inconnu, relations canoniques décalées, seuil sans calibration, alias applicable).
- Classification et contrôle des arêtes, non-mutation, candidats d'alias sans approbation.
- Intégration additive dans `loopback.py` : section `ontology`, métriques et décision historiques inchangées.
- Fixtures synthétiques positive et négative, avec `expected.json`.
- Contrat de skill `docs/REINFORCE-KB-SKILL-CONTRACT.md` (sans SKILL.md versionné).
- Décision d'architecture `docs/ONTOLOGY.md` (D13 à D16).
- Suite : 131 tests passent. Gate racine et renderer pédagogique rejoués localement.

## Chiffres mesurés (fixture synthétique, pas la KB réelle)

- 18 nœuds, 18 arêtes ; densité historique 0,059 (inchangée).
- Sémantique : 11 nœuds ; 4 titres sortis de la densité sémantique (classe `structure.heading`).
- Violations sur le graphe propre : 0. Déclencheurs : aucun.
- Négatif : 3 violations, 1 non classé, 1 candidat d'alias, déclencheur `directive_in_material`.

## Ce qui n'est pas fait, et pourquoi

- Aucune calibration de cadence : elle exige le corpus réel (D16). Décision humaine.
- Relecture métier des règles `answers` et `causes` : décision humaine.
- Application de l'ontologie à la KB réelle (Graph1) : dépôt privé hors scope GitHub de cette session.
- Revue sémantique du delta du catalogue racine (`contracts/relation-types.json`, 8 vers 12) avant toute promotion `main` : décision humaine.
- HITL-258 (piliers, trame, side stories) : toujours ouvert.

## Interdits maintenus

- Pas de promotion vers `main`. Pas de PR. Pas de `workflow_dispatch`.
- Pas de seuil fixé comme cible. Pas d'approbation de candidat. Pas de fusion d'identifiant.
- Pas de contenu privé dans le dépôt public.

## Proposition S7 — ce qu'une passe sans humain peut faire

Faisable sans intervention, en local et en fast-forward :

1. Étendre les négatifs : titre classé en HIL, entité dans une structure, relation hors catalogue, kind inconnu en masse.
2. Ajouter une commande `reinforce` qui assemble loopback + ontologie en un seul reçu, sans mutation.
3. Dresser le tableau de couverture des règles (quelles règles sont exercées par une fixture) et l'exposer en test.
4. Préparer le protocole de calibration de la cadence (script de mesure, sans seuil), à lancer sur le corpus réel quand il sera accessible.
5. Mettre à jour le board R2 par des reçus, sans toucher au fichier de l'autre passe.

Bloqué, décision humaine requise :

- Calibration de la cadence HIL (corpus réel).
- Validation métier de `answers` et `causes`.
- Accès au dépôt Graph1 et au namespace business.
- Coordination avec Codex sur l'écriture de `dev` pendant R2-11.
- Revue du delta racine avant `main`.

## Prochaine action immédiate

Pousser le gate final et cette capsule, puis lancer S7 sur les points 1 à 3 (les seuls qui n'exigent aucune décision).
