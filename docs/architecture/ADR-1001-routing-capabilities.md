# ADR-1001 — Routage et capacités d’analyse

- Statut : accepté comme principe documentaire ; implémentation selon les contrats publiés.
- Date : 2026-11-13.
- Portée : dépôt entier ; les choix spécifiques restent dans leur périmètre.
- Autorité : accord utilisateur du 13 novembre sur l’architecture cible et sa publication documentaire.
- Tickets : [#23](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/23), [#42](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/42), [#165](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/165).

## Contexte

Le catalogue mêle intention, méthode et format. Cette ambiguïté multiplie les variantes et rend les transferts fragiles.

## Décision

Le mandat choisit une route principale parmi pédagogie, business, produit et technique, avec des angles secondaires justifiés. Les méthodes (business model, pricing, SWOT→TOWS, architecture, conception pédagogique) sont sélectionnées selon la question et les preuves nécessaires. Une capacité décrit déclencheur, entrées, sortie, limites et contrôle ; elle peut être une procédure ou une référence avant de justifier une skill autonome.

## Conséquences et vérification

Les clés et enums existants restent les contrats exécutables jusqu’à une migration versionnée. Le présent ADR approuve une cible documentaire ; il ne déclare pas les quatre routes implémentées. Aucun framework n’est une section obligatoire. Un pilote doit démontrer le partage d’une méthode entre deux routes sans contamination.

## Réexamen

Réviser si un pilote de transfert révèle un couplage ou une perte de valeur ; tracer le changement, les contrats affectés et sa validation. Les autres principes sont accessibles dans [l’index](README.md).
