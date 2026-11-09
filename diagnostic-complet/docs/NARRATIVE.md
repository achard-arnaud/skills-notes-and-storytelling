# Composition du rapport long

## Du mandat au paragraphe

Le mandat borne la décision à éclairer. L'arc propose une démonstration ; les piliers en fournissent les vues analytiques. Le scaffold lecteur fixe les questions successives, la tension, les objections, les transitions et les emplacements latéraux. Chaque paragraphe a une fonction identifiable et consomme un paquet local de claims/fragments/relations ; le remplissage n'est pas un résumé global relancé à chaque passe.

Pour chaque section, conserver question, bénéfice lecteur, points démontrés, objection, limites et transition. Pour chaque paragraphe, conserver texte, claims mobilisés, piliers pertinents, état de revue et empreinte. Un paragraphe réécrit perd son verdict éditorial précédent. La vérification d'un fait peut rester valide si sa source et son scope n'ont pas changé ; une source infirmée invalide ses descendants.

La génération, la vérification mécanique, la revue par un autre agent et l'approbation humaine sont quatre actes distincts. Le prototype contrôle des liens et des empreintes ; il ne sait pas approuver la qualité argumentative à la place du lecteur. Les tests ne doivent jamais poser `editorial=true` au nom de François.

## Side stories

Une side story doit expliquer pourquoi elle est hors du tronc, ce qu'elle apporte, où elle se place et où elle ramène. Lifecycle : candidate → validated → promoted → retired, sans passage automatique par rendu. Une illustration n'est pas une nouvelle preuve.

| Type | Rôle business possible | Condition de retour |
|---|---|---|
| analytical_focus | Déplier une architecture, un mécanisme de valeur ou un point de gouvernance | Retour à une décision précise |
| dezoom | Passer du site au portefeuille, puis au marché | Échelles, mécanisme de transmission et payoff local explicites |
| comparator | Comparer un acteur ou un cas aux conditions de la cible | Différences et limites de transférabilité visibles |
| method | Expliquer baseline, mesure, évaluation ou ROI | Dans ce prototype, retour obligatoire pour simplicité ; adaptation plus stricte que certaines exceptions du donneur |
| false_lead | Examiner une solution séduisante puis ses limites | L'objection change l'interprétation du cas |
| object_focus | Partir d'un équipement, d'un document ou d'une mesure | L'objet éclaire le mécanisme et la décision |
| callback | Reprendre une notion déjà éclairée | Ancre stable vers le passage concerné |
| portrait / detour / also | Apporter un acteur ou un complément utile | Contribution et borne explicites, sans anecdote gratuite |
| veille_corporate_perso | Lire les signaux publics d'un acteur (trajectoire, communications, décisions) à travers un point de vue personnel explicitement signé | Retour vers une décision précise du mandat ; observation et lecture séparées |
| veille_academique | Faire le point sur une littérature, un résultat de recherche ou une méthode éprouvée | Retour vers la question méthodologique posée ; niveau de preuve explicite |

Le contrat local est volontairement plus strict sur les retours que le donneur, qui admet certaines exceptions apparatus/method. Cette différence est une décision d'expérimentation, pas une réécriture silencieuse de la source.

### Choisir entre veille corporate personnelle et veille académique

| Question du lecteur | Type à retenir |
|---|---|
| Que fait cet acteur, et que dit-il de sa trajectoire ? | veille_corporate_perso |
| Que sait-on, avec quel niveau de preuve, sur ce mécanisme ? | veille_academique |
| Ai-je besoin d'un jugement sur une stratégie d'acteur ? | veille_corporate_perso, à condition que le jugement soit signé |
| Ai-je besoin de savoir si un résultat tient hors de son étude ? | veille_academique |

Une même matière peut relever des deux types. Dans ce cas, deux side stories séparées, chacune avec son tag, plutôt qu'un encart mixte.

## Formats et lignes éditoriales des veilles

Les deux lignes restent séparées : une veille ne reprend jamais le ton, la source ou le verdict de l'autre. Chaque encart porte un tag couleur visible dans le plan et dans le HTML candidat.

| Tag | Type | Couleur (fond / bordure) | Usage |
|---|---|---|---|
| `[VCP]` | veille_corporate_perso | ambre `#FEF3C7` / `#B45309` | Signal public d'un acteur + lecture personnelle |
| `[VAC]` | veille_academique | indigo `#E0E7FF` / `#3730A3` | Littérature et niveau de preuve |

Les couleurs sont des tokens de thème provisoires ; elles ne doivent pas entrer en conflit avec les couleurs de piliers.

### Veille corporate personnelle — `[VCP]`

- **Format** : 150 à 300 mots, un encart, une figure optionnelle. Structure fixe : signal daté et sourcé → lecture personnelle → implication pour la décision du lecteur → retour vers le tronc.
- **Sources** : publications de l'acteur (communiqués, rapports annuels, pages corporate), presse identifiée. Chaque signal porte date, source et URL ou empreinte. Aucune source tierce non vérifiée.
- **Ligne éditoriale** : le fait d'abord, l'opinion ensuite, jamais dans la même phrase. La lecture personnelle est signée (« lecture de l'auteur ») et ne vaut ni position de l'entreprise ni verdict du rapport. Pas de jugement sur des personnes. Aucun argument d'offre ou de fit fournisseur dans cet encart.
- **Niveau de preuve** : `observed` (signal publié) ou `interpreted` (lecture). Un encart ne contient pas de tendance présentée comme fait.
- **Limites à écrire** : date de collecte, périmètre couvert, un signal n'est pas une tendance.
- **Retour** : une décision précise du tronc (piliers ou section), jamais une conclusion générale.

### Veille académique — `[VAC]`

- **Format** : 250 à 450 mots, ou un tableau de 3 à 5 références. Structure fixe : question de recherche → références (auteur, année, venue, DOI ou URL) → résultat et niveau de preuve → portée et transférabilité au cas → retour.
- **Sources** : revues à comité de lecture, rapports de référence identifiables. Les préprints sont signalés comme tels. Une source non citable n'entre pas.
- **Ligne éditoriale** : prudence sur les résultats. Distinguer résultat rapporté, reproduit et contesté. Dire le contexte de l'étude (taille, population, durée, conditions) avant toute extrapolation. Aucune généralisation au-delà de ce contexte sans étape de transfert explicite.
- **Niveau de preuve** : `peer_reviewed`, `preprint`, `grey_literature` ou `opinion`, affiché dans l'encart.
- **Limites à écrire** : ce que l'étude ne mesure pas, et les contre-résultats connus.
- **Retour** : la question méthodologique du tronc (baseline, ROI, protocole de pilote), pas un argument de vente.

### Règles communes

- Une side story ne crée aucune preuve nouvelle : toute affirmation renvoie à une source du corpus ou à une référence citée.
- Un tag manquant ou un format non respecté rend l'encart `candidate` et bloque sa promotion.
- Les formats des autres types (analytical_focus, dezoom, comparator, method, false_lead, object_focus, callback, portrait/detour/also) restent à définir : ils sont à rechallenger avec l'inventaire.

## Inventaire candidat à valider après import GreenYellow

**Statut : à rechallenger (retour HITL-258).** Trop peu de pistes, descriptions insuffisantes, pas de format, pas d'objectif ni de critère permettant de choisir entre deux options. Chaque candidat doit être réécrit avec : objectif, format, tag, ligne éditoriale et critère de choix.

1. Vision et diagnostic thermique : de l'observation au signal exploitable, puis à la décision d'inspection. L'apport VisioSense annoncé reste à recevoir et à vérifier ; aucun fit fournisseur n'est établi.
2. Ombrières et réalité du site : ombrage, géographie, accès et exploitation, au service du diagnostic industriel.
3. Sous-performance et faux positifs : météo, capteurs, modèle attendu, équipement et contrat ; revenir au triage opérationnel.
4. OEM et couche d'orchestration : architecture, droits sur les données, interfaces, dépendances et sortie ; revenir au choix build/buy/partner.
5. Baseline et ROI : pourquoi une promesse de gain n'est pas encore une économie attribuable ; revenir au protocole de pilote.
6. Finance des actifs et performance : relier mesures, engagements, risque et financement sans réduire le sujet à la comptabilité.
7. Fonctions corporate : usages transverses avec leur propre économie et adoption, distincts des usages industriels.
8. Gouvernance et déploiement local : responsabilités groupe/pays/site, compétences, droits et supervision.
9. Data, ML et LLM : expliquer le choix technique par la décision à prendre, pas par effet de mode.

Cet inventaire est un ensemble de pistes, pas neuf encarts à produire obligatoirement. Chaque candidat sera relié à sa preuve, son emplacement, sa question et son retour lors du dry run.

## Couverture et profondeur

Une disposition explicite rend les absents visibles : inclus dans le tronc, inclus en side story, recherche requise, différé ou non retenu avec motif. Un graphe dense ou `unaccounted=0` ne prouve ni qualité ni profondeur. Ne jamais raccourcir une limite matérielle uniquement pour passer un budget de contexte : scinder la tâche.

## Visuels

Le diagramme doit rendre une relation exacte plus claire. Mermaid conserve les relations typées et les limites ; le prototype peut fournir la source lisible sans prétendre exécuter un moteur Mermaid. Ne pas transformer une flèche de navigation ou une hypothèse en causalité certaine.
