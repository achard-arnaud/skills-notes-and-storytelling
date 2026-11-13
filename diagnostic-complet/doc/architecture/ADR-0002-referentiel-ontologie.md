# ADR-0002 — Ontologie documentaire et validation structurelle

- Statut : proposé, implémentation locale en lecture seule.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D13–D21.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Proposition locale avec implémentation décrite.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Le graphe documentaire a besoin de contraintes de classes, de relations et de domaine/codomaine pour rendre visibles des incohérences structurelles. Un tel contrôle ne tranche ni la pertinence métier ni la vérité d’une proposition ; l’existence d’un outil ne transforme pas le statut proposé en accepté.

## Décision

Le référentiel local décrit classes, types, relations et contraintes de domaine/codomaine. Il sert à détecter des écarts structurels sans modifier les données ni promouvoir des faits. Les nombres de types et versions viennent du référentiel au SHA considéré. La terminologie courante de l’ADR-0009 remplace les anciennes formulations evidence_basis/tier. La pertinence métier reste un jugement distinct.

## Alternatives et justification documentée

Le choix entre référentiel déclaratif, contrôles dispersés et validation sémantique automatique n’est pas documenté comme comparaison d’options. La validation métier automatique n’est pas autorisée par cette proposition.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

Les écarts structurels peuvent être signalés sans mutation des données ni promotion de faits. Une validation structurelle laisse entière la revue sémantique ; les versions et types restent ceux du référentiel épinglé, avec la terminologie courante de l’ADR-0009.

Le principe général applicable est [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0002-referentiel-ontologie.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/ontology/ontology-v1.json).
- [Index local](README.md).

## Repères opérationnels

Le déclencheur `cadence_semantic` est défini dans le [référentiel](../../ontology/ontology-v1.json) et exposé par [ontology.py](../../ontology.py) ; aucun seuil ni objectif n’est fixé tant que la calibration reste `pending_real_corpus`.

## Réexamen

Réexaminer lors d’une évolution du référentiel, d’une incompatibilité de domaines ou d’une demande de mutation automatique. Une éventuelle acceptation exige une décision explicite distincte de la disponibilité de l’implémentation. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
