# Calibration de l'effort de raisonnement par étape

Le skill ne code jamais un nom de modèle. Il déclare un **niveau d'effort de raisonnement** par étape du pipeline, dans `config/reasoning-effort.json`, exprimé en niveaux abstraits (`low`, `medium`, `high`) que le runtime hôte mappe vers ses propres capacités (budget de réflexion, nombre de passes, modèle utilisé).

## Principe

- `low` : tâche mécanique, à forte structure, faible ambiguïté — extraction, formatage, déduplication syntaxique.
- `medium` : tâche qui demande un jugement local mais borné — reranking, scaffolding.
- `high` : tâche qui demande un arbitrage global, une synthèse ou un jugement irréversible — arbitrage de claims contradictoires, synthèse exécutive, décision de routage d'un side story ambigu.

## Table par étape (voir aussi `config/reasoning-effort.json`)

| Étape du pipeline | Effort | Justification |
|---|---|---|
| Recherche / collecte de sources | medium | jugement de pertinence mais pas d'arbitrage final |
| Extraction en fragments | low | atomisation mécanique d'une source déjà identifiée |
| Déduplication de fragments | low | comparaison syntaxique/sémantique locale à faible enjeu |
| Construction claims graph light | medium | typage des nœuds/arêtes, jugement local |
| Arbitrage de claims contradictoires | high | décision qui engage la fiabilité de toute la note |
| Reranking | medium | pondération multi-critère mais règles explicites |
| Scaffold | medium | structuration, réversible tant que le fill n'a pas eu lieu |
| Fill / rédaction de section | medium | rédaction guidée par le scaffold et les fragments |
| Routage des side stories | medium | décision bornée par la grille de routage (side-stories-retro.md) |
| Synthèse exécutive / thèse centrale | high | condense l'ensemble du raisonnement en une décision lisible |
| QA / fact-check | high | dernière ligne de défense avant livraison |
| Feedback / dreaming (proposition de patch) | high | modifie potentiellement le système, pas seulement un livrable |

## Règle d'implémentation

- Ne jamais coder en dur un identifiant de modèle (`claude-...`, `gpt-...`) dans ce fichier ni dans le SKILL.md.
- Le mapping niveau → configuration concrète appartient au runtime hôte, pas au skill.
- En mode `chat` (voir execution-modes.md), un budget de raisonnement `high` peut être indisponible : dégrader vers `medium` et signaler explicitement à l'utilisateur les étapes où l'arbitrage a été simplifié.
- Chaque étape marquée `high` doit produire une trace courte de sa décision (1-3 lignes) dans le manifest de run, pour audit ultérieur en `feedback-dreaming`.
