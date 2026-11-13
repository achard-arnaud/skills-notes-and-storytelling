# Transfert pédagogique du 14 novembre 2026

| Étape | Observation à la source | Adaptation et contrôle |
|---|---|---|
| 1 | Le guide de narration relie chaque paragraphe à une question, un bénéfice lecteur et un paquet local. | Le bénéfice devient un geste vérifiable. L’exercice est le seul bloc rouvert. [Guide épinglé](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/diagnostic-complet/docs/NARRATIVE.md) |
| 2 | Le template organise six fonctions et sépare contenu, structure puis design. Le schéma laisse les contenus de page ouverts. | Préserver la fiche existante, injecter l’exercice uniquement dans le slot Transmettre et valider le schéma. [Template](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/templates/ai-enterprise-learning-six-page.md) · [Schéma](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/contracts/pedagogical-sheet.schema.json) |
| 3 | La skill pédagogique prévoit animation et critère de compréhension. | L’agent rédacteur fournit consigne, matériaux, correction et réessai en texte affichable. [Skill](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/ca67c1ebe940f5a548b2fd76fc75a8f0f149087c/skills/pedagogical-ai-learning/SKILL.md) |
| 4 | Lesson Plan Builder prépare l’épreuve finale à partir de l’objectif et prévoit une remédiation. | Transférer l’alignement exercice/jugement. Choisir une erreur déterminante propre à la tâche. La durée et les seuils scolaires restent spécifiques au donneur. [Source primaire, consultée le 14 novembre](https://github.com/SkillMedev/skills/blob/main/skills/lesson-plan-builder/SKILL.md) |

Le cas Perception est résolu depuis son commit et les seules variantes enregistrées sont des patches de l’exercice. V1 et V2 sont deux productions du même agent. Les contrôles portent sur ce matériel synthétique. Le résultat humain en formation et le rendu physique restent à mesurer.

Rejouer avec Python et jsonschema depuis un checkout qui contient le commit source : `python replay.py --repo /chemin/du/checkout`. Le script vérifie les pages inchangées, le schéma et trois critères ciblés sur la fixture. Les assertions textuelles sur le corrigé sont propres à cet exercice.

