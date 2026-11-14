# Interfaces v0 — expérimentation, sans changement des contrats canoniques

Fichier d'étude JSON autonome, UTF-8 :
- id, mandate {question, scope, audience}, pillars [{id,title,scope}], sources [{id,kind,access,title,locator}], fragments [{id,source_id,locator,text}], claims [{id,text,status,fragment_ids,pillar_ids}].
- statuts claim : supplied_claim, attributed_claim, inference, hypothesis, verified_fact, unknown. verified_fact exige verification {reviewed:true, source_ids:[...], note:...}, sources consultées et fragments ; aucune promotion automatique à l'import.
- relations [{id,from,to,kind, rationale}] relient uniquement des claims ; kind : supports, contradicts, depends_on, illustrates, compares, contextualizes, causal_hypothesis. La causalité reste hypothèse explicitée.
- sections [{id,title,claim_ids,pillar_ids,paragraphs:[{id,text,claim_ids,pillar_ids,review:{evidence:false,editorial:false}}]}]. Leur ordre est le reader scaffold. Les relations ne dictent pas cet ordre.
- side_stories [{id,kind,title,claim_ids,pillar_ids,parent_section_id,return_to,state,reason_outside,payoff,text}]. return_to résout une section ou un paragraphe ; state candidate|validated|promoted|retired ; kind detour|dezoom|also|method|false_lead|portrait|object_focus|comparator|callback|analytical_focus. dezoom ajoute scale_from,scale_to,mechanism. La validation structurelle ne promeut rien.
- Toutes les listes peuvent être vides pendant l'enquête ; la commande validate donne erreurs structurelles et lacunes éditoriales distinctes. Les IDs doivent être uniques ; les références doivent résoudre. Les hypothèses peuvent rester sans fragments. Le rendu marque les lacunes et statuts.

runtime.py (stdlib) : fonctions import_markdown(path, study_id), validate_study(study), build_graph(study), main CLI import/validate/graph. Import délimité aux titres/blocs, localisateurs lignes exacts et IDs déterministes ; préserver texte et provenance, pas de claim automatiquement vérifié. Pas de réseau.

context.py (stdlib) : fonctions/CLI pour valider le DAG de board.json, sélectionner tâche ready, construire un packet borné depuis les seuls chemins déclarés, produire checkpoint avec empreintes et RESUME ; refuser chemins hors racine et dépassement de budget, cycles et dépendances manquantes. UTF-8 bytes mesurés, tokens estimés étiquetés. Aucun effacement réel de fenêtre de contexte.

render.py (stdlib) : render_study(study)-> HTML autonome avec onglets accessibles Récit/Piliers/Preuves/Side stories, texte échappé, liens d'ancres internes résolvables. Les piliers filtrent les vues, sans imposer huit sections. Compatible file:// sans dépendance ni CDN. N'annonce pas de rendu Mermaid réel sans moteur présent ; montrer source Mermaid explicitement si fourni.

Tests négatifs significatifs pour chaque contrat. Aucun auteur ne clôture les tickets sans validation et reçu par le coordinateur.

## Enveloppe analytique v1 — #295.A1

`analysis.py` expose `validate_analysis_envelope(envelope, study)` (stdlib, sans mutation,
réseau ni génération). Contrat : `schemas/analysis-envelope.v1.schema.json`. L'enveloppe
reste extérieure à l'étude et n'est jamais ajoutée à l'entrée de `writing.prepare_from_scratch`.

- `schema_version: "1.0"`, `study_ref: study.id`, `input_revision` : SHA-256 obtenu par
  `writing.study_hash({k: study[k] for k in writing.EVIDENCE_KEYS if k in study})`.
  La présence/absence d'une clé fait partie de la révision. Sources, fragments et claims
  modifiés la périment ; sections, paragraphes et mise en page seuls ne la modifient pas.
- `analyses` non vide : `id`, `question_ref` (identité stable indépendante des sections),
  `question`, `method`, `method_version`, `scope`, `as_of` (date ISO réelle),
  `input_claim_refs`, `findings`, `counterevidence`, `unknowns`, `state`, `needs_research`.
  `method_version` est une version déclarée non vide ; sa présence ne prouve pas sa
  résolution dans un catalogue. La résolution de méthode/question sera une tranche séparée.
- `findings` conserve les objets `statement`, `status`, `claim_refs` non vide ; statuts :
  attributed_claim, inference, hypothesis, recommendation, unknown. Une recommandation
  reste une analyse ; aucun statut ni claim n'est créé dans l'étude. Contre-preuves et
  inconnues restent des textes conservés, même sans fragment disponible.
- `state: partial` autorise zéro finding et zéro claim d'entrée, exige `needs_research: true`
  et au moins une inconnue textuelle non vide. `complete` exige au moins un finding et
  un claim d'entrée ; il qualifie la matière structurelle, jamais la vérité ou l'approbation.
  Aucun `affects_blocks` requis ni accepté ici : le binding narratif est différé.
- Identifiants d'analyse uniques et distincts des claims ; chaque référence de claim
  d'entrée ou de finding résout dans l'étude fournie. `study_ref` étranger ou révision
  périmée sont refusés même si les IDs de claims coïncident.

Retour : `valid`, `errors`, `structural_errors`, `reference_errors`, `gaps`,
`human_approval: false`. Les références sont contrôlées après la structure ; les lacunes
ne deviennent pas des erreurs structurelles. Le validateur contrôle l'identité et l'index
claims nécessaires ici ; la validation complète de l'étude reste `runtime.validate_study`.
Il ne résout pas de catalogue, ne valide pas la sémantique, ne lie pas de blocs et
n'invalide pas le DAG. Le helper de schéma interne ne couvre que le vocabulaire du contrat
local publié ; ce n'est pas une bibliothèque JSON Schema générale.

### Voie legacy explicite

`validate_legacy_analysis_result(payload, study)` lit sans migration le contrat donneur
`75c8293de6984c6fac80e016528bdfa4ec019226`, blob `b2303d0bd50e23a7c7a2ad7eb71b896fcacdc446`
(copie exacte dans `$defs.legacyResult`). Il conserve les onze champs et les contraintes,
dont `affects_blocks`, `findings` et `input_claim_refs` non vides. Pas de détection
implicite par absence de version : le demandeur choisit cette API distincte.
Les claims sont résolus contre l'étude passée ; l'origine inter-études, la révision
historique et l'existence des blocs ne sont pas démontrables par ce payload et restent
une limite explicite dans `gaps`. Aucun appel à `resolve_method.select` ni faux bloc.

Oracles : [mapping #303](ANALYSIS-CONTRACT-MAPPING.md) et sa fixture synthétique ;
régression : `python3 -m unittest discover -s diagnostic-complet/tests -p 'test_analysis.py' -v`.
#295 reste ouvert : IntentBrief/AnalysisPlan, résolution par question, liaison tardive,
synthèse métier et invalidation des descendants ne sont pas livrés par A1.

## Intention et plan d'analyse v1 — #295.A2

`planning.py` expose `validate_analysis_plan(plan, brief, study)`,
`resolve_question(plan, brief, study, question_ref)` et
`validate_planned_analysis(envelope, plan, brief, study)`. Fonctions stdlib,
sans mutation, collecte réseau, génération, calcul d'adoption ni approbation.
Le schéma `schemas/analysis-planning.v1.schema.json` contient AnalysisPlan et
`$defs.intentBrief`. Le helper structurel local accepte désormais une racine de
schéma explicite et les entiers/minimum ; les contrats A1/legacy restent identiques.

IntentBrief contient `schema_version: "1.0"`, `id`, `study_ref`, `question`, `scope`,
`audience`, `intent`, `decision_requested` booléen explicite et `as_of` ISO.
Cette tranche couvre `traction-commerciale` et `clients-360`. Les six autres
finalités et les parcours business/pédagogiques ne sont pas activés par ce contrat.
Aucune recommandation/pilote n'est déduit d'un nom d'entreprise ou de produit.

AnalysisPlan contient version, `id`, `intent_ref`, `study_ref`, `input_revision`
(projection evidence-only A1), `intent_revision` (`writing.study_hash(brief)`),
`catalog_revision` (`writing.study_hash(planning.CATALOG)`), `questions` non vide et
`budget` (`max_publications`, `max_queries`, entiers positifs). Le budget est un
plafond déclaré, pas un compteur de consommation ou un ordonnanceur de recherche.
Une mise en page seule ne périme pas les preuves ; étude, brief ou catalogue
modifiés imposent une relecture des révisions. Ni plan ni brief ne deviennent
une clé de l'étude ou une entrée de `writing.prepare_from_scratch`.

Chaque question porte `id`, `question`, `method`, `method_version`,
`input_claim_refs`, `evidence_map` (exigence → claims d'entrée), `unknowns`,
`queries` et `stop_condition`. Les IDs sont uniques et disjoints des identités
étude/brief/plan/claims. Référence étrangère, exigence inconnue/dupliquée ou
claim hors entrées est refusé. Une exigence sans claim reste une lacune ; aucun
fragment ni résultat factice n'est construit. Référencer un claim ne démontre
pas qu'il prouve sémantiquement l'exigence : cette revue appartient à l'analyste.

`workflows/analysis-methods.v1.json` est une adaptation minimale et attribuée du
donneur `75c8293...`, catalogue `1821cd99`, manifest produit `91a3a46b` :
`product.adoption`, version = blob de note `514cac66e7fe571d85e2dd71e65142f481148b20`.
La note est liée à ce commit exact. Exigences : population éligible, événement
utile, fréquence attendue, cohorte et période. L'activation requiert la finalité
et la version exactes ; aucune méthode supplémentaire n'est implicite. La note
reste candidate ; aucune conformité externe ni donnée réelle n'est attestée.

Le paquet de question contient copies du brief, question, méthode, claims et
budget, les révisions, les lacunes, `analysis_executed: false`,
`human_approval: false` et l'état `ready_for_analysis` ou `needs_research`.
Il n'appelle pas la voie legacy `resolve_method.select` et ne fabrique pas de bloc.

Une enveloppe A1 **fournie par l'analyste** peut ensuite être comparée au plan :
question/méthode/version/scope/claims d'entrée exacts ; au plus un résultat par
question. Une question sans analyse reste une lacune. Un résultat `complete`
masquant des lacunes du plan est refusé ; un résultat `partial` conserve ses
inconnues. Une recommandation exige `decision_requested: true`. Cette comparaison
ne prouve ni la vérité de l'analyse, ni l'originalité historique du plan fourni,
ni une analyse exécutée par le script. La production et la revue des résultats
restent des opérations distinctes ; l'enveloppe A1 n'est pas migrée silencieusement.

Validation : `python3 -m unittest discover -s diagnostic-complet/tests -p 'test_planning.py' -v`.
Les fixtures sont synthétiques. S1 reste ouvert pour synthèse et invalidation des
consommateurs ; S2/S3 et le rendu ne sont pas déclarés livrés par cette tranche.
