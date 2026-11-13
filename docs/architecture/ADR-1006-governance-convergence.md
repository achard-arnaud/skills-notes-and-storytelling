# ADR-1006 — Autorités documentaires et convergence progressive

- Statut : accepté comme principe documentaire ; implémentation selon les contrats publiés.
- Date : 2026-11-13.
- Portée : dépôt entier ; les choix spécifiques restent dans leur périmètre.
- Autorité : accord utilisateur du 13 novembre sur l’architecture cible et sa publication documentaire.
- Tickets : [#21](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/21), [#22](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/22), [#48](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/48), [#171](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/171), [#259](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/259).

## Contexte

La racine, le prototype et les propositions de Workbench coexistent avec des degrés différents d’implémentation.

## Décision

Les ADR 1001–1006 portent les principes communs approuvés le 13 novembre 2026. Les ADR 0000–0013 restent locaux à diagnostic-complet ; leurs IDs demeurent stables. Les schémas/manifests fixent les capacités exécutables ; les ADR expliquent leur intention. Un écart crée un delta de migration explicite. Les propositions de backlog ne deviennent pas implémentées par référencement.

## Conséquences et vérification

Cette livraison publie les principes communs sur main et dev, et la clarification locale sur dev. La stratégie de migration du prototype reste à choisir. Les futurs lots seront bornés par capacité, avec compatibilité, fixtures, contrôle du contexte et retour arrière. Une branche supplémentaire n’est créée que si un besoin d’isolation concret le justifie. La décision actuelle n’autorise aucune refonte fonctionnelle.

## Réexamen

Réviser si un pilote de transfert révèle un couplage ou une perte de valeur ; tracer le changement, les contrats affectés et sa validation. Les autres principes sont accessibles dans [l’index](README.md).
