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
