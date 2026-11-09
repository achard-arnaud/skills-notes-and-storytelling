# Protocole de calibration de la cadence de revue HIL

Statut : **protocole, aucun seuil**. Le code mesure et journalise ; il ne décide jamais. Un seuil n'entre dans le référentiel que par une décision humaine référencée (D16).

## Pourquoi un protocole

La règle `cadence_semantic` mesure le nombre de nœuds sémantiques ajoutés depuis le rapport précédent. Sans corpus réel, tout seuil serait arbitraire, et un seuil arbitraire devient une cible implicite. Ce protocole sépare : mesure (automatique), proposition (automatique, hypothèse marquée), décision (humaine).

## Étapes

1. **Mesurer.** À chaque cycle de revue, produire le rapport et l'ajouter au journal :

   ```bash
   python3 diagnostic-complet/reinforce.py graph.json --recent-id … --output rapport.json
   python3 diagnostic-complet/ontology.py log-cadence rapport.json --log diagnostic-complet/runs/onto/cadence.jsonl
   ```

   Chaque ligne porte `sequence`, `semantic_nodes`, `class_counts` et l'empreinte du graphe. Aucun seuil n'y figure.

2. **Accumuler.** Le protocole ne fixe pas N. Le nombre de cycles nécessaires à une calibration lisible relève de la décision humaine, et doit être noté dans la décision.

3. **Décrire.** Sur le journal, calculer les écarts successifs de `semantic_nodes` et leur distribution (médiane, dispersion, valeurs extrêmes). Cette description est une observation, pas une conclusion.

4. **Proposer une hypothèse.** Un candidat de seuil peut être écrit comme hypothèse, avec : la distribution observée, le déclencheur visé (revue HIL, revue d'un pilier), le coût d'une fausse alerte et celui d'une alerte manquée. L'hypothèse est marquée `hypothesis`, jamais `target`.

5. **Décider (humain).** La personne responsable consigne une décision datée dans `docs/DECISIONS.md` (identifiant `Dxx`), accepte ou refuse le seuil, et précise sa réévaluation.

6. **Inscrire.** Seulement après la décision :

   ```json
   {"id": "cadence_semantic", "threshold": 40, "calibration": "human_approved", "decision_ref": "docs/DECISIONS.md#Dxx"}
   ```

   Le validateur du référentiel refuse un seuil sans `calibration: human_approved` **et** un `decision_ref`. Le refus est testé : `CalibrationPathTests`.

## Ce que le code ne fera jamais

- Choisir un seuil.
- Affirmer qu'un seuil est « bon » ou optimal.
- Transformer une mesure de cadence en objectif de production de nœuds.
- Lier une cadence à une promotion ou à une approbation de candidat.

## Limites

- La fixture synthétique ne calibre rien. Les mesures issues des fixtures ne doivent pas servir de seuil.
- Une cadence élevée peut signaler un corpus bruyant, ou simplement un apport massif et légitime. Le journal ne tranche pas.
- L'accès au corpus réel (Graph1) reste à confirmer.
