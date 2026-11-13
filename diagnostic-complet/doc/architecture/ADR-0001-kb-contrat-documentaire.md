# ADR-0001 — Ingestion documentaire et identités

- Statut : accepté, local.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D06.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

L’ingestion doit distinguer les octets d’une source, chacune de ses occurrences et les atomes dédupliqués. Sans cette séparation, réutiliser un atome pourrait effacer son origine ou faire passer un apport fourni pour une preuve vérifiée.

## Décision

La KB conserve les octets des sources, les localisateurs des occurrences et les atomes dédupliqués. Une unité fournie reste non vérifiée après import. Les identités, offsets, normalisations, verrous et reçus suivent kb.py et ses tests. Le graphe documentaire est une projection ; la provenance documentaire ne vaut pas corroboration. Les corpus restent dans un espace privé.

## Alternatives et justification documentée

La comparaison avec un stockage sans déduplication ou sans séparation source/occurrence/atome n’est pas documentée. Aucune de ces options n’est présentée ici comme historiquement évaluée.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

La provenance reste traçable malgré la déduplication et les imports ne confèrent pas de vérification factuelle. Les détails d’identité et d’offset restent couplés au contrat de kb.py ; leur évolution peut nécessiter une migration préservant les occurrences. Le corpus reste privé.

Le principe général applicable est [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0001-kb-contrat-documentaire.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/kb.py).
- [Index local](README.md).

## Réexamen

Réexaminer si la normalisation, les offsets, la déduplication ou les identifiants changent, ou si une occurrence ne permet plus de retrouver son passage source. Exiger alors des fixtures synthétiques et une stratégie de conservation des références. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
