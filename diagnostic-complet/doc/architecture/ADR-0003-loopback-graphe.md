# ADR-0003 — Loopback du graphe

- Statut : accepté, observation locale.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D17.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Le loopback doit rendre visibles les isolés, liens non résolus, classifications et variations du graphe. Une mesure telle que la densité risquerait d’encourager des liens sans justification si elle devenait un objectif de qualité.

## Décision

Le loopback observe structure, isolés, liens non résolus, classifications et deltas. Une densité est une mesure descriptive ; elle n’est ni une cible ni un score de qualité. Les propositions restent candidates. Le nombre de constats n’est pas plafonné ; le traitement des blocages et réparations conserve un budget explicite.

## Alternatives et justification documentée

Les métriques cibles et plafonds de constats ne font pas l’objet d’une comparaison historique documentée. Le texte exclut la densité comme cible ; il ne prouve pas qu’une étude comparative des métriques a été menée.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

L’observation produit des candidats à qualifier, sans validation automatique ni quota de densité. Un inventaire non plafonné peut accroître le travail de revue ; le traitement des réparations et blocages garde donc un budget explicite.

Le principe général applicable est [ADR-1005](../../../docs/architecture/ADR-1005-learning-validation.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0003-loopback-graphe.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/loopback.py).
- [Index local](README.md).

## Réexamen

Réexaminer si une métrique devient un critère de promotion, si un plafond masque des constats ou si le budget de traitement ne permet plus de traiter les blocages identifiés. Documenter séparément observation et arbitrage de traitement. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
