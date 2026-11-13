# ADR-0013 — Migration sûre et statuts de revue

- Statut : accepté, contrat local.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D41, D42.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale de migration et de revue.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Une migration de profil peut masquer une incompatibilité si elle se limite à changer une étiquette. Les statuts de lecture et de revue doivent également distinguer accès à une source, décision humaine et validation des différentes assertions d’un cas.

## Décision

kb_migrate.py privilégie un essai à blanc, une sauvegarde et un reçu ; il refuse une simple réétiquette lorsque le schéma ou le lexique diffère. read_at_source signifie lecture à la source, sans promotion factuelle ; human_validated exige une décision humaine datée et bornée. Une décision sur une partie d’un cas ne valide pas ses gains, son déploiement ou ses autres assertions.

## Alternatives et justification documentée

Les stratégies de migration concurrentes ne sont pas comparées dans ce texte. La séparation des statuts est conservée ; aucun arbitrage humain nouveau ni validation de cas n’est créé par cette revue.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

L’essai à blanc, la sauvegarde et le reçu encadrent la migration ; une différence de schéma ou de lexique interdit la simple réétiquette. read_at_source ne promeut pas les faits et human_validated reste borné par une décision humaine datée, assertion par assertion.

Le principe général applicable est [ADR-1005](../../../docs/architecture/ADR-1005-learning-validation.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0013-statuts-de-lecture-et-outil-de-migration.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/kb_migrate.py).
- [Index local](README.md).

## Réexamen

Réexaminer lors d’une évolution des conditions de migration ou des statuts de revue, ou si une validation partielle est étendue à tout un cas. Vérifier les sauvegardes, reçus et limites de validation avant de réutiliser le résultat. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
