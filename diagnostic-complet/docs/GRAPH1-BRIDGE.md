# Pont vers Graph1 — projection de la KB business privée

Statut : outil `project.py` livré et testé ; publication consignée dans `runs/r2/DELIVERY.md`. Document public : méthode seulement, aucun contenu de corpus.

## Principe

Graph1 est le référentiel de formation **gelé** (graphe de 877 nœuds et 1 282 arêtes, empreinte `dd784af7a527a8e1ecddcc6bc1b231b49981362aa1e5c862e7aa9946f198b9ca`). La KB business y vit dans un namespace séparé, `knowledge/business/greenyellow/`, qui ne modifie ni ne référence ce graphe comme source.

## Garde-fous de `project.py`

| Garde-fou | Effet |
|---|---|
| Empreinte du graphe gelé vérifiée **avant** | Refus si elle ne correspond pas à la baseline déclarée. |
| Empreinte vérifiée **après** | Échec si le graphe gelé a changé pendant l'écriture. |
| Namespace sous `knowledge/business/` | Refus de `canonical/`, `build/`, `tmp_extract/`, `scripts/`, `tests/`, `docs/`, `.github/`, de toute remontée `..` et des chemins absolus. |
| Aucune suppression | Seuls des fichiers sont écrits ; un fichier identique n'est pas réécrit. |
| MANIFEST | Chemins, SHA-256, tailles ; `original_sha256` pour les fichiers compressés. |
| Compression sans perte | gzip déterministe (`mtime=0`) pour les JSON volumineux et le HTML brut. |
| Atomes répartis | Sous-dossiers par préfixe hexadécimal de l'identifiant, pour éviter un dossier plat de dizaines de milliers de fichiers. |
| Lots | `--only <préfixe>` publie un sous-ensemble : un lot par commit, fast-forward, `[skip ci]`. |

## Pourquoi compresser et répartir

Mesure sur 80 pages : `kb.json` 9,3 Mo, `graph.json` 6,7 Mo, atomes 2,5 Mo. Extrapolé au corpus complet, `kb.json` dépasserait 80 Mo non compressé, près de la limite de 100 Mo par fichier de GitHub. La compression est sans perte et vérifiable par `original_sha256`.

## Disposition

`sources/` (Markdown source), `kb/` (KB, graphe compressé, atomes répartis), `coverage/` (état de la collecte), `raw/` (HTML brut compressé), `MANIFEST.json`, `README.md`.

## Limites

- Le contenu reste privé : le dépôt public ne reçoit que des comptes et des empreintes.
- La projection ne vérifie pas la visibilité du dépôt de destination ; l'appelant la garantit.
- Une projection n'est pas une validation : tout est `SOURCE`, rien n'est `HUMAN_ADJUDICATED`.
