# ADR-0000 — Registre des décisions du run

- **Statut** : accepté (registre historique)
- **Date** : 2026-11-10 (consignation ; décisions d'origine ci-dessous)
- **Décisions liées** : D01 à D26
- **Tickets** : docs/PLAN.md, runs/r2

## Contexte

Les décisions du run (7 au 10 novembre 2026) étaient consignées dans un journal unique, sans statut ni lien vers leur justification.

## Décision

Ce document reste le registre historique D01 à D26. Les décisions postérieures sont consignées dans l'ADR de leur sujet ; l'index `README.md` donne la correspondance.

## Conséquences

La numérotation continue à D35 ; D27 à D34 vivent dans les ADR 0005, 0008 et 0009. Les reçus de run gardent leurs chemins d'origine.

## Spécification migrée (contenu d'origine, non modifié)

- **D01 — 2026-11-07** : espace isolé `diagnostic-complet/` et branche de travail depuis dev. Le mandat courant autorise code/tests locaux/fast-forward dev ; aucune promotion main.
- **D02** : invariants Sri Lanka transférés avec provenance ; pas de copier-coller de la voix, de la chronologie, de quotas HIL ou de pages.
- **D03** : le mandat ordonne les questions ; les piliers traversent le récit. Industrie et corporate ont des scopes différents ; data et IA aussi.
- **D04** : ResearchMap (navigation), EvidenceGraph (propositions/relations), ReaderScaffold (ordre argumentatif) sont séparés conceptuellement. Le prototype implémente le graphe probatoire et le scaffold ; la carte de recherche est une méthode/document, pas encore moteur de recherche autonome.
- **D05** : source fournie et synthèse antérieure ne deviennent pas fait primaire. La validation de schéma ne vérifie pas le monde réel. Import sans promotion automatique.
- **D06** : corpus privé hors dépôt public et hors issues. Les fixtures sont entièrement synthétiques. Le cas GreenYellow est préparé depuis les matériaux accessibles, sans publier son entretien.
- **D07** : outils locaux stdlib, aucun serveur, base SQL, embeddings, webhook, scheduler ou installation de skill dans ce run.
- **D08** : tickets liés et board versionné ; aucune surface Jira/GitHub Projects disponible. Ne pas simuler une modification de ces produits.
- **D09** : `[skip ci]` à chaque commit ; aucun PR/dispatch. Les contrôles locaux sont exigés et leur preuve distincte de CI intentionally not run.
- **D10** : deux corrections maximum sur la même cause, puis BLOCKED et travail indépendant. Pas de suppression de preuves pour réduire un paquet.
- **D11** : le drop est logique : ne plus réinjecter des entrées archivées dans les nouveaux paquets. Aucune promesse d'effacer ou de forcer la compaction réelle, de mesure exacte des tokens ni de remboursement des tokens déjà lus.
- **D12** : choix des piliers, fil narratif et side stories restent candidats ; aucune approbation éditoriale humaine inférée des tests ou du temps écoulé.
- **D22 — 2026-11-09** : les types de side stories passent de dix à six, définis dans `workflows/side-stories.workflow.json`, source unique lue par `sidestories.py`, `runtime.py` et `render.py` (même principe que D17 pour les relations). Les anciens types restent acceptés et produisent une lacune. `NARRATIVE.md` ne garde qu'un index.
- **D23 — 2026-11-09** : dix `SKILL.md` éditoriaux (huit piliers, `designing-main-story`, `side-stories-business`) sont versionnés dans `skills/`. Cela supersède pour cette famille seule la réserve de D07 et du mandat R2, car ils ne portent aucun texte privé : les exemples de la KB y sont des identifiants opaques d'atomes, à résoudre dans Graph1. Les opérations atomiques gardent leurs `SKILL.md` hors dépôt. Les cas d'évaluation sont écrits et non exécutés.
- **D24 — 2026-11-09** : décision humaine sur HITL-258 : piliers et fil narratif validés ; side stories à rechallenger. Les types de veille corporate personnelle et de veille académique sont ajoutés avec leurs formats. L'inventaire est réécrit sans validation ; la première vague proposée est une suggestion de l'agent.


## Décisions du 9 novembre 2026 (séparation build/run et terminologie)

- **D27** : le code de build est run-agnostique. Le vocabulaire de run (entités, piliers, namespace) vit dans `profiles/`. Le défaut est le profil `neutral`. Tests de garde-fou : `tests/test_profiles_terminology.py`.
- **D28** : une KB = un profil (`profile_id` dans l'index). Mélange refusé ; migration explicite.
- **D29** : une seule terminologie, `ontology/terminology.json`. La facette `evidence_basis` est retirée (ontologie 0.5.0) et remplacée par les tiers de source.
- **D30** : un tier vendeur (T2) ou corporate (T1) ne soutient jamais un `verified_fact`, même qualifié. Seuls T3 et T4 le peuvent, après revue humaine référencée.
- **D25 — 2026-11-09** : pour les livrables éditoriaux, l'exécution (corpus privé, notes de recherche, sorties d'évaluation) et la construction (contrats, code, tests, skills) sont découplées. Un défaut vu en exécution devient une proposition de construction liée ; aucun test de construction ne lit le corpus privé. Détail : `docs/RUN-BUILD-BOUNDARY.md`.
- **D26 — 2026-11-09** : les exemples issus de la base de connaissances se stockent en deux parties : identifiants d'atomes côté exécution, et un jumeau synthétique par type de side story côté construction (`fixtures/examples/`), vérifié par les tests. Aucun extrait du corpus ne va dans le dépôt public.

## Décisions du 10 novembre 2026 (skill intégrée, plafonds retirés, microsoft, périmètre d'AGENTS.md)

- **D31** : la skill `reinforce-kb-loopback` est versionnée dans `diagnostic-complet/operational-skills/reinforce-kb-loopback/`, copiée à l'identique dans `.claude/skills/` et `.agents/skills/` pour être appelable depuis Claude Code comme depuis Codex après un run. Exception décidée par l'utilisateur à la réserve R2 : la skill ne contient aucun texte privé, seulement des méthodes et des chemins. `dependencies.json` relie chaque cas d'usage à ses commandes, lectures, tests et évaluations ; `tests/test_reinforce_skill.py` vérifie les copies et les chemins.
- **D32** : aucun plafond sur le nombre de propositions d'un cycle de loopback. Un run peut produire des propositions à plusieurs endroits du graphe ; une limite de trois masquait des constats (`deferred_actions` était non nul sur le corpus réel). Chaque proposition reste un candidat non appliqué, décidé par un humain. Le budget anti-boucle (deux réparations par blocage) est conservé : il protège contre les boucles, pas contre la taille d'un cycle.
- **D33** : l'entité `microsoft` du profil GreenYellow est conservée (RF-08). Justification : la suite Microsoft (Copilot et Copilot Studio, Power Platform, Fabric, Azure) couvre les gammes IA et données pertinentes pour l'intégration GreenYellow. Ajouter ces sous-produits au lexique changerait sa version et exigerait la migration RF-06 ; c'est une décision séparée.
- **D34** : `diagnostic-complet/AGENTS.md` reste léger et non intégré au framework racine. Il conserve les mandats R2, éditorial (D22 à D24) et le périmètre léger ; il ne contient pas de règles numérotées supplémentaires. Une fusion du 10 novembre a remplacé ces mandats par une version plus lourde : rétabli, et protégé par un test de régression.

