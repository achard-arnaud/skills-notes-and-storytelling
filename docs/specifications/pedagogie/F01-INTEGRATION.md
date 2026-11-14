# Intégration fonctionnelle pédagogique — familles F01 et compatibilité essais 2/3

## Mandat et statut
Story transverse à #294, #295, #296 et #297. Demande utilisateur du 14 novembre 2026 : analyser le fil Sarah F01, identifier ses outputs, reconstituer les sommaires et métaprompts, spécifier leurs références et préparer l’intégration du profil pédagogique des essais 2 et 3.
Statut SPEC_READY_FOR_REVIEW. Livrable de cette tranche : spécification, catalogue et références candidates, diagnostic de reprise. L’implémentation des nouveaux contrats/rendus et leur validation pédagogique font l’objet des lots ci-dessous.

## Sources et limites de la rétro-analyse
Éléments disponibles : demandes successives visibles dans le contexte sur les cinq modes, le mémo recto verso et la matrice ; extraits de recherche d’historique ; fiche Prédiction textuelle (version 5 lue intégralement), Perception six-pages paysage v3 (six pages textuelles lues), fiche Matrice de confusion (six pages textuelles lues) et support Matrice de confusion PPTX (lecture partielle). Le livre cité est identifié, sans nouvel audit complet dans cette tranche.
Les recherches ne restituent pas le fil complet ni les prompts historiques intégraux. Les dates et contraintes 3/6/8 pages remontées par les résumés se rapportent à plusieurs variantes. Aucune n’est promue en longueur universelle. Les sommaires proposés ci-dessous sont une reconstruction fonctionnelle. Les métaprompts sont réécrits pour généraliser, sans être présentés comme verbatim du fil.
Le corpus privé et les liens personnels restent hors dépôt public. Seules la méthode et des exemples synthétiques peuvent être versionnés.

## Bootstrap constaté
Candidat essai 2 : experiment/narrative-procedure-ab-20261113 au SHA 75c8293de6984c6fac80e016528bdfa4ec019226, verticales/pedagogie/PROFILE.md, manifest.json, TRANSFER.md.
Cible dev observée : 3dc0d2a555ccb1aa5956751f3a55355a714b0ca1 ; revalider avant BUILD.
- Le profil sait définir une tâche observable, une épreuve, un corrigé et un réessai. C’est un invariant à conserver.
- Son manifeste sélectionne un seul template ai-enterprise-learning-six-page et une seule entrée Perception ; pin source ca67c1e historique.
- Les références de transfert soulignent les variantes du même agent et l’absence de mesure d’apprentissage/rendu physique. Les assertions textuelles sont propres à l’exercice.
- La skill canonique pedagogical-ai-learning conduit un format six-pages paysage. Le schéma pédagogique impose exactement six pages ; les slots content restent ouverts. Le schéma seul ne contrôle pas l’utilisabilité d’une consigne ou d’une correction.
- Une erreur d’exercice renvoyée systématiquement à Transmettre dépend du template ; dans une autre famille il faut rouvrir l’unité portant l’exercice.
Conclusion bootstrap-session/v1 : READY_FOR_SPECIFICATION. Implémentation multi-familles non établie ; renderer physique et acquisition non réévalués dans cette passe.

## Découpage des outputs
Huit familles candidates ; cinq modes constituent des variantes de contenu de la même famille d’approfondissement. Bibliographie, auto-évaluation et glossaire sont des composants réutilisables, avec export autonome sur demande.
1. PED-DEEP-DIVE : annexe d’approfondissement d’un concept ou mode.
2. PED-MEMO : aide-mémoire autonome, notamment récapitulatif des cinq modes sur un recto verso.
3. PED-MATRIX : matrice ou outil de diagnostic accompagné de sa méthode de lecture.
4. PED-PRACTICE : kit d’exercice, pièces apprenant, corrigé/rubrique et situation de transfert.
5. PED-FACILITATOR : note formatrice/Train-the-Trainer.
6. PED-METAPROMPT : instructions de génération à transmettre à une IA, avec procédure et contrat de sortie.
7. PED-ADDENDUM : complément borné à un support existant, ou révision globale explicitement demandée.
8. PED-VISUAL : carte, schéma ou support visuel d’un contenu validé, avec légende et version alternative textuelle.
Familles 1–6 étayées par les demandes/artefacts retrouvés ; 7–8 issues des échanges pédagogiques voisins, à traiter comme extensions candidates sans prétendre leur présence dans chaque tour F01.

## Sommaires et spécification de chaque famille

### PED-DEEP-DIVE — comprendre puis utiliser
ToC : acquis et prérequis ; définition et frontières ; mécanisme expliqué depuis une situation ; usages et combinaisons ; cas fil rouge ; essai guidé ; compréhension de la sortie et relances ; erreurs/limites ; mémo détachable ; ressources. Donner une note formatrice séparée si demandée.
La fiche Prédiction retrouvée matérialise trois blocs : comprendre avec un même service et deux besoins ; essayer/classer des messages fictifs avec ambiguïté et relances ; mémo autonome. Le six-pages ambassadeur ajoute TOWS, transmission, Ishikawa, intégration, chaîne de valeur et action : c’est un profil avancé explicite.
Mode Prédiction : valeur/catégorie/score, classification/régression, apprentissage vs utilisation, règle de comparaison, exemple numérique vérifié.
Mode Perception : entrée document/image/son, extrait ou signal, localisateur, absent/illisible/contradictoire, extraction distincte de l’interprétation.
Mode Création : brief et destinataire, génération, variantes, vérification des contraintes, factualité et droits selon le contexte ; production plausible et validée distinctes.
Mode Réflexion/Raisonnement : question, critères, hypothèses, alternatives, justification contrôlable et vérification ; aucune assurance fondée sur le seul récit des étapes.
Mode Agentique : objectif, outils et droits, plan d’action, événements, retour humain, erreurs et reprise ; une règle déterministe n’est pas automatiquement un agent.
Métaprompt de bloc : « À partir des sources retenues et de l’acquis [X], expliquer [notion] à [public]. Développer une situation fil rouge et montrer entrée, opération, sortie et vérification. Nommer les frontières. Écrire une activité avec pièces et correction, puis une situation nouvelle. Conserver les inconnues et attribuer les adaptations pédagogiques. »
QC : vocabulaire accessible, exemple cohérent, aucune fonctionnalité inventée, consigne réalisable, corrigé propre aux données et exercice de transfert distinct.

### PED-MEMO — retrouver et agir
ToC : repère des cinq modes ; quand choisir chacun ; entrée/sortie ; exemple bref ; contrôle utile ; combinaisons ; questions avant usage ; ressources courtes.
Recto proposé : tableau de repérage avec libellés stables et distinctions. Verso : un flux combiné, contrôle et auto-positionnement. Le recto verso est une contrainte explicite de ce cas.
Métaprompt : « Condenser les éléments validés en aide-mémoire autonome. Conserver les distinctions nécessaires et un exemple par mode. Prévoir une lecture rapide et une action accessible. Composer sur deux faces physiques si demandé, puis vérifier ce rendu. »
QC : un débutant identifie un mode et son contrôle sans renvoi au dossier complet ; taille de police et contenu vérifiés sur PDF.

### PED-MATRIX — lire deux dimensions sans les confondre
ToC : question ; axes ou convention du positif ; quadrants/cases ; exemple rempli ; interprétation ; limites ; gabarit à compléter ; correction ou discussion ; transfert.
Variante intégration/automatisation : axe vertical = intégration aux outils, données et processus ; horizontal = automatisation des tâches/actions. Distinguer ces axes de l’autonomie. Les postures Assistant/Copilot/Autopilot/Agent sont des repères de flux ; la progression peut suivre plusieurs chemins.
Variante confusion : définir l’unité observée, le positif, la référence et les deux erreurs avant les taux. Une analogie qualitative hors critère binaire ne devient pas une métrique statistique. Les cinq familles d’erreurs sont une typologie pédagogique attribuée ; ne pas présenter une norme officielle.
Métaprompt : « Définir la question et les conventions ; expliquer une case depuis un exemple, puis remplir l’ensemble sur des données cohérentes. Faire appliquer la matrice à un cas nouveau. Expliquer ce qu’elle permet et laisse ouvert. Vérifier les calculs et l’orientation des axes. »
QC : changer de convention inverse correctement FP/FN sans inverser le risque métier ; une matrice fournie avec axes inversés déclenche correction. Un mapping marque commerciale→posture ne suffit pas : vérifier la fonction, l’édition et la date si exemples outils demandés.

### PED-PRACTICE — fournir la situation complète
ToC apprenant : objectif ; scénario ; pièces autorisées ; consigne ; sortie attendue ; critères ; aide graduée ; réessai.
ToC corrigé séparé : attendus et variantes recevables ; règle de jugement ; erreurs fréquentes ; feedback ; nouvelle situation de transfert.
Métaprompt : « Concevoir une tâche observable depuis l’acquis. Fournir toutes les pièces nécessaires, une ambiguïté utile et une sortie attendue. Résoudre l’exercice sur ces pièces. Préparer une correction exploitable et une situation différente testant le même acquis. »
QC : pièce manquante ou illisible conservée comme telle ; aucune réponse inventée pour compléter ; identifiants pièce→réponse résolvables. Changer seulement l’ID ne constitue pas le transfert. La correction ne doit pas apparaître dans l’énoncé apprenant.

### PED-FACILITATOR — permettre une animation réutilisable
ToC : public et acquis ; matériel ; déroulé et durée proposée ; questions ; réponses et erreurs ; debrief ; adaptation de niveau ; remédiation ; vérification.
Métaprompt : « Préparer l’animation d’un support déjà défini. Décrire gestes et questions du formateur, points d’observation et feedback selon une réponse plausible. Étiqueter les durées proposées et expliquer une adaptation. »
QC : le formateur dispose des pièces/corrigés ; ce guide n’alourdit pas la fiche participant. L’acquisition réelle reste à observer.

### PED-METAPROMPT — déléguer la production avec précision
ToC : rôle et public ; résultat/acquis ; sources/périmètre ; famille/contraintes ; recherche ; conception pédagogique ; rédaction ; revue ; livraison/reprises.
Métaprompt maître : « Produire [famille] sur [sujet] pour [public/acquis], depuis [sources]. Reprendre [baseline/delta]. Identifier lacunes et rechercher seulement ce qui est nécessaire dans le budget. Concevoir l’épreuve et le fil de compréhension, puis proposer un sommaire relié aux acquis. Rédiger bloc par bloc avec exemples et pièces. Vérifier fond, correction, progression et lisibilité. Livrer les variantes demandées et préciser les validations réalisées. »
QC : expliciter si on demande un prompt ou un support final. Un prompt complet ne vaut pas document généré ; un document généré ne vaut pas apprentissage mesuré.

### PED-ADDENDUM — compléter à périmètre maîtrisé
ToC : point de départ et version ; manque visé ; apport ; insertion et raccord ; limites ; mise à jour du récapitulatif/sources.
Métaprompt : « Reprendre [support/version] et ajouter [apport] dans [périmètre]. Préserver les contenus acceptés hors delta, vérifier transitions et renvois. Si une reconception globale est demandée, la déclarer avant de restructurer. »
QC : les blocs hors delta sont préservés ; une refonte autorisée invalide la revue de forme concernée ; éviter répétitions et contradictions.

### PED-VISUAL — rendre une relation intelligible
ToC : question visuelle ; relations et hiérarchie ; labels ; légende ; exemple ; alternative textuelle ; contrôle.
Métaprompt : « Choisir un visuel qui explique [relation] depuis le contenu validé. Conserver distinctions, direction des axes et niveaux de preuve. Produire légende et description textuelle, inspecter lisibilité et intégration dans le support. »
QC : pas de branches coupées, labels dupliqués ou corrélation transformée en causalité. Le visuel ne peut créer un fait.

## Procédé commun et interfaces
Phase 1 contexte/recherche : PedagogicalIntent avec audience, acquis, prérequis, modalité, usage, famille provisoire, contraintes, sources, baseline/delta, budget et validation attendue.
Phase 2 analyse/conception : LearningAnalysis avec concepts, erreurs de compréhension, cas, épreuve, correction, transfert, besoins de recherche et preuves. Méthodes métier telles que TOWS/Ishikawa/Porter chargées uniquement si elles éclairent l’acquis et le mandat ; aucun format court ne les rend toutes obligatoires.
Phase 3 direction : PedagogicalBrief avec fil de compréhension, questions par bloc, exemples, pièces, sources et références d’analyse, densité et support. Chaque référence contribue à un bloc désigné après conception.
Phase 4 rédaction/rendu : contenu canonique par famille, manifeste des composants, sorties apprenant/formateur et références de corrections. Séparer revue des faits, cohérence pédagogique, contrôle physique et validation humaine.

Les noms d’objets ci-dessus sont des contrats conceptuels proposés, pas des classes implémentées. Réutiliser l’état et les identités du socle ; un seul graphe logique avec vues distinctes. JSON complet seulement quand des outils consomment ce schéma ; une fiche textuelle simple peut garder un canonique Markdown avec métadonnées. Ne pas multiplier des copies de contenu.

## Retrofit du catalogue et des références
Prévoir un index de familles avec id, statut, objectif, entrées, sections obligatoires/conditionnelles, composants, règles de longueur, références, renderer, cas d’évaluation et compatibilité.
References proposées : deep-dive.md, memo.md, matrix.md, practice.md, facilitator.md, metaprompt.md, addendum.md, visual.md. Cinq modes en paramètres et références ciblées, sans cinq workflows concurrents.
Le six-pages existant devient un profil explicite ambassadeurs/entreprise. Sa compatibilité demeure couverte. Les besoins F01 ne sont pas réduits à six fonctions fixes. Les contraintes de page appartiennent à chaque demande ou profil choisi, avec provenance.

## Compatibilité essai 2 / essai 3
Essai 2 : enrichir le manifeste de finalités/familles ; conserver l’ancienne route six-pages comme alias. Ouvrir la référence de famille puis les seuls paramètres de mode nécessaires.
Essai 3 : raccorder LearningAnalysis et PedagogicalBrief aux phases 2/3 du workflow commun, stocker l’état de recherche hors de la skill. La direction pédagogique remplace les critères de décision business par des acquis observables.
Ne pas copier toute la bibliothèque MBA dans le corps. Un retour d’exercice cible son unité, un changement de source cible ses descendants, un défaut de mise en page cible le renderer.
La pédagogie peut réutiliser des cas business avec leur attribution ; les objectifs d’apprentissage et le public restent propres à Sarah/F01.

## Lots d’intégration et dépendances
P1 : catalogue/routage multi-familles et contrat intention ; dépend #295, #23 et ADR-1007 proposé. Acceptation : mémo sélectionne memo, approfondissement sélectionne deep-dive, six-pages historique reste résolvable.
P2 : références de sommaires et métaprompts ; dépend P1 et #296. Acceptation : deux familles produisent des trames différentes depuis la même matière ; aucune instruction d’achat/pilote inventée.
P3 : kit exercice/corrigé et fixtures sémantiques ; dépend P2 et #130/#297. Acceptation : consigne exécutée avec ses seules pièces, correction plausible, cas inédit ; confusion/axes incorrects rejetés.
P4 : adaptateurs de rendu par famille ; dépend contenu stable et #128/#129. Acceptation : memo deux faces, deep-dive longueur demandée, six-pages legacy six pages, PDF relu et contenu accessible.
Réutiliser les owners existants. Une story transverse ne bloque pas les trois sprints business indépendants ; les adaptateurs pédagogiques sont un parcours supplémentaire.

## Cas de recette minimaux
- Prédiction pour débutant : estimation vs décision, modèle entraîné vs exemples de consigne, exercice de classement avec ambiguïté.
- Perception : pièce illisible et source localisable ; extraction vs interprétation ; corrigé sans invention.
- Création : contrainte obligatoire omise et source inventée à repérer.
- Réflexion : hypothèse fragile et alternative recevable ; correction indépendante de l’assurance du texte.
- Agentique : action hors périmètre, droits, retour humain et reprise.
- Mémo cinq modes : autonome sur deux faces ; au moins un flux combiné sans prétendre que les modes sont exclusifs.
- Matrice intégration : corriger axe vertical, conserver les deux trajectoires ; mapping marques conditionnel.
- Addendum : delta borné puis reconception explicite ; conservation et invalidation appropriées.
Chaque cas a données synthétiques, sortie attendue et contre-test. Les contrôles textuels ne remplacent pas le lecteur débutant.

## Done et preuves
Catalogue et références résolubles, legacy préservé, scénario entrant passant par le point d’entrée normal, résultat apprenant/formateur distinct, rendu effectivement contrôlé sur support demandé, revue humaine explicitement référencée quand obtenue. Comptabiliser NOT_RUN pour acquisition et formats non rendus. Conserver prompt original, versions et retours comme fixture d’acceptation ; sources privées dans leur espace, sans publier le livre.
