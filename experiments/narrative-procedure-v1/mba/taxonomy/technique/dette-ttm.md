# Dette technique et délai de lancement — expliciter le prix du raccourci

TECH-07 · architecture-note, integration-note

## Cas et entrées

Une date de lancement proche pousse à reporter une automatisation. Recueillir échéance, enjeu du lancement, effort de remise en état et fréquence prévisible des opérations manuelles.

## Protocole

Comparer lancement anticipé et conception durable sur un horizon explicite. Détailler le coût différé et les opérations répétées. Tester au moins deux niveaux de fréquence. Désigner un responsable et un signal de remboursement. Revoir après observation de l’usage réel.

## Bon usage et piège

Distinguer hypothèse d’effort et temps effectivement consommé. Éviter d’appeler dette toute imperfection ou d’annoncer une valeur commerciale sans preuve.

## Sortie et relais

Émettre un résultat analytique daté avec sa question, ses claim_refs, ses conclusions bornées et ses inconnues. Rattacher les blocs `alternative`, `decision`, `countertest`. Poursuivre si nécessaire avec [la méthode associée](choix-stack.md).

## Oracles synthétiques

- Positif — La décision est révisée lorsque la charge manuelle observée dépasse le budget retenu. 
- Négatif — Le gain de délai est affiché mais l’effort futur et son propriétaire sont absents.

## Source primaire

Protocole adapté au dépôt. [Référence de méthode consultée le 14 novembre 2026](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html).

