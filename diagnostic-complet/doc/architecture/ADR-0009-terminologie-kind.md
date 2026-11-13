# ADR-0009 — Terminologie et éligibilité des sources

- Statut : accepté, contrat local courant.
- Date de décision : 2026-11-10 ou mandats historiques cités ; restructuration documentaire : 2026-11-13.
- Portée : prototype diagnostic-complet uniquement.
- Décisions liées : D29, D30, D36.
- Couverture documentaire : voir [la revue des 14 ADR](../../../docs/architecture/ADR-REVIEW-2026-11-13.md).
- Nature documentaire : Décision locale de terminologie.
- Autorité de décision : approbateur et trace d’approbation non documentés dans cet ADR ; statut historique conservé, sans nouvelle approbation.
- Qualification des dates : la mention « Date de décision » est reprise de la version source ; elle ne permet pas d’attribuer une date de décision précise à cet ADR. La date de restructuration n’est pas une date d’acceptation.
- Normalisation documentaire : 2026-11-14, sans changement du statut ni du choix consigné.

## Contexte

Lecture de revue du choix consigné ci-dessous ; aucune nouvelle circonstance historique n’est attestée par cette reformulation.

Les anciennes formulations T0–T4 et evidence_basis/tier peuvent entrer en concurrence avec le vocabulaire courant. Un référentiel unique de statuts et de kinds évite que chaque consommateur déduise sa propre règle d’éligibilité factuelle.

## Décision

ontology/terminology.json est l’autorité locale pour statuts et kinds de source. kind remplace les tiers historiques T0–T4. Les contrôles d’attribution et d’éligibilité à verified_fact suivent ce contrat ; les kinds corporate et vendeur ne deviennent pas indépendamment vérifiés par réemploi. Une validation de schéma ne certifie pas le monde réel.

## Alternatives et justification documentée

Le maintien des tiers et les autres taxonomies ne font pas l’objet d’une comparaison documentée ici. Le remplacement par kind est conservé sans lui attribuer une étude comparative absente.

La formulation conservée dans « Décision » est le choix consigné ; les raisons explicitées dans le contexte sont une lecture de ce contrat, pas la reconstitution d’une délibération absente.

## Conséquences

Les prescriptions rappelées ci-dessous viennent du choix consigné. Les risques et coûts qui en sont déduits sont des implications de revue, sans mesure ni validation runtime nouvelle.

ontology/terminology.json reste l’autorité locale. Le réemploi d’une source corporate ou vendeur ne lui confère pas une vérification indépendante ; les contrôles structurels doivent rester distincts de la corroboration réelle.

Le principe général applicable est [ADR-1002](../../../docs/architecture/ADR-1002-evidence-knowledge.md). Les contrats et le code au SHA du run restent les autorités exécutables ; cette normalisation ne change aucune implémentation.

## Preuves et références

Ces liens identifient les sources documentaires ; ils ne constituent pas un reçu d’exécution ni une nouvelle preuve d’approbation. Les références épinglées restent historiques : pour exécuter un run, lire ses contrats au SHA du run.

### Historique immuable

- [Version complète avant restructuration](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/doc/architecture/ADR-0009-terminologie-kind.md) : justification et spécification historique conservées dans Git.
- [Ressource opérationnelle](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ae8d78fb07c17b7df3637e45925d3c29fe5cc1fd/diagnostic-complet/ontology/terminology.json).
- [Index local](README.md).

## Réexamen

Réexaminer lors d’un changement de statut, de kind ou d’éligibilité, ou si un consommateur réintroduit les tiers historiques. Vérifier les consommateurs et la compatibilité des données avant toute migration de vocabulaire. Toute évolution de comportement demande un delta BUILD explicite et une validation adaptée ; la normalisation documentaire ne vaut pas approbation de ce delta.
