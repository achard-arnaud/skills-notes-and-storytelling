# ADR-1004 — Séparation RUN/BUILD et contexte portable

- Statut : accepté comme principe documentaire ; implémentation selon les contrats publiés.
- Date : 2026-11-13.
- Portée : dépôt entier ; les choix spécifiques restent dans leur périmètre.
- Autorité : accord utilisateur du 13 novembre sur l’architecture cible et sa publication documentaire.
- Tickets : [#22](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/22), [#25](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/25), [#26](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/26), [#39](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/39), [#141](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/141).

## Contexte

Les méthodes évoluent tandis que les runs doivent rester explicables et reprenables.

## Décision

BUILD conserve méthodes, contrats, skills, tests et fixtures. RUN conserve sources privées, entrées, analyses, scaffolds, sorties et revues. Un paquet de reprise porte sujet, objectif, cutoff, versions/pins, état, preuves décisives, contradictions, inconnues et prochaine action. Charger les références de la seule étape active. Un défaut observé produit une proposition BUILD liée au run ; son application est une opération distincte.

## Conséquences et vérification

Les profils métier peuvent enrichir un run sans introduire de vocabulaire d’entreprise dans le moteur commun. Changer une classification ou une identité exige une migration explicite et réversible. Une représentation exportable vers une KB doit conserver provenance et dépendances. Cette décision n’impose ni SQL, ni bus, ni worker permanent, ni agents supplémentaires.

## Réexamen

Réviser si un pilote de transfert révèle un couplage ou une perte de valeur ; tracer le changement, les contrats affectés et sa validation. Les autres principes sont accessibles dans [l’index](README.md).
