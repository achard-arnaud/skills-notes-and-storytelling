# Résultats de l’essai — procédure rédactionnelle factorisée
Date : 13 novembre 2026. Statut : candidat expérimental, pas de migration main/dev.

## Décision proposée
Poursuivre une procédure rédactionnelle commune avec références conditionnelles, en préservant des contrats de contenu distincts et des analystes spécialisés. Le test soutient une réduction du contexte méthodologique chargé. Il ne démontre ni un gain de coût total ni une supériorité qualitative globale.

## Versions et cas
- A : main 16bcb4325bcace66c2c22fa33a97402cb00e1de9, skill racine et références sélectionnées.
- B : candidat 0.1, commit 849c5c5c14a02a4dfe8c8b73febbcf8ef3ffb51c, même brief et même source.
- B2 : candidat renforcé 0.2, nouvelle exécution dans un thread frais.
- Cas : prompt Current AI / AI Potluck fourni dans cette conversation ; two-pager produit et one-pager company compagnon. Le run original n’est pas horodaté de manière vérifiable dans la fenêtre des dernières 24 heures.
- Source : extrait d’annonce attribué, non corroboré dans cet essai ; aucune recherche externe pour maintenir le même paquet de preuves.

## Mesures observées de navigation
Les cohortes excluent le brief commun, les sorties rédigées et les journaux ; elles gardent toutes les instructions et références de méthode réellement lues, y compris AGENTS et l’ADR commun.

| Mesure | A actuel | B candidat 0.1 |
|---|---:|---:|
| Fichiers de méthode lus | 15 | 10 |
| Octets UTF-8 de méthode | 60 473 | 20 009 |
| Mots whitespace de méthode | 7 567 | 2 731 |
| Mots du two-pager | 1 034 | 883 |
| Octets des artefacts Markdown/JSON produits | 26 326 | 33 276 |
| Tokens modèle / coût / cache | inconnus | inconnus |

B charge 66,91 % d’octets de méthode en moins dans cette paire. Ses sidecars structurés produisent davantage d’artefacts. Les octets/mots ne sont pas les tokens modèle, ni le contexte total système/historique, ni l’effort cognitif. Aucun résultat de vitesse : le temps mur inclut staging, attente et concurrence ; trois dépendances A initialement manquantes du snapshot ont été rétablies depuis main.

[Mesures et liste des fichiers](evals/current-ai/metrics.json) ; logs complets dans les dossiers A/B. Le volume total d’un pipeline de recherche/analyse/rendu n’est pas testé.

## Revue indépendante en aveugle
Mapping révélé après revue : X = B ; Y = A. Le reviewer ne voyait ni méthode ni compteurs.
- Aucun fait matériel inventé identifié dans les deux two-pagers.
- B est plus autonome sans sidecar et plus explicite sur les capacités nécessaires au premier use case.
- A formule mieux l’objection qui pourrait inverser la thèse et le test discriminant.
- Titres d’action partiellement appliqués dans les deux.
- Aucun vainqueur global ; choix dépendant de l’usage de diffusion ou de discussion critique.

[Revue aveugle détaillée](evals/current-ai/blind-review.md). Le reviewer ne recevait volontairement que le two-pager de chaque paquet : ses réserves sur le compagnon absent ou le déroulé de production sont des limites du champ de revue, pas une absence réelle des fichiers conservés.

## Renforcement 0.2 et deuxième exécution
Les ajouts exigent une objection/test de révision visibles dans le document, une revue des titres seuls, la résolution autonome des renvois et la vérification des capacités nécessaires aux cas proposés. Le mapping des chemins a été rendu portable.

Une nouvelle revue, depuis le brief et le seul two-pager B2, donne PASS sur ce document : attribution, utilité produit, objection, test discriminant et autonomie. Une amélioration reste proposée : aligner explicitement la fréquence d’un usage hebdomadaire avec l’objectif d’usage quotidien. Le compagnon et les sidecars sont conservés dans B2 ; cette revue ne les certifie pas.

B2 est une passe de renforcement sur le même cas ; elle ne compte pas comme réplication indépendante du résultat A/B. Les contrôles de rendu physique, liens réseau et autres domaines restent NOT_RUN.

## Contrat analytique
Le schéma et le validateur acceptent un résultat semi-structuré, ses input_claim_refs, contre-preuves, inconnues et affects_blocks. Onze tests exécutés passent, couvrant aussi références malformées, statuts non autorisés, dates et réouverture ciblée. La fixture TOWS est entièrement synthétique. Aucun vrai pipeline de dizaines de skills, aucune qualité de raisonnement TOWS, PESTEL ou VRIO ne sont certifiés.

## Leçons de migration
1. Main est déjà partiellement organisé comme procédure + références. Le gain attendu porte sur la sélection et le chargement, pas sur le déplacement de tous les fichiers.
2. Un scaffold sémantique est plus qu’un CSS : il impose parfois des questions et des preuves. Versionner et tester cette obligation.
3. Conserver les huit compétences d’analyse comme spécialisations ; factoriser leurs chartes répétées. Le rédacteur reçoit leurs résultats, il ne les absorbe pas toutes.
4. Les quatre routes ne sont pas MECE par nature. Déclarer une route principale et les angles secondaires ; appliquer MECE aux découpages sur un critère explicite.
5. Préserver la spécificité pédagogique (acquis, exercice, feedback) et technique (frontières, contraintes, échecs). Leur transfert n’est pas testé ici.
6. Le contexte évité peut être remplacé par de la génération structurée supplémentaire ; mesurer l’ensemble avant toute promesse de coût.
7. Migrer un contrat à la fois sur dev, via branche courte, avec cas de transfert et reprise contradictoire ; garder cette expérience sur sa branche jusqu’à décision.

## Conditions qui changeraient la recommandation
Rejeter ou restreindre la factorisation si elle fait disparaître une exigence métier, augmente les références non chargées, exige des retours fréquents au canon ou dégrade l’apprentissage/les compromis techniques. Renforcer l’adoption si des cas indépendants multi-domaines et une reprise à froid montrent fidélité, autonomie et contrôle de l’effort.

