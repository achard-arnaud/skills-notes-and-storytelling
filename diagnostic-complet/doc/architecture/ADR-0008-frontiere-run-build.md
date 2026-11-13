# ADR-0008 — Frontière RUN/BUILD et profils

- Statut : accepté, spécialisation locale.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D25–D28, D33.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

Le moteur et ses tests restent indépendants du corpus réel. Les lexiques et namespaces d’un run viennent d’un profil explicite ; l’index local est lié à un profil. Les fixtures sont synthétiques, les pointeurs réels sont opaques. L’emplacement du profil métier public reste un choix local à instruire (RF-18), pas un modèle de stockage universel. Un changement de lexique exige version et migration.

## Conséquences

Le principe général applicable est [ADR-1004](../../../docs/architecture/ADR-1004-run-build-context.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0008-frontiere-run-build.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/profiles/neutral.profile.json).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
