---
id: ishikawa
family: opérations
asset: mba/methods/ishikawa.json
---

# Ishikawa

Deux causes compatibles avec un même effet appellent un test capable de les départager.

## Activation

Quelles causes possibles faut-il départager pour réduire les retours ? Condition préalable : disposer de question et périmètre, claims identifiés à date, bloc consommateur. La carte exécutable `mba/methods/ishikawa.json` fixe le contrat de production ; la présente note précise quand l’employer.

## Passage de l’entrée à la décision

Cas synthétique. Le poste B compte six retours sur vingt dossiers dans la semaine fictive. Le gabarit et la répartition des dossiers ont changé ensemble. L’analyste relie ces propositions au résultat suivant : « Le changement de gabarit pourrait expliquer une partie des retours du poste B. » Statut proposé : `hypothesis`. Le rédacteur peut rouvrir le bloc `options` pour intégrer ce résultat en conservant les références C1 et C2.

## Pratiques et limites

- À faire : Décrire l’effet avec dénominateur, fenêtre et population puis associer chaque piste à un observable.
- À éviter : Éviter de choisir comme cause racine la branche la plus détaillée du dessin.
- Contre-test : Apparier les dossiers par complexité puis comparer les retours avec les deux gabarits. Une inversion du classement affaiblirait l’hypothèse initiale.

## Application et recombinaison

Formats envisagés : integration-note, architecture-note, ai-enterprise-learning-six-page. La sélection du bloc, l’étiquette de statut et le contrôle de transfert sont des conventions éditoriales locales. La référence méthodologique justifie l’outil ; l’exemple et l’option décrits ici sont fictifs.

Notes liées : [unit-economics](unit-economics.md).

## Sources de méthode

- https://www.ihi.org/library/tools/cause-and-effect-diagram
