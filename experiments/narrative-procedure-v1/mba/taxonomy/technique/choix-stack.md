# Choix de stack — comparer sur le travail à accomplir

TECH-02 · architecture-note

## Cas et entrées

Une équipe doit choisir le mode de stockage d’un catalogue. Prendre la charge attendue, les compétences de support, les contraintes d’exploitation et deux options plausibles.

## Protocole

Établir d’abord les exigences éliminatoires. Construire une matrice sur les mêmes critères. Étiqueter les observations, hypothèses et inconnues. Choisir l’essai qui départagerait les deux meilleures options et consigner les conséquences dans une décision proposée.

## Bon usage et piège

Inclure le coût de sortie et le maintien de la solution en place. Écarter les scores pondérés dont les entrées manquent de preuves.

## Sortie et relais

Émettre un résultat analytique daté avec sa question, ses claim_refs, ses conclusions bornées et ses inconnues. Rattacher les blocs `decision`, `alternative`. Poursuivre si nécessaire avec [la méthode associée](contre-test.md).

## Oracles synthétiques

- Positif — Une exigence de reprise élimine une option à partir d’un essai représentatif. 
- Négatif — Le gagnant dépend d’un benchmark fournisseur mené sur une charge différente.

## Source primaire

Protocole adapté au dépôt. [Référence de méthode consultée le 14 novembre 2026](https://martinfowler.com/bliki/ArchitectureDecisionRecord.html).

