# ADR-0011 — Acquisition du 10 novembre 2026 et migration du profil de la KB privée

- **Statut** : accepté
- **Date** : 2026-11-10
- **Décisions liées** : D37 (migration explicite du profil), D38 (registre des exemples sans namespace), D28 (une KB, un profil)
- **Tickets** : RF-06, RF-07, #141, #94, #75

## Contexte

François a fourni treize documents (document Ask for the Moon, douze documents de réponses, dont une directive de style) et demandé : insérer le document dans la KB, vérifier les fragments utiles, chercher des cas d'usage de jumeau numérique. L'index de la KB privée avait été produit avant l'introduction de `profile_id` : l'outil d'ingestion le refusait (RF-06).

## Décision

1. **D37 — migration explicite.** L'index de la KB privée reçoit `profile_id: greenyellow` ; schéma (1.0.0) et lexique (1.0.0) sont inchangés, donc aucune classification n'est recalculée. Une copie de l'index d'origine est gardée hors dépôt, et le reçu `runs/acq-2026-11-10/receipt.json` donne les empreintes. L'outil de migration reproductible reste à écrire côté construction (RF-06 partiellement traité).
2. **Ingestion sans perte.** Les treize documents sont ingérés en entier ; le tri (corroboré, sans source, pertinent pour quels encarts) est un registre ingéré à son tour, pas une sélection qui supprime. La directive de style est un type de source distinct (`supplied_style_directive`) : elle n'est appliquée qu'après validation de François.
3. **D38 — registre sans namespace.** `workflows/kb-examples.json` ne nomme plus le namespace de projection ; il renvoie au champ `projection.namespace` du profil. `pointers_check.py` vérifie, côté exécution, que chaque identifiant résout dans la KB privée ; aucun test ne lit le corpus.
4. **Promotion.** Aucun fragment n'est promu en fait vérifié. Les chiffres du site de l'entreprise (50 millions de données par jour, disponibilité supérieure à 98,5 %) sont corroborés par une source de l'entreprise : déclaration corroborée, pas indépendante.

## Conséquences

- 18 sources et 830 atomes ajoutés (677 sources, 23 004 atomes au total) ; graphe de formation gelé inchangé.
- Les exemples du registre passent de 21 à 24 (Ask for the Moon, maintenance sur site et documentation, jumeau numérique, VizioSense).
- Les fragments sans source (disponibilités, délais, taux de filtrage, attributions à des cabinets) restent à instruire ; la liste est dans le registre de tri de la KB.
