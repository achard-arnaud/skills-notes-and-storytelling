# ADR-0008 — Frontière RUN/BUILD et profils

- Statut : accepté, spécialisation locale.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D25–D28, D33.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale de séparation RUN/BUILD.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Le moteur doit être testable sans dépendre d’un corpus réel ni du lexique d’un run. Le profil explicite et l’attachement de l’index à un profil rendent cette dépendance visible ; le stockage public du profil métier reste une question locale ouverte (RF-18).

## Décision

Le moteur et ses tests restent indépendants du corpus réel. Les lexiques et namespaces d’un run viennent d’un profil explicite ; l’index local est lié à un profil. Les fixtures sont synthétiques, les pointeurs réels sont opaques. L’emplacement du profil métier public reste un choix local à instruire (RF-18), pas un modèle de stockage universel. Un changement de lexique exige version et migration.

## Alternatives et justification documentée

La comparaison des emplacements possibles du profil métier public n’est pas tranchée ici : RF-18 reste à instruire. Les autres options de séparation ne sont pas documentées comme ayant été évaluées.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

Les tests BUILD utilisent des fixtures synthétiques et les références réelles restent opaques. Les lexiques de run sont versionnés dans les profils ; un changement de lexique exige une migration, avec un coût de compatibilité à traiter explicitement.

Le principe général applicable est [ADR-1004](../../../docs/architecture/ADR-1004-run-build-context.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0008-frontiere-run-build.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/profiles/neutral.profile.json).
- [Index local](README.md).

## Réexamen

Réexaminer si le moteur ou ses tests dépendent d’un corpus réel, si un index est associé à un profil incompatible, ou lors de la résolution de RF-18. Conserver la version du lexique et la voie de migration des runs antérieurs. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
