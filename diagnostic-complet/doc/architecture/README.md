# Architecture — index des ADR du sous-projet diagnostic-complet

Ce dossier consigne les décisions d'architecture et les spécifications internes, selon le format ADR. Les documents internes qui étaient dans `docs/` y ont été migrés (10 novembre 2026) ; leur contenu d'origine est conservé dans chaque ADR, sous « Spécification migrée ».

## Conventions

- Nom : `ADR-NNNN-sujet.md`, numérotation croissante, jamais réutilisée.
- Sections obligatoires : **Statut**, **Date**, **Décisions liées** (numéros `D..`), **Tickets**, **Contexte**, **Décision**, **Conséquences**.
- Une décision remplacée reste dans son ADR ; le statut indique son remplaçant. Aucune réécriture silencieuse.
- Les reçus et registres de run (`runs/`) gardent leurs chemins d'origine : ce sont des preuves historiques.
- Un ADR qui change de fond après consignation reçoit une note datée, pas une réécriture.

## Liste

| ADR | Sujet | Statut | Décisions | Ancien chemin |
|---|---|---|---|---|
| [ADR-0000](ADR-0000-registre-decisions-run.md) | Registre des décisions du run | accepté (historique) | D01 à D26 | `docs/DECISIONS.md` |
| [ADR-0001](ADR-0001-kb-contrat-documentaire.md) | Contrat de la KB documentaire | accepté | D06 | `docs/KB.md` |
| [ADR-0002](ADR-0002-referentiel-ontologie.md) | Référentiel d'ontologie | proposé, lecture seule | D13 à D21 | `docs/ONTOLOGY.md` |
| [ADR-0003](ADR-0003-loopback-graphe.md) | Loopback du graphe | accepté | D17 | `docs/LOOPBACK.md` |
| [ADR-0004](ADR-0004-renforcement-kb-spec.md) | Renforcement KB (spécification) | partiellement remplacée | D32 | `docs/KB-REINFORCEMENT.md` |
| [ADR-0005](ADR-0005-contrat-skill-reinforce.md) | Contrat de la skill reinforce | accepté | D31, D32 | `docs/REINFORCE-KB-SKILL-CONTRACT.md` |
| [ADR-0006](ADR-0006-calibration-cadence.md) | Calibration de la cadence | accepté, aucun seuil | D16, D18 | `docs/CADENCE-CALIBRATION-PROTOCOL.md` |
| [ADR-0007](ADR-0007-projection-graph1.md) | Projection vers Graph1 | accepté | lots R2-13, R2-14 | `docs/GRAPH1-BRIDGE.md` |
| [ADR-0008](ADR-0008-frontiere-run-build.md) | Frontière run / build et profils | accepté | D25 à D28, D33 | `docs/RUN-BUILD-BOUNDARY.md` |
| [ADR-0009](ADR-0009-terminologie-kind.md) | Terminologie et kinds de source | accepté | D29, D30, D36 | `docs/TERMINOLOGY.md` |
| [ADR-0010](ADR-0010-detection-directive.md) | Détection des directives | accepté, migration à planifier | D35 | (nouveau) |

| [ADR-0011](ADR-0011-acquisition-2026-11-10-et-migration-profil.md) | Acquisition du 10 novembre et migration du profil de la KB privée | accepté | D37, D38 | (nouveau) |

D34 (périmètre léger de `AGENTS.md`) relève du fichier `AGENTS.md`, pas d'un ADR.

## Pour ajouter une décision

1. Copier le gabarit de la section « Conventions » dans un nouvel `ADR-NNNN-sujet.md`.
2. Renseigner les décisions et tickets liés, et mettre à jour la liste ci-dessus.
3. Si une décision remplace une autre, mettre à jour le statut des deux.
