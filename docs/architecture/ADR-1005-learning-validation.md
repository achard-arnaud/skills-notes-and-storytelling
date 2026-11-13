# ADR-1005 — Loopback, validations et promotion

- Statut : accepté comme principe documentaire ; implémentation selon les contrats publiés.
- Date : 2026-11-13.
- Portée : dépôt entier ; les choix spécifiques restent dans leur périmètre.
- Autorité : accord utilisateur du 13 novembre sur l’architecture cible et sa publication documentaire.
- Tickets : [#31](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/31), [#130](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/130), [#133](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/133), [#142](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/142), [#146](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/146), [#289](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/289).

## Contexte

Un run apprécié fournit des hypothèses de réemploi ; il ne suffit pas à généraliser un comportement.

## Décision

Le loopback relie observation, cause présumée, couche concernée, changement candidat et scénario de validation. Séparer qualité de preuve, conformité de contrat, résultat analytique, cohérence narrative, rendu et acceptation humaine. NO_REUSABLE_DELTA est valide. Une évaluation indépendante et un cas de transfert servent à vérifier les généralisations ; le niveau de contrôle dépend du risque et de la frontière modifiée.

## Conséquences et vérification

Les compteurs de graphe mesurent une structure, pas sa qualité métier. Une évaluation écrite n’est pas exécutée ; un test réussi ne certifie pas le monde réel. Consigner PASS/FAIL/NOT_RUN et les versions examinées. La calibration des seuils nécessite des observations et une décision référencée. Le bootstrap de GreenYellow reste une source de patterns candidats.

## Réexamen

Réviser si un pilote de transfert révèle un couplage ou une perte de valeur ; tracer le changement, les contrats affectés et sa validation. Les autres principes sont accessibles dans [l’index](README.md).
