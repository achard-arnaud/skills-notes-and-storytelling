# Décisions du run

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
