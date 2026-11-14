---
id: unit-economics
family: économie
asset: mba/methods/unit-economics.json
---

# Économie unitaire

Le seuil en unités entières mesure un volume nécessaire. Le volume réalisable dépend de la demande et de la capacité.

## Activation

Quel volume rendrait l’essai économiquement viable ? Condition préalable : disposer de question et périmètre, claims identifiés à date, bloc consommateur. La carte exécutable `mba/methods/unit-economics.json` fixe le contrat de production ; la présente note précise quand l’employer.

## Passage de l’entrée à la décision

Cas synthétique. Scénario fictif mensuel : prix 30 EUR, coût variable 20 EUR par kit. Le coût fixe du mois est de 105 EUR. L’analyste relie ces propositions au résultat suivant : « Il faudrait vendre au moins onze kits dans le mois aux conditions du scénario. » Statut proposé : `inference`. Le rédacteur peut rouvrir le bloc `options` pour intégrer ce résultat en conservant les références C1 et C2.

## Pratiques et limites

- À faire : Aligner coûts fixes, volumes et période ; documenter l’origine du prix et des coûts variables.
- À éviter : Éviter de multiplier une économie annoncée par tout le portefeuille lorsque seule une fraction des cas est éligible.
- Contre-test : Au prix de 30 EUR, passer de 20 à 25 EUR de coût variable porte le seuil de 11 à 21 kits pour 105 EUR de coûts fixes mensuels.

## Application et recombinaison

Formats envisagés : one-pager, two-pager, diagnostic-reco-sellside. La sélection du bloc, l’étiquette de statut et le contrôle de transfert sont des conventions éditoriales locales. La référence méthodologique justifie l’outil ; l’exemple et l’option décrits ici sont fictifs.

Notes liées : [marketing-4p](marketing-4p.md), [porter](porter.md).

## Sources de méthode

- https://www.sba.gov/counseling/plan-your-business/break-even-point-calculator/
