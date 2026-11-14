# Valeur actuelle nette

Identifiant `business.van` · Famille economie · Révision 1.

## Décision et entrées

Arbitrer des investissements dont les flux se réalisent à des dates différentes. Réunir flux incrémentaux après impôt, investissement initial et taux cohérent.

## Protocole

VAN = somme de CF_t/(1+r)^t, flux initial inclus à t=0. Tester taux, volumes et valeur terminale. Comparer les alternatives compatibles avec le budget et les contraintes.

**À faire.** Aligner devise, inflation et périodicité du taux et des flux.

**Erreur à détecter.** Ajouter deux fois l’investissement initial ou actualiser des euros réels avec un taux nominal sans ajustement.

## Dépendances et restitution

Flux de trésorerie, BFR, coût d’opportunité du capital. Valeur monétaire par scénario vers alternatives. Contrats du dépôt applicables selon le mandat : `buy-side-gap-analysis`, `strategic-market-note`.

## Oracle synthétique

- Cas attendu. −100 aujourd’hui, +121 dans deux ans, taux annuel 10 % donnent une VAN de zéro.
- Cas qui invalide une conclusion trop large. Une VAN positive ne rend pas un projet finançable si la trésorerie initiale manque.

## Source de méthode

[Publication de référence](https://openstax.org/books/principles-finance/pages/16-summary). Consultation du 14 novembre 2026. Les exemples et les règles d’intégration au dépôt sont des adaptations originales.
