# Seuil de rentabilité

Identifiant `business.break-even` · Famille economie · Révision 1.

## Décision et entrées

Décider quel volume couvre un coût fixe sur une période donnée. Réunir prix ou gain unitaire, coût variable unitaire, capacité et coûts fixes.

## Protocole

Pour une offre homogène, Q = F / (p − v). Pour des unités indivisibles, arrondir au supérieur. Recalculer si un palier de capacité ou le mix change.

**À faire.** Exposer la marge contributive et le domaine où les coûts restent linéaires.

**Erreur à détecter.** Calculer un volume atteignable si la marge unitaire est nulle ou négative et les frais fixes positifs.

## Dépendances et restitution

Prix, coût variable, demande accessible et capacité. Volume seuil et marge de sécurité vers next_step. Contrats du dépôt applicables selon le mandat : `buy-side-gap-analysis`, `strategic-market-note`, `one-pager`.

## Oracle synthétique

- Cas attendu. 1 200 € de frais fixes / (12 € − 4 €) = 150 unités.
- Cas qui invalide une conclusion trop large. Avec une capacité de 100 unités et un nouveau palier ensuite, 150 unités exige un recalcul.

## Source de méthode

[Publication de référence](https://openstax.org/books/principles-managerial-accounting/pages/3-2-calculate-a-break-even-point-in-units-and-dollars). Consultation du 14 novembre 2026. Les exemples et les règles d’intégration au dépôt sont des adaptations originales.
