# Investigation et collecte avant rédaction

Une section ne se rédige pas tant que son investigation n'est pas planifiée. Cette fiche renforce la phase de recherche des deux modes.

## 1. Plan d'investigation par section

Pour chaque section du scaffold, remplir :

| Champ | Contenu |
|---|---|
| Question | Celle de la section, une seule |
| Décision éclairée | Ce que le lecteur pourra décider |
| Niveaux à couvrir | Macro (statistiques officielles, secteur), mezzo (communications de l'entreprise), micro (pages produit, cas, mesures) |
| Sources attendues | Public identifié, échange fourni, document fourni, à collecter |
| Preuve visée par claim | `verified_fact` seulement après revue déclarée ; sinon `supplied_claim`, `attributed_claim`, `inference` ou `hypothesis` |
| Inconnues | Ce qui manque et qui le détient |
| Condition d'arrêt | Résultat utile atteint, ou blocage qualifié après deux corrections |

## 2. Marqueurs de statut

Tout fait écrit porte l'un des marqueurs : **Publié** (source publique identifiée), **Échange** (signal attribué à une discussion, à revérifier sur la transcription), **Inférence**, **Hypothèse**. Modèle de forme : `EX-NAR-01`.

## 3. Collecte, dans l'ordre

1. **Inventorier** ce que la KB contient déjà (`kb.py`, atomes par pilier candidat) avant de chercher dehors.
2. **Combler** par les opérations atomiques : `source-convert` (fichiers), `corporate-crawl` (site de l'hôte déclaré, robots.txt respecté), `kb-ingest` (atomisation), sans promouvoir.
3. **Lister les manques** : annonce originale, transcript, conversation de travail, archives. Un apport non importé reste listé ; il n'est jamais remplacé par un résumé.
4. **Recherche ciblée** pour les exemples dont le statut est `research_required` ou `to_collect` (`workflows/kb-examples.json`) : une question, une condition d'arrêt, une source citable.
5. **Boucler** : `reinforce-kb-loopback` signale densité, types et cadence de revue, sans seuil ni mutation automatique.

## 4. Distinctions à garder

- Compte (acheteur) et offre (vendeur) : deux dossiers, un fit explicite plus tard.
- Industrie et corporate : deux piliers aux scopes différents. Données et IA : deux piliers.
- Indicateur national : contexte, pas mesure de maturité de la cible.
- Benchmark de concurrents : archétypes à instruire, pas classement de performances.

## 5. Gates humains

- Choix des piliers et du fil : François (validés pour la première passe, #258).
- Side stories : François, une par une, au passage `validated`.
- Promotion d'une preuve en fait vérifié : revue déclarée, jamais automatique.
