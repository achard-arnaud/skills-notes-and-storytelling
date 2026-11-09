# Audit du changement de contrat racine (`d29882b`)

Objet : `contracts/claims-graph-light.schema.json`, `contracts/relation-types.json`, `references/workflow.md`, `scripts/validate_contracts.py`.

## Constats

- **Delta sémantique additif.** `edges.type` passe de 8 à 12 valeurs : ajout de `integrates_with`, `substitutes`, `complements`, `enables`. Les 8 valeurs existantes sont conservées. Un producteur valide sous l'ancien schéma reste valide sous le nouveau.
- **Cohérence restaurée.** La prose de `references/workflow.md` listait déjà les 12 types ; le schéma n'en listait que 8. Le catalogue `contracts/relation-types.json` rend cette divergence explicite et vérifiable.
- **Consommateurs.** Recherche sur le dépôt : le schéma est lu par `scripts/validate_contracts.py` et par les tests `diagnostic-complet/tests/test_relation_catalog.py`. Aucun autre consommateur n'énumère les types.
- **Bruit de revue.** Le fichier schéma est réindenté en entier (diff de ~70 lignes pour 4 valeurs ajoutées), et le retour à la ligne final est ajouté. La revue du delta réel demande de comparer en mode `--ignore-all-space`.
- **Fixture de non-régression.** `tests/fixtures/relation-catalog-v1.json` et `check_relation_catalog()` dans le validateur, conformément à `AGENTS.md` racine (« contract change : add or update a regression fixture »).
- **Aucune exécution CI.** La règle « promotion vers main seulement si dev est vert » s'appuie donc sur le gate local (`docs/LOCAL-GATE.md`), pas sur un run GitHub.

## Verdict

Changement acceptable en l'état : additif, cohérent avec la prose, couvert par fixture et validateur. Deux suites à traiter avant toute promotion vers `main` :

1. Vérification humaine du delta sémantique (4 valeurs) hors réindentation.
2. Un run CI réel sur `dev` au moment de la promotion, à déclencher quand la décision sera prise, et non avant.

Aucune modification de `contracts/` ni de `templates/` n'est faite dans cette passe.
