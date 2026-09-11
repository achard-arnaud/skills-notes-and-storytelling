# Analyse prospective — non exécutée (2026-09-11)

## Cas de référence

Aucune trace de "François Rivard / Meridian" n'a été trouvée ni dans l'historique de conversation transmis à cet agent, ni dans les deux dépôts (`achard-arnaud/tourisme-etude-historico-geographique`, `achard-arnaud/skills-notes-and-storytelling`). Conformément à la consigne de repli, le cas représentatif retenu est le run déjà présent dans le repo : `examples/runs/2026-09-astraforge-plasma-opportunity.md` (template `OPPORTUNITY_NOTE_ICP`, décision AstraForge × Plasma).

## Méthode

- **Avant** : état du repo au commit `18ae0de` (dernier commit de `main` avant cette refonte) — SKILL.md + `references/modes.md` + `references/side-stories-retro.md` + `references/workflow.md`, sans `execution_mode`/`runtime_mode`/effort de raisonnement déclaré, sans registre narratif explicite, sans distinction formalisée retrieval claims vs fragments.
- **Après** : état du repo sur `claude/sleepy-archimedes-8novca` après cette refonte.
- Le run lui-même (`examples/runs/2026-09-astraforge-plasma-opportunity.md`) n'a pas été régénéré from scratch (aucun accès à un intake documentaire réel dans cette session) ; la comparaison porte sur **ce que le pipeline aurait fait différemment** en rejouant ce run sous la nouvelle architecture, en s'appuyant sur les contrats déjà passés du fixture (`qa_status: passed`).

## Constats "avant"

1. Aucune variable ne distingue un run `chat` d'un run `cowork` : un utilisateur en chat léger pouvait déclencher malgré lui un run lourd, saturant le contexte disponible.
2. Aucun effort de raisonnement différencié par étape : rien n'empêchait de traiter l'arbitrage de claims contradictoires (étape à fort enjeu) avec le même niveau d'attention qu'une déduplication mécanique de fragments.
3. Claims et fragments étaient contractuellement séparés (`contracts/claim.schema.json` vs `contracts/fragment.schema.json`) mais sans règle de reranking différenciée écrite : le risque était de reranker les fragments avec la grille de pertinence décisionnelle des claims (30/25/20/15/10), qui n'est pas adaptée à un choix de preuve.
4. Aucun registre explicite des méthodes narratives : le respect de Pyramid Principle / Action Titles était appliqué implicitement par le style-contract mais non nommé, non audité, non réutilisable pour justifier un choix éditorial en revue.
5. Pas de règle explicite forçant le run lourd sur intake documentaire, ni de règle de ciblage des recherches complémentaires (risque de requêtes larges et bruitées).
6. Le mode itératif ne permettait pas de "zoomer" sur des IDs précis sans (au moins implicitement) relire toute la baseline.

## Constats "après" (rejeu du cas AstraForge × Plasma)

1. `execution_mode: cowork` aurait été déclaré dès l'ouverture du run (accès repo/fichiers disponible), autorisant la persistance complète des fragments/claims produits — cohérent avec ce que le fixture montre déjà (fichier de run versionné).
2. `runtime_mode: run_lourd` aurait été forcé explicitement (le run traite un intake produit/marché réel), avec trace dans le manifest plutôt qu'implicite.
3. L'arbitrage "durable UiPath queue semantics remains a hard gap instead of being attributed to AstraForge" — le point le plus sensible du run — est exactement le type de décision classée `claims_arbitration` (effort `high`) dans `config/reasoning-effort.json` : la nouvelle architecture le rend traçable et auditable au lieu d'un jugement non catégorisé.
4. Les trois side stories du fixture (`false_lead`, `dezoom`, `analytical_focus`) se retrouvent explicitement couvertes par la grille de routage de `retrieval-and-reranking.md` (exclusion/relégation) : chacune reste justifiée comme rattachée à un claim existant, aucune n'aurait été exclue.
5. Le template `OPPORTUNITY_NOTE_ICP` déclare désormais ses frameworks narratifs par défaut (`pyramid_principle`, `mece`) dans `layered-architecture.md` — la structure observée dans le fixture (décision d'abord, gates ensuite, preuve représentative en dernier) est effectivement conforme à Pyramid Principle, ce qui valide a posteriori le choix par défaut plutôt que de l'avoir laissé implicite.
6. La typologie de nodes du fixture (gates, lanes de parties prenantes, mapping gap→mécanisme→outcome) est bien multiple (stratégique + preuve), confirmant la généralisation par rapport à la logique causale unique du repo historique décrite dans `layered-architecture.md`.

## Delta mesurable

| Dimension | Avant | Après |
|---|---|---|
| Variable de mode d'exécution déclarée | Absente | `execution_mode` + `runtime_mode` déclarés et justifiés |
| Effort de raisonnement par étape | Implicite, non catégorisé | Explicite, configuré, dégradable en `chat` |
| Règle de reranking fragments | Absente (seule la grille claims existait) | Grille dédiée à 4 critères (spécificité/fraîcheur/indépendance/coût de vérification) |
| Registre narratif | Implicite | 5 frameworks nommés, mappés par template |
| Règle intake ⇒ run lourd | Non écrite | Règle écrite ; comportement non testé par ce rapport |
| Mode itératif ciblé | Non disponible | Sous-mode "zoom" par ID, profondeur de voisinage bornée |

## Recommandations de fine-tuning / optimisation

1. **Prochain run réel** : rejouer un run `from-scratch` complet sous la nouvelle architecture (pas seulement une relecture) pour vérifier que la déclaration `execution_mode`/`runtime_mode` en tête de run ne casse pas la fluidité conversationnelle en mode `chat` — actuellement seul un raisonnement a priori a été fait, pas un test de bout en bout.
2. **Fragments reranking** : les poids proposés (35/25/25/15) sont un défaut non calibré sur données réelles — les ajuster après au moins 3 runs `feedback-dreaming` avec des QA humaines, comme le prévoit déjà `dreaming-self-healing.md`.
3. **Registre narratif** : n'a que 5 entrées ; envisager d'ajouter un framework spécifique aux notes très denses (`TWO_PAGER`) type "So-What Bullet" si les futurs runs montrent un besoin récurrent non couvert par MECE/Action Titles.
4. **Retro-engineering** : rester TODO ; le déclencher seulement une fois qu'au moins deux cas réels auront traversé le pipeline `run_lourd` sous la nouvelle architecture pour fournir des exemples d'entraînement à l'inférence de template.
