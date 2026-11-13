# ADR-0007 — Projection privée Graph1

- Statut : accepté, adaptateur local.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D06, R2-13, R2-14.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale d’adaptateur.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

La projection vers Graph1 doit conserver les identifiants et éviter d’altérer le graphe protégé. La publication d’un lot atteste un événement passé ; elle ne garantit ni la disponibilité actuelle du service ni son adoption par les autres parcours.

## Décision

Graph1 reçoit une projection dans un namespace privé déclaré. Vérifier les empreintes du graphe protégé avant et après, le manifeste et les chemins écrits. Les identifiants restent résolvables. La publication d’un lot est une preuve historique à consulter dans son reçu ; elle ne prouve pas la disponibilité actuelle. Graph1 n’est pas imposé aux autres parcours.

## Alternatives et justification documentée

La comparaison de Graph1 avec d’autres adaptateurs n’est pas documentée. L’adaptateur choisi localement n’est pas une recommandation générale de plateforme.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

La projection utilise un namespace privé déclaré et exige des empreintes avant/après ainsi qu’un contrôle des chemins écrits. Ces contrôles ajoutent un travail de vérification ; un reçu de publication ne remplace pas un contrôle de disponibilité actuel.

Le principe général applicable est [ADR-1004](../../../docs/architecture/ADR-1004-run-build-context.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0007-projection-graph1.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/project.py).
- [Index local](README.md).

## Réexamen

Réexaminer si le namespace, le graphe protégé, les règles d’écriture ou les identifiants changent. Vérifier la résolvabilité et l’isolation sur le run concerné avant de conclure à une projection sûre. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
