# Mesurer le délai jusqu’à la première valeur

Identifiant `product.ttv`. Famille produit.

## Cas et entrées

Utiliser pour renseigner les blocs « parcours, délai de valeur, taux de réussite ». Entrées requises — identifiant sujet, début d’exposition, premier résultat utile, horodatage, horizon commun.

## Protocole

Définir la valeur du point de vue utilisateur. Pour chaque sujet ayant atteint l’événement, TTV = instant de première valeur − instant de départ. Présenter médiane parmi les réussites et proportion ayant atteint la valeur à horizon fixe. Garder visibles les sujets censurés.

## Bon usage et erreur fréquente

Vérifier que le proxy de valeur correspond à une tâche réellement achevée. Éviter de compter une connexion comme première valeur sans justification du lien métier.

## Dépendances et sortie

Dépendances analytiques conditionnelles — segmentation. Livrer un résultat daté, son périmètre, ses claim_refs, ses limites et ses blocs destinataires (parcours, délai de valeur, taux de réussite). Formats candidats — three-pager.

## Oracles synthétiques

- Cas positif. Pour trois entrants, deux atteignent la valeur à J2 et J6, un reste sans événement à J7. Médiane conditionnelle 4 jours, réussite à J7 2/3.
- Cas négatif. Attribuer zéro jour au sujet encore en attente fausse la distribution.

## Source et portée

[Référence de méthode](https://go.pendo.io/rs/185-LQW-370/images/Pendo_eBook_2021_10KPIs.pdf). Exemple et oracles conçus pour ce dépôt. Alignement pédagogique possible avec le travail d’analyse du besoin ou de suivi de la valeur. L’usage de cette technique ne constitue ni une exigence universelle ni une attestation de certification PMI-PBA ou PMP. [PMI-PBA](https://www.pmi.org/certifications/business-analysis-pba) · [PMP](https://www.pmi.org/certifications/project-management-pmp).


Finalités produit applicables : usages-chaine-valeur.
