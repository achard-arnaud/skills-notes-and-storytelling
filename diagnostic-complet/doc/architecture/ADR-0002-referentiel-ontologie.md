# ADR-0002 — Ontologie documentaire et validation structurelle

- Statut : proposé, implémentation locale en lecture seule.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D13–D21.
- Tickets : voir [la revue et les owners](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).

## Contexte

Cette décision a été consignée pendant le développement du prototype. La revue du 13 novembre sépare le principe commun, la spécialisation locale et les preuves de run.

## Décision

Le référentiel local décrit classes, types, relations et contraintes de domaine/codomaine. Il sert à détecter des écarts structurels sans modifier les données ni promouvoir des faits. Les nombres de types et versions viennent du référentiel au SHA considéré. La terminologie courante de l’ADR-0009 remplace les anciennes formulations evidence_basis/tier. La pertinence métier reste un jugement distinct.

## Conséquences

Le principe général applicable est [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette réécriture ne change aucune implémentation.

## Références et historique

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0002-referentiel-ontologie.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/ontology/ontology-v1.json).
- [Index local](README.md).

## Réexamen

Toute évolution de comportement demande un delta BUILD explicite, une validation adaptée et la préservation des références de RUN. Les limites de revue humaine restent applicables.
