# AI Potluck — Faire de l’assemblage ouvert un usage quotidien

## Page logique 1/2 — Ce qui est annoncé, ce qu’il reste à prouver

**Recommandation — Centrer la discussion produit sur une preuve d’usage récurrent d’Alpha dans une organisation partenaire ; traiter l’ouverture du Router aux développeurs comme une décision distincte.** L’annonce fixe ces deux ambitions dans les six premiers mois, sans fournir encore de résultats d’adoption. [F06–F07 ; I01 ; R01]

### Quelle proposition produit ?

**Fait rapporté —** Current AI présente AI Potluck comme un projet open source qui assemble des composants ouverts en un produit verticalement intégré, utilisable et construit avec l’écosystème. [F01] **Inférence —** La valeur à démontrer réside dans la continuité entre composants, expérience et usage ; la seule disponibilité des composants ne prouve pas cette valeur. [I01]

| Composante annoncée | Fonction et état rapportés | Question produit à trancher |
|---|---|---|
| **Alpha** — [chat](https://www.aipotluck.org/chat) | Assistant assemblé à partir de composants open source ; présenté comme lancé en juillet 2026 à AI for Good, Genève, et en test ouvert. [F03] | Quel travail récurrent justifie de revenir chaque jour ? |
| **Gap Map** — [carte](https://www.aipotluck.org/map) | Insights sur les lacunes de l’écosystème et les zones à financer ou auxquelles contribuer. [F04] | Quelle décision change après lecture ? |
| **Alpha Public Router** | Endpoint unique vers des modèles de fournisseurs publics ou alignés avec la mission ; alimente Alpha ; doit devenir un produit développeur. [F05] | Quel besoin autonome existe au-delà d’Alpha ? |

Les questions de la dernière colonne sont **proposées**, pas des constats de marché.

### Pourquoi cette discussion maintenant ?

**Faits rapportés —** Les six premiers mois visent quatre résultats : usage quotidien d’Alpha dans un petit nombre d’organisations partenaires ; décision sur le produit Router et son appel aux développeurs ; roadmap 2027 construite avec partenaires et bénéficiaires de financement ; hausse des contributions à Alpha. [F06]

La réussite annoncée combine livraison et adoption : dates publiques tenues ; organisations activement utilisatrices d’Alpha et du Router ; projets intégrés et contributions reversées ; partenaires livrant une intégration ; roadmap compréhensible sans réunion. Aucun niveau atteint ni seuil chiffré n’est fourni. [F07]

**Inférence —** Ces objectifs relient trois boucles : usage, intégration et contribution. Leur articulation est une hypothèse de pilotage ; le matériau ne démontre pas qu’une hausse des contributions améliore effectivement l’usage. [I02]

### Ce qui borne la confiance

**Inconnues —** Utilisateurs et tâches réellement servis, fréquence actuelle, qualité des réponses, modèles disponibles, politique de données, licences détaillées, coûts, support et garanties de service. [U01–U03] « Open source » et « aligné avec la mission » ne suffisent pas à établir la souveraineté opérationnelle ou la portabilité. [I03]

*Source commune — SRC-JOB, extrait fourni attribué à l’annonce VP Product, non corroboré. Les liens sont repris de cet extrait et n’ont pas été consultés. Identifiants détaillés dans process.json. La date de publication de l’annonce et l’horodatage du run original ne sont pas vérifiés.*

---

## Page logique 2/2 — Trois usages à éprouver, une prochaine décision

### Où chercher la valeur ?

Les trois cas ci-dessous sont des **propositions exploratoires**, sans demande client ni performance démontrée. Ils mettent chaque composante face à une décision observable. [R02]

| Cas proposé | Utilisateur et travail | Preuve proposée, face au point de départ |
|---|---|---|
| **Alpha : préparer une note de travail** | Un collaborateur partenaire transforme des documents autorisés en une synthèse vérifiable, puis la corrige. | Comparer au travail habituel : temps jusqu’à une note validée, corrections et réutilisation volontaire. |
| **Router : intégrer une fonction IA** | Un développeur partenaire teste un appel via l’endpoint unique pour une tâche qu’il connaît déjà. | Comparer à son intégration actuelle : effort, qualité et traitement des erreurs ; vérifier les changements de fournisseur réellement possibles. |
| **Gap Map : orienter une contribution** | Un responsable d’écosystème repère une lacune puis choisit une piste de financement ou de contribution. | Documenter une décision avant/après la carte, le projet retenu et la justification de ce changement. |

### Quel arbitrage proposer ?

**Recommandation —** Faire d’Alpha le premier terrain de validation, parce que l’annonce vise explicitement son usage quotidien chez des partenaires. Le Router conserve une exploration propre : l’usage d’Alpha ne démontre pas une demande développeur autonome. Gap Map peut éclairer les priorités de contribution ; cette complémentarité reste à vérifier. [F04–F06 ; I02 ; R01]

**Alternative crédible —** Commencer par le Router si un partenaire apporte un besoin développeur précis et une intégration testable. Le matériau ne permet pas de classer la demande entre ces deux voies. **Condition de révision :** un besoin Router documenté et un usage Alpha insuffisamment récurrent justifieraient de changer l’ordre proposé. [U01 ; R03]

### Quelles conditions avant un essai ?

**Conditions proposées —** Choisir une tâche, un responsable métier et un référent technique ; vérifier l’autorisation des données et les conditions d’usage ; convenir d’une solution de repli et du traitement des erreurs. Sans ces éléments, différer l’essai sur données réelles. [R04]

**Point de contrôle —** Pour Alpha : export des entrées et résultats utiles ; pour le Router : portabilité des appels, des modèles et des comportements ; pour les contributions : licences et maintien des composants. Ces dépendances sont à examiner, pas des défauts établis. Prévoir le retour au processus actuel et mesurer le coût de reprise. [I03 ; R04]

### Prochaine étape unique

**Proposition — Tenir une séance de cadrage avec une organisation partenaire pour décider d’un essai Alpha de deux semaines sur une seule tâche.** À son issue, disposer d’un protocole : point de départ, données autorisées, responsable, critères d’acceptation et arrêt. Durée et mesures sont proposées, non annoncées par Current AI. [R05]

**Objection décisive —** L’assemblage ouvert peut répondre à un objectif d’écosystème sans améliorer le travail du partenaire. **Test discriminant proposé :** comparer à la méthode actuelle et observer la réutilisation volontaire après accompagnement. Si l’usage reste artificiellement soutenu ou la qualité insuffisante, réviser le cas d’usage avant d’élargir le déploiement. [I01 ; R05]

*SRC-JOB reste l’unique matériau ; aucun tarif, résultat de pilote, KPI additionnel ou engagement de service n’est présenté comme établi.*
