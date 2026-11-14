# Plan de convergence et état du dépôt — 14 novembre 2026

## État observé
181 issues et quatre PR ouvertes avant ce lot. Inventaire API paginé de 185 objets issues+PR, dernière page vide ; quatre PR relues avec leurs fichiers et checks. Inventaire des 181 titres et corps récupérés, approfondissement des owners centraux ; aucune prétention à une revue technique de chacune des 181 implémentations.
main 7000c86a7e54cafc68c5bb5ada9aeed5df186aae. dev absent puis restauré au même SHA par le mandat courant. Branche de préparation plan/convergence-essai3-20261114 issue de dev. Le troisième essai fonctionnel démarrera sur une branche de lot depuis le dev revalidé.
La branche experiment/narrative-procedure-ab-20261113 est conservée à 75c8293de6984c6fac80e016528bdfa4ec019226 comme source des deux essais. Son merge global importerait trop de changements pour constituer le protocole du troisième essai.

## Pilotage
Epic #294 ; S1 #295, S2 #296, S3 #297. #48 conserve le programme et les owners métier existants.
Préparation documentaire faite avant BUILD. Trois sprints séquentiels constituent un plan pour la prochaine journée de développement ; au calendrier courant, « demain » désigne le 15 novembre 2026 en Europe/Paris. L’ordre reste valable si l’exécution commence dès le 14. Aucun horaire de lancement, échéance ferme ni nouvelle automation n’est créé.
S1 effort moyen/élevé, S2 moyen, S3 moyen/élevé. Pas de points de vélocité ni d’estimation horaire fiable sans première tranche mesurée.

| Lot | Résultat et portée | Dépendance | Repli utile |
|---|---|---|---|
| Préparation | Inventaire, epic, ADR complémentaire, plan et handoff | Présente publication | Relecture documentaire sans BUILD |
| S1 #295 | Compatibilité étude/AnalysisResult ; question avant bloc ; plan et budget de recherche | Mapping et périmètre exact READY | Fixture de mapping et lacunes sans changement canonique |
| S2 #296 | Synthèse vers brief/scaffold et rédaction, perspectives produit/business | S1 intégré et contrôlé sur dev | Revue narrative manuelle sur sortie S1 |
| S3 #297 | Essai complet, reprise à froid et cas de réserve, rendu réel | S2 intégré, corpus et outils accessibles | Reçu de blocage précis, protocole et cas accessibles |

Une unité à la fois sur les fichiers partagés. Réutiliser une branche de lot existante après vérification de son owner. Branches feat/294-analysis-contracts, feat/294-narrative-binding, feat/294-trial3-validation proposées seulement lors du démarrage de chaque lot. PR de lot vers dev ; promotion cumulative vers main après preuves exactes de compatibilité et contrôle SDLC. Ni absence de CI ni ancien validate vert ne valent recette du nouveau HEAD.

## PR ouvertes
| PR | Objet | Fusion | Vérification observée | Disposition de revue |
|---|---|---|---|---|
| #12 | feat: add evidence-grounded CLOSING template | dirty | validate success au HEAD | CLOSING différé |
| #13 | docs: forbid run outputs in repo source | clean | validate success au HEAD | extraire hygiène RUN/BUILD après revue |
| #17 | Candidate: note fonds Hivest, storytelling et contrat de rendu | dirty | validate success au HEAD | harvest ciblé, template différé |
| #33 | [Draft] Storyteller Workbench — specs, Superpowers framing and gated delivery backlog | dirty | validate success au HEAD | conserver comme archive de conception |
Les quatre dispositions ont été commentées dans les PR. Aucun merge ni fermeture automatique. Les trois conflits demandent un réemploi ciblé ou une décision d’archivage après extraction, pas un écrasement.
Pour #13, vérifier les exceptions fixtures et l’autorité ADR-1004 avant d’adopter le patch.

## Backlog
[Inventaire des 181 issues et orientation proposée](BACKLOG-TRIAGE-2026-11-14.tsv).
Classement initial : 14 prioritaires convergence ; 32 run/dettes GreenYellow ; 117 en réserve pour réemploi ciblé ; 10 différés infrastructure ; sept owners/programmes ; un pilotage transversal.
Ce classement est une proposition de navigation issue de l’inventaire. Aucun ticket fermé sur cette seule classification. Les sujets anciens SPEC_ONLY ne deviennent pas automatiquement exécutables.
Douze issues existantes enrichies avec rapprochement daté : #26 #36 #42 #43 #44 #45 #46 #47 #48 #130 #165 #258.
Le nombre ouvert après création de l’epic et des trois lots est attendu à 185 issues ; vérifier avant d’annoncer le compte courant.

## ADR
Lecture des six ADR communs 1001–1006 et des quatorze locaux 0000–0013. Conserver les principes approuvés et leurs statuts. Réutiliser 1001 routage, 1002 connaissance, 1003 narration, 1004 RUN/BUILD, 1005 validation et 1006 convergence. Ajouter ADR-1007 proposé pour le workflow et la frontière analyse/brief ; réexaminer 1006 pour refléter la restauration de dev et le cycle de PR.
Les ADR locaux restent attachés au prototype. 0000 et 0004 historiques ; 0007 projection Graph1 optionnelle ; 0008 frontière RUN/BUILD et profils à préserver ; 0010 heuristique et migrations locales ; 0012 style/contextes de run distincts ; 0011 et 0013 migration et statuts de lecture à vérifier sur corpus lors d’un lot concerné. Les autres décisions locales conservent leur champ, sans élargissement du fait de la convergence.
La normalisation du 14 novembre déjà présente dans main explicite les lacunes d’autorité historique ; elle ne fournit pas une nouvelle approbation. Réécrire tous les ADR effacerait du contexte utile sans résoudre les bindings manquants.

## Critères anti-dérive
Avant chaque lot, mandat original, corpus autorisé, résultat attendu, références de méthode, scope fichiers, propriétaire, contrôle positif/négatif et condition de sortie.
Avant toute synthèse, analyses effectivement produites, limites et questions résiduelles.
Avant livraison, intelligibilité du produit et de la logique business, parcours concrets, preuves et inconnues ; aucune recommandation fabriquée.
Tout progrès est lié à un artefact et une version. Les scores A/B précédents ne sont pas des critères d’acceptation.
