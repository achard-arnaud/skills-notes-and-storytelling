# Storyteller Workbench — spécification consolidée
Date de revue : 2026-10-22. Statut : DESIGN_ONLY. Aucun GO_DEV, runner ni webhook activé par ce document.
Complète docs/workbench-proposal/00..04 ; en cas de conflit, les précisions utilisateur du 22 octobre ci-dessous remplacent la proposition initiale. Les contrats exécutables existants restent inchangés jusqu'au développement autorisé.

## Audit et autorité
main README dernière modification observée : 2026-09-10T15:00:13Z (5a2d819), donc >5 jours ; catalogue incomplet (7/9), architecture-note candidate dans manifest, pas validated.
Backlog du jour retrouvé dans la branche distante design/business-notes-workbench-20261022, HEAD observé 4efa0c380cfb78da1791928e41d6666a51f26640, PR #33 vers dev. Ce n'est pas un HEAD Git détaché accessible : les commits locaux non poussés ne sont pas observables via GitHub.
BN-00..BN-10 sont déjà enregistrés #22..#32 sous #21. Ne pas les dupliquer. #19 tests par impact et #20 contrats par domaine restent candidats séparés.
Le prototype React préexistant est une maquette sans backend ni vrai export, pas une application livrée.

## Sources relues et réutilisation
- Skills-SDLC-superpower README + profiles/ai-maturity-diagnostic/PROFILE.md : adapter la méthode seulement, upstream obra/superpowers pin 44c9b2d6e889982ac18c27d05a19fefe335194e1 ; aucun changement automatique du pin.
- Candidatures-nice workflow/read-manifest.json, references/gate-3-coach.md, gate-4-render.md : route/phase seulement, contexte borné, revue coach, gel puis rendu et QA. La route V3 est explicitement development_only, ne pas la décrire comme autonome disponible. Réutiliser les contrats génériques sans données ni règles CV.
- Candidatures-nice job-alerts/README.md et V3_RUNBOOK.md : collecteur prépare, interface GPT/Claude cherche, receipts et multi-passes ; tâche native distincte du cron. Transposer les états, pas les horaires ni scoring emplois.
- Hivest-ptf-analysis README, docs/agent/gates.md et context-and-resume.md : Extract/Transform/Publish, GO_DRAFT humain, contenu gelé, top claims + inconnues + hashes, reprise ciblée, renderer sans recherche.
- tourisme-etude-historico-geographique skills/storytelling-historical-travel/SKILL.md : séparer evidence scaffold et reader scaffold, écrire à partir des fragments riches, review avant placement, host/return_to, registre des dispositions. Ne pas importer la voix Sarah, longueurs historiques ou exceptions muséales dans les notes business.

## Parcours utilisateur et états
Stepper : 1 Contexte → 2 Analyste & plan → 3 Recherche & preuves → 4 Storyteller → 5 Débrief & relecture → 6 Canvas & formats → 7 Livraison & loopback.
Chaque étape affiche owner, entrées, version, sortie, statut, prochaine action ; boutons Reprendre/Annuler/Retour ciblé. Retour amont invalide seulement descendants affectés.
Entrées : dossier KB ; alerte déjà qualifiée avec provenance ; contexte constitué manuellement ; document/front-end fourni. Résoudre workspace/persona/entité avant retrieval. Profil utilisateur ≠ rôle agent.
Axes indépendants :
- source_mode = kb | alert | manual_context | supplied_document ;
- research_depth = one_shot | deep_search ;
- generation_mode = from-scratch | iterative | feedback-dreaming (retro-engineering reste TODO) ;
- analysis_dimension = business | product | technical ;
- execution_surface = gpt_interface | claude_interface | authorized_runner.
one_shot = plan court + KB ciblée + vérifications nécessaires dans un budget, pas dispense de sourcing. deep_search = questions décomposées, plusieurs passes, contre-preuves et arrêt par couverture/budget. Absence d'outil = NATIVE_SEARCH_PENDING ou BLOCKED_CAPABILITY, jamais recherche prétendue.
L'Analyste peut cadrer avant recherche et réviser ensuite son brief par delta ; les deux versions sont reliées. GO_BRIEF/GO_DRAFT sont des décisions humaines sur une version, pas des statuts donnés par un agent.
Ne pas confondre une validation de plan éditorial, GO_DRAFT, GO_DEV et permission de diffusion.

## Analyste (ancien Coach)
Objectif : décision visée, lecteur, contexte, thèse, hypothèses concurrentes, contraintes, stratégie business et plan de preuves.
Reçoit template choisi ou front-end/document. Match template par jobs/audience/dimensions/format ; proposer au plus 3 options justifiées. Un front-end fourni est une contrainte de présentation ; jamais une preuve. Sans ToC contractuelle, extraction candidate et validation, pas activation du mode retro-engineering.
Recherche KB avant collecte nouvelle ; produit REUSE/REFRESH/NEW par question, sources manquantes et budget.
Sortie AnalysisBrief : brief_id/revision, workspace_id, entity_id, decision_question, reader, thesis, alternative_theses, primary_dimension, template_id/version/sha, evidence_refs, unknowns, research_plan, toc_overlay, side_story_choices, output_intent, gates.
Prompt : « Tu es l'Analyste de décision. Reconstitue enjeux, modèle de valeur, options et contraintes à partir des seules preuves chargées. Distingue fait/inférence/hypothèse/recommandation/inconnu. Propose le template compatible puis un plan adapté au lecteur. Identifie les recherches qui peuvent inverser la décision. Ne rédige pas le rapport et n'améliore pas artificiellement le statut des sources. Retourne un brief versionné, 3 arbitrages maximum et le gate attendu. »

## ToC front-end et overlay
Chargement du template → container liste avec sections/sous-sections à IDs stables, intitulé, consigne courte, obligatoire/optionnel, ordre, slot/container, sélection.
UNE étoile binaire : strategic_importance=true signifie « partie d'importance stratégique » ; augmente la place et l'approfondissement dans l'enveloppe approuvée, jamais la force de preuve. Remplace la proposition étoiles 0–3. Ne pas modifier maintenant le schema v0 ni la maquette préexistante ; migration future explicite.
Drag/clavier ↑↓, suppression si permis, insertion manuelle avec ID custom stable. Empêcher retrait de sections requises et violation de precedence/slot ; expliquer le blocage.
Le bouton Valider transmet explicitement toc_order et sections sélectionnées dans JSON ; ordre visuel, ordre JSON, reader scaffold et export identiques. Le ToC de base reste immuable.
Exemple DTO cible :
{
 "template_ref":{"id":"two-pager","version":"1.2.0","sha":"<exact>"},
 "brief_revision":2,
 "toc_order":["decision","market","custom-001","risks","sources"],
 "sections":[{"id":"market","selected":true,"strategic_importance":true,"instruction":"Éclairer le mécanisme de valeur","container_id":"main"},{"id":"custom-001","selected":true,"origin":"user","instruction":"Comparer option sans IA","container_id":"main"}],
 "side_story_options":[{"kind":"counter_perspective","enabled":true,"slot":"right-panel"}]
}
Exemple illustratif, IDs à résoudre depuis le vrai contrat, pas nouvelle vérité sur le template two-pager.

## Blind-spot
Bouton depuis le ToC : chat simplifié, version du brief analysée, diagnostic et patchs ToC proposés. Aucune application silencieuse.
Revue de niveau stratégie MBA/BCG, sans affiliation revendiquée ; exploration ToT bornée, synthèse de critères et alternatives, pas journal de raisonnement privé.
Prompt : « Revois le brief et le ToC comme un contradicteur senior de stratégie. Examine trois branches indépendantes : 1 hypothèse business et causalité/économie, 2 alternatives, parties prenantes et exécution, 3 preuves, inconnues et lecture décisionnelle. Compare leurs objections, retiens celles qui peuvent changer la décision, puis fais une seule auto-revue de tes recommandations. Produis au plus cinq angles morts avec gravité, preuve ou manque, conséquence, question falsifiante, recherche ciblée et patch ToC éventuel. Ne fabrique ni fait ni autorité. Termine par conserver/recentrer/rechercher et un diff proposé. »
Budget standard 1 revue + 1 vérification ciblée ; profondeur supplémentaire seulement autorisée. Confirmation utilisateur pour appliquer patch, réordonner ou rouvrir recherche. Historique et rejet conservés.

## Side stories et multi-container
Types permis par template : contre-perspective, dézoom, exemple, portrait, méthode ou autres explicitement déclarés. Toggle désactive un encart ou sous-partie autorisé ; toute omission reçoit une disposition. Un risque/gate obligatoire ne disparaît pas parce qu'un encart est masqué.
Contrat template : allowed_side_story_types, container_ids, slot_rules, capacity, ordering_constraints, required_sections. Panneau vertical droit uniquement si ce template le permet ; sinon placement inline/interstitial compatible, pas slot inventé.
Distinguer story principale, side story et coordination multi-container. SideStory = objet éditorial, pas preuve nouvelle. Enregistrer source_refs/claim_refs, host_section/paragraph, trigger, return_to, type, selection, rationale et lifecycle.
Promotion side→main = arbitrage narratif explicite, jamais promotion de factualité.
Un seul owner compose les containers ; relecture continuité et couverture avant rendu. Aucun encart non résolu déplacé arbitrairement en fin de document.

## Storyteller
Prompt : « Reçois le brief approuvé, template épinglé, ToC ordonné, choix de side stories et paquets de preuves. Planifie sections, angles et transitions avant rédaction. Cherche dans la KB seulement les manques du plan. Écris depuis les fragments sourcés riches, utilise les claims comme contrôle factuel, sépare récit principal/encarts/containers. Chaque unité éligible est incluse, déplacée ou écartée avec motif. Préserve les nuances et contradictions ; une longueur cible n'autorise pas la perte silencieuse de matière stratégique. Retourne draft, reader scaffold et ledger de couverture. »
Plan par section : narrative_job, angle, evidence_ids, word_budget indicatif, container_id, dependencies, side_story_ids.
Recherche complémentaire matérielle rouvre Analyste/GO_DRAFT ; le Storyteller ne change pas le template canonique.
Distinguer fragments→claims graph (preuve) et reader scaffold (ordre de lecture). Ne pas transformer le graphe entier en récit ni conserver un claim par une phrase vide.
Check anti-inflation, anti-répétition, attribution, contradictions, couverture du brief et ToC explicite.

## Débriefer, proofreader, Canvas et sortie
Débriefer : relire demande→brief→récit, constater écarts et arbitrages, état des questions, retours humain. Débrief utilisateur peut retourner à Analyste ou Storyteller.
Proofreader : conformité, contre-perspective, qualité de lecture ; signaler incohérences, réécritures proposées en diff, sans ajouter de faits. 1 réparation puis 1 vérification ; récidive matérielle → issue + gate ciblé.
Contenu accepté → freeze par hash → Canvas pour édition finale/composition. Toute édition sémantique ou ajout factuel invalide freeze et QA dépendante ; typo/style ne dispense pas de version/hash et QA de rendu.
Choisir formats en amont (contrainte) puis confirmer à la livraison : MD/HTML/PDF/DOCX selon capacités réellement disponibles ; pas de PowerPoint promis.
Artifact receipt par format : frozen_content_sha, edited_revision_sha, renderer_version, path, byte_hash, qa_status, preview_ref, delivery_status. Download seulement si fichier existe et QA requise passée. Échec PDF ne bloque pas MD accepté.
Renderer sans recherche ni changement d'analyse ; QA visuelle réelle pour PDF/DOCX, pas un simple schéma vert.

## Open Canvas : identité et bootstrap à instruire
Hypothèse identifiée : https://github.com/langchain-ai/open-canvas (orthographe Open Canvas, distinct de Canva). API GitHub relue le 22/10/2026 : archived=true, MIT, dernier push 2026-02-25. Ne pas confondre éditeur Markdown agentique et moteur de mise en page PDF/DOCX.
README upstream : monorepo Yarn, packages partagés, apps/web et apps/agents, LangGraph local, Supabase auth, traçage LangSmith et configuration fournisseurs. Ces prérequis ne sont pas automatiquement des exigences de notre démonstrateur.
Lot discovery : épingler commit + licence, inventorier réutilisation UI vs fork complet, compatibilité Node/Yarn et dépendances, dépendances distantes et licence transitive, coût de maintien et sortie.
Après GO_DEV seulement : bootstrap dans branche/spike isolé ; verrouiller deps ; lancer build partagé, agent local puis web selon README exact ; fixtures synthétiques, secrets côté serveur, aucune KB privée ; vérifier import rapport, sélection+édition ciblée, diff, versions, undo, mapping section/claim et re-export.
Adaptateur ReportEditor import/export DocumentRevision avec stable IDs, content hashes, selection ranges, edit diff et provenance ; pas de réécriture autonome des preuves.
Mémoire/reflection automatique upstream désactivée ou cloisonnée en propositions sans promotion KB ; isolation persona/workspace. Aucun remplacement automatique par Canva SaaS.
ADR BUILD/PLUGIN/SERVICE/HYBRID/DEFER ; adapter mince préféré à dépendance monolithique si faisable. Échec du spike documenté, arbitrage humain avant alternative.

## Acceptance end-to-end cible (pas exécutée)
Fixture synthétique : alerte + KB fraîche + source périmée + contradiction ; template deux containers ; étoile unique ; section ajoutée, retirée et reorder valide/invalide ; blind-spot accepté/rejeté ; one-shot puis deep-search delta ; crash/reprise ; draft avec side story ; édition factuelle Canvas ; QA indépendante par format.
Exiger : ordre UI=JSON=export ; aucune fuite persona ; pas d'upgrade de preuve ; aucune suppression silencieuse ; recherche non disponible visible ; receipt fiable ; GO_DEV absent interdit toute implémentation.
