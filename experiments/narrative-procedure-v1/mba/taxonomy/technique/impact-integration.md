# Impact d’intégration — suivre le transfert de contrôle

TECH-05 · integration-note

## Cas et entrées

Deux systèmes doivent partager des statuts de commande. Recueillir le modèle de chaque partie, les identifiants, contrats d’échange et responsabilités opérationnelles.

## Protocole

Tracer une commande depuis la source jusqu’au consommateur. Comparer unités, identifiants, états et dates. Repérer où une traduction est requise, qui possède la transformation et comment rapprocher le résultat. Étendre l’analyse au parcours utilisateur et aux obligations de support.

## Bon usage et piège

Faire apparaître le comportement lors d’une indisponibilité ou d’une évolution de schéma. Éviter d’inférer une compatibilité métier de la simple présence de deux interfaces.

## Sortie et relais

Émettre un résultat analytique daté avec sa question, ses claim_refs, ses conclusions bornées et ses inconnues. Rattacher les blocs `party_truth`, `flow`, `exit`. Poursuivre si nécessaire avec [la méthode associée](c4.md).

## Oracles synthétiques

- Positif — Une correspondance d’états ambiguë déclenche une question bloquante au propriétaire du domaine. 
- Négatif — Deux états de sens différent sont fusionnés sur la seule identité du libellé.

## Source primaire

Protocole adapté au dépôt. [Référence de méthode consultée le 14 novembre 2026](https://learn.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer).

