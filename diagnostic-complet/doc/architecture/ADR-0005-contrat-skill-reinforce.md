# ADR-0005 — Distribution de la skill de renforcement

- Statut : accepté, choix local de packaging.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D31, D32.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale de distribution.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

La capacité reinforce-kb-loopback est distribuée sur plusieurs surfaces. Sans source identifiée et correspondance des dépendances, des copies divergentes pourraient décrire des contrats différents pour une même opération.

## Décision

La source locale de reinforce-kb-loopback est versionnée dans operational-skills/. Les copies .claude et .agents servent des surfaces différentes ; elles doivent rester identiques. dependencies.json relie opérations et ressources. Cette distribution n’impose pas trois copies pour toutes les futures skills. Une nouvelle capacité autonome doit justifier ses déclencheurs, frontières et évaluation.

## Alternatives et justification documentée

La comparaison entre copies, liens et génération de paquets n’est pas documentée. Le choix local de copies identiques ne permet pas de conclure qu’une stratégie universelle de distribution a été évaluée.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

Les copies destinées aux surfaces .claude et .agents doivent rester identiques à leur source locale ; cette redondance impose un contrôle de synchronisation. Ce packaging local ne crée aucune obligation de duplication pour les autres capacités.

Le principe général applicable est [ADR-1001](../../../docs/architecture/ADR-1001-routing-capabilities.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0005-contrat-skill-reinforce.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/operational-skills/reinforce-kb-loopback/SKILL.md).
- [Index local](README.md).

## Repères opérationnels

Les scénarios `positive`, `negative`, `negative-structure`, `relations-all` et leurs attentes vivent dans [fixtures/onto/expected.json](../../fixtures/onto/expected.json) ; la suite [tests/test_ontology.py](../../tests/test_ontology.py) les vérifie.

## Réexamen

Réexaminer lors de l’ajout d’une surface, d’une divergence des copies ou d’un changement de dépendance. Toute nouvelle capacité autonome doit justifier ses déclencheurs, ses frontières et son évaluation avant de reprendre ce packaging. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
