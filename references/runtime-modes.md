# Modes d'exécution runtime (`RuntimeMode`)

Distinct du `GenerationMode` (from-scratch/iterative/feedback-dreaming/retro-engineering, voir modes.md) et de l'`ExecutionMode` (chat/cowork, voir execution-modes.md). Le `RuntimeMode` décrit **l'intensité d'exécution du pipeline pour ce run précis**.

## Valeurs

- `debug` — exécution pas à pas, chaque étape du state machine (workflow.md) est explicitée et son contrat de sortie vérifié avant de passer à la suivante ; utilisé pour diagnostiquer un défaut de pipeline, jamais pour une livraison normale.
- `run_lourd` (full pipeline) — exécute l'intégralité du state machine, de `MODE_SELECTED` à `DELIVERED`, avec intake documentaire complet, fragmentation, claims graph, scaffold, side stories, DOCX QA.
- `run_léger` (chat, réponse rapide) — répond directement à une question sans dérouler le pipeline complet ; pas de fragments/claims persistés, pas de scaffold formel, pas de DOCX.

## Règle impérative : intake documentaire force le run lourd

Si l'utilisateur fournit un ou plusieurs documents en intake (fichier, texte collé long, lien vers un document), le `run_lourd` est **forcé**, quel que soit le `RuntimeMode` demandé ou déduit par défaut, et quel que soit l'`ExecutionMode`. Un run léger ne peut jamais absorber un intake documentaire réel — au mieux il peut faire une lecture superficielle et doit alors le signaler explicitement comme dégradé plutôt que prétendre avoir traité l'intake avec le pipeline complet.

Exception : une question ponctuelle sur un document déjà traité dans un run antérieur (mode itératif "zoom", voir modes.md §5) reste éligible au run léger tant qu'elle ne réouvre pas d'intake nouveau.

## Règle de priorisation : input manuel > recherche complémentaire

1. Tout ce que l'utilisateur fournit explicitement (données, documents, affirmations, corrections) est traité comme source primaire et retrievé/fragmenté en premier.
2. La recherche complémentaire (web ou autre) ne sert qu'à combler des trous explicitement identifiés après épuisement de l'input fourni — jamais à contredire silencieusement un input utilisateur explicite (un désaccord doit être signalé, pas substitué).
3. Voir [retrieval-and-reranking.md](retrieval-and-reranking.md) pour la règle de ciblage des requêtes (claims précis, jamais de recherche thématique large).

## Sélection du RuntimeMode par défaut

| Situation | RuntimeMode par défaut |
|---|---|
| Intake documentaire fourni | `run_lourd` (forcé) |
| Question courte sans intake, pas de livrable DOCX demandé | `run_léger` |
| Livrable DOCX/template complet demandé, pas d'intake | `run_lourd` |
| Diagnostic d'un défaut de pipeline signalé par l'utilisateur ou la QA | `debug` |
| Run itératif "zoom" sur des IDs déjà produits | `run_léger` si le périmètre est petit et local, sinon `run_lourd` si le zoom réouvre une portion large du document |

Le `RuntimeMode` retenu doit être déclaré explicitement en une ligne avant de commencer l'exécution (`runtime_mode: debug|run_lourd|run_léger`), avec sa justification si elle diffère du choix par défaut de l'utilisateur.
