# Registre des méthodes narratives connues

Ce registre est la couche "storytelling / stratégie narrative" du skill (couche 2 de [layered-architecture.md](layered-architecture.md)). Chaque template référence dans son propre fichier `templates/<template>.md` les frameworks qu'il utilise par défaut, via l'`id` ci-dessous.

| id | Nom | Principe | Signal d'usage | Signal d'abus/à éviter |
|---|---|---|---|---|
| `pyramid_principle` | Pyramid Principle (Minto) | Ouvrir par la réponse/la thèse, puis descendre vers les arguments et les preuves — jamais l'inverse | Toute note dont le lecteur décide en <60 secondes doit ouvrir par la conclusion | Une intro qui reconstitue la démarche chronologique de recherche au lieu de la conclusion |
| `action_titles` | Action Titles (Barbara Minto / conseil en stratégie) | Le titre de chaque section/slide porte l'insight, pas le thème | `"Le TCO double après 18 mois de migration incrémentale"` au lieu de `"Coûts"` | Titre générique réutilisable pour n'importe quel contenu (`"Analyse"`, `"Overview"`) |
| `mece` | MECE (Mutually Exclusive, Collectively Exhaustive) | Structurer les preuves/sections sans trou ni recouvrement | Grille de critères de benchmark, matrice de gap buy-side, typologie de risques | Deux sections qui répondent en partie à la même question, ou un critère de décision non couvert |
| `ghost_deck` | Ghost Deck first | Valider la logique (scaffold + titres d'action) avant tout travail de mise en forme visuelle | Étape "scaffold" du workflow, avant DOCX QA | Itérer sur la mise en page avant que le scaffold soit stable |
| `signal_to_noise` | Signal-to-noise | Retirer tout ce qui ne prouve pas directement le point de la section | Étape "fill" et arbitrage des side stories | Garder un fragment "intéressant" mais non probant par simple curiosité |

## Règle de sélection par défaut

- Toute note à décision unique (`ONE_PAGER`, `OPPORTUNITY_NOTE_ICP` en synthèse) : `pyramid_principle` + `action_titles` + `signal_to_noise`.
- Toute note à comparaison structurée (`BENCHMARKING`, `BUY_SIDE_GAP_ANALYSIS`) : `mece` en premier, puis `pyramid_principle` pour l'ouverture et `action_titles` pour chaque ligne de matrice.
- Toute note longue avec diagrammes (`ARCHITECTURE_NOTE`, `DIAGNOSTIC_RECO_SELL_SIDE`) : `ghost_deck` obligatoire avant la couche mise en page, puis `pyramid_principle` + `signal_to_noise`.
- `signal_to_noise` s'applique **toujours** en dernière passe avant sourcing, quel que soit le template.

## Extension du registre

Un nouveau framework ne peut être ajouté au registre qu'avec : un id stable, un principe en une phrase, un signal d'usage vérifiable, un signal d'abus vérifiable, et au moins un template qui le référence explicitement dans sa couche 2. Passage par le cycle `feedback-dreaming` (voir dreaming-self-healing.md) comme tout changement de contrat réutilisable.
