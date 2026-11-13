# Évaluation rapide des dix skills éditoriaux (9 novembre 2026)

Cette évaluation est une **exécution** (RUN) : ses sorties brutes restent hors du dépôt. Seul ce résumé, sans contenu privé, est versionné (voir `doc/architecture/ADR-0008-frontiere-run-build.md`).

## Méthode

- 13 cas d'évaluation, soit au moins un par skill, avec des entrées **synthétiques** inférées à partir de la forme des vrais exemples (entreprise fictive AcmeÉnergie).
- Chaque cas est joué deux fois par un agent indépendant : **avec** le skill et **sans** skill (connaissances générales seulement).
- Chaque réponse est notée par un autre agent sur 3 à 6 assertions écrites à l'avance (59 au total), avec preuve citée.
- Méthode du skill-creator : exécution, notation, lecture des écarts, seconde passe de corrections.

## Résultats

| Skill | Cas | Avec skill | Sans skill |
|---|---|---|---|
| Adoption et changement | usines à prototypes ou pratique durable | 4/4 | 1/4 |
| Capacités d'intelligence artificielle | capacité avant produit | 5/5 | 3/5 |
| Fonctions transverses | transverse ou industriel | 3/3 | 2/3 |
| Fondations de données | pilotage décisionnel avant IA | 3/4 | 2/4 |
| Économie et financement | gain annoncé ou économie attribuable | 5/5 | 3/5 |
| Gouvernance et contrôle | dépendance fournisseur et réversibilité | 4/4 | 2/4 |
| Chaîne de valeur industrielle | du signal à la décision | 4/4 | 1/4 |
| Marché et concurrence | archétypes avant les noms | 5/5 | 4/5 |
| Conception du fil principal | repartir de zéro, preuves seules | 5/5 | 2/5 |
| Conception du fil principal | révision par différence | 5/5 | 4/5 |
| Side stories | lexique avec contre-point | 5/5 | 2/5 |
| Side stories | choix du type et pitch | 6/6 | 2/6 |
| Side stories | refus d'une citation sans source | 4/4 | 2/4 |
| **Total** | | **58/59** | **30/59** |

## Ce que montrent les écarts

- Sans skill, les réponses inventent des chiffres, supposent des fonctions de l'organisation, reprennent l'ancien rapport comme réserve de paragraphes, rédigent une citation entre guillemets attribuée à une direction fictive, et laissent les side stories sans problématique ni ponts.
- Les cas où le gain est faible (marché 5/5 contre 4/5, révision par différence 5/5 contre 4/5) portent sur des consignes que le modèle suit souvent seul : leurs assertions discriminent peu.
- Une seule assertion échoue avec skill : un lexique dont deux entrées étaient écrites « aucune source retenue ».

## Seconde passe (correctifs de construction)

1. Veille académique : une entrée sans source citable n'est pas écrite ; s'il reste moins de cinq entrées sourcées, demander des références.
2. Skill des side stories : si le texte du passage n'est pas fourni, en demander deux phrases clés avant d'écrire les liens avec le passage (un cas avec skill restait vague : « à confirmer »).
3. Skill des fondations de données : le même rappel pour les lexiques.
4. Test de non-régression : `tests/test_sidestories.py::test_second_pass_rules_from_the_eval_run_are_kept`.

## Limites

- **Biais d'écriture** : les assertions reprennent les règles des skills ; l'écart avec/sans skill mesure surtout l'application de ces règles, pas la qualité éditoriale.
- Une seule itération, notation par un modèle, aucune relecture humaine. Les pages de revue statiques (`eval-viewer`) sont prêtes hors dépôt ; la relecture de François reste à faire.
- Les durées et volumes de jetons par exécution n'ont pas été enregistrés ; aucune moyenne de coût n'est donnée.
- Les seconds correctifs n'ont pas été rejoués : une itération 2 reste à lancer.
