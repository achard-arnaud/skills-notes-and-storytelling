# Contre revue par persona

Utiliser cette référence pendant la contre-perspective existante du workflow. Les personas sont des prismes de lecture construits pour ce dépôt ; ils ne constituent ni une expertise certifiée ni l’avis réel de dirigeants. « Partner McKinsey » interprète le libellé utilisateur « partner KC Kinsey » ; aucun avis du cabinet n’est revendiqué.

## Sélection et portée

Sélectionner la famille à partir du mandat et de l’analyse principale, puis les personas dont l’objection peut changer la thèse ou la décision. Une demande explicite de revue par plusieurs personas entraîne une couverture distincte de chacun ; un run courant ne charge pas automatiquement tous les prismes. Conserver les différences entre COO business et COO produit.

La réglementation demeure une route spécialisée sans nouvel enum. Les formats, budgets et états existants restent propriétaires. Une note descriptive reçoit une objection sur sa thèse et son périmètre ; elle ne devient pas une recommandation implicite.

## Deux passes

1. **Devil advocate.** Pour chaque persona retenu, relever passage/claim, objection forte, preuve disponible, ce qui manque et conséquence. Distinguer défaut matériel, préférence de forme et question sans effet sur la conclusion. Un persona ne crée aucune preuve.
2. **Correction.** Répondre accepter/rejeter/borner/laisser ouvert avec raison. Corriger source, claim, raisonnement ou présentation à la première couche fautive. Préserver les faits valides et le statut de preuve. Relire une fois la proposition corrigée ; si le défaut matériel persiste, utiliser le verdict existant REOPEN_TARGETED.

Réutiliser les verdicts et la limite d’itération de [workflow](workflow.md). Ne pas créer d’états runtime. Le reçu de travail conserve persona, passage, objection, réponse, delta, preuve et vérification. Une relecture documentaire ne démontre pas un gain de performance de la skill.

## Fiches des personas

### CEO

Famille : business.

- Question : Quelle décision change la trajectoire et à quoi renonce t on ?
- Faiblesse recherchée : La thèse décrit une entreprise convaincante mais ne montre pas le coût d’opportunité du choix.
- Correction : Relier ambition, contrainte stratégique, alternative de maintien et allocation de ressources ; distinguer description business et recommandation demandée.
- Formulation attendue : Thèse → mécanisme de valeur → option écartée → condition de révision.
- Cas discriminant synthétique : Une croissance publiée est traitée comme preuve que la transformation IA en est la cause.
- Réponse attendue : Présenter la croissance comme observation ; qualifier séparément la contribution IA et les autres explications.

### COO business

Famille : business.

- Question : Quel opérateur absorbe les exceptions et la charge récurrente ?
- Faiblesse recherchée : La trajectoire paraît finançable mais la charge de transition et le fonctionnement courant restent implicites.
- Correction : Préciser propriétaire de processus, capacité disponible, interfaces, exceptions, continuité et coût récurrent ; marquer les hypothèses.
- Formulation attendue : Processus → responsable → dépendances → incident/reprise → mesure de fonctionnement.
- Cas discriminant synthétique : Le gain de temps individuel est intégralement converti en réduction de coûts.
- Réponse attendue : Distinguer capacité libérée, capacité réellement réaffectée et dépense effectivement évitée.

### VC

Famille : business.

- Question : La croissance peut elle produire une économie soutenable ?
- Faiblesse recherchée : Le marché et les capacités sont décrits, mais la marge, la distribution et le besoin de financement restent non discriminants.
- Correction : Séparer taille de marché, marché accessible et acquisition réalisable ; expliquer hypothèses de revenu, marge contributive, rétention et financement lorsqu’elles sont matérielles.
- Formulation attendue : Hypothèse de croissance → mécanisme de distribution → économie unitaire → sensibilité → preuve manquante.
- Cas discriminant synthétique : Un prototype et un marché large suffisent à conclure à un avantage défendable.
- Réponse attendue : Qualifier le prototype et tester distribution, coûts complets, différenciation et dépendances ; conserver inconnu ce qui manque.

### Partner McKinsey

Famille : business.

- Question : Quelle hypothèse alternative renverse la conclusion ?
- Faiblesse recherchée : Une structure de conseil peut rester élégante sans tester les explications concurrentes.
- Correction : Présenter hypothèse centrale, explication concurrente crédible, preuves qui les discriminent et limite de généralisation ; choisir les frameworks selon leur utilité.
- Formulation attendue : Question → hypothèses → preuve discriminante → implication → limite.
- Cas discriminant synthétique : Une matrice SWOT est présentée comme preuve causale.
- Réponse attendue : Utiliser la matrice comme structuration ; rattacher les mécanismes aux sources et conserver les liens causaux non établis comme hypothèses.

### CPO

Famille : product.

- Question : Qui change effectivement de comportement et pourquoi ?
- Faiblesse recherchée : Le contrat produit couvre utilisateurs et capacités, mais une liste de fonctionnalités peut encore tenir lieu de valeur.
- Correction : Distinguer utilisateur, acheteur et administrateur ; préciser job, alternative actuelle, friction, activation, usage répété et résultat. En cas de roadmap, expliciter valeur, risque, dépendances et choix écarté.
- Formulation attendue : Job → alternative → première valeur → usage répété → résultat → arbitrage.
- Cas discriminant synthétique : Une hausse des inscriptions est assimilée à la rétention.
- Réponse attendue : Conserver les inscriptions comme acquisition ; demander cohorte, période et définition de rétention avant toute conclusion.

### COO produit

Famille : product.

- Question : Que coûte réellement le service lorsque les volumes et exceptions augmentent ?
- Faiblesse recherchée : La roadmap peut sous estimer support, opérations manuelles et responsabilités post lancement.
- Correction : Examiner onboarding, support, exceptions, maintenance, intégration, coût de service et responsabilité après livraison ; distinguer pilote et produit opéré.
- Formulation attendue : Parcours → opérations visibles/cachées → capacité → coût de service → critères de déploiement.
- Cas discriminant synthétique : Un pilote réussi sur utilisateurs accompagnés est présenté comme déploiement autonome.
- Réponse attendue : Qualifier l’accompagnement et vérifier instrumentation, support, droits, exceptions et dépendances avant d’étendre la conclusion.

### Head of L&D

Famille : pedagogical.

- Question : Quel apprentissage observable sera transféré dans le travail ?
- Faiblesse recherchée : L’explication et le critère de compréhension sont présents, mais l’acquis initial, le transfert différé et l’accessibilité restent peu explicites.
- Correction : Définir acquis et objectif observable ; faire pratiquer avec feedback ; prévoir adaptation du niveau, accessibilité et contexte de transfert. Séparer satisfaction, compréhension et performance.
- Formulation attendue : Acquis → objectif → exercice → critère/feedback → essai au travail.
- Cas discriminant synthétique : Une satisfaction élevée après atelier est présentée comme compétence acquise.
- Réponse attendue : Présenter la satisfaction comme telle ; utiliser une tâche observable et préciser les limites du transfert sans suivi.

### sharp CTO

Famille : technical.

- Question : Qu’est ce qui fonctionne lorsque le contexte, un outil ou le modèle échoue ?
- Faiblesse recherchée : La capacité IA est qualifiée mais les frontières entre jugement, exécution et exploitation peuvent rester abstraites.
- Correction : Décrire contrats I/O, permissions, isolation, échec/reprise, observabilité, évaluation et coût complet lorsque matériels. Séparer prototype, benchmark fournisseur et fonctionnement observé.
- Formulation attendue : Besoin → frontière modèle/code/outils → test d’échec → coût/latence → preuve de production.
- Cas discriminant synthétique : Une promesse de coût modèle inférieur est présentée comme réduction du coût du workflow.
- Réponse attendue : Inclure orchestration, retrieval, reprises, évaluations et escalades ; tester le workflow et qualifier les gains non mesurés.

### Data lead

Famille : technical.

- Question : La donnée rend elle cette décision fiable à cet instant ?
- Faiblesse recherchée : La baseline et la temporalité sont couvertes mais les dérives de définition, la fraîcheur et les contrats producteurs/consommateurs restent à expliciter.
- Correction : Tracer origine, propriétaire, sémantique, qualité, fraîcheur requise et effective, droits et devenir des transformations ; prévoir traitement du défaut et responsabilité de correction.
- Formulation attendue : Décision → définition → origine → transformation → fraîcheur/qualité → correction.
- Cas discriminant synthétique : Des données présentes dans un catalogue sont supposées utilisables par le modèle.
- Réponse attendue : Vérifier accès effectif, licence, qualité, disponibilité et adéquation à la tâche ; distinguer catalogué, accessible et exploitable.

### Head of Risk & Compliance

Famille : regulatory.

- Question : Quelles responsabilités et quelles limites de contrôle sont établies ?
- Faiblesse recherchée : La précision des textes est forte mais peut donner une apparence de conformité opérationnelle sans preuve d’efficacité des contrôles.
- Correction : Séparer obligation applicable, interprétation, dispositif décrit, efficacité testée et risque résiduel ; préciser périmètre, exceptions, responsables et date. Garder la note descriptive sauf demande de recommandations.
- Formulation attendue : Texte/statut → applicabilité → responsabilité → contrôle/preuve → limite/risque résiduel.
- Cas discriminant synthétique : La présence d’une procédure est présentée comme preuve de conformité.
- Réponse attendue : Qualifier la procédure comme dispositif déclaré ; identifier les preuves de fonctionnement et les inconnues sans rendre un avis de conformité global.

## Persona technique sourcé

Pour une revue technique/IA, lire [sharp CTO](personas/sharp-cto.md) si sélectionné. Les autres rôles sont des constructions analytiques, sans attribution à une personne réelle.
