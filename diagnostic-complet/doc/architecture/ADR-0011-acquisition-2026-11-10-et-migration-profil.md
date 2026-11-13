# ADR-0011 — Migration de profil et résolution des exemples

- Statut : accepté, décision locale ; bilan du lot conservé historiquement.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D37, D38.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale et renvoi à un bilan historique.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Un index ancien peut recevoir une déclaration de profil seulement si schéma et lexique sont compatibles. Le registre d’exemples doit résoudre ses pointeurs à partir du namespace du profil ; les résultats du lot d’acquisition restent des événements de RUN.

## Décision

Une déclaration de profil sur un index ancien exige compatibilité du schéma et du lexique, sauvegarde et reçu. Un changement de vocabulaire exige une nouvelle classification contrôlée. Le registre des exemples lit le namespace depuis le profil ; les pointeurs se vérifient côté RUN sans ouvrir le corpus dans les tests BUILD. Les quantités ingérées et les résultats métier du lot restent dans les reçus de run.

## Alternatives et justification documentée

La comparaison de différentes stratégies de migration n’est pas documentée ici. Le texte définit la condition de compatibilité ; il ne prouve ni la réussite d’un lot actuel ni une reclassification déjà effectuée.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

Une simple déclaration de profil ne remplace pas une nouvelle classification lorsque le vocabulaire change. La sauvegarde et le reçu rendent la migration traçable ; la vérification des pointeurs reste côté RUN, sans exposer le corpus aux tests BUILD.

Le principe général applicable est [ADR-1004](../../../docs/architecture/ADR-1004-run-build-context.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0011-acquisition-2026-11-10-et-migration-profil.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/kb_migrate.py).
- [Index local](README.md).

## Réexamen

Réexaminer si le schéma, le lexique ou le namespace diffère, ou si un pointeur ne se résout plus. Distinguer une migration compatible d’une reclassification ; conserver les quantités et résultats métier dans les reçus de run. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
