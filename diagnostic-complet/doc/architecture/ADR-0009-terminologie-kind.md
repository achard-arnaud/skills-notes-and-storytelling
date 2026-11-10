# ADR-0009 — Terminologie unique : statuts, kinds de source et correspondances

- **Statut** : accepté
- **Date** : 2026-11-10 (consignation ; décisions d'origine ci-dessous)
- **Décisions liées** : D29, D30, D36 (kind seul, tier retiré, #287)
- **Tickets** : #287, RF-03, RF-04, RF-10, RF-14

## Contexte

Trois vocabulaires de statut ne se recouvraient pas, et une proposition de « tier » s'ajoutait à `kind` sans apporter de règle nouvelle.

## Décision

`ontology/terminology.json` est la source unique. `kind` est le seul terme de source ; sa table indique les statuts qu'il peut soutenir et son éligibilité à `verified_fact`. Un kind vendeur ou corporate n'est jamais éligible. Un `attributed_claim` doit reposer sur un kind attribuable.

## Conséquences

Les tiers T0 à T4 disparaissent. Le mapping legacy n'est plus nécessaire : aucune étude n'utilisait `tier`. Un kind inconnu n'est pas éligible.

## Spécification migrée (contenu d'origine, non modifié)

> **Note de consignation (10 novembre 2026)** : la spécification ci-dessous décrit les tiers T0 à T4. Ils sont remplacés par les kinds de source (D36, #287). Seule la décision ci-dessus fait foi.

Source de vérité : `ontology/terminology.json` (version 1.0.0, proposé). Ce document est la version lisible ; en cas d'écart, le JSON fait foi et un test échoue (`TerminologyTests`). Aucun module ne redéfinit ces chaînes.

## 1. Statuts de claim (`runtime.py`)

| Statut | Sens | Peut être posé par |
|---|---|---|
| `supplied_claim` | Assertion de la matière fournie, non vérifiée (défaut) | Import |
| `attributed_claim` | « Un acteur déclare X » ; ne porte pas le fait | Import, avec source T1 à T3 |
| `inference` | Conclusion à partir d'autres claims ; jamais une source | Analyse |
| `hypothesis` | Piste à éprouver, avec contre-hypothèse | Analyse |
| `verified_fact` | Revu par un humain, source consultée d'un tier éligible, `qualified: true` | Humain uniquement |
| `unknown` | Non déterminé | Tout |

## 2. Tiers de source

| Tier | Exemples | Peut soutenir | Éligible à `verified_fact` |
|---|---|---|---|
| T0 | Matière fournie, transcript interne, note | `supplied_claim` | Non |
| T1 | Site corporate, communiqué, rapport annuel | `attributed_claim` | Non |
| T2 | Presse, analystes, fournisseur, benchmark commercial | `attributed_claim` | Non |
| T3 | Régulateur, dépôt légal, statistique officielle, standard, étude publiée | `attributed_claim`, `verified_fact` | **Oui** |
| T4 | Mesure interne avec méthode, donnée client avec périmètre | `verified_fact` | **Oui** (reste privée) |
| unassessed | Tier absent ou non mappé (défaut sûr) | `supplied_claim` | Non |

Résolution : `tier` explicite prime ; sinon le mapping legacy `kind` (`primary_regulatory`, `primary_official`, `primary_research`, `primary_repo` → T3 ; `primary_corporate` → T1 ; `primary_vendor` → T2 ; `primary` → unassessed) ; sinon `unassessed`.

Règle transverse : répéter une même origine (un communiqué repris par plusieurs médias) ne change pas son tier.

## 3. États de validation et correspondances

| Concept | Claim (runtime) | Documentaire (`kb.py`) | Validation (ontologie) | `knowledge_status` (Graph1) |
|---|---|---|---|---|
| Matière fournie | `supplied_claim` | `supplied_unverified` | `supplied_unverified` | `SOURCE` |
| Candidat | — | — | `candidate_unconfirmed` | `CANDIDATE` |
| Revu humainement | `verified_fact` | — | `candidate_confirmed` | `HUMAN_ADJUDICATED` (exige `decision_ref`) |

Une machine ne pose jamais `HUMAN_ADJUDICATED`. La facette `evidence_basis` est retirée : elle était déclarée, jamais produite, et son rôle est tenu par le tier.

## 4. Ce que la terminologie ne dit pas

Un statut ou un tier n'établit pas la vérité. Seule une revue humaine référencée peut poser `verified_fact` ou `HUMAN_ADJUDICATED`.

