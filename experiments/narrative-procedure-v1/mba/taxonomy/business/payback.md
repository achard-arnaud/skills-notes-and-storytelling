# Délai de récupération

Identifiant `business.payback` · Famille economie · Révision 1.

## Décision et entrées

Évaluer le temps d’exposition de trésorerie avant récupération de la mise. Réunir investissement et flux nets par période.

## Protocole

Cumuler les flux jusqu’au premier solde nul ou positif. Distinguer délai simple et actualisé. Une fraction de période suppose une génération de cash répartie dans la période.

**À faire.** Examiner aussi la valeur créée après le seuil et les éventuels décaissements ultérieurs.

**Erreur à détecter.** Déduire un délai précis au mois à partir de flux annuels uniquement versés en fin d’année.

## Dépendances et restitution

Flux nets, fréquence d’encaissement et VAN. Délai, hypothèses et liquidité vers risques. Contrats du dépôt applicables selon le mandat : `buy-side-gap-analysis`, `one-pager`.

## Oracle synthétique

- Cas attendu. −100 puis +40 par an, régulièrement dans l’année, donnent 2,5 ans.
- Cas qui invalide une conclusion trop large. Si les 40 sont versés chaque 31 décembre, le franchissement intervient au troisième versement.

## Source de méthode

[Publication de référence](https://openstax.org/books/principles-finance/pages/16-summary). Consultation du 14 novembre 2026. Les exemples et les règles d’intégration au dépôt sont des adaptations originales.
