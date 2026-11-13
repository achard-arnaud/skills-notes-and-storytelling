# ADR-0012 — Style éditorial et contexte métier

- Statut : accepté pour le style ; interprétations métier hors architecture commune.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D39, D40.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale de style ; contexte métier historique.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Le style doit servir le public et le mandat ; une vérification mécanique ne peut approuver une qualité éditoriale. Le texte rapproche D39, directive de style, et D40, définition fournie dans un run : leurs portées doivent rester distinctes.

## Décision

La directive de style guide une prose directe, factuelle, didactique et orientée décision. Les contrôles mécaniques signalent des lacunes ; ils ne remplacent pas une revue éditoriale. Le style dépend du public et du mandat. D40 désigne une définition fournie dans un run et une piste d’analyse ; elle ne constitue pas une définition d’architecture du framework commun.

## Alternatives et justification documentée

Les styles alternatifs et interprétations métier de D40 ne font pas l’objet d’un arbitrage documenté ici. La normalisation ne les transforme pas en options historiquement évaluées.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

La prose directe, factuelle, didactique et orientée décision reste une directive locale à adapter au public. La revue humaine reste nécessaire ; D40 conserve son statut d’apport de run et de piste d’analyse sans devenir une définition commune.

Le principe général applicable est [ADR-1003](../../../docs/architecture/ADR-1003-narrative-artifacts.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0012-directive-de-style-et-double-cerveau.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/workflows/side-stories.workflow.json).
- [Index local](README.md).

## Réexamen

Réexaminer si le public ou le mandat change, ou si un contrôle mécanique est utilisé comme approbation éditoriale. Une éventuelle définition d’architecture issue de D40 demanderait une décision distincte et des preuves adaptées. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
