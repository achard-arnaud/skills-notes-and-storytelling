# ADR-0007 — Projection privée Graph1

- Statut : accepté, adaptateur local.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D06, R2-13, R2-14.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

Graph1 reçoit une projection dans un namespace privé déclaré. Vérifier les empreintes du graphe protégé avant et après, le manifeste et les chemins écrits. Les identifiants restent résolvables. La publication d’un lot est une preuve historique à consulter dans son reçu ; elle ne prouve pas la disponibilité actuelle. Graph1 n’est pas imposé aux autres parcours.

## Conséquences

Le principe général applicable est [ADR-1004](../../../docs/architecture/ADR-1004-run-build-context.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0007-projection-graph1.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/project.py).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
