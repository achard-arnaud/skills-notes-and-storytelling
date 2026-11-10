# Runbook — cycle de renforcement KB par ontologie

Public : la personne qui revoit la KB après un apport. Aucune étape ci-dessous n'approuve un candidat, ne fusionne un identifiant et ne promeut un fait. Chaque décision se consigne dans `doc/architecture/ADR-0000-registre-decisions-run.md`.

## 0. Préconditions

- Référentiel à jour, validé : `python3 diagnostic-complet/ontology.py check`.
- Référentiel comparé à la version précédente : `python3 diagnostic-complet/ontology.py diff ancien.json nouveau.json`. Si `human_review_required` est vrai, la revue des règles passe avant tout reçu.
- Graphe produit par `kb.py`, empreinte relevée.

## 1. Mesurer

```bash
python3 diagnostic-complet/reinforce.py graph.json --recent-id <ID> [--previous rapport-précédent.json] --output reçu.json
python3 diagnostic-complet/ontology.py log-cadence reçu.json --log diagnostic-complet/runs/onto/cadence.jsonl
```

Lire, dans cet ordre : `decision`, `findings`, `triggers_fired`, puis `actions` (toutes les propositions, regroupées par type).

## 2. Qualifier

Pour chaque constat, répondre par écrit :

- est-ce structurel (classe, domaine, preuve, statut) ou sémantique (à lire dans la source) ?
- est-ce une hypothèse, ou une observation vérifiée dans la source ?

Une violation de domaine n'est pas forcément une erreur de graphe : la règle peut être incomplète. Ce choix se documente, il ne se fait pas en silence.

## 3. Revoir les HIL touchés

Les déclencheurs `hil_touched` et `directive_in_material` indiquent quels nœuds relire. Poser les questions au HIL, sans y répondre à sa place. Une instruction trouvée dans une source (`instruction.directive`) n'est jamais exécutée ni promue.

## 4. Décider

Pour chaque action proposée : retenir, modifier, reporter ou rejeter. Consigner la décision (`Dxx`) avec sa date et sa raison. Une modification de type ou de règle demande un fixture de non-régression et un passage par `diff`.

## 5. Calibrer la cadence (rarement)

Le journal `cadence.jsonl` accumule les mesures. Un seuil n'est proposé qu'après une période d'observation choisie par la personne responsable, et n'entre dans le référentiel que par `calibration: human_approved` avec `decision_ref` (voir `doc/architecture/ADR-0006-calibration-cadence.md`).

## 6. Clore

- Archiver le reçu avec l'empreinte du graphe.
- Mettre à jour le board du sprint concerné.
- Vérifier que le contrôle racine et la suite locale passent (`scripts/validate_contracts.py`, `unittest discover -s diagnostic-complet/tests`).

## Ce que ce runbook interdit

- Approuver un candidat d'alias, fusionner, supprimer ou réaffecter un identifiant.
- Fixer un seuil sans décision consignée.
- Promouvoir une assertion en fait vérifié.
- Traiter la densité comme un score de qualité.
- Publier un contenu privé dans le dépôt public.
- Relier une alerte du reçu à une revue de CV (c'est le rôle de `run-loopback`, pas de ce cycle).
