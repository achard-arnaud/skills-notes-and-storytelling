# Audit contradictoire et consolidation — 11 septembre 2026

## Verdict
Le passage Claude 744279c améliore les consignes, mais ne démontre pas une exécution complète.
La consolidation conserve son effort par étape et son classement distinct des fragments, puis les
branche sur les helpers déterministes et les tests développés dans cette conversation.

| Point | Constat vérifié | Décision et contrôle |
|---|---|---|
| QA comparative | Le rapport dit explicitement « aurait fait » et absence de régénération | Conserver comme analyse prospective ; ne pas l’appeler test réussi |
| Priorité aux entrées | Le texte qualifiait toute affirmation utilisateur de source primaire | Priorité de traitement seulement ; statut de preuve conservé |
| Debug | Un enum opposait debug et lourd | Debug indépendant de la profondeur ; alias anciens acceptés |
| Effort par étape | JSON configurable pertinent, absent de mon premier runtime | Configuration consommée par plan ; réglage réel non présumé |
| Classement fragments | Poids dédiés utiles mais non calibrés | Classement séparé ; top-k d’affichage par claim ; toutes les pièces conservées |
| Indépendance | Deux documents étaient censés renforcer la preuve | L’indépendance dépend des familles de sources, pas du nombre de documents |
| Zoom | Voisinage profondeur 1 insuffisant pour certaines dépendances | Fermeture typée avec contradictions conservées ; dépassement signalé |
| Quatre couches | Renvois documentaires ajoutés aux sept templates | Profils structurés par template, consultables séparément |
| Historique | « Logique causale unique » trop réducteur | Dominante causale avec relations et composition déjà multiples |
| Installation | Nom renommé par Claude | Conserver skills-notes-and-storytelling ; ne pas installer deux variantes |

## Ce qui est réellement exécuté
30 tests unitaires et de régression passent localement. Ils vérifient les configurations, l’intake
forçant lourd, les alias, les lignées, les contradictions, le zoom, les limites de contexte et les
révisions hors périmètre. Le validateur historique passe pour 7 templates et 4 modes. Les tests
n’établissent ni vérité des sources, ni qualité narrative, ni équivalence entre modèles.

Le rejeu Rivard produit quatre notes distinctes et un registre : 16 fragments, 25 claims, 6 relations,
4 sections. 43 pages physiques sur 146 ont été déclarées lues par le passage de recherche ; les 103
autres ont été inventoriées puis exclues du périmètre borné. Ce n’est pas une lecture intégrale.
Le contrôle initial du registre a rejeté des sources « scoped » sans détail de couverture. La couverture
existante a été rattachée au registre ; les contrôles ont ensuite été relancés. L’essai indépendant a
atteint sa limite d’usage après avoir écrit ses artefacts : leur reprise ne vaut pas une validation
indépendante complète. Le rapport et les données utilisateur restent hors du dépôt public.

## Comparaison au premier livrable Rivard
| Avant observé | Après observé | Limite |
|---|---|---|
| Une note regroupant quatre axes | Quatre notes : cabinet, personne, mouvement, méthode | Version texte, pas nouveau DOCX inspecté |
| Traçabilité de pipeline non matérialisée | Fragments, claims, graphe, couverture et packet enregistrés | La QA de structure ne prouve pas la lecture |
| Numéros d’articles confondus avec pages | Localisateurs en pages physiques | Contrôle humain des passages reste nécessaire |
| Risque de recommander un ajout financier à Meridian | Chapitre financier explicitement identifié, pages 103–105 | Résultats modélisés séparés des gains réalisés |
| Croisement demandé mais référence imprécise | Matrice préparée, identité du comparateur non substituée | The AI Profitable Advantage reste à fournir précisément |

## Coût et architecture
Une skill est un ensemble d’instructions chargé selon sa pertinence. Le modèle suit ses étapes ; le
harnais fournit les outils et peut exécuter les scripts. Un script de routage n’est ni un modèle ni un
système d’exploitation. Les artefacts intermédiaires rendent le travail reprenable sans devoir relire
le corpus entier. Les quatre couches évitent de dupliquer méthode, preuve et style dans chaque template.
Le mode chat garde des paquets plus petits ; le mode work peut conserver les fichiers et exécuter la QA.
Les capacités réelles priment sur le nom de l’interface. Un PDF force la discipline lourde dans les deux.

Le premier point d’entrée comptait 892 mots. La première refonte le ramenait à 519 avant consolidation.
Ces comptes sont des mots, pas des tokens facturés ; les références, sources, outils, sorties et reprises
s’ajoutent. Les pourcentages antérieurs d’économie sans mesure sont retirés. Aucune comparaison contrôlée
entre modèles économiques n’a été réalisée. La skill réduit des ambiguïtés et délègue des contrôles
mécaniques, mais ne remplace pas le jugement nécessaire pour arbitrer des preuves contradictoires.

## Suite priorisée
1. Évaluer plusieurs tâches à qualité égale avec télémétrie de coûts et corrections, avant downsizing.
2. Calibrer les poids de fragments sur erreurs observées, pas sur trois succès déclarés.
3. Mesurer rappel des preuves et taille des fermetures de dépendances avant un reranker appris.
4. Garder débrief 360, plan d’action et rétro-ingénierie candidats jusqu’à leurs propres cas de validation.
