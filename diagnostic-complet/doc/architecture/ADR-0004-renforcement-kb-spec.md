# ADR-0004 — Spécification historique du renforcement

- Statut : historique, consolidé par ADR-0003 et ADR-0005.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D32.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Spécification historique consolidée.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Le texte conserve un parcours de renforcement et une ancienne limite de trois propositions. D32 et les ADR-0003/0005 ont consolidé ce parcours ; relire la limite historique comme une contrainte active contredirait la décision décrite.

## Décision

Le parcours déclencheur → observation → qualification → propositions → reçu reste utile. Les contrats courants vivent dans reinforce.py et la skill opérationnelle. La limite historique de trois propositions est remplacée par D32 ; elle ne doit pas être réintroduite depuis l’ancienne spécification. L’outil ne décide pas de la promotion humaine.

## Alternatives et justification documentée

La justification comparée du plafond historique et de son abandon n’est pas documentée ici. D32 est référencée comme remplacement ; aucune nouvelle comparaison d’options n’est attribuée à cette normalisation.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

Cette fiche reste un pointeur historique. Le parcours aide à comprendre l’intention, mais ses anciens détails ne constituent pas le contrat courant ; les propositions et reçus ne valent pas promotion humaine.

Le principe général applicable est [ADR-1005](../../../docs/architecture/ADR-1005-learning-validation.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0004-renforcement-kb-spec.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/reinforce.py).
- [Index local](README.md).

## Réexamen

En cas de divergence avec reinforce.py ou la skill opérationnelle au SHA du run, instruire un delta sur le contrat courant et l’ADR concerné. Préserver la version historique et ne pas réactiver son plafond de trois propositions. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
