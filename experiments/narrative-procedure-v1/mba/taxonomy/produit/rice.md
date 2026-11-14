# Prioriser des initiatives avec RICE

Identifiant `product.rice`. Famille produit.

## Cas et entrées

Utiliser pour renseigner les blocs « arbitrage de roadmap, sensibilité ». Entrées requises — utilisateurs atteints sur la même période, impact estimé, confiance, effort en personnes-mois.

## Protocole

Calculer portée × impact × confiance / effort. Utiliser la même échelle d’impact et la même fenêtre pour toutes les initiatives. Tester un scénario de confiance plus faible avant de décider.

## Bon usage et erreur fréquente

Documenter origine de chaque estimation, dépendances et prérequis. Écarter les mélanges entre percent et fraction ; une obligation de conformité peut primer sur le classement.

## Dépendances et sortie

Dépendances analytiques conditionnelles — segmentation. Livrer un résultat daté, son périmètre, ses claim_refs, ses limites et ses blocs destinataires (arbitrage de roadmap, sensibilité). Formats candidats — three-pager.

## Oracles synthétiques

- Cas positif. Pour 100 utilisateurs/trimestre × impact 2 × confiance 0,5 / 2 personnes-mois, le score est 50.
- Cas négatif. Un effort nul rend le score indéfini. Deux fenêtres de portée différentes rendent le classement trompeur.

## Source et portée

[Référence de méthode](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers). Exemple et oracles conçus pour ce dépôt. Alignement pédagogique possible avec le travail d’analyse du besoin ou de suivi de la valeur. L’usage de cette technique ne constitue ni une exigence universelle ni une attestation de certification PMI-PBA ou PMP. [PMI-PBA](https://www.pmi.org/certifications/business-analysis-pba) · [PMP](https://www.pmi.org/certifications/project-management-pmp).


Finalités produit applicables : diagnostic-produit.
