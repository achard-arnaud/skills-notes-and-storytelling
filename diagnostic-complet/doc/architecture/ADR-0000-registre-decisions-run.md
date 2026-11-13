# ADR-0000 — Registre historique et portée des décisions

- Statut : historique ; principes transverses repris par ADR-1001 à ADR-1006.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D01–D34.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Registre historique.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Le registre rassemble D01–D34 et des mandats de run. Les lire comme une politique active du dépôt étendrait des autorisations datées au-delà de leur objet. La restructuration du 13 novembre 2026 distingue cet historique des principes communs.

## Décision

Les décisions D01–D34 constituent un historique du prototype. Les mandats de run restent datés ; leurs autorisations ne sont pas des permissions générales du dépôt. Les principes communs sont désormais portés par les ADR 1001–1006. Les reçus historiques gardent leurs identités et leurs chemins.

## Alternatives et justification documentée

La comparaison entre maintien du registre comme politique active, archivage et extraction des principes n’est pas documentée comme un arbitrage historique. La présente classification décrit son rôle, sans attribuer une évaluation passée.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

Le registre conserve la traçabilité des décisions antérieures. Il ne constitue ni un nouveau mandat ni une spécification exécutable ; consulter les ADR communs pour les principes et la version du run pour son exécution.

Le principe général applicable est [ADR-1006](../../../docs/architecture/ADR-1006-governance-convergence.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0000-registre-decisions-run.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/runs/bootstrap/RESUME.md).
- [Index local](README.md).

## Réexamen

Une nouvelle décision transverse ou une contradiction entre un mandat daté et un principe courant appelle une décision distincte et liée ; ne pas réécrire rétroactivement le mandat historique. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
