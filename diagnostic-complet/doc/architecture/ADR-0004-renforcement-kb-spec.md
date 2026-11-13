# ADR-0004 — Spécification historique du renforcement

- Statut : historique, consolidé par ADR-0003 et ADR-0005.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D32.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

Le parcours déclencheur → observation → qualification → propositions → reçu reste utile. Les contrats courants vivent dans reinforce.py et la skill opérationnelle. La limite historique de trois propositions est remplacée par D32 ; elle ne doit pas être réintroduite depuis l’ancienne spécification. L’outil ne décide pas de la promotion humaine.

## Conséquences

Le principe général applicable est [ADR-1005](../../../docs/architecture/ADR-1005-learning-validation.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0004-renforcement-kb-spec.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/reinforce.py).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
