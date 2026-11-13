# Revue de transfert du rapport long vers les quatre verticales

Lecture au commit [ca67c1e](https://github.com/achard-arnaud/skills-notes-and-storytelling/commit/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c) demandé dans la PR 292. La tête de cette PR diffère du commit examiné. Le transfert porte sur les mécanismes de composition.

| Étape | Autorité lue | Décision dans le candidat | Épreuve |
|---|---|---|---|
| 1. Choix du récit | [NARRATIVE.md](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/docs/NARRATIVE.md) et designing-main-story | Partir de la question du lecteur, donner une fonction à chaque bloc, réserver l’objection qui change le choix. | Une section sans apport peut être retirée en conservant les preuves décisives. |
| 2. Distribution des rôles | SKILLS-MAP et INTERFACES | Attacher inputs, résultats et retour de revue aux responsabilités de chaque profil. | Identifier l’étape à rouvrir après une correction. |
| 3. Apartés | Workflow, inventaire candidat, registre des exemples et skill de side stories | Un encart a une question, une insertion, une contribution et un retour. Conserver la provenance, le statut et la distinction entre exemple et preuve. | Une illustration isolée peut être omise. Sa présence ne valide aucun claim. |
| 4. Format | [Internal Comms](https://github.com/anthropics/skills/blob/2c5958ecac7cee2b583967a2c4981d0f4a75c579/skills/internal-comms/SKILL.md) et sa référence 3P | Router depuis le besoin vers une seule charte. Adapter la granularité au lecteur. | Même longueur, deux routes différentes, contrats et contrôles différents. |
| 5. Données et décision | [Data Storytelling](https://github.com/wshobson/agents/blob/9c61ab243def98f72da12abd41cfcf5bcd91af9d/plugins/business-analytics/skills/data-storytelling/SKILL.md) et ses exemples détaillés | Identifier baseline, observation, explication plausible et décision. Charger la vue chiffrée quand le raisonnement l’exige. | Une tendance descriptive conserve son statut même lorsqu’elle apparaît dans un titre. |
| 6. Généralisation | Synthèse des quatre dossiers | Les IDs canoniques de template restent communs. La sélection porte sur le couple verticale–format, avec fixture et responsabilités propres. | Rejouer les contrôles métier séparément de la résolution des chemins. |

Les six types d’encarts et leurs budgets appartiennent au rapport long. Leur intégration dans un autre format demande une justification lecteur et un budget adapté. La revue d’un paragraphe modifié est à reprendre. La validité d’une preuve dépend de sa source, de sa portée et de sa fraîcheur.

## Ressources examinées au commit demandé

- [diagnostic-complet/skills/designing-main-story/SKILL.md](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/skills/designing-main-story/SKILL.md)
- [diagnostic-complet/workflows/side-stories.workflow.json](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/workflows/side-stories.workflow.json)
- [diagnostic-complet/skills/side-stories-business/SKILL.md](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/skills/side-stories-business/SKILL.md)
- [diagnostic-complet/docs/SKILLS-MAP.md](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/docs/SKILLS-MAP.md)
- [diagnostic-complet/docs/INTERFACES.md](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/docs/INTERFACES.md)
- [diagnostic-complet/workflows/kb-examples.json](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/workflows/kb-examples.json)
- [diagnostic-complet/workflows/side-stories.candidates.json](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/workflows/side-stories.candidates.json)

## Revue de conception Skill Creator

Le corps de la skill possède le déclencheur et la procédure. Le registre sélectionne les ressources conditionnelles. Chaque verticale fournit profil, contrat de scaffold, exemples synthétiques et tests. Les références externes servent de comparables méthodologiques. La qualité argumentative et l’utilité terrain requièrent une revue distincte des contrôles mécaniques.

