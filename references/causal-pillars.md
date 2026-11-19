# Piliers causaux du profil narratif candidat S3

Le [PRD #258](../docs/specifications/PRD-258-selecteur-narratif.md) fixe les critères du pilote. Le [profil](../workflow/narrative-profile.json) porte les identifiants actifs. Chaque claim atomique examiné reçoit un pilier principal pour son mécanisme. Les rattachements secondaires éclairent les effets ou conditions. Le tronc peut croiser plusieurs piliers. Le mandat fixe la couverture utile. La grille reste une projection de lecture et conserve les statuts d’origine.

| Pilier | Question et frontière |
| --- | --- |
| `P-STRATEGY` | Où et comment gagner ? Concurrence, positionnement, moat et ruptures. L’exécution interne relève du moteur opérationnel et de l’organisation. |
| `P-VALUE-ENGINE` | Où les opérations créent-elles ou perdent-elles de la valeur ? Chaîne de valeur, flux, goulots, non-qualité et terrain. La monétisation relève de l’économie. |
| `P-ECONOMICS` | Comment l’activité monétise-t-elle et où investir ? Marges, cash, allocation, TCO/ROI et risque financier. Une promesse reste une affirmation attribuée. |
| `P-TECH-DATA` | Quelles données et capacités peuvent fonctionner dans ce SI ? Qualité, intégration, architecture, IA et évaluations. La responsabilité et les contrôles relèvent de la maîtrise des risques. |
| `P-ORG-EXECUTION` | Quelles personnes, pratiques et incitations rendent l’exécution durable ? Organisation, compétences et usage réel. Les flux eux-mêmes relèvent du moteur opérationnel. |
| `P-RISK-CONTROL` | Quels mandats et contrôles rendent la décision maîtrisable et réversible ? Responsabilité, conformité, sécurité, supervision et dépendances. Le risque financier reste dans l’économie. |

**Exemple.** « Le fournisseur prévoit 30 % de ROI » relève de `P-ECONOMICS` avec statut `attributed_claim`. « Les données couvrent un seul site » relève de `P-TECH-DATA`. Cette condition limite la portée de la promesse. Une mesure locale peut la confirmer ou la réfuter. L’attribution, les preuves et les relations restent des informations distinctes.

L’échelle, la dimension analytique et la couche d'activité sont des axes indépendants. Le profil pilote reconnaît `core` et `support`. Si le mécanisme reste ambigu, consigner un motif de non-classement. Une lacune de preuve retourne à la collecte ; un problème de frontière retourne à A1 et au propriétaire métier. La projection ne change ni ontologie historique ni enum D22. Le profil reste candidat jusqu’au rejeu comparatif.
