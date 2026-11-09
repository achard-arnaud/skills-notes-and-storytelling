# Bootstrap Sri Lanka → diagnostic business : audit source

Audit ciblé du 7 novembre 2026. Source : `achard-arnaud/tourisme-etude-historico-geographique`, commit **fb83e0e759d1fef78bbb2cca766fecbb23eda8d5**. Dépôt lu sans mutation Git ; aucun test exécuté dans cette passe. Ce document intermédiaire décrit les mécanismes observés, pas une certification générale du dépôt.

## Constat essentiel : trois structures distinctes

1. **Arc** : colonne vertébrale du cas. Dans l'histoire, il est délimité par des ruptures du système ; pour le business, un arc devient un cas d'entreprise borné par un mandat et une question de décision, éventuellement décliné en séquences argumentatives.
2. **HIL** : vues analytiques transversales qui éclairent les éléments réellement utilisés. Elles ne sont ni huit chapitres obligatoires, ni huit angles à injecter dans chaque paragraphe, ni des validations humaines acquises.
3. **Scaffolds** : `story_scaffold.json` cartographie les preuves et relations ; `reader_scaffold.json` fixe l'ordre éditorial. Le graphe probatoire ne dicte pas automatiquement l'ordre de lecture.

Le terme utilisateur « piliers/HITL » recouvre ici les axes HIL et leurs points de revue. Le dépôt distingue bien le scope HIL d'un paragraphe du jugement de revue indépendant ; ne pas transformer un label de pilier en accord humain.

## Les huit piliers exacts retrouvés

Autorités : `docs/architecture.md` §HIL ownership ; `SKILL.md` étape 6 ; index réels dans `examples/sri_lanka_pre_1948/02_hil/*/baseline.json`.

| ID / dossier source | Vue analytique réelle | Ce qu'il faut transférer |
|---|---|---|
| HIL-01_institutions-chronology | Institutions et chronologie | Gouvernance, mandats, responsabilités et dynamique de transformation |
| HIL-02_geography-environment | Géographie et environnement | Contraintes physiques, sites et territoires ; climat/vents sont des sous-thèmes |
| HIL-03_economy-infrastructure | Économie et infrastructure | Unité économique, actifs, financement, chaînes de valeur |
| HIL-04_society-demography | Société et démographie | Acteurs, compétences, travail et adoption, après adaptation métier |
| HIL-05_religion-culture-legitimacy | Religion, culture et légitimité | Principe d'analyse des représentations/incitations ; ne pas copier le domaine religieux |
| HIL-06_security-coercion | Sécurité et coercition | Risques, résilience et contrôle, en évitant l'équivalence forcée coercition/cybersécurité |
| HIL-07_regional-global-system | Systèmes régionaux et mondiaux | Marchés, concurrence, partenaires et contexte macro/sectoriel |
| HIL-08_historiography-bias | Historiographie et biais | Critique des sources, intérêts, contre-hypothèses et dérives narratives |

**Aucune correspondance 1:1 ne s'impose.** Les piliers business doivent être reconstruits à partir du mandat et du corpus. En particulier, opérations industrielles énergie et fonctions corporate transverses doivent avoir des frontières distinctes ; data et IA constituent aussi des axes différents, connectés par leurs dépendances. Le nombre huit décrit la source, pas une contrainte automatique pour la cible.

## Matrice de transfert

| Mécanisme et chemins vérifiés | Décision | Adaptation business / oracle de vérification |
|---|---|---|
| `SKILL.md` ; `docs/architecture.md` : recherche → composition → Markdown canonique → export | **Réutiliser** la séparation | Une sortie HTML ou un encart ne crée pas une preuve ; un état explicite désigne le canonique, jamais un nom de fichier supposé. |
| `skills/structuring-chronological-arcs/SKILL.md` : entrée, question, drivers, amplificateurs, conséquences, non-causes, permanence, sortie | **Adapter** | Remplacer le découpage chronologique historique par le mandat et les transitions de décision. Un apport documentaire ne crée pas seul un nouvel arc. |
| `02_hil/*/baseline.json` ; `skills/storytelling-historical-travel/references/paragraph_review_checklist.md` | **Adapter** | Registre de piliers business, frontières et exclusions ; affectations multiples seulement si elles éclairent le claim. Rejeter un pilier de paragraphe non soutenu par ses claims. |
| `scripts/build_story_scaffold.py` | **Réutiliser le principe**, adapter les chemins/contracts | Vue globale limitée aux IDs, titres, quantités, connexions, questions et files d'attente ; rédaction sur paquet local avec bridges adjacents. Aucun chargement intégral par défaut. |
| `scripts/import_reader_scaffold.py` | **Adapter**, sans dépendance DOCX obligatoire | Scaffold éditorial explicite avec ordre, hiérarchie et slots d'encarts. Ne pas importer les volumes, la voix ou le sommaire Sri Lanka. |
| `skills/maintaining-wiki-and-graph/SKILL.md` ; `scripts/graph_link_audit.py` ; `docs/zettelkasten_graphlight_decision.md` | **Réutiliser** les invariants | Tous endpoints et tags résolvent ; relation typée et provenance pour interprétation/causalité ; bridge orienté conforme ; doublon `from/relation/to` rejeté. Densité de liens ≠ qualité de démonstration. |
| `docs/SOP_SIDE_STORIES.md` ; `templates/side-story.json` ; `templates/side-stories/type_profiles.json` | **Adapter** les types et non les règles de preuve | Candidate → validated → promoted → retired ; home arc, purpose, raison hors-tronc, payoff, placement, lineage, retour résolvable. Type `method`/apparatus peut légitimement ne pas revenir au tronc. |
| `templates/side-stories/analytical-focus.json` ; `docs/SOP_SIDE_STORIES.md` | **Adapter** | Question, thèse, contrastes bornés, mécanismes avec statut, callback et takeaway : utile au contrechamp fournisseur/vision/ROI ; exclure le format A4/deux pages et les seuils typographiques comme contraintes universelles. |
| `skills/zooming-geographic-scales/SKILL.md` | **Adapter** | Échelles équipement/site/portefeuille/groupe/secteur, définies selon l'étude ; changement d'échelle accompagné d'un canal de transmission. Site performant ≠ groupe performant, benchmark ≠ ROI local. |
| `scripts/paragraph_review_gate.py` ; checklist de revue ; `scripts/paragraph_repair_loop.py` | **Réutiliser le contrôle**, adapter le jugement | Trois revues séparées : contenu/preuve, style business, pertinence piliers. SHA du texte + contrat de style ; réécriture invalide la revue. Génération ≠ revue. Réparation bornée à 3 tentatives puis disposition motivée, pas omission silencieuse. |
| `scripts/audit_context_budget.py` ; `tests/test_context_budget_runtime.py` | **Réutiliser et renforcer** | Compter orchestrateur + skills effectivement routées + compagnons Markdown transitifs + fichiers runtime explicites. Refuser un faux « dernier run » sans manifeste. Mesure actuelle en mots, pas tokens réels ni compaction technique. Ajouter journal des lectures effectives, bornes par tâche et paquet de reprise. |
| `00_method/output_state.json` mentionné dans `SKILL.md` ; manifests de run | **Adapter** | État de reprise versionné : tâche, entrées/SHA, sorties/SHA, preuves, décisions, blocages, prochains IDs, limite de contexte et propriétaire writer. L'agent reprend depuis ces artefacts après interruption. |
| Voix Sarah, récit de voyage, causalité historique spécifique, règles iconographiques cartographiques | **Exclure comme obligations de la cible** | Préserver seulement la séparation backstage/frontstage et l'exigence de clarté. Une revue business François remplace la signature historique ; les cartes deviennent des visuels optionnels pertinents. |

## Subtilités à conserver

- **Couverture n'est pas promotion.** La SOP distingue `traced`, `declared`, `discovered`, `untracked`. `untracked == 0` prouve la comptabilisation, pas la qualité probatoire ; un legacy fragment déclaré reste une dette et ne peut être promu sans lineage.
- **Scaffold partiel n'est pas enquête finie.** Une coque d'arc `shell` peut porter une structure ; elle ne vaut pas `researched` ou recap-ready. Un slice `partial` peut livrer seulement ses unités prouvées.
- **État éditorial et factuel sont distincts.** Une révision globale de forme invalide les revues de paragraphes dans le scope sans détruire les validations factuelles indépendantes ; une source changée invalide en revanche ses dépendances probatoires.
- **Intention utilisateur n'est pas preuve.** Un futur exemple VisioSense décrit une piste tant que les sources et l'identité produit ne sont pas vérifiées.
- **Graphes différents.** Navigation de recherche, preuve et ordre narratif doivent rester distincts même si leurs IDs se relient.
- **Budget borné n'est pas compression du fond.** Si un paquet dépasse le budget, scinder la tâche/hydrater localement ; ne pas supprimer les limites, contradictions ou faits requis pour passer le contrôle.
- **Drop logique seulement.** Un manifeste et un handoff permettent de ne plus recharger certains matériaux ; aucun de ces scripts ne vide la fenêtre de contexte réelle ni ne force sa compaction.

## Dix petites tâches recommandées pour le board

| Tâche | Entrée bornée | Artefact de sortie | Critère concret de validation |
|---|---|---|---|
| B01 — Épingler le donneur | HEAD + inventaire de chemins utiles | registre de transfert avec commit et blobs | Toute règle reprise renvoie à un chemin réel au commit source |
| B02 — Fixer arc/brief business | mandat utilisateur + contrat arc source | contrat brief/arc candidat | Une pièce nouvelle n'élargit pas le mandat sans décision explicite |
| B03 — Définir les piliers | huit HIL source + mandat métier | registre piliers candidat, frontières/exclusions | Industrie et corporate séparés ; data ≠ IA ; aucun quota imposé par paragraphe |
| B04 — Séparer les scaffolds | builder et importer source | schémas topology / reader order | Un changement d'ordre lecteur ne modifie pas les claims ou la confiance |
| B05 — Définir lineage de composition | SOP + types source | contrat side-story business | Encadré non sourcé bloqué ; retour invalide bloqué ; méthode sans retour admise |
| B06 — Écrire les contre-tests de graphe | graph audit source | fixtures positive et négatives | Endpoint/tag fantôme, bridge inversé et relation dupliquée rejetés |
| B07 — Adapter les revues | checklist + repair loop | contrat revue business | Prose modifiée invalide revue ; génération et revue même passe rejetées |
| B08 — Produire les paquets de contexte | budget auditor + routed manifest | paquet tâche, registre lecture et handoff | Compagnon caché compté ; input absent/SHA périmé bloqué ; budget déclaré en mots/proxy |
| B09 — Simuler une reprise froide | sorties B02–B08 seules | receipt de reprise | Agent/reviewer retrouve mandat, état, prochain ID et limites sans conversation complète |
| B10 — Auditer un slice synthétique | brief public factice + quelques sources/claims | graphe + scaffold + paragraphe + encart candidat | Zéro référence non résolue ; aucune conclusion sur GreenYellow ni promotion humaine simulée |

## Limites de cette passe

Audit orienté mécanismes : lecture du root orchestrateur, architecture, SOP side stories, skills arcs/zoom/graph, checklist et scripts scaffold/review/context/graph. Les 23 sous-skills n'ont pas fait l'objet d'une lecture intégrale et le corpus historique n'a pas été réaudité. Les tests sont identifiés comme oracles réutilisables ; ils n'ont pas été exécutés ici. Les apports GreenYellow restent à rapprocher du brief et des fichiers réellement accessibles par l'orchestrateur principal.
