# ADR-0010 — Heuristique de détection des directives

- Statut : accepté, règle d’implémentation locale.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D35.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale d’heuristique.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Un texte peut contenir une directive sans qu’un infinitif isolé suffise à la reconnaître. La détection par marqueurs explicites est une heuristique locale ; une reclassification peut modifier l’identité de l’atome et affecter ses références.

## Décision

La détection applique les marqueurs explicites définis dans kb.py. Elle reste une heuristique et peut manquer des directives. Les infinitifs seuls ne suffisent pas. Un changement de type peut changer l’identité de l’atome : toute migration conserve les occurrences et les références, avec sauvegarde et reçu. La règle n’est pas généralisée aux autres analyseurs par cet ADR.

## Alternatives et justification documentée

Le texte exclut les infinitifs seuls, sans documenter de benchmark ni de comparaison avec d’autres détecteurs. Aucun résultat de précision ou de rappel ne peut en être déduit.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

La règle borne les marqueurs acceptés, mais peut manquer des directives. Les changements de type imposent de préserver occurrences et références avec sauvegarde et reçu ; aucune précision ou couverture mesurée n’est affirmée ici.

Le principe général applicable est [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0010-detection-directive.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/kb.py).
- [Index local](README.md).

## Réexamen

Réexaminer à partir de faux positifs ou faux négatifs documentés, ou d’un changement de marqueurs ou d’identité. Vérifier la migration et les références ; ne pas généraliser cette heuristique aux autres analyseurs sans décision propre. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
