# ADR-0000 — Registre historique et portée des décisions

- Statut : historique ; principes transverses repris par ADR-1001 à ADR-1006.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D01–D34.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

Les décisions D01–D34 constituent un historique du prototype. Les mandats de run restent datés ; leurs autorisations ne sont pas des permissions générales du dépôt. Les principes communs sont désormais portés par les ADR 1001–1006. Les reçus historiques gardent leurs identités et leurs chemins.

## Conséquences

Le principe général applicable est [ADR-1006](../../../docs/architecture/ADR-1006-governance-convergence.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0000-registre-decisions-run.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/runs/bootstrap/RESUME.md).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
