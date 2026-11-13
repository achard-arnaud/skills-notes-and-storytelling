# Architecture commune — décisions et guide de lecture

Revue du 13 novembre 2026. Principes approuvés ; migration fonctionnelle encore à instruire.

Lire cet index, puis uniquement l’ADR utile à la tâche. Les manifests, schémas et capacités au SHA du run restent les autorités exécutables. Ces ADR n’installent aucun moteur ni ne migrent les enums existants.

| Besoin | Décision |
|---|---|
| Routage et capacités d’analyse | [ADR-1001](ADR-1001-routing-capabilities.md) |
| Connaissance, provenance et cycle de vie | [ADR-1002](ADR-1002-evidence-knowledge.md) |
| Narration, contrats de contenu et rendu | [ADR-1003](ADR-1003-narrative-artifacts.md) |
| Séparation RUN/BUILD et contexte portable | [ADR-1004](ADR-1004-run-build-context.md) |
| Loopback, validations et promotion | [ADR-1005](ADR-1005-learning-validation.md) |
| Autorités documentaires et convergence progressive | [ADR-1006](ADR-1006-governance-convergence.md) |

La racine exprime l’architecture commune. Le sous-projet diagnostic-complet conserve ses décisions locales et ses preuves de run. Leur [revue complète](ADR-REVIEW-2026-11-13.md) explicite la correspondance et donne les liens historiques immuables, consultables même depuis main.

## Navigation et changement

1. Identifier objectif, sujet, route et activité RUN/BUILD/revue.
2. Lire le contrat de l’étape et seulement les décisions applicables.
3. Réutiliser les preuves avec leurs dates et statuts ; sélectionner les méthodes utiles.
4. Distinguer analyse, récit, contenu et rendu ; déclarer les capacités manquantes.
5. En BUILD, proposer un delta borné avec validation adaptée et compatibilité.

Un ADR porte une décision cohérente : contexte, choix, conséquences et condition de réexamen. Une spécification de commande va dans une référence opérationnelle ; un bilan de run dans son reçu privé ou expurgé. Conserver les IDs historiques et marquer les remplacements. Le [registre documentaire](registry.json) est un index de lecture, pas un nouveau manifeste runtime.
