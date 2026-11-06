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
