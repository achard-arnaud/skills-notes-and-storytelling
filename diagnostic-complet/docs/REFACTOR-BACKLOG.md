# Registre des tickets de refactor — séparation build / run et terminologie

Document public : méthode et état du code uniquement. Aucun contenu de corpus. Chaque ticket a une preuve de clôture mécanique (test) ou un statut humain explicite. Convention : `RF-nn`, règles dans `AGENTS.md` (M1–M11, P5).

## Clôturés dans ce changement (9 novembre 2026)

| ID | Constat initial | Action | Preuve de clôture |
|---|---|---|---|
| RF-01 | `kb.py` embarquait `ENTITY_LEXICON` et `PILLAR_LEXICON` (GreenYellow, VisioSense, PV, onduleur…) | Lexiques déplacés dans `profiles/greenyellow.profile.json` (identiques, version 1.0.0). `kb.py` lit un profil passé en argument, défaut `neutral` | `test_golden_greenyellow_classification_is_unchanged` ; `test_core_code_contains_no_run_vocabulary` |
| RF-02 | `project.py` avait `DEFAULT_NAMESPACE = knowledge/business/greenyellow` | Défaut supprimé. Namespace exigé par argument ou par `projection.namespace` du profil | `test_projection_requires_a_namespace` ; tests `test_project.py` sur `knowledge/business/fixture-run` |
| RF-03 | Trois vocabulaires de statut sans correspondance (claims, `evidence_basis`, `knowledge_status`) | `ontology/terminology.json` unique. `evidence_basis` retirée de l'ontologie (facette jamais produite). Ontologie 0.5.0 | `TerminologyTests` ; `ontology.validate_referential` refuse toute divergence |
| RF-04 | Un kind vendeur ou corporate pouvait valider un `verified_fact` | closed | D30, D36 | Ces kinds ne sont jamais éligibles, même qualifiés. Preuves : `test_vendor_and_corporate_kinds_rejected_even_qualified` |
| RF-05 | Aucun second profil : la généricité n'était pas prouvée | `profiles/synthetic-logistics.profile.json` (fictif) ; isolation et exclusivité des termes testées | `test_synthetic_profile_is_isolated_from_greenyellow` |

## Ouverts

| ID | Sujet | Statut | Décideur | Note |
|---|---|---|---|---|
| RF-06 | Migrer les index KB sans `profile_id` (produits avant ce changement) vers un profil déclaré | open | coordinateur | Refus explicite aujourd'hui. Le corpus privé n'est pas présent dans ce conteneur |
| RF-07 | Projection Graph1 : passer `--profile` ou `--namespace` explicitement à chaque lot ; ajouter `profile_id` au MANIFEST | open | coordinateur + rédacteur business | Lien avec le lot R2-14 déjà publié : ne rien rejouer sans reçu |
| RF-08 | Entité `microsoft` dans le profil GreenYellow | closed | D33 | Conservée : la suite Microsoft (Copilot et Copilot Studio, Power Platform, Fabric, Azure) couvre les gammes IA et données de l'intégration GreenYellow. Sous-produits au lexique = version 1.1.0 + migration RF-06, à décider à part |
| RF-09 | Faux positifs « directive » (9 sur 18 directives) | closed pour la règle (D35) ; migration des atomes existants ouverte (RF-22) | D35 | Règle resserrée à des marqueurs non ambigus (ADR-0010) ; `Analyse les données.` devient une assertion, compromis accepté |
| RF-10 | Un `attributed_claim` doit reposer sur une source de kind attribuable | closed | D36 | `runtime.py` refuse un `attributed_claim` sans source dont le kind peut soutenir une attribution. Preuve : `test_attributed_claim_needs_an_attributable_kind` |
| RF-11 | Skill `reinforce-kb-loopback` : intégration dans le dépôt | closed dans le dépôt (D31) ; installation personnelle à faire par l'utilisateur | humain | Versionnée dans `operational-skills/`, copies `.claude/` et `.agents/`, dépendances mappées |
| RF-12 | Calibrer la cadence HIL (D18) | open, backlog | humain | Plusieurs cycles mesurés requis ; aucun seuil avant `decision_ref` |
| RF-13 | Revue sémantique des 12 relations | closed, remplacé par RF-24 | — | Le sujet est repris sous RF-24 ; l'écart 8 → 12 était déjà clos |
| RF-14 | Migrer les études de `kind` vers `tier` | closed (sans objet) | D36 | Décision : `kind` est le seul terme. Aucune étude n'utilisait `tier` ; il n'y a donc rien à migrer |
| RF-15 | Plafond d'une modification de type par cycle | closed | D32 | Plafond retiré du contrat, de `loopback.py` et de `reinforce.py`. Preuves : `test_no_cap_on_candidates_and_repair_loop_still_bounded`, `test_every_proposal_is_listed_and_none_is_applied` |
| RF-16 | Évaluation de la skill : le groupe témoin « sans skill » et le jugement LLM n'ont pas été exécutés ; les cas de refus sont vérifiés sur des réponses rédigées pour le test | open | humain | Relancer avec un juge indépendant avant de déclarer la skill validée |
| RF-17 | Chaque proposition doit porter la liste explicite de ses nœuds et arêtes visés (aujourd'hui seulement un échantillon dans `observation`) | open | — | Nécessaire pour regrouper par emplacement, comme demandé ; à faire dans `loopback.py` avec test |
| RF-18 | Emplacement du profil GreenYellow : `RUN-BUILD-BOUNDARY.md` range la connaissance sur l'entreprise côté run, alors que `profiles/greenyellow.profile.json` est dans le dépôt public | open | humain | Options : garder (vocabulaire public, faible risque) ou déplacer vers le namespace Graph1 et ne garder dans le dépôt que le schéma. Décision à prendre avant tout nouveau lot |
| RF-19 | PR #285 mergée dans `main` (commit `92e9fc9`) | closed | humain | Confirmé par l'utilisateur : merge manuel de sa part |
| RF-20 | `origin/dev` réécrit de force par une autre session | closed (récupéré) | — | Récupéré par rebase sans force puis fast-forward. Règle : fetch et rebase avant chaque commit |
| RF-21 | Une fusion `main → dev` (01384d3) a remplacé le AGENTS.md riche de `dev` par une version plus lourde, perdant les mandats éditoriaux | closed (restauré) | D34 | Restauré et protégé par `test_agents_keeps_its_mandates` |
| RF-22 | Migrer les atomes existants classés `directive` à tort vers le nouveau classement (D35) | open, bloqué | humain | L'identifiant d'un atome dépend de son type : reclasser crée un nouvel identifiant. Il faut garder les occurrences résolvables et produire un reçu. Demande l'accès au corpus réel, non disponible dans cette session |
| RF-23 | Valider la structure de types de la KB réelle (nœuds, arêtes) | open, bloqué | humain | Fait sur un corpus synthétique (8 atomes, 0 violation) et sur les agrégats du run. Le graphe réel exige l'accès au dépôt Graph1, refusé par le classifieur dans cette session |
| RF-24 | Revue sémantique des 12 relations (voir ADR-0002 et #272) | open | humain | Remplace l'ancien RF-13 : l'écart 8 → 12 est clos depuis `d29882b` |
