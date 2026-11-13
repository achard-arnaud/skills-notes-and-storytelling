# ADR-0005 — Distribution de la skill de renforcement

- Statut : accepté, choix local de packaging.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D31, D32.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

La source locale de reinforce-kb-loopback est versionnée dans operational-skills/. Les copies .claude et .agents servent des surfaces différentes ; elles doivent rester identiques. dependencies.json relie opérations et ressources. Cette distribution n’impose pas trois copies pour toutes les futures skills. Une nouvelle capacité autonome doit justifier ses déclencheurs, frontières et évaluation.

## Conséquences

Le principe général applicable est [ADR-1001](../../../docs/architecture/ADR-1001-routing-capabilities.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0005-contrat-skill-reinforce.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/operational-skills/reinforce-kb-loopback/SKILL.md).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
