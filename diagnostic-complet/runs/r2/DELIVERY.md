# R2 — reçu de livraison

Date : 7 novembre 2026. Coordinateur : reprise de la passe après l'arrêt de la précédente.

## Graph1 (dépôt privé) — namespace `knowledge/business/greenyellow/`

| Contrôle | Résultat |
|---|---|
| Base | `ad4bf02d7b70c30649bfd29d0e518cc8fad2c739` (`dev` et `main`) |
| Tête `dev` livrée | `c4cb6720e759d781d6fd120d0ea09eb69e8c1fc3` |
| Commits | 15, linéaires, fast-forward, sans force, chacun `[skip ci]` (confirmé par l'API) |
| `main` | inchangé à `ad4bf02` |
| Fichiers modifiés depuis la base | 23 337, **tous** sous `knowledge/business/greenyellow/` |
| Graphe de formation gelé | `build/graph.json` sha256 `dd784af7a527a8e1ecddcc6bc1b231b49981362aa1e5c862e7aa9946f198b9ca`, identique avant et après (877 nœuds, 1 282 arêtes) |
| `MANIFEST.json` | 23 336 entrées, 60 898 036 octets ; relu au SHA livré : 0 absente, 0 empreinte divergente |
| Runs Actions | aucun pour les têtes livrées ; le dernier run de `dev` date du 23 octobre, sur la base |
| Test de non-régression local de Graph1 | 7 tests OK avant publication |

Lots : sources et couverture (660 fichiers), `kb.json` et `graph.json` compressés (gzip déterministe, `original_sha256` au manifeste), atomes répartis par préfixe en quatre lots (≈ 5 500 fichiers chacun), HTML brut compressé en huit lots.

## Ce dépôt (public)

Outils, tests, documents et reçus uniquement. **Aucun contenu du corpus** n'y figure.

## Ce qui n'a pas été livré

- Transcript de l'entretien R1, conversation de travail, annonce originale, archive ZIP des éléments à charger : non accessibles (voir `docs/R2-INTAKE.md`).
- Deux PDF de rapports RSE listés sur le site : le serveur répond HTTP 500.
- Installation des 12 skills dans un circuit personnel : impossible depuis cet environnement ; brouillons générés et contrôlés hors dépôt.

## Limites

Tout le corpus est fourni et non vérifié (`SOURCE`). Aucun atome n'est `HUMAN_ADJUDICATED`. Un test local qui passe n'est ni une validation métier ni une validation CI.
