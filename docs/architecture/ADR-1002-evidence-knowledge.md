# ADR-1002 — Connaissance, provenance et cycle de vie

- Statut : accepté comme principe documentaire ; implémentation selon les contrats publiés.
- Date : 2026-11-13.
- Portée : dépôt entier ; les choix spécifiques restent dans leur périmètre.
- Autorité : accord utilisateur du 13 novembre sur l’architecture cible et sa publication documentaire.
- Tickets : [#25](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/25), [#28](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/28), [#43](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/43), [#46](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/46), [#166](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/166).

## Contexte

L’approfondissement d’un sujet doit conserver les recherches sans transformer les anciens livrables en preuves fraîches.

## Décision

Conserver une identité stable pour les organisations, produits et cas d’usage. La chaîne source → fragment → claim → analyse reste traçable. Les repères d’entreprise sont une projection sourcée : pays, ville, effectifs, chiffre d’affaires/période, maturité, présence commerciale et financement conditionnel. Chaque valeur conserve scope, unité, dates, statut et source. Distinguer inconnu, non trouvé, non applicable, périmé et contradictoire. Une reprise décide REUSE/REFRESH/NEW et invalide les seuls descendants touchés.

## Conséquences et vérification

Un graphe documentaire, une preuve qualifiée et un index sont des objets distincts. Une seule autorité par connaissance ; les vues peuvent être reconstruites. La source corporate peut soutenir une attribution ; ses règles d’éligibilité suivent le contrat du périmètre. Graph1 et Obsidian sont des destinations/adaptateurs possibles, pas des dépendances générales imposées. Corpus réel privé ; fixtures publiques synthétiques.

## Réexamen

Réviser si un pilote de transfert révèle un couplage ou une perte de valeur ; tracer le changement, les contrats affectés et sa validation. Les autres principes sont accessibles dans [l’index](README.md).
