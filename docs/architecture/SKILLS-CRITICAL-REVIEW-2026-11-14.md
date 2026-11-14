# Revue critique et renforcement des méthodes rédactionnelles

14 novembre 2026. Cette passe corrige la nomenclature des trois méthodes d’ingénierie, harmonise les ressources d’icônes et renforce les contrats de preuve, de révision et d’évaluation. Elle s’appuie sur le [rapport de normalisation des 14 ADR](ADR-NORMALIZATION-2026-11-14.md), sans présenter cette lecture comme une nouvelle revue intégrale des quatorze textes ni un audit du runtime.

Les méthodes personnelles restent hors du dépôt public. Ce rapport décrit le changement et ses preuves ; il ne copie aucun SKILL.md, n’active aucun workflow et ne modifie aucun manifeste de projet.

## Noms et catégories

| Ancien nom | Nom canonique | Catégorie visuelle |
| --- | --- | --- |
| prd-master | engineering-prd-authoring | AGILE |
| adr-master | engineering-adr-authoring | Développement et IT, `</>` |
| story-tdd-master | engineering-story-specification | AGILE |
| learning-note-maintenance | inchangé | Pédagogie, mortier |
| schema-flow-master | inchangé | Développement et IT, `</>` |

Le préfixe engineering- reprend la convention de la famille d’ingénierie. Le rôle agile se traduit par la catégorie graphique, sans introduire un second préfixe concurrent. Les identités et liens des skills sont conservés ; les anciens noms restent des repères documentaires, sans promesse d’alias d’invocation automatique. Les bindings courants et prompts d’entrée sont actualisés ; les traces historiques ne sont pas réécrites.

Les trois ressources de catégorie proviennent des assets canoniques existants. Leurs SVG ont été rendus localement et inspectés. Les ressources de catégorie sont conservées dans chaque paquet. En revanche, la plateforme réécrit le chemin configuré vers son icône générée et remplace également une substitution directe du fichier par défaut : l’alignement des logos visibles n’est donc pas acquis. Le contrôle de l’interface a rencontré une page de connexion ; aucune authentification n’a été effectuée. Le contenu méthodologique publié et les assets de catégorie sont contrôlés séparément de ce blocage visuel.

## Critique et axes appliqués

| Axe | Faiblesse observée | Changement concret | Contrôle pertinent |
| --- | --- | --- | --- |
| Routage et coût de lecture | Des références de rédaction étaient lues systématiquement pour une correction mineure | PRD : voie patch local et minimum de contrat selon risque ; détails conditionnels | Revue d’un extrait, sans audit de marché ni élargissement implicite |
| Histoire et arbitrage | La chaîne argumentative neuve pouvait être appliquée à une normalisation historique | ADR : distinguer trace source, implication de revue et proposition actuelle ; ne pas reconstituer un débat absent | Replay historique lacunaire et comparaison actuelle correctement étiquetée |
| Autorité | Approbation d’un périmètre susceptible d’être étendue à tout le document | PRD/ADR : statut et preuve par clause lorsque nécessaire ; dates et portées conservées | Pilote approuvé sans multi-sites ; conservation acceptée sans projection groupe acceptée |
| Nature de preuve | Matériau fourni, hypothèse et preuve corroborée trop facilement confondus | PRD : nature et vérification séparées ; registres des décisions et hypothèses | Estimation de 40 % conservée comme hypothèse, sans gain mesuré ni cible approuvée |
| Valeur et mesure | Indicateur de parcours pouvant devenir preuve de valeur | PRD : distinguer proxy, résultat et mécanisme de valeur ; baseline et seuil à instruire | Clics économisés distincts du temps effectivement gagné |
| Qualité des tests | Attendu produit par la fonction testée et couverture proclamée sans dénominateur | Stories : oracle indépendant, contre-exemple discriminant, traçabilité versionnée et exclusions | Sérialiseur circulaire rejeté ; « 100 % » non justifié ; comportement indécis bloquant |
| Péremption | Un reçu vert ancien ou une ancienne image pouvait survivre au changement de besoin | Invalidation des dépendants, source exacte du rendu, vérification de version et d’intégration | Besoin v2 non couvert par reçu v1 ; hash de rendu périmé refusé |
| Intégrité d’évaluation | Prompts et attendus co-localisés ; ancien reçu de conception dans une référence active | Séparer prompts bruts/oracles, déplacer le reçu historique hors de la méthode active | Replays sans accès à l’oracle ; validation structurelle distinguée du comportement |
| Contrôle exécutable | Reçu décrit en prose seulement | Contrat de méthode v1.1.0, reçu v1.0 et contrôleur Python standard, optionnel pour changements matériels | Treize cas de cohérence, dont faux PASS, preuve absente et source périmée |
| Présentation | Noms et icônes disparates | Renommage par identité conservée, prompts canoniques et trois icônes de catégorie | Validation noms, liens internes, assets et contenu publié ; remplacement des icônes par la plateforme détecté |

L’objectif reste une procédure courte avec références mobilisées au bon moment. Les noyaux restent sous 220 lignes. Les scripts optionnels ne deviennent pas une formalité imposée à chaque correction orthographique.

## Contrôle du reçu et limites de sa preuve

Le reçu sépare syntaxe, sémantique, rendu et intégration avec PASS, FAIL ou NOT_RUN. PASS/FAIL exige une action déclarée effectuée, sa méthode et une preuve ; NOT_RUN exige une raison. Un rendu PASS exige une ressource et une empreinte correspondant à la source courante. Une sortie prête ou livrée ne conserve pas de dérivé explicitement invalidé. Une livraison visuelle réclame un rendu inspecté et une preuve d’intégration.

Le contrôleur détecte les incohérences de déclaration. Il ne vérifie ni l’authenticité d’un log, ni la vérité métier, ni une approbation, ni la disponibilité d’une ressource distante. L’égalité des empreintes établit un rattachement déclaré, pas la justesse du schéma. Une image Graphviz ne prouve pas un parseur ou rendu Mermaid exécuté.

Les treize cas ont été exécutés sur chacune des cinq copies du contrôleur : il s’agit des mêmes treize scénarios répétés sur cinq paquets, pas de soixante-cinq scénarios indépendants. Les checksums des copies sont comparés pour repérer une divergence de distribution.

## Replays comportementaux exécutés

Les agents relecteurs ont reçu la demande brute et l’accès à la méthode, sans oracle ni ancien résultat. Ils n’ont effectué aucune mutation de produit.

| Replay | Résultat observé | Limite |
| --- | --- | --- |
| PRD : réservation/annulation approuvées, multi-sites non approuvé, 40 % non mesurés et KPI de clics | Périmètre borné, approbation attribuée, bénéfice hypothétique, proxy distingué du résultat et conditions d’engagement explicites | Énoncé seulement ; PRD intégral et trace d’approbation non fournis ; aucune mesure terrain |
| ADR : date ambiguë, acceptation partielle, alternatives absentes, reçu passé et revendication « 100 % qualité » | Histoire préservée, autorité par clause, alternatives actuelles étiquetées, disponibilité non extrapolée et couverture structurelle distinguée de qualité | Aucun original ni corpus de quatorze fichiers relu par cet agent ; preuve du comité non inspectée |
| Stories : besoin v2 proposé, rôle inconnu, reçu vert v1 et oracle circulaire | Statut bloqué, oracles indépendants et contre-exemples proposés, reçu v1 non recyclé pour v2, aucune couverture fictive | Spécification de tests seulement ; aucun test logiciel ni cycle Red/Green exécuté |
| Stories et graphique : deux relectures parallèles, deux accords et refus bloquant | Lecture effective de Schema Flow Master ; AC, tests spécifiés et source de processus avec synchronisation explicitée | Notation pédagogique non normative ; parseur, rendu et intégration NOT_RUN, aucun asset inventé |

Les sorties et traces ont été revues contre les contraintes des cas. Ces observations ne constituent ni une statistique de performance, ni un test d’apprentissage utilisateur, ni un benchmark multi-modèles. La réussite des cas ne garantit pas toutes les demandes futures.

## Protocole de réemploi

1. Capturer la version de méthode et la révision des sources réellement utilisées.
2. Choisir la plus petite branche de travail et les seules références nécessaires.
3. Identifier chaque défaut à sa première couche : preuve, autorité, périmètre, modèle, texte, rendu ou intégration.
4. Corriger puis invalider et rejouer les dérivés touchés, sans réécriture globale par défaut.
5. Séparer les vérifications structurelles, les contrôles déterministes et les replays comportementaux ; conserver les inconnues.

Le passage d’une correction locale à une règle générale exige un signal réutilisable ou une demande explicite. Les fixtures restent synthétiques ; les ressources privées ne sont pas copiées dans ce dépôt. Le rapport précédent et ses résultats de runtime demeurent historiques : cette passe ne relance pas les 312 tests du prototype, car aucun code de ce prototype n’a changé.

## Sources officielles consultées

- [OpenAI — Build skills](https://learn.chatgpt.com/docs/build-skills), consulté le 14 novembre 2026 : description comme signal de sélection, structure du paquet et chargement progressif.
- [OpenAI — Testing Agent Skills Systematically with Evals](https://developers.openai.com/blog/eval-skills), consulté le 14 novembre 2026 : demandes de test, traces et livrables capturés, contrôles et itération.
- [OpenAI — Rethinking skills and prompts for GPT-6 Astra](https://learn.chatgpt.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra), consulté le 14 novembre 2026 : noyau minimal et références contextuelles ; pas de garantie spécifique de qualité de ces skills.

Les contrats de reçu, règles d’autorité par clause et critères des replays sont des adaptations de conception de ce lot, pas des standards officiels OpenAI ou une certification de conformité.


## Ancrage dans le backlog et admission SDD/TDD

Synchronisation de la PR #300 (main 2b3de4d4fc23455d21a76fdee8a81b98df66a098) vers dev. Le rapport décrit les méthodes personnelles ; il ne les installe pas dans ce dépôt.

| Besoin | Ticket owner | Application attendue |
|---|---|---|
| Mapping et compatibilité de l’analyse | [#303](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/303), parent #295 | Champ, statut, source/destination, invariant et traitement des inconnues ; question avant blocs |
| Synthèse et brief | [#296](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/296) | Hypothèses, résultats et justifications contrôlables ; approbation périmétrée |
| Cas de réserve et rendu | [#297](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/297), #130 | Oracles distincts, versions épinglées, contre-exemples et contrôles de rendu réellement exécutés |
| Pédagogie | [#301](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/301) | Acquis observables ; correction et transfert distincts ; familles candidates et rendu non validé explicités |
| Risques et preuves de tests | [#142](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/142) | Schéma, sémantique, rendu et intégration évalués séparément, avec dénominateur de couverture |

Entrée de navigation : [epic #294](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/294). La tranche #303 est documentaire et bornée ; l’admission vérifie base dev, disponibilité de l’owner et synchronisation. Les autres lots gardent leurs dépendances. Une méthode publiée ou un reçu ancien ne rend pas automatiquement le BUILD éligible.

Noms canoniques à utiliser dans les nouveaux handoffs : engineering-prd-authoring, engineering-adr-authoring et engineering-story-specification. Les anciens noms demeurent des références historiques, pas des alias d’invocation garantis. Pour chaque exécution, résoudre les skills effectivement disponibles.
