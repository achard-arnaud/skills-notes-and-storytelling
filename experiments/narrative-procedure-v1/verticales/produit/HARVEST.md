# Transfert produit

Revue du 14 novembre 2026. Cas et valeurs inventés pour l’essai.

| Étape | Ressource lue | Transfert retenu | Limite |
|---|---|---|---|
| 1 | [NARRATIVE à la révision de PR](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/docs/NARRATIVE.md) | Une question et des claims par bloc ; réouvrir le seul bloc défectueux | Les règles d’encart restent facultatives dans un brief court |
| 2 | [Two-pager](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/templates/two-pager.md) | Demande produit, deux usages, décision réversible | Pagination logique vérifiée |
| 3 | [Qualification ICP](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/templates/opportunity-note-icp.md) | Besoin et capacité décrits séparément, verdict conditionnel | Une validation du pilote reste à obtenir |
| 4 | [Value proposition, skill du mainteneur](https://github.com/phuryn/pm-skills/blob/9af7bfd0bc47fdad43c2eaa7a43cd13918e7aaef/pm-product-strategy/skills/value-proposition/SKILL.md) | Situer l’usage proposé par rapport au processus actuel et à une alternative | L’amélioration projetée demande une observation |
| 5 | [Three-pager de la première expérience](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/0341c0cb6deaf81ec1b2ac5482f3562a8d9809d1/experiments/narrative-procedure-v1/references/three-pager.md) | Relier écart de couverture et décision d’extension | Template candidat |

Les trois fixtures contiennent claims et attentes structurelles. Les six textes courts V1/V2 sont des exemples rédigés de correction d’un bloc dans son contexte. Ils testent respectivement cadence de mesure, faisabilité du pilote et validité du transfert entre populations. Ils constituent des micro-essais et non une certification de toutes les obligations d’un template ni une comparaison aveugle.

Rejouer avec Python standard dans ce dossier : `python verify.py`. Le reçu matérialise l’échec sur trois contrôles discriminants en V1 et leur passage en V2 pour chaque template. L’oracle lexical est propre à ces fixtures. Il resterait possible de faire passer un texte incohérent qui reprendrait les mots attendus. La revue éditoriale humaine, le rendu et l’adoption effective restent à vérifier.
