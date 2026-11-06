# Audit cible — diagnostic complet, 7 novembre 2026

## Périmètre vérifié

- Dépôt `achard-arnaud/skills-notes-and-storytelling`, HEAD cloné `74a6354a4aeb128ade6db951073eeb825efca0a6`; `origin/dev` et `origin/main` sur ce SHA au début du run.
- Lectures : `AGENTS.md`, `SKILL.md`, `README.md`, `references/workflow.md`, `references/bridges-integration-and-run-memory.md`, `references/side-stories-retro.md`, `contracts/{fragment,claim,claims-graph-light,scaffold,side-story}.schema.json`, `scripts/validate_contracts.py`, `.github/workflows/{qa,pedagogical-render}.yml`.
- Audit des issues #48–55 non effectué par cet agent : les descriptions déjà obtenues par l'orchestrateur restent à utiliser comme inventaire de déduplication, pas comme preuve de capacité implémentée.

## Diagnostic

Le socle est une méthode gouvernée de notes de décision, pas un orchestrateur autonome opérationnel. Sa chaîne recherche → fragments → claims → rerank → scaffold → remplissage → side stories → sourcing → revue contradictoire est directement réutilisable. Le format long demandé exige une route isolée : ni nouveau template à pages fixes, ni changement du catalogue canonique.

Les piliers analytiques n'existent pas encore comme entités explicites. La distinction `analysis_dimension=business|product|technical` sélectionne une perspective principale ; ce n'est pas un remplacement des piliers. Pour GreenYellow : `business` reste la perspective principale ; data, IA, industrie et fonctions corporate peuvent devenir des vues analytiques multiples du même arc, sans être huit chapitres imposés.

## Matrice de transfert cible

| Actif | Réutilisation | Adaptation isolée / exclusion |
|---|---|---|
| `AGENTS.md` | Frontières de stages et indépendance account/product truth | Instructions du sous-projet documentent le rapport long autorisé et le run sans CI ; pas de promotion main |
| `SKILL.md` | Statuts `fact/inference/hypothesis/recommendation/unknown`, contenu préservé en itératif | Ne pas appliquer son choix obligatoire de template au sous-projet ; ne pas ajouter un enum global |
| `references/workflow.md` | Machine à états, trois revues distinctes, repair borné | Réaliser les étapes par unités paragraphes/sections ; une reprise ne relance pas toute l'enquête |
| `references/bridges-integration-and-run-memory.md` | RunContext, lineage, inconnues, falsifiers, alternatives rejetées | Ajouter état de tâche, entrées versionnées, delta, sortie, reprise, invalidation et budget contexte ; pas de base SQL imposée |
| `contracts/fragment.schema.json` | Fragment atomique sourcé et localisable | Couche d'import conserve source originale, capture/version et locator ; un texte Gemini est `supplied_context`, pas preuve primaire |
| `contracts/claim.schema.json` | Assertions typées et fragments de support | Ajouter vue de couverture hors contrat canonique ; ne pas promouvoir la confiance par réemploi |
| `contracts/claims-graph-light.schema.json` | Graphe probatoire compact | Graphe d'exploration et scaffold lecteur séparés ; aucune flèche de navigation interprétée comme causalité |
| `contracts/scaffold.schema.json` | Section = question, claims, payload | Schéma de rapport isolé sans `template_type`, sans page range, avec paragraphes, piliers et transitions |
| `references/side-stories-retro.md` | Six types business, lifecycle, retour et payoff | Contrat isolé exige `return_to` résolvable ; pas d'encart décoratif sans contribution |
| `.github/workflows/qa.yml` | Vérification locale `python scripts/validate_contracts.py` | Déclenche tout push dev/main : commits `[skip ci]` et aucune PR pour ce run ; ne pas désactiver les workflows |

## Divergences réelles à consigner, sans réparation globale opportuniste

1. `references/workflow.md` annonce 12 types de relations ; `contracts/claims-graph-light.schema.json` n'en autorise que 8. Les quatre supplémentaires ne doivent pas être produits puis annoncés conformes au contrat.
2. `contracts/side-story.schema.json` autorise `return_to=null`, alors que les règles narratives demandent un retour. Le sous-projet doit contrôler résolution et non-null pour toute side story promue.
3. Le scaffold canonique exige un `template_type` connu et ne porte ni pilier ni paragraphe. Lui ajouter silencieusement un rapport libre modifierait le contrat général et le manifeste.
4. Le validateur canonique vérifie surtout manifests, enum et fixtures déclarées ; PASS ne signifie pas que toutes les instances de graphes ou les liens sémantiques ont été validés.
5. `RETRO_ENGINEERING` est TODO et son validateur impose ce statut : importer des matériaux dans une enquête ne doit pas être présenté comme l'activation de ce mode.

## Plus petite intégration viable

Créer `diagnostic-complet/` avec :

- `AGENTS.md`, `README.md` : scope, autorités et commande de reprise.
- `method/` : règles de piliers, exploration, preuve, narration et side stories ; seulement des documents de méthode, pas encore des skills installées.
- `contracts/` : instances de travail à rapport libre, sans toucher aux contrats canoniques.
- `scripts/` : validateur local des références/états et générateur de vues HTML depuis les seules données autorisées.
- `tests/` : fixtures synthétiques positives/négatives ciblées.
- `planning/` : plan, index de tickets/epics, dépendances, sprints et reçus validés.
- `runtime/` : protocole et exemples de checkpoint ; les données réelles privées sont hors arbre versionné public.
- `examples/synthetic/` : démonstration générique publique ; le cas GreenYellow intégral doit garder son corpus source dans une destination privée.

Ne pas créer un serveur, service webhook, orchestration LangGraph, Obsidian, Postgres ou installateur de skills pour démontrer le premier cycle. Des Markdown + JSON avec identités stables et des commandes locales suffisent à rendre le run contrôlable et reprenable.

## Dix petits tickets recommandés

| ID local | Travail | Entrées minimales | Sortie / validation |
|---|---|---|---|
| B01 | Épingler état initial et inventaire cible | SHA + AGENTS + manifests | `baseline.json`, chemins et SHA ; main/dev inchangés au départ |
| B02 | Délimiter le sous-projet | Mandat utilisateur + audit | ADR d'isolation ; aucun changement global de template/mode |
| B03 | Mapper les invariants vers les futurs tickets | Matrice ci-dessus + #48–55 | Table reuse/adapt/exclude et owners ; absence de capacité revendiquée sans implémentation |
| B04 | Définir les piliers comme vues | Brief + exemples HIL source | Contrat pilier candidat + liens multi-piliers ; séparation industrie/corporate |
| B05 | Définir import et lineage | Fragment/claim existants | Source/capture/version/locator + statut ; Gemini ne devient jamais source primaire |
| B06 | Séparer trois graphes | Workflow + contrats | ResearchMap, evidence graph, reader scaffold avec IDs ; liens qualifiés |
| B07 | Formaliser le scaffold libre | Mandat + piliers + claims | Arc→section→paragraphe + question/payoff/transitions ; aucune pagination forcée |
| B08 | Durcir les side stories dans le sous-projet | SOP transférée + types business | Insertion et retour résolvables, claim_ids existants, lifecycle ; encart hors-tronc justifié |
| B09 | Implémenter le paquet de reprise | RunContext + plan | Travail en cours, versions d'entrées, décisions, inconnues, next action, périmètre de fichiers ; reprise sans conversation |
| B10 | Vérifier puis recevoir le sprint | Fixtures + code + état local | Résultats de contrôles locaux, limites, commit `[skip ci]`, vérification distante par orchestrateur |

## Oracles négatifs utiles

- Reject unknown source/fragment/claim/paragraph/pillar ID; duplicated stable IDs also fail.
- Reject a claim marked fact whose only origin is uncorroborated supplied/model-generated context.
- Reject a causal edge without a typed, scoped evidential mechanism; exploratory link cannot satisfy it.
- Reject promoted side story with `return_to=null`, missing anchor, unresolved claim or no reason outside trunk.
- Reject checkpoint whose pinned input hash differs from current input; invalidate downstream, do not silently resume.
- Reject task marked DONE without artifact + local validation receipt; distinguish planned, written and verified.
- Reject automatic promotion of candidate pillar/story scaffold to human-approved status.
- Reject report scaffold forced to eight sections merely because it references eight analytical pillars.
- Reject disclosure/import of sensitive source captures into public Git tracking.
- Confirm root contract validation still passes and existing canonical enums/manifests remain byte-identical.

## Limites de l'audit

Aucun code modifié, aucune issue créée et aucun test exécuté par cet agent. Le plan ci-dessus est une proposition d'intégration, pas une capacité livrée. La suppression réelle du contexte ou la compaction système n'est pas contrôlable ; seul le chargement sélectif et la reprise sur artefacts peuvent être contractés.
