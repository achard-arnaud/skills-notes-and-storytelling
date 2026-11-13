# ADR-0012 — Style éditorial et contexte métier

- Statut : accepté pour le style ; interprétations métier hors architecture commune.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D39, D40.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

La directive de style guide une prose directe, factuelle, didactique et orientée décision. Les contrôles mécaniques signalent des lacunes ; ils ne remplacent pas une revue éditoriale. Le style dépend du public et du mandat. D40 désigne une définition fournie dans un run et une piste d’analyse ; elle ne constitue pas une définition d’architecture du framework commun.

## Conséquences

Le principe général applicable est [ADR-1003](../../../docs/architecture/ADR-1003-narrative-artifacts.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0012-directive-de-style-et-double-cerveau.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/workflows/side-stories.workflow.json).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
