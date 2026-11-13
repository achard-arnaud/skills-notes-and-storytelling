# ADR-0009 — Terminologie et éligibilité des sources

- Statut : accepté, contrat local courant.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D29, D30, D36.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

ontology/terminology.json est l’autorité locale pour statuts et kinds de source. kind remplace les tiers historiques T0–T4. Les contrôles d’attribution et d’éligibilité à verified_fact suivent ce contrat ; les kinds corporate et vendeur ne deviennent pas indépendamment vérifiés par réemploi. Une validation de schéma ne certifie pas le monde réel.

## Conséquences

Le principe général applicable est [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0009-terminologie-kind.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/ontology/terminology.json).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
