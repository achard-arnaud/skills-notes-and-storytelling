# Posture d’intégration — borner le pilote et la sortie

TECH-06 · integration-note

## Cas et entrées

Un portail pourrait afficher ou administrer des données externes. Réunir droits d’écriture, source d’autorité, canal d’échange et attentes d’adoption.

## Protocole

Qualifier d’abord la décision stratégique, puis la posture technique envisagée. Choisir projection, coexistence ou dépendance opérationnelle selon les droits réellement nécessaires. Définir le plus petit segment à tester, le rapprochement des données et les gestes de retrait. Affecter chaque geste à un responsable.

## Bon usage et piège

Conserver les identifiants métier au retrait de la surface pilote. Éviter de transformer une projection en source de vérité par commodité.

## Sortie et relais

Émettre un résultat analytique daté avec sa question, ses claim_refs, ses conclusions bornées et ses inconnues. Rattacher les blocs `decision`, `posture`, `pilot`, `exit`. Poursuivre si nécessaire avec [la méthode associée](impact-integration.md).

## Oracles synthétiques

- Positif — Le portail peut être retiré avec une procédure de retour vérifiable et le référentiel continue d’opérer. 
- Négatif — Le retrait du pilote efface une donnée dont aucune autre partie ne conserve l’autorité.

## Source primaire

Protocole adapté au dépôt. [Référence de méthode consultée le 14 novembre 2026](https://martinfowler.com/bliki/StranglerFigApplication.html).

