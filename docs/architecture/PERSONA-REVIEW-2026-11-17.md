# Revue contradictoire des skills par persona

Date : 17 novembre 2026. Base examinée : dev d490ddf97f76e0c4d94af8ea72b3dbfc70494ab8. Statut : corrections documentaires proposées. Cette revue effectue les deux passes demandées sur les instructions des skills ; elle ne constitue pas dix avis de professionnels réels ni dix tests de runs en contexte neuf.

## Passe 1 puis passe 2

Les instructions prévoient déjà une contre-perspective, une réparation et une vérification. Le manque principal est le caractère peu discriminant des rôles de revue. Le présent lot précise les critères par persona et corrige les clauses locales identifiées, sans nouvelle phase runtime.

| Persona | Faiblesse examinée | Réponse et correction |
|---|---|---|
| CEO | La thèse décrit une entreprise convaincante mais ne montre pas le coût d’opportunité du choix. | Relier ambition, contrainte stratégique, alternative de maintien et allocation de ressources ; distinguer description business et recommandation demandée. |
| COO business | La trajectoire paraît finançable mais la charge de transition et le fonctionnement courant restent implicites. | Préciser propriétaire de processus, capacité disponible, interfaces, exceptions, continuité et coût récurrent ; marquer les hypothèses. |
| VC | Le marché et les capacités sont décrits, mais la marge, la distribution et le besoin de financement restent non discriminants. | Séparer taille de marché, marché accessible et acquisition réalisable ; expliquer hypothèses de revenu, marge contributive, rétention et financement lorsqu’elles sont matérielles. |
| Partner McKinsey | Une structure de conseil peut rester élégante sans tester les explications concurrentes. | Présenter hypothèse centrale, explication concurrente crédible, preuves qui les discriminent et limite de généralisation ; choisir les frameworks selon leur utilité. |
| CPO | Le contrat produit couvre utilisateurs et capacités, mais une liste de fonctionnalités peut encore tenir lieu de valeur. | Distinguer utilisateur, acheteur et administrateur ; préciser job, alternative actuelle, friction, activation, usage répété et résultat. En cas de roadmap, expliciter valeur, risque, dépendances et choix écarté. |
| COO produit | La roadmap peut sous estimer support, opérations manuelles et responsabilités post lancement. | Examiner onboarding, support, exceptions, maintenance, intégration, coût de service et responsabilité après livraison ; distinguer pilote et produit opéré. |
| Head of L&D | L’explication et le critère de compréhension sont présents, mais l’acquis initial, le transfert différé et l’accessibilité restent peu explicites. | Définir acquis et objectif observable ; faire pratiquer avec feedback ; prévoir adaptation du niveau, accessibilité et contexte de transfert. Séparer satisfaction, compréhension et performance. |
| sharp CTO | La capacité IA est qualifiée mais les frontières entre jugement, exécution et exploitation peuvent rester abstraites. | Décrire contrats I/O, permissions, isolation, échec/reprise, observabilité, évaluation et coût complet lorsque matériels. Séparer prototype, benchmark fournisseur et fonctionnement observé. |
| Data lead | La baseline et la temporalité sont couvertes mais les dérives de définition, la fraîcheur et les contrats producteurs/consommateurs restent à expliciter. | Tracer origine, propriétaire, sémantique, qualité, fraîcheur requise et effective, droits et devenir des transformations ; prévoir traitement du défaut et responsabilité de correction. |
| Head of Risk & Compliance | La précision des textes est forte mais peut donner une apparence de conformité opérationnelle sans preuve d’efficacité des contrôles. | Séparer obligation applicable, interprétation, dispositif décrit, efficacité testée et risque résiduel ; préciser périmètre, exceptions, responsables et date. Garder la note descriptive sauf demande de recommandations. |

## Corrections localisées

- Business et économie : la clause de réinvestissement du temps libéré pouvait être lue comme une économie comptable ; distinction capacité, réaffectation et dépense évitée intégrée.
- Opérations : la chaîne de valeur commençait par une séquence site/étude/construction ; cette séquence devient un exemple conditionnel pour les actifs physiques.
- Produit : l’entrée commune et le template architecture couvrent des capacités et une roadmap ; ajout dans l’entrée de skill de définitions distinctes acquisition/activation/rétention, coût de service et généralisation du pilote.
- IA : la séquence assistants/copilotes pouvait imposer un parcours universel ; le choix dépend désormais du risque et des capacités disponibles.
- L&D : ajout d’acquis initiaux, exercice observable, feedback et transfert ; six pages restent un format.
- Risk & Compliance : distinction procédure déclarée et efficacité testée, sans avis implicite de conformité ni modification du budget de recherche.
- sharp CTO : fiche sourcée sur quatre articles complets et réserve critique sur les formulations vulgarisées. Aucun benchmark repris comme fait validé.

## Couverture et limites

Treize SKILL.md canoniques relient le contrat commun : entrée racine, dix skills analytiques/narratifs diagnostic-complet et deux spécialisées pédagogie/réglementaire. Le produit et la technique sont des dimensions de l’entrée commune, pas des skills autonomes inventées pour cette revue. Les adaptateurs reinforce-kb-loopback sont hors production éditoriale et hors de ces familles ; les copies historiques upstream et les anciennes revues sont conservées. Les liens du contrat partagé et les critères spécialisés complètent la revue transverse exigée par AGENTS.md.

Le rapport ne prétend pas une synchronisation des skills personnelles installées dans Work ; la portée est le dépôt storytelling. Les tests ajoutés vérifient liens, couverture des personas et présence des critères et sources. Les dix situations synthétiques sont un corpus de futurs essais comportementaux, pas des preuves de performance mesurées.

Les contrats de template, de mode et les enums restent inchangés ; aucun catalogue de templates n’est promu. Le dossier de persona constitue une référence de revue. Son alias sharp CTO reste une convention du dépôt, sans enregistrement global implicite.

## Vérification du delta

Une relecture a vérifié la séparation des critères par famille, la réserve descriptive réglementaire, les deux COO distincts et l’absence de nouvelles données de cas dans les méthodes. Les contrôles mécaniques sont consignés dans la PR après exécution. Les défauts résiduels d’un run réel restent à traiter dans leur périmètre ; aucun gain qualitatif universel n’est revendiqué.
