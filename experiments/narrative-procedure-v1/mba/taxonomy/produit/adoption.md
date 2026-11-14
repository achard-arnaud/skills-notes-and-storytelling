# Relier adoption, cadence métier et KPI

Identifiant `product.adoption`. Famille produit.

## Cas et entrées

Utiliser pour renseigner les blocs « preuve d’usage, critère de poursuite ». Entrées requises — population éligible, événement utile, fréquence attendue, cohorte et période.

## Protocole

Adoption sur la fenêtre = utilisateurs distincts ayant réalisé l’action utile / utilisateurs éligibles du périmètre. Mesurer séparément les répétitions après un intervalle compatible avec le travail. Documenter exclusions, fuseau et déduplication.

## Bon usage et erreur fréquente

Choisir une fréquence cohérente avec la tâche et expliquer si le dénominateur est actif ou éligible. Éviter de prendre les inscriptions cumulées pour un usage récurrent.

## Dépendances et sortie

Dépendances analytiques conditionnelles — segmentation,ttv. Livrer un résultat daté, son périmètre, ses claim_refs, ses limites et ses blocs destinataires (preuve d’usage, critère de poursuite). Formats candidats — three-pager.

## Oracles synthétiques

- Cas positif. Sur 40 éligibles, 12 ont accompli la tâche hebdomadaire : adoption 30 %. Si 9 de ces 12 répètent la semaine suivante, répétition 75 % sur cette cohorte.
- Cas négatif. Un taux mensuel agrégé ne démontre pas un objectif de répétition quotidienne.

## Source et portée

[Référence de méthode](https://amplitude.com/docs/analytics/product-analytics). Exemple et oracles conçus pour ce dépôt. Alignement pédagogique possible avec le travail d’analyse du besoin ou de suivi de la valeur. L’usage de cette technique ne constitue ni une exigence universelle ni une attestation de certification PMI-PBA ou PMP. [PMI-PBA](https://www.pmi.org/certifications/business-analysis-pba) · [PMP](https://www.pmi.org/certifications/project-management-pmp).


Finalités produit applicables : traction-commerciale, clients-360.
