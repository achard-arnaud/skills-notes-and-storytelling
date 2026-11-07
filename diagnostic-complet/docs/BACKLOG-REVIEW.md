# Revue du backlog R2 et planification des sprints

Date : 7 novembre 2026. Base : `dev` `0bd21f1`. Document public, sans corpus privé. Statuts : `planned` (board R2 inchangé, passe Codex), `candidate` (code/test présents, reçu absent), `proposed` (nouveau).

Principes appliqués : chaque ticket a un artefact, un contrôle, un contre-exemple et une limite. Un test qui passe n'est pas une validation humaine. Aucun ticket n'autorise une promotion automatique.

## 1. Revue des 16 tickets R2

| Ticket | Statut proposé | Renforcement retenu | Négatif ajouté |
|---|---|---|---|
| R2-01 Cadrer sources et destinations | candidate | Ajouter un contrôle de SHA épinglés pour les deux dépôts. | Dépôt hors scope refusé. |
| R2-02 Rapatrier matériaux | partial | Séparer explicitement inventaire public (métadonnées) et contenu privé. Aucun texte privé dans Git. | Fichier privé écrit dans le dépôt → échec. |
| R2-03 Rédaction from-scratch | candidate | Ajouter critère : chaque paragraphe a un fait ou une hypothèse marquée. | Prose antérieure acceptée sans preuve → refus (déjà testé). |
| R2-04 Révision itérative | candidate | Ajouter : le delta ne réécrit pas le hors-delta (empreinte avant/après). | Modification hors delta → rejet (déjà testé). |
| R2-05 Loopback graphe et piliers | candidate | Remplacer « mesurer types densité » par le protocole de `docs/KB-REINFORCEMENT.md` ; ajouter K2 (titres). | Titre compté comme assertion → constat structurel. |
| R2-06 Catalogue des relations | candidate | Revue sémantique humaine du delta (4 valeurs) avant promotion `main`. | Relation sans source → refus. |
| R2-07 Douze skills atomiques | planned | Critère : chaque skill a déclencheurs et exclusions testés ; rien de copié dans le dépôt. | SKILL.md versionné dans le dépôt → refus. |
| R2-08 Éprouver et installer | planned | Évals avec et sans skill (méthode skill-creator), conservées hors dépôt. | Skill qui ne discrimine pas → à réécrire. |
| R2-09 Formats sources | partial | Ajouter tests de conversion PDF/DOCX/HTML sur fixtures synthétiques, empreintes avant conversion. | Archive avec traversée de chemin → refus. |
| R2-10 KB atomique | candidate | Idempotence et liens de preuve vérifiés ; doublons conservés comme occurrences distinctes. | Fusion sans source → refus. |
| R2-11 Collecte corporate | planned | Ajouter : robots.txt, limitation de débit, liste d'exclusion (données personnelles, pages de contact). | Page exclue par robots → non collectée et notée. |
| R2-12 Enrichissement graphe | planned | Rattacher les piliers comme candidats seulement ; zéro lien causal non sourcé. | Corrélation lexicale convertie en `causes` → refus. |
| R2-13 Projection Graph1 | planned | Vérifier séparation du graphe de formation gelé (hash avant/après). | Écriture dans le namespace formation → refus. |
| R2-14 Publication Graph1 | planned | Commit `[skip ci]`, FF seulement, relecture au SHA livré. | Push forcé → refus. |
| R2-15 Revue et intégration | planned | Inclure un cycle loopback réel et les évals négatives de `KB-REINFORCEMENT.md`. | Tests verts sans négatifs → revue incomplète. |
| R2-16 Capsule | planned | Capsule ≤ 800 mots, prochaine action unique. | Capsule sans gate humain → refus. |

## 2. Tickets manquants (proposés)

| Ticket | Objet | Sortie | Dépend de |
|---|---|---|---|
| K1 | Catalogue versionné des **types de nœuds** (structure vs contenu), avec fixture | `contracts/` ou `docs/`, plus test | R2-05 |
| K2 | Règle `structural_atom_share` : titres comptés hors densité, constat dédié | `loopback.py` + test | R2-05 |
| K3 | Cadence de revue HIL : déclencheur explicite (IDs récents, seuil à calibrer), sans cible | `docs/KB-REINFORCEMENT.md` §4 + test | K2 |
| K4 | Politique de candidats alias/doublon : tombstone réversible, source et contre-exemple obligatoires | `docs/` + fixture négative | R2-10 |
| K5 | Contrat de la skill `reinforce-kb-loopback` et évals (positives et négatives) | `docs/` + `fixtures/` | K1–K4 |
| K6 | Benchmark avec et sans skill, conservé hors dépôt | `runs/` privé | K5 |

## 3. Sprints proposés

| Sprint | Contenu | Gate de sortie |
|---|---|---|
| **S6** (maintenant, local) | K2 + test ; reçus R2-01, R2-03, R2-04, R2-05, R2-06 après revue ; cette revue et la proposition K1–K5. | Tests verts ; reçus ; `dev` FF `[skip ci]` ; board R2 non modifié. |
| **S7** | K1, K3, K4 ; R2-09 et R2-10 complétés par tests de conversion et d'idempotence. | Négatifs de `KB-REINFORCEMENT.md` passent ; aucun seuil fixé comme cible. |
| **S8** | R2-11 collecte corporate (après accord avec Codex sur l'écriture de `dev`) ; R2-12 enrichissement ; K5. | Couverture et exclusions documentées ; aucune relation causale sans source. |
| **S9** | R2-13 et R2-14 (projection Graph1, dépend d'un accès au dépôt privé à confirmer) ; R2-15 avec cycle loopback réel ; K6. | Hash du graphe de formation inchangé ; capsule R2-16. |

Voie parallèle, hors dépôt : R2-07 et R2-08 (skills personnelles, environnement privé). Décision humaine HITL-258 : piliers, trame et side stories, toujours ouverte.

## 4. Points à trancher

1. Accès au dépôt Graph1 pour S9 : hors scope GitHub actuel.
2. Coordination avec Codex sur R2-11 et sur l'écriture de `dev` pendant S8.
3. Calibrage de la cadence HIL (K3) : à faire sur le corpus réel, pas sur la fixture.
