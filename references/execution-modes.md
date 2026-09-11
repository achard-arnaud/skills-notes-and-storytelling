# Mode d'exécution du skill (`ExecutionMode`)

Cette variable est distincte du `GenerationMode` (`from-scratch` / `iterative` / `feedback-dreaming` / `retro-engineering`) et du `RuntimeMode` (voir [runtime-modes.md](runtime-modes.md)). Elle décrit **l'environnement d'hébergement** dans lequel le skill tourne, et doit être déclarée avant toute autre décision de consommation de contexte.

## Valeurs

- `chat` — session de conversation légère (ex. Claude.ai chat, intégration mobile). Contexte contraint, pas de garantie d'accès fichiers/scripts/dépôt, latence attendue faible.
- `cowork` — session outillée (Claude Code, Cowork, agent avec accès fichiers/scripts/repo). Contexte large possible, exécution de `scripts/validate_contracts.py` et lecture/écriture de fichiers disponibles.

Si l'environnement n'expose aucun moyen de détecter le mode, traiter la session comme `chat` par défaut (posture la plus prudente en consommation de contexte).

## Règles de consommation de contexte par mode

| Aspect | `chat` | `cowork` |
|---|---|---|
| Lecture des références | Charger uniquement le fichier de référence strictement nécessaire à l'étape en cours (ex. `modes.md` seul au moment de choisir le mode) | Peut charger l'ensemble `references/` + `contracts/` en une passe si le run est lourd |
| Fragments/claims en mémoire | Garder un registre minimal (IDs + résumé une ligne), ne pas reproduire le texte source intégral | Peut matérialiser fragments/claims complets dans des fichiers versionnés |
| Scripts déterministes | Ne pas supposer leur exécution possible ; réaliser les vérifications de contrat "à la main" en suivant les schémas JSON | Exécuter `scripts/validate_contracts.py` avant livraison |
| Intake documentaire volumineux | Résumer et extraire au fil de l'eau, éviter de garder plusieurs documents bruts complets en contexte simultanément | Peut persister l'intake complet en fichiers et le relire par fragments à la demande |
| Side stories | Se limiter aux 2-3 side stories à plus forte valeur ; couper le reste en surface même si éligible | Peut router l'ensemble des side stories éligibles |
| Style de sortie | Répondre directement dans le fil, en évitant les manifestes/fichiers intermédiaires si non demandés | Peut produire des artefacts intermédiaires (scaffold, source ledger) comme fichiers séparés |

## Interaction avec le `RuntimeMode`

Le mode `chat` force en pratique une préférence pour `run léger` (voir runtime-modes.md), sauf si l'utilisateur fournit explicitement des documents à ingérer — auquel cas la règle "intake documentaire ⇒ run lourd" prévaut et le modèle doit avertir l'utilisateur que le run sera plus long/plus consommateur de contexte malgré le mode `chat`.

Le mode `cowork` autorise mais n'impose pas un run lourd : un `run léger` reste légitime en `cowork` pour une question rapide sans intake.

## Déclaration

Déclarer `execution_mode` en tête de run (dans le manifest de run si un fichier est produit, sinon dans la première ligne de raisonnement visible du modèle) : `execution_mode: chat|cowork`.
