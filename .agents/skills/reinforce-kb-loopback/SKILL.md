---
name: reinforce-kb-loopback
description: Renforce la base de connaissances documentaire (KB) après un apport de matériaux. Lance le loopback du graphe sur des identifiants récents explicites via reinforce.py (ontologie, densité, structure, piliers), qualifie chaque constat (structurel, sémantique, hypothèse), liste toutes les propositions de modification, en précisant leur nature, et produit un reçu sans mutation. Utilise-la dès que l'utilisateur veut revoir, renforcer, contrôler ou diagnostiquer la KB ou son graphe après un ajout de sources ou d'atomes, demande un reçu de renforcement, évoque doublons ou alias candidats, types d'ontologie à revoir, cadence de revue HIL, ou relit un lot publié, même sans prononcer « loopback ». Ne l'utilise pas pour diagnostiquer un run CV (run-loopback), revoir un A1, fusionner ou supprimer des atomes, promouvoir un fait, choisir un pilier, fixer un seuil, ou installer une skill.
compatibility: Dépôt skills-notes-and-storytelling, sous-projet diagnostic-complet (Python 3, bibliothèque standard uniquement). Nécessite un graph.json produit par kb.py. Aucun accès réseau.
---

# reinforce-kb-loopback

Cette skill **diagnostique** la KB après un apport. Elle ne modifie jamais le graphe, la KB, le profil, la terminologie ni les contrats. Elle ne promeut rien et n'approuve rien : chaque proposition reste un candidat, et la décision revient à un humain.

Contrat : `diagnostic-complet/docs/REINFORCE-KB-SKILL-CONTRACT.md`. Dépendances, cas d'usage et chemins vérifiés par test : `dependencies.json`, dans ce même dossier. En cas d'écart entre cette skill et le contrat, le contrat fait foi et l'écart doit être signalé.

## Où et comment l'appeler

Cette skill vit dans le dépôt, à `diagnostic-complet/skills/reinforce-kb-loopback/`. Des copies identiques sont chargées par Claude Code (`.claude/skills/`) et par Codex (`.agents/skills/`). Un test vérifie qu'elles restent identiques. Appelle-la **après un run** : une ingestion (`kb.py`) qui produit un `graph.json`, puis un apport identifié.

## Entrées à réunir avant de commencer

1. `graph.json` : la projection documentaire produite par `kb.py` (dossier KB privé). Ne jamais le recalculer à partir d'un corpus publié.
2. Une liste **explicite** d'identifiants récents (`ATOM-…`, `SRC-…`, ou les IDs de nœuds du lot). Sans liste, voir l'étape 0.
3. Optionnel : le rapport précédent, pour le delta de cadence.

Toutes les commandes s'exécutent depuis la racine du dépôt.

## Étapes

**Étape 0 — Vérifier le déclencheur.** Le cycle n'a lieu que si l'une de ces conditions est vraie :
- des identifiants récents explicites sont fournis ;
- un nœud `instruction.directive` figure dans le matériau récent ;
- un humain demande une revue ciblée d'un pilier ou d'un HIL.

Sans déclencheur, la réponse est `no_change`. Dis-le et arrête-toi. Ne cherche pas un déclencheur en parcourant le graphe.

**Étape 1 — Valider le référentiel.**
```bash
python3 diagnostic-complet/ontology.py check
```
Échec : arrêter, signaler l'erreur, ne rien mesurer.

**Étape 2 — Mesurer.**
```bash
python3 diagnostic-complet/reinforce.py <graph.json> --recent-id <ID> [--recent-id <ID> ...] [--previous <rapport.json>] --output <reçu.json>
```
Un identifiant absent du graphe apparaît comme `unknown_recent_ids` : signale-le, ne le devine pas.

**Étape 3 — Qualifier chaque constat.** Étiquette chacun, sans fusionner les étiquettes :
- *structurel* : isolé, doublon, lien non résolu, violation de domaine ou de codomaine, preuve manquante, hors ontologie ;
- *sémantique* : à relire par un humain (classification, sens d'un type) ;
- *hypothèse* : explication possible, non vérifiée.

**Étape 4 — Périmètre HIL.** Liste les piliers et questions HIL touchés par le matériau récent, et les questions à poser. Ne réponds pas à leur place.

**Étape 5 — Lister toutes les propositions.** Il n'y a pas de plafond : un même cycle peut toucher plusieurs endroits du graphe, et une limite artificielle masquerait les constats. Pour chaque proposition, donne :
- son type (`actions_by_kind` du reçu : `structural_review`, `pillar_review`, `type_review`, `ontology_violation`, `compaction_review`, `ontology_trigger`) ;
- l'observation, l'hypothèse, la proposition, le test à exécuter.

Regroupe les propositions par type pour la lecture. Un test décrit n'est pas un test exécuté : écris « à exécuter », jamais « exécuté ». Deux échecs identiques sur un même blocage : arrêt, réserve consignée.

**Étape 6 — Vérifier le reçu.** Confirme que `automatic_mutations`, `automatic_promotion` et `candidate_approval` valent tous `false`, et que chaque action a `status: candidate_not_applied`. Si l'un de ces points n'est pas vrai, arrête-toi et signale une anomalie du code : ne corrige pas le reçu.

**Étape 7 — Rendre la main.** Donne le résumé et le chemin du reçu. La décision (accepter, reporter, rejeter une proposition) revient à l'humain.

## Qualification : règles de lecture

| Ce que l'on voit | Ce que l'on peut dire | Ce que l'on ne peut pas dire |
|---|---|---|
| Densité dirigée | Taille relative des liens documentaires | Qualité, couverture, pertinence |
| Densité sémantique à 0 | Aucune relation probatoire qualifiée entre atomes | Que le corpus est pauvre |
| Rattachement lexical à un pilier | Piste candidate (mot-clé) | Que le pilier est pertinent |
| Titre classé dans un pilier | Ancrage thématique accepté (D20) | Une assertion |
| Instruction classée dans un pilier | Violation à relire | Une consigne à exécuter |
| Candidat d'alias | Même texte normalisé dans des sources distinctes | Un doublon de sens (vérifier l'homonymie) |

La validation mécanique est une validation de forme. Elle ne prouve ni la véracité d'un atome, ni l'adéquation d'un lien à une question HIL.

## Cas à refuser ou à rediriger

| Demande | Réponse |
|---|---|
| Fusionner deux atomes ou sources sans source ni contre-exemple | Refuser. Proposer un candidat d'alias avec `requires: [source_review, counter_example_check]` |
| Passer un atome en `verified_fact` ou `HUMAN_ADJUDICATED` | Refuser. Seul un humain peut poser ce statut, avec un `decision_ref` |
| Appliquer une proposition | Refuser. La skill ne mute rien ; l'application relève du coordinateur, proposition par proposition |
| Fixer un seuil de cadence comme objectif | Refuser. Un seuil exige `calibration: human_approved` et un `decision_ref` (D18) |
| Relire un run CV, un A1 sans incident | Hors périmètre : `run-loopback` ou `challenge-a1` |
| « Revois toute la KB » sans identifiants | Demander la liste d'identifiants récents ou la cadence explicite ; ne pas parcourir le graphe au hasard |
| Installer ou modifier cette skill dans l'environnement personnel | Hors périmètre de la skill. Les copies de dépôt doivent rester identiques (test) |
| Afficher des passages du corpus | Refuser si le corpus est privé. Ne cite que les identifiants et les comptes |

## Format de sortie

Résumé court en français, puis le reçu :
- décision (`no_change` ou `review_required`) et déclencheurs déclenchés ;
- comptes : violations, non classés, hors ontologie, candidats d'alias, densités ;
- toutes les propositions, regroupées par type (`actions_by_kind`), chacune étiquetée structurelle, sémantique ou hypothèse ;
- chemin du reçu, et rappel que `candidate_approval` est `false`.

Termes : utilise les statuts et tiers de `diagnostic-complet/ontology/terminology.json`. N'en invente aucun.

## Limites à rappeler quand elles comptent

- Pas de LLM dans la boucle : les classifications sont lexicales.
- Les propositions ne portent pas encore de liste explicite de nœuds par emplacement (RF-17) : le regroupement se fait par type.
- Un PASS local n'est pas un PASS CI : la CI de `dev` est désactivée.
- Les mesures portent sur la structure du graphe, pas sur la vérité du contenu.
