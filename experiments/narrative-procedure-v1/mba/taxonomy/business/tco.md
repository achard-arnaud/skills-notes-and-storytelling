# Coût total de possession

Identifiant `business.tco` · Famille economie · Révision 1.

## Décision et entrées

Comparer deux solutions capables de rendre un service équivalent pendant la même durée. Rassembler licences, intégration, exploitation, formation, sortie et valeur résiduelle.

## Protocole

Établir le calendrier des décaissements. Additionner les coûts et déduire la valeur de revente. Si leur calendrier diffère fortement, présenter aussi les valeurs actualisées au même taux.

**À faire.** Documenter les coûts internes mobilisés et les hypothèses de consommation.

**Erreur à détecter.** Compter deux fois une facture déjà incluse dans le forfait de service.

## Dépendances et restitution

Volume, SLA, horizon et scénario de sortie. Table des coûts par option vers le bloc economics. Contrats du dépôt applicables selon le mandat : `buy-side-gap-analysis`, `benchmarking`.

## Oracle synthétique

- Cas attendu. 10 k€ de lancement + 3 × 4 k€ de run + 2 k€ de sortie − 1 k€ de revente = 23 k€ nominaux.
- Cas qui invalide une conclusion trop large. 12 k€ de licences ne représentent pas le coût complet de cette option.

## Source de méthode

[Publication de référence](https://www.procurement.govt.nz/assets/procurement-property/documents/guide-total-cost-ownership.pdf). Consultation du 14 novembre 2026. Les exemples et les règles d’intégration au dépôt sont des adaptations originales.
