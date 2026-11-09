# Reprise — R2 clôturée par le coordinateur (7 novembre 2026)

La passe précédente s'est arrêtée ; ce coordinateur a repris tous les tickets R2. Aucun PR, aucune promotion `main`, tous les commits `[skip ci]` en fast-forward.

## État fiable

- **Outils** (dépôt public) : `crawl.py`, `convert.py`, `kb.py`, `ontology.py`, `reinforce.py`, `project.py`, `skills_catalog.py`. 223 tests locaux, gate racine et renderer pédagogique rejoués.
- **Corpus réel** (privé, dans Graph1) : 654 pages corporate distinctes + 1 analyse fournie, soit 655 sources, 22 001 atomes, 34 210 occurrences. Publié sous `knowledge/business/greenyellow/` au SHA `c4cb6720e759d781d6fd120d0ea09eb69e8c1fc3` ; graphe de formation gelé intact. Détails : `runs/r2/DELIVERY.md`.
- **Ontologie v0.4.0** : 14 violations sur 50 038 arêtes, toutes réelles. Chiffres : `docs/R2-RESULTS.md`.
- **Board R2** : 14 tickets `verified` (contrôles mécaniques), 2 `awaiting_human` (R2-02, R2-08). Reçus : `runs/r2/receipts/`.

## À ne pas perdre

Les fichiers de travail privés (KB locale, corpus brut, brouillons de skills) vivaient dans le conteneur de session et ne sont pas persistants. La copie durable de la KB est dans Graph1. Les 12 brouillons de skills se régénèrent : `python3 diagnostic-complet/skills_catalog.py drafts --out <dossier hors dépôt>`.

## Décisions humaines ouvertes

1. **HITL-258** : piliers, trame, side stories. Les rattachements lexicaux ne sont pas une conclusion (industrie 5 510 liens : effet du vocabulaire d'un site énergie).
2. **9 atomes `directive`** : faux positifs de l'heuristique de `kb.py` ; décider de la corriger ou de la laisser signalée.
3. **Revue sémantique** du catalogue de relations (8 vers 12) avant toute promotion `main`.
4. **Installation des 12 skills** dans un circuit personnel (brouillons livrés, impossibles à installer depuis cet environnement).
5. **Apports manquants** : transcript R1, conversation de travail, annonce originale, ZIP des éléments à charger.
6. **Cadence HIL** : aucun seuil ; le corpus réel existe désormais, mais une calibration exige plusieurs cycles mesurés (D18).

## Non fait, et pourquoi

- Deux PDF de rapports RSE : le serveur répond HTTP 500.
- Relations probatoires entre atomes : aucune qualifiée ; le graphe est documentaire (densité sémantique 0).
- Évals avec et sans skill : hors de portée ici.

## Interdits maintenus

Pas de promotion `main`, pas de PR, pas de `workflow_dispatch`, pas de force. Pas de contenu du corpus dans le dépôt public. Rien n'est `HUMAN_ADJUDICATED` sans décision humaine référencée. Aucun seuil de cadence sans `decision_ref`.

## Reprendre

Lire ce fichier, puis `docs/R2-RESULTS.md` et `runs/r2/DELIVERY.md`. Régénérer l'état avec `reinforce.py` sur `kb/graph.json.gz` décompressé depuis Graph1 ; ne jamais relancer une collecte complète sans raison (le HTML brut est conservé : `crawl.py --reextract`).
