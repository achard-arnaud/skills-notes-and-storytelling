# Procédure rédactionnelle factorisée — candidat 0.2

Expérience sur branche dédiée ; aucune migration de main/dev ni installation personnelle. Les capacités d’analyse et les contrats canoniques existants sont conservés.

- [Skill candidate](SKILL.md)
- [Résultats A/B et renforcement](REPORT.md)
- [Mandat normalisé](MANDATE.md)
- [Architecture et stratégie de migration](ARCHITECTURE.md)
- [Harvest des 13 corps de skills main](AUDIT.md)
- [Protocole et limites](EVAL-PROTOCOL.md)
- [Modifications de la deuxième passe](V2-CHANGELOG.md)
- [Revue aveugle initiale](evals/current-ai/blind-review.md) et [revue du document renforcé](evals/current-ai/reinforced-review.md)

## Livrables comparables

| Paquet | Two-pager | Compagnon company | Trace |
|---|---|---|---|
| A main | [A](evals/current-ai/A/two-pager.md) | [A](evals/current-ai/A/company-one-pager.md) | [process](evals/current-ai/A/process.json) |
| B 0.1 | [B](evals/current-ai/B/two-pager.md) | [B](evals/current-ai/B/company-one-pager.md) | [process](evals/current-ai/B/process.json) |
| B2 0.2 | [B2](evals/current-ai/B2/two-pager.md) | [B2](evals/current-ai/B2/company-one-pager.md) | [process](evals/current-ai/B2/process.json) |

## Utilisation du candidat

Invoquer SKILL.md avec objectif, public, sources et format. Lire les références à la demande ; sélectionner les templates depuis la racine du dépôt épinglé. Le harness de test matérialise ces mêmes contrats sous baseline/templates/. Une note technique ou pédagogique exige ses contrôles distinctifs ; le seul cas produit testé ne valide pas leur transfert.

## Contrôles exécutables

Python 3 et requirements.txt pour le validateur optionnel. Depuis ce dossier : `python -m unittest discover -s tests -v`. Onze tests réussis : [reçu](test-receipt.json). Ils contrôlent schéma, bindings et sélection des blocs, pas vérité ou qualité analytique.

La source Markdown reste éditable. Les pages sont logiques ; aucun PDF, rendu navigateur, live preview ou coût/token modèle n’est revendiqué. Les limites et les volumes de lecture sont explicites dans REPORT.md.
