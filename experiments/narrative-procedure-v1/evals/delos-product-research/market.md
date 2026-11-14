# Delos AI Worker dans son marché : sur quelle partie du travail se situe la différence ?

Observation documentaire au 14 novembre 2026. Les capacités ci-dessous sont documentées par les éditeurs. Les essais en tenant, les taux de réussite, les coûts par résultat utilisable et les données de rétention clients n'ont pas été mesurés. Les statistiques publiques mesurent l'usage de l'IA au sens large.

## Comparer des tâches identiques

| Travail à accomplir | Delos AI Worker | AstraForge | Dust | Microsoft Copilot Studio |
|---|---|---|---|---|
| Confier à un agent une mission avec des sources et des outils | Définition du métier, compétences, initiative et règles par action dans Behavior Studio (M01–02) | Un Bot peut recevoir directement une mission en conversation et utiliser les outils ou sessions autorisés. La composition d'un workflow reste facultative (M04–05) | Un Pod réunit les conversations, fichiers et tâches d'une équipe et de ses agents ; chacun peut contribuer au même dossier (M09–11) | Le concepteur définit les actions et les outils disponibles ; l'agent choisit parmi eux selon son déclencheur et ses instructions (M13, M15) |
| Transformer un signal en travail assigné | Missions programmées, récurrentes ou sur événement ; initiative et consignes déterminent le comportement attendu (M01–02) | Déclenchement par webhook, planification, ticket Jira ou exécution manuelle ; les étapes peuvent transmettre leurs livrables (M04, M06) | Un événement Jira ou Slack peut ouvrir une conversation contextualisée dans le Pod ; une tâche est assignable et réouvrable (M10–11) | Un événement structuré déclenche l'agent après publication ; l'historique d'activité expose déclencheur et réaction (M13) |
| Faire passer une action à une personne | Les règles « demander » appellent un outil de confirmation. Maximum de 20 règles actives ; ces consignes ne sont pas un verrou de permission en code et ne se propagent pas automatiquement aux sous-agents (M01) | Une étape d'approbation peut suspendre la procédure ; vérifier séparément la portée des permissions de l'outil (M04, M06) | Les tâches et discussions permettent revue et réassignation. Leur documentation seule ne garantit pas un blocage transactionnel de l'action externe (M09–11) | Un workflow peut attendre une réponse ou rendre une approbation explicite nécessaire avant l'action visée, selon le modèle de workflow (M14) |
| Rendre le résultat réutilisable | Les compétences codifient le comportement ; le journal d'activité décrit les actions du Worker (M02) | Une démonstration peut devenir une compétence revue et publiée ; les workflows versionnés transmettent des fichiers et critères (M05–06) | Le Pod conserve les conversations et fichiers et indexe le contexte pour les agents (M09) | L'historique d'activité aide à diagnostiquer un parcours ; une spécification réutilisable suppose de documenter le flux configuré (M13, M15) |

**Lecture fonctionnelle.** Comparer le Worker au Bot d'AstraForge éclaire la délégation individuelle. Comparer un processus Delos multi-acteurs à un workflow AstraForge éclaire les transmissions, les frontières d'autorisation et les preuves. Dust constitue un autre point de comparaison lorsque l'équipe veut surtout partager sa connaissance et suivre des tâches. Copilot Studio renseigne le choix « construire dans son environnement Microsoft ». Un workflow à règles ou une procédure manuelle restent des substituts pour une tâche déterministe. Aucune de ces comparaisons ne détermine la satisfaction des utilisateurs ni la préférence acheteur.

## 4P du Worker et limites interprétatives

| Dimension | Observation | Diagnostic / inconnue |
|---|---|---|
| Produit | Le configurateur distingue compétence, niveau d'initiative et règle par action (M01–02). AstraForge distingue Bots et workflows (M05–06). | L'interface de configuration déplace une part du travail vers le métier. La proposition couvre collecte, préparation, exécution et revue ; la robustesse de l'action sur un outil tiers dépend aussi des droits de connexion. |
| Prix | Delos propose l'essai gratuit et présente des offres évolutives par Worker (M03). AstraForge indique des forfaits par siège, Dust combine siège et consommation, Microsoft propose une capacité de crédits ou une facturation à l'usage (M07, M12, M16). | Normaliser sur la même période, le nombre de personnes et d'agents, le volume de tâches finalisées et le coût de supervision. Un prix du siège ou de la suite ne suffit pas pour inférer le coût d'une tâche terminée. |
| Distribution | Le site Delos associe découverte des Workers, démonstrations par canal, essai et téléchargement (M03). AstraForge indique une liste d'attente pour l'accès initial (M08). | Distinguer le canal d'acquisition, le lieu où l'utilisateur travaille et le canal de vente. La répartition de l'acquisition par canal et les coûts d'intégration restent inconnus. |
| Promotion | Delos se présente comme une équipe de travailleurs modulable ; les pages de prix et les exemples du configurateur mettent la mission métier au premier plan (M02–03). AstraForge utilise aussi la figure du collègue virtuel (M05). | Ce vocabulaire partagé ne démontre pas une différenciation propre. Une différence se juge au comportement précis, à la permission effectivement contrôlée, au livrable retourné et à son usage répété. |

## Demande, segments et portée de l'étude

En 2025, l'Insee mesure en France un usage d'au moins une technologie IA chez 18 % des entreprises de son champ. Les taux sont de 15 % parmi les entreprises de 10 à 49 salariés, 31 % parmi celles de 50 à 249 et 58 % à partir de 250. Le champ exclut notamment agriculture, finance et assurance. Eurostat mesure 20,0 % dans son champ européen des entreprises d'au moins dix personnes et 11,8 % pour l'analyse de langage écrit (M17–18). Ces statistiques éclairent le contexte d'adoption ; on ne peut en déduire ni le nombre d'acheteurs d'agents autonomes ni les revenus adressables de Delos.

Pour construire une estimation ascendante défendable, définir une géographie et une activité, compter les établissements réellement équipés des canaux compatibles, estimer sur enquêtes la proportion ayant une tâche récurrente éligible et un budget, puis appliquer un revenu annuel observé par client et une analyse de sensibilité. Séparer équipes acheteuses, opérateurs, responsables IT et personnes dont les dossiers sont traités. Leur déclaratif, le comportement d'usage, le renouvellement et le bénéfice mesuré répondent à quatre questions différentes. Les données disponibles ici documentent mieux le fonctionnement de l'offre que ces quatre dimensions de demande.

## Registre documentaire

Chaque ligne désigne une publication distincte ouverte, avec son domaine de preuve. Les différentes documentations d'un fournisseur comptent comme sources de fonctionnement et partagent un même intérêt commercial. Les deux organismes statistiques mobilisent des enquêtes liées et ne constituent pas deux corroborations indépendantes du même taux français.

| ID | Publication | Ce qu’elle étaye |
|---|---|---|
| M01 | [Delos, règles du Worker](https://help.delos.so/categories/workers/rules-for-workers) | Confirmation, limite de 20 et absence de propagation automatique. |
| M02 | [Delos, Behavior Studio](https://help.delos.so/categories/workers/behaviour-studio) | Compétences, niveaux d’initiative, réglage du comportement et journal. |
| M03 | [Delos, offre commerciale](https://delos.so/fr/pricing) | Essai, absence d'engagement annoncée, distribution et parcours vers les Workers ; aucun coût réalisé dans la page. |
| M04 | [AstraForge, plateforme](https://astraforgeos.ai/platform) | Déclencheurs, connecteurs, contrôles et conditions de disponibilité. |
| M05 | [AstraForge, Bots](https://astraforgeos.ai/bots) | Délégation conversationnelle, compétence réutilisable et exemple de note de version. |
| M06 | [AstraForge, workflows](https://astraforgeos.ai/workflows) | Transmissions, approbation, versionnement et vérification. |
| M07 | [AstraForge, prix](https://astraforgeos.ai/pricing) | Unité siège, essai sur invitation et offre Enterprise négociée. |
| M08 | [AstraForge, accès anticipé](https://astraforgeos.ai/waitlist) | Modalité d'accès ; aucune indication du nombre de clients. |
| M09 | [Dust, Pods](https://docs.dust.tt/docs/user-documentation/pods/overview) | Espace et contexte partagés entre personnes et agents. |
| M10 | [Dust, conversations](https://docs.dust.tt/docs/user-documentation/pods/conversations) | Événements externes créant des conversations et exemples Jira et Slack. |
| M11 | [Dust, tâches](https://docs.dust.tt/docs/user-documentation/pods/tasks) | État, assignation, réouverture et synchronisation d'une tâche. |
| M12 | [Dust, tarification](https://dust.tt/home/pricing) | Sièges, crédits liés aux outils et aux modèles, limites. |
| M13 | [Microsoft, déclencheurs](https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about) | Autorisation, activation après publication et trace d'activité. |
| M14 | [Microsoft, étapes humaines](https://learn.microsoft.com/en-us/training/modules/add-human-loop-workflows-copilot-studio/) | Étape d'approbation explicite ; formation visant le workflow concerné. |
| M15 | [Microsoft, conception de l'autonomie](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/autonomous-agents) | Frontières de conception de l'agent et gouvernance du processus. |
| M16 | [Microsoft, licences et consommation](https://www.microsoft.com/licensing/guidance/Microsoft-Copilot-Studio) | Capacités groupées de 25 000 crédits et paiement à l'usage. |
| M17 | [Insee Première 2120, enquête TIC entreprises 2025](https://www.insee.fr/fr/statistiques/fichier/9025878/ip2120.pdf) | Adoption en France selon la taille, champ précis de l'enquête. |
| M18 | [Eurostat, enquête européenne 2025](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20251211-2) | Adoption européenne et type de technologie ; aucune mesure de la dépense agentique. |
