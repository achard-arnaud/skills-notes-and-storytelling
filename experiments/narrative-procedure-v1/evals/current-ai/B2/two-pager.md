# AI Potluck — prouver l’usage avant d’élargir le portefeuille

**Page logique 1/2 — Proposition : ancrer la priorité dans l’usage d’Alpha, puis tester le Router séparément**

Pour préparer la discussion produit, partir d’une question : **quelle tâche récurrente justifierait l’adoption d’AI Potluck dans une organisation partenaire ?** L’annonce vise un usage quotidien d’Alpha dans un petit nombre d’organisations et une décision sur le Router développeur dans les six premiers mois. Proposition : utiliser Alpha pour apprendre sur les tâches réelles, tout en testant une demande propre au Router. Ce séquencement est une hypothèse de travail, pas une conclusion de marché.

### Trois composantes relient expérience, infrastructure et orientation des contributions

Selon l’annonce VP Product fournie, Current AI décrit AI Potluck comme un projet open source assemblant des composants ouverts dans un produit verticalement intégré, utilisable et construit avec l’écosystème.

| Composante | Ce que l’annonce lui attribue | Implication pour la discussion |
|---|---|---|
| **Alpha** | Assistant assemblé à partir de composants open source ; lancement annoncé en juillet 2026 à AI for Good, Genève ; test ouvert. | Identifier une tâche qui mérite un retour quotidien, puis vérifier que l’assistant sait la traiter. |
| **Gap Map** | Produit d’insights signalant les lacunes de l’écosystème et les zones à financer ou auxquelles contribuer. | Vérifier comment un insight devient une décision de contribution ou de financement. |
| **Alpha Public Router** | Endpoint unique vers des modèles de fournisseurs publics ou alignés avec la mission ; alimente Alpha ; produit développeur visé. | Distinguer le besoin interne d’Alpha de la demande de développeurs externes. |

La seule dépendance technique explicitée dans la source est **Router → Alpha**. Gap Map éclaire les lacunes ; aucune connexion automatisée à Alpha ou au Router n’est attestée. L’intégration verticale constitue donc un positionnement annoncé, sans preuve fournie de supériorité sur un assemblage existant.

### Les six premiers mois visent l’adoption et la capacité de livraison

L’annonce fixe quatre résultats attendus : usage quotidien d’Alpha chez quelques partenaires ; décision sur le produit Router et son appel aux développeurs ; roadmap 2027 construite avec partenaires et bénéficiaires de financement ; hausse des contributions à Alpha. Son horizon de six mois est relatif au poste : aucune date de début n’est fournie.

Le succès annoncé combine dates publiques tenues, organisations utilisant activement Alpha et le Router, projets intégrés et contributions reversées, partenaires livrant une intégration, et roadmap compréhensible sans réunion. **Ce sont des critères annoncés, pas des résultats observés.**

La confiance reste limitée par l’absence de données d’usage, de rétention, de performances, de coûts et de conditions de service. Sont également inconnus : accès et ingestion documentaire d’Alpha, traitement des données, modalités d’accès au Router, couverture et fraîcheur de Gap Map. Ces inconnues déterminent ce qu’un pilote peut réellement tester.

---

**Page logique 2/2 — Trois cas proposés permettent de tester la valeur sans présumer les capacités**

### Alpha doit d’abord réussir une tâche récurrente et délimitée

**Cas proposé, non démontré.** Un collaborateur d’une organisation partenaire prépare chaque semaine une courte synthèse sur un sujet non sensible. Parcours proposé : formuler la demande, faire produire un brouillon par Alpha, contrôler les éléments puis finaliser. Valeur attendue : réduire l’effort de préparation en conservant une qualité acceptable. **Avant tout pilote**, vérifier qu’Alpha traite la tâche et, si des documents sont nécessaires, qu’il permet effectivement leur accès et leur ingestion ; ces capacités ne sont pas attestées. À défaut, limiter le test à une tâche réalisable avec les entrées autorisées. Mesures proposées : temps total, corrections nécessaires, réutilisation volontaire, comparés à la méthode actuelle.

### Le Router doit gagner une intégration utile pour un développeur externe

**Cas proposé, non démontré.** Un développeur partenaire veut appeler des modèles via un point d’entrée unique. Parcours proposé : examiner la documentation, obtenir un accès, intégrer un appel dans un environnement de test, observer les réponses et les erreurs. Valeur attendue : simplifier son intégration. Conditions à vérifier : documentation, authentification, modèles accessibles, compatibilité, limites, coûts et conditions de données ; aucune garantie de disponibilité n’est fournie. Mesures proposées : temps jusqu’au premier appel utile, effort d’intégration, réussite des appels et réemploi. Alternative à comparer : accès direct aux fournisseurs ou routeur déjà utilisé ; le bénéfice relatif reste à prouver.

### Gap Map doit éclairer une décision traçable de contribution

**Cas proposé, non démontré.** Un responsable de contribution ou de financement recherche une lacune à traiter. Parcours proposé : explorer la carte, qualifier un signal, le confronter aux besoins d’un partenaire, décider de poursuivre ou d’écarter. Valeur attendue : mieux orienter l’effort. Conditions : vérifier provenance, actualisation et pertinence des insights ; aucune fonction d’allocation ou de suivi automatisé n’est attestée. Mesures proposées : décisions dont le raisonnement est traçable et signaux confirmés par les partenaires, comparés à leur recherche habituelle. Ce cas éclaire la roadmap ; il ne démontre pas l’adoption d’Alpha.

### Une demande Router autonome pourrait inverser la recommandation

**Objection décisive :** le meilleur point d’entrée peut être le Router si les développeurs ont un besoin urgent, tandis qu’Alpha ne trouve aucune tâche récurrente. L’observation qui ferait changer la priorité serait une intégration externe effectivement réutilisée, apportant un avantage documenté face à l’accès direct, alors que les utilisateurs d’Alpha ne reviennent pas après une tâche réussie. Comparer les deux signaux dans un périmètre convenu ; ne pas traiter un intérêt déclaré comme un usage.

### Proposition : autoriser seulement un cadrage de pilote réversible

Le VP Product, en collaboration avec le Head of Engineering et un partenaire volontaire, pourrait porter **une fiche de pilote** : tâche prioritaire, utilisateur, baseline actuelle, capacités vérifiées, critères d’arrêt et mesure convenue. C’est le prochain pas proposé, sans engagement de déploiement. Ne démarrer qu’après validation des accès, du traitement des données et de la capacité minimale ; si une condition manque, garder le test au niveau démonstrateur. La discussion doit aboutir à une priorité testable, avec des critères de poursuite explicites plutôt qu’un élargissement simultané des trois composantes.

**Source et statut —** Toutes les descriptions et tous les objectifs annoncés ci-dessus proviennent uniquement de l’extrait d’annonce VP Product fourni dans le brief, non corroboré. Date de publication et état actuel non vérifiés. Les cas, mesures, alternatives et recommandations sont des propositions. Liens cités dans l’annonce, non testés : [Alpha](https://www.aipotluck.org/chat) ; [Gap Map](https://www.aipotluck.org/map). Aucun endpoint public du Router n’est fourni. Deux pages logiques Markdown ; pagination physique non vérifiée.
