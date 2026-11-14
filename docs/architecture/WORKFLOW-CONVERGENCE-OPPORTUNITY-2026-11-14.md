# Convergence des workflows de recherche, analyse et composition
Étude d’opportunité du 14 novembre 2026. Proposition à arbitrer, sans migration de contrats ni de runtime.

## Baselines et portée de la revue
- Storytelling main : 7000c86a7e54cafc68c5bb5ada9aeed5df186aae.
- Candidat de refonte : ea4c4cde38f4d6c0aae0a6dd8c74a2be249ae018.
- Candidatures Nice dev : 1bd568775b7903623c2ae21d892c791963b5756a.
- Candidatures Nice main : 710c0db29d865af0c15d3dced64f72aa65a2c710.
La branche dev de storytelling répond Branch not found. Le module diagnostic-complet est déjà présent dans main. Son README continue de décrire une livraison sur dev sans promotion main ; cette mention historique ne reflète donc plus la présence des fichiers. La revue n’établit pas la date ni la décision de leur intégration.
Inventaires récursifs main et Candidatures obtenus sans troncature. Lecture ciblée de contrats, procédures et modules ; aucun code exécuté, aucune CI récente vérifiée, aucune évaluation de qualité rédactionnelle relancée. Température du backlog sur 25 issues ouvertes triées par mise à jour, lecture détaillée des sujets structurants. Ce périmètre ne constitue pas un audit complet du backlog.

## Décision proposée
Réutiliser diagnostic-complet comme socle de données, provenance, reprise et composition. Y intégrer les résultats analytiques du candidat et l’hygiène des transitions de Candidatures. Garder un point d’entrée documentaire principal et quatre phases de travail. Les verticales orientent les questions et les contrôles ; elles ne créent pas quatre moteurs divergents. Une phase est une unité de responsabilité et de reprise, pas automatiquement une skill ou un agent.

Une skill peut porter ce workflow en lecture progressive. Elle n’offre, par sa seule présence, ni persistance, ni contrôle de transitions, ni budget effectif. Ces fonctions appartiennent au projet. Prévoir au départ une compétence principale de conduite d’étude et une compétence de rendu séparée quand le support exige des outils. Une analyse spécialisée devient une skill autonome si elle possède un mandat réutilisable, des entrées/sorties utiles et des évaluations propres ; une méthode courte peut rester une référence.

## Grille comparative
| Critère | Main et candidat léger | Diagnostic complet / GreenYellow | Candidatures Nice |
|---|---|---|---|
| Finalité | Notes multi-formats ; candidat avec huit finalités produit | Enquête et récit long depuis une étude structurée | Adaptation d’un dossier de candidature à une offre |
| Recherche | Chaîne documentée ; candidat relance le corpus et propose 40–70 publications approfondies | ResearchMap, collecte et couverture ; recherche autonome non livrée d’après la documentation | Offre figée, exigences, retrieval dans la KB de la persona |
| Analyse métier | Main porte des trames détaillées ; candidat ajoute catalogue MBA et AnalysisResult | Huit compétences par pilier ; sorties surtout claims, lacunes et candidats d’encarts | Couverture exigence→fait→zone ; pertinence professionnelle, pas diagnostic stratégique général |
| Chaînage observable | Sélecteur méthode/finalité/bloc ; il rend un chemin et un contrat | Source→fragment→claim→section/paragraphe ; reprise et invalidation ciblées | A1→A2→A3→A4, handoffs versionnés, réouverture des descendants |
| Narration | Procédure générique et références ; rendu aimé non reproduit | Scaffold lecteur, tronc, revue, encarts et retours | Composition dans zones et budgets du template |
| État et contexte | RunContext documentaire et références ; orchestration légère | Paquets locaux, hashes, DAG de tâches, budgets mots/octets | Process, read-manifest, artefacts d’étape, BUS synchronisé par mutations |
| Limite démontrée | Tests de liaison ne démontrent pas l’usage analytique dans une sortie | writing.py prépare et conserve ; il ne génère pas la prose ; carte des skills annonce rerank et fill partiellement externes | Process manuel ; scripts ne génèrent ni recherche ni texte via LLM |
| Coût d’intégration cible | Facile en surface, profondeur et reprises encore à relier | Adaptation de contrats et généralisation de profils | Forte adaptation du domaine ; risque de copier cardinalités CV, gates et déploiement BUS |
| Usage recommandé | Façade, finalités, méthodes et chartes | Socle technique minimal de l’étude | Donneur de patterns de transitions, traçabilité et QA |

## Ce que l’on corrige dans les hypothèses de départ
Main contient déjà une procédure commune, des contrats de preuves et le sous-projet long. La séparation main/dev ne représente plus exactement les deux architectures.
Le candidat n’a pas zéro liaison MBA : resolve_method.py contrôle méthode, finalité et bloc, et AnalysisResult porte question, claims d’entrée, résultats, contre-preuves, inconnues et blocs affectés. La lacune est sa consommation démontrée dans le parcours d’étude.
Le sous-projet GreenYellow ne se réduit pas au renderer. Le placement des side stories relève de la composition ; leur rendu relève du renderer. La distinction est déjà documentée et doit être conservée.
Les skills analytiques GreenYellow demeurent parfois attachées à un passage de tronc et à un paquet de rendu d’encart. C’est un bon raccord éditorial mais un couplage prématuré pour une enquête qui doit produire ses conclusions avant de choisir le récit.
Le contrat AnalysisResult candidat exige affects_blocks avant que le scaffold ne soit établi. Pour le workflow cible, prévoir d’abord des questions analytiques et lier ensuite les résultats aux blocs. Adapter cette frontière exige une migration explicite et une compatibilité avec les fixtures historiques.

## Workflow cible en quatre phases
| Phase | Travail | Sortie durable minimale | Retour ciblé |
|---|---|---|---|
| 1. Contexte et recherche | Identifier l’entité, le mandat, les études existantes et leur fraîcheur ; constituer la carte des questions, le budget et le corpus | Mandat, sources/fragments/claims, questions ouvertes, état de collecte | Nouvelle question ou contre-preuve issue de 2 ou 3 |
| 2. Analyse et synthèse | Sélectionner des méthodes selon la question et les preuves disponibles ; appliquer, croiser, qualifier les limites | Résultats analytiques et note de synthèse avec arguments, alternatives et questions résiduelles | Recherche complémentaire en 1 ; autre analyse en 2 |
| 3. Direction narrative | Choisir tension, lecteur, angle principal, ordre des questions, niveau de détail, tronc/encarts et contraintes du support | Brief narratif et scaffold reliés aux résultats et claims | Analyse manquante en 2 ; mandat ambigu en 1 |
| 4. Rédaction, revue et livraison | Rédiger bloc par bloc ; relire le récit et les preuves ; produire et vérifier le rendu | Contenu, références, exports et revue ; état de reprise | Défaut de récit en 3 ; de raisonnement en 2 ; de preuve en 1 ; de géométrie dans le rendu |

Un même opérateur peut conduire les quatre phases. Un agent séparé se justifie par une tâche indépendante, un contexte volumineux ou une revue dont on veut l’indépendance. Aucun nombre d’agents ne découle du nombre de phases.
Les documents courts utilisent le même contrat logique avec champs proportionnés ; ils ne produisent pas une multitude de fichiers vides. Le volume de recherche dépend de la profondeur et du corpus disponible. Une référence déjà validée est réutilisée avec sa date.

## Rendre le chaînage analytique réel
Exemple de contrat à expérimenter :
- Question : quels segments bénéficient du mécanisme observé ?
- Méthodes candidates : segmentation, chaîne de valeur, analyse des usages ; sélection et refus motivés.
- Entrées : claims et cas attestés, scope, dates, limites.
- Résultat : segments comparables, mécanisme de valeur, contradictions, inconnues, statut et références.
- Analyse suivante : 4P ou économie unitaire uniquement si une question résiduelle le requiert.
- Synthèse : ce qui converge, ce qui reste alternatif, ce qui change la compréhension.
- Narration : assigner les résultats retenus aux blocs, avec leur conclusion qualifiée.
La bibliothèque sert d’instrument. Une fiche « Porter » consultée ou une clé de manifeste résolue ne vaut pas une analyse Porter exécutée.

Conserver un seul espace logique de preuves et d’analyses. Le graphe probatoire établit provenance et dépendances ; la carte de questions guide l’enquête ; le scaffold guide le lecteur. Un même stockage peut porter ces vues sans les confondre. Ajouter seulement les relations nécessaires au cas, avec statut et justification.

## Budgets et mémoire hors skill
Le run possède ses budgets de recherche et de contexte ; la skill explique comment les utiliser. Déclarer limites de temps/requêtes/lectures quand connues, allocation par question, consommation observée, couverture et conditions d’arrêt. Un plafond de mots d’un paquet ne contrôle pas le budget de recherche externe. Ce sont deux dimensions.
Réutiliser sources, claims et analyses datés par entreprise/produit ; les sorties sont des vues de ce même dossier. Une nouvelle source invalide les descendants concernés. Les préférences éditoriales du projet gardent provenance et portée, et ne deviennent pas des faits sur l’entreprise.
Un état courant et un journal de transitions suffisent pour le premier parcours. Le bus de Candidatures devient pertinent si plusieurs exécuteurs doivent réconcilier des événements, des reprises ou des publications. Pour un opérateur séquentiel, son coût doit être justifié par un incident que les fichiers et hashes ne résolvent pas.

## Taxonomie maintenable
- Agent : exécuteur doté d’un mandat, de droits et d’un paquet de contexte.
- Skill : procédure réutilisable pour atteindre un résultat, avec entrées/sorties et ressources.
- Référence : méthode, charte ou politique chargée à la demande.
- Asset : schéma, exemple, données de test ou ressource de rendu.
- Artefact de run : état, recherche, résultat analytique, scaffold ou sortie datée.
Un fichier interne ne devient pas une sous-skill par sa taille. Les références aux méthodes précisent quand les utiliser et quel résultat en attendre. Les sorties d’analyse restent indépendantes du support final.

## Effort et trajectoire de convergence
| Lot | Effort relatif | Acceptation |
|---|---|---|
| 0. Réconcilier état et autorités | Faible | Inventaire actuel, docs de branche corrigées, propriétaire par contrat, pas de double moteur |
| 1. Brancher une finalité produit sur diagnostic-complet | Moyen | Un mandat, une étude, une analyse effectivement appliquée, un brief et un résultat ; reprise après interruption |
| 2. Établir la couche analyse→synthèse | Moyen à élevé, principal effort | Sélection conditionnelle, sources suffisantes ou lacunes, résultat utilisable en narratif ; aucune obligation de connaître les blocs à l’avance |
| 3. Généraliser business et combiné | Moyen | Même corpus exploité sous deux questions, distinction société/produit, aucune duplication de faits |
| 4. Retirer progressivement les routes redondantes | Moyen et dépendant des validations | Compatibilité des anciens cas et comparaison sur cas de réserve ; signalement des migrations |
Estimations relatives tirées de la lecture ; aucun calendrier de développement fiable sans un premier lot mesuré.

Réutiliser provenance, sources/fragments/claims, paquets, checkpoints, writing.py et renderer de diagnostic-complet après vérification ciblée. Adapter les cadres de main et les méthodes MBA du candidat. Éviter une quatrième architecture parallèle. Une branche temporaire d’intégration peut porter les changements, mais son nom ne définit pas la cible produit.

## Backlog à rapprocher
- #42 : plan d’analyse et activation conditionnelle des frameworks. Priorité fonctionnelle centrale.
- #43 : résultats et mécanismes entre claims et récit. Complément indispensable de #42.
- #165 : profils de recherche ; les décliner par finalité et question en conservant le support comme contrainte.
- #25 et #137 : mémoire/réutilisation et lectures ciblées ; réutiliser le travail déjà livré dans diagnostic-complet.
- #36 : composition et side stories ; après stabilisation de la synthèse analytique.
- #130 : cas de réserve sémantiques et visuels ; validation utile à la migration.
- #258 : choix éditoriaux et profondeur du premier cas encore soumis au lecteur.
- #286 et #288 : migrations KB concrètes, dépendantes des données existantes ; aucune nécessité d’attendre leur résolution pour comparer une fixture synthétique isolée.
- #289 : évaluation indépendante ; rappelle la distinction entre assertions qui passent et qualité fonctionnelle.
Ces liens proposent un ordre d’intégration. Les statuts des issues et les autorisations de développement propres à chaque périmètre restent à lire au moment de l’implémentation.

## Premier essai discriminant proposé
Un cas nouveau, un corpus partagé et trois finalités : fiche produit, diagnostic de traction, étude combinée business-produit. Produire deux résultats analytiques seulement si utiles, puis les lier à un brief et au texte final. Reprendre à froid après phase 2 ; changer un fait matériel et vérifier les invalidations. Faire relire le produit final par l’utilisateur. Mesurer effort de contexte et recherche réellement consommés. Réussite : compréhension métier, narration et reprise vérifiées. Un schéma valide seul ne clôt pas ce test.

## Preuves de lecture
Storytelling main, chemins au SHA ci-dessus : SKILL.md ; references/workflow.md ; templates/architecture-note.md ; diagnostic-complet/README.md ; docs/BUSINESS-TRANSFER.md, WRITING-WORKFLOWS.md, INTERFACES.md, CONTEXT-PROTOCOL.md, NARRATIVE.md, SKILLS-MAP.md, OWNERSHIP.md, RESEARCH.md ; context.py ; writing.py ; skills/analyzing-market-and-competition/SKILL.md.
Candidat : contracts/analysis-result.schema.json ; mba/taxonomy/tools/resolve_method.py ; SKILL.md et refs de cadrage audités lors de la passe précédente.
Candidatures, lecture des contrats génériques au SHA dev ci-dessus : workflow/PROCESS.md, process-manifest.json, storage-boundaries.json, phases/A2/instructions.md, phases/A3/instructions.md, phases/A4/instructions.md. Aucun dossier candidat ni donnée de persona utilisé pour la publication de cette étude.
