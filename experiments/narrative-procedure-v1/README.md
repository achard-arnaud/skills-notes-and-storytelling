# Procédure rédactionnelle factorisée — expérience candidate

Branche dédiée ; base main 16bcb4325bcace66c2c22fa33a97402cb00e1de9. Aucune migration de la skill racine ni installation personnelle.

[Skill candidate](SKILL.md) · [Routage](references/routing.md) · [Contrat analytique](references/analysis-interface.md) · [Sources](references/sources.md).

La procédure cadre le mandat, dirige le scaffold, rédige par bloc, relit le récit puis contrôle la livraison. Les formats sont des contrats chargés conditionnellement ; les analystes restent des producteurs d’inputs sourcés. Les templates canoniques du dépôt sont conservés.

Le harness local mappe les originaux templates/ vers baseline/templates/ au SHA de base. Il ne s’agit pas d’un nouveau catalogue runtime. Les chemins baseline mentionnés dans le routage concernent uniquement cet essai.

## Contrôles exécutables

Python 3 et jsonschema sont nécessaires. Depuis ce dossier : python -m unittest discover -s tests -v. Le validateur contrôle le schéma et les références ; il ne certifie pas l’analyse métier. Fixture TOWS synthétique, aucune donnée client.

## Essai

Le brief figé est dans evals/current-ai/brief.md. A utilise main, B ce candidat ; chaque agent travaille dans un contexte frais, avec la même source et sans recherche web. Les résultats et limites seront ajoutés après revue. Le cas est disponible dans la conversation ; l’horodatage de son run original n’est pas attesté comme inférieur à 24 heures. Les mots/octets chargés seront mesurés ; tokens modèle, coût et temps actif exact restent inconnus. Cet essai ne prouve pas un gain statistique.
