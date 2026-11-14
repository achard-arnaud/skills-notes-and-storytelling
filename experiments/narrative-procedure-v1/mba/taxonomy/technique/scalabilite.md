# Scalabilité — caractériser la capacité à charge variable

TECH-03 · architecture-note

## Cas et entrées

Un service traite des demandes interactives et des lots. Réunir profil de trafic, taille des données, plafond utile, environnement autorisé et instrumentation.

## Protocole

Définir une charge métier représentative et une progression bornée en environnement de performance contrôlé. Mesurer débit utile, percentiles de latence, erreurs et ressources à chaque palier. Consigner le premier objectif manqué et la récupération après retour au nominal. Répéter après une seule modification.

## Bon usage et piège

Conserver les paramètres et le statut mesuré ou estimé pour chaque chiffre. Éviter d’extrapoler une capacité de production depuis un environnement non comparable.

## Sortie et relais

Émettre un résultat analytique daté avec sa question, ses claim_refs, ses conclusions bornées et ses inconnues. Rattacher les blocs `flow`, `failure`, `countertest`. Poursuivre si nécessaire avec [la méthode associée](choix-stack.md).

## Oracles synthétiques

- Positif — Le résultat associe un palier à une latence, une population et un intervalle de mesure. 
- Négatif — Un débit maximal est annoncé sans scénario ni taux d’erreurs.

## Source primaire

Protocole adapté au dépôt. [Référence de méthode consultée le 14 novembre 2026](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/performance-test).

