# ADR-0006 — Calibration de cadence

- Statut : accepté ; aucun seuil calibré par cette revue.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D16, D18.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale ; calibration non établie.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

La cadence est mesurable, mais un nombre de nœuds ou un volume d’apport ne suffit pas à prouver une valeur sémantique. Un seuil utilisé sans cycles observés présenterait une convention non calibrée comme une règle démontrée.

## Décision

Le code mesure et consigne la cadence. Un seuil de revue doit être motivé par des cycles observés et une décision référencée. L’absence de calibration reste explicite. Le nombre de nœuds ou le volume d’un apport ne suffisent pas à démontrer sa valeur sémantique.

## Alternatives et justification documentée

Aucune comparaison chiffrée de cadences ou de seuils n’est documentée ici. Ne pas inventer de valeur par défaut ni présenter le statut accepté comme une calibration réalisée.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

Les mesures peuvent être consignées ; aucun seuil calibré n’est établi par cette revue. Une décision de seuil doit citer ses cycles observés. Cette exigence rend la calibration explicable, tout en laissant son résultat ouvert.

Le principe général applicable est [ADR-1005](../../../docs/architecture/ADR-1005-learning-validation.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0006-calibration-cadence.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/ontology.py).
- [Index local](README.md).

## Réexamen

Réexaminer lorsque des cycles observés permettent de proposer un seuil, ou lorsqu’un seuil existant devient incompatible avec les observations. Consigner les observations, le périmètre et la décision plutôt que déduire la valeur du seul volume. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
