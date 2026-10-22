# Livraison par lots, plan nocturne et traçabilité
Revue 2026-10-22. DESIGN_ONLY. Les fenêtres de développement sont une cible ; aucun exécuteur nocturne activé.
## Ordre de livraison proposé
| Lot | Issues | Résultat vérifiable |
|---|---|---|
| S0 cadrage | #22 #39 #41, #19 #20 | bootstrap court, prompt système, règles/impact tests et autorisations |
| S1 contrats | #23 #24 #34 | ToC stable, UNE étoile, Analyste/stepper et handoffs |
| S2 démonstrateur minimal | #26 #27 + minimum #25 #28 | un two-pager synthétique bout en bout ; store simple, pas migration Obsidian obligatoire |
| S3 qualité narrative | #35 #36 #38 #31 | blind-spot, side stories multi-container, proofreader/loopback |
| S4 édition/publication | discovery #37 peut être avancée ; intégration #37 #30 #29 | Canvas remplaçable et vrais exports, QA/receipts |
| S5 autonomie contrôlée | #40 puis #32 | scheduling autorisé, budget/resume, packaging utile |
Les dépendances de capacité ne demandent pas nécessairement tout un epic terminé. Découper minimum vertical pilote ; architecture-note ensuite, neuf templates plus tard. Obsidian demeure option de branchement, pas prérequis bloquant au premier rapport.

## Séparation des mécanismes
Reprise radar : un cron prépare données/plan ; une tâche native fait les opérations accessibles à son environnement. Aucune connexion implicite entre eux, aucun accès présumé à la recherche interne GPT/Claude depuis GitHub Actions.
Option MVP : tâche native à 22h pour présenter le workload et recueillir GO_DEV. Plus tard un runner autorisé, local ou hébergé, exécute un workflow_dispatch ou un mécanisme programmé dont les capacités sont démontrées.
Un webhook signale un événement, il ne crée ni capacité LLM, ni jetons API, ni droits de développement. Choisir et tester le canal avant activation ; ne pas supposer que l'abonnement UI finance l'API ou un runner.
GitHub Actions futur : branche isolée, permissions minimales, lock par repo/nuit, secrets serveur, checks ciblés. Publication/merge distincts du push vérifié.

## Cycle nocturne Europe/Paris
| Heure locale | Action proposée | Gate |
|---|---|---|
| 22h | Lire backlog/checkpoints/CI et présenter 1 ticket principal, option de secours et planning ; pas de développement | Choix humain et GO_DEV versionné |
| 03h | Acquérir lease, relire autorisation/SHA/budget, développer le ticket prioritaire approuvé | Autorisation valide, dépendances prêtes, budget disponible |
| 04h | Reprise ou revues conformité/qualité du même ticket ; second ticket seulement dans plan approuvé | Pas de concurrence sur les mêmes fichiers |
| 05h | Vérification, PR candidate, loopback ; continuer seulement si prévu et avant cut-off | Réserve matin et expiration |
Silence à 22h = absence d'approbation, donc aucun développement la nuit suivante. Notification de plan n'est pas GO_DEV.
Au passage heure été/hiver : une exécution logique par date locale et slot, même si heure répétée ; heure inexistante = skipped avec receipt, pas exécution surprise. Scheduler doit prouver sa résolution timezone ; les crons UTC nécessitent conversion/réconciliation explicite.
Les fenêtres ne garantissent pas démarrage à la minute ; définir latest_start et expires_at. Retard hors fenêtre = DEFERRED, pas catch-up automatique.

## ApprovalRecord cible
approval_id, actor, approved_at, local_night_date, timezone, issue_number, issue_body_hash, spec_revision/hash, base_sha, allowed_paths/actions, plan_hash, slot_allowlist, token_cap/call_cap/wall_time_cap, provider, morning_reserve, latest_start, expires_at, revoked_at.
Autorisation d'une sélection bornée pour une nuit par défaut. Un changement matériel de scope/plan ou de SHA impose revalidation, sauf règle explicite de rebase déjà approuvée.
Avant chaque mutation : autorisation et lease encore valides. Annulation utilisateur = checkpoint puis arrêt. Aucune CI verte ne vaut autorisation de merge.

## Économie, quotas et arrêt
Paramètres à valider à 22h, pas de chiffres inventés : budget nuit, coût par rôle, réserve matin par fournisseur, concurrence max (1 worker initial), retry max, cut-off.
Consommation observable par API/provider ; limites des interfaces parfois opaques. Quand quota/réserve non observables, appliquer plafond prudent approuvé ou différer ; ne pas promettre de préserver un quota non mesurable.
Retry 429/5xx : Retry-After si fourni, backoff exponentiel+jitter, nombre borné et respect cut-off ; auth/permission = blocage, pas retries aveugles.
Checkpoint pré-emptif avant limite. Cache par hash, retrieval ciblé, suite tests par impact #19. Pas de run complet pour changement documentation.
Idempotency = repo+date_locale+slot+issue+plan_hash ; lease expirante avec heartbeat et fencing token ; réception doublon = no-op. Crash = état reprenable, aucun commit doublé.
Receipts : planned→authorized→started→checkpointed→verified|failed|deferred ; refs SHA/tests/PR, coût réel ou unknown, défauts restants. Loopback ≤3 actions et au plus 1 patch proposé ; déduplication avant nouvelle issue.

## Matrice d'exigences
| Exigence du 22/10 | Issues autoritaires |
|---|---|
| README exact/récent, bootstrap, cadre Superpowers | #22 #39 |
| Backlog du jour et couverture des tickets | #21 #41 |
| KB/alerte/contexte, one-shot/deep-search | #25 #28 #34 |
| Analyste et template/frontend | #24 #34 |
| ToC ordre JSON, ajout/retrait, UNE étoile | #23 #24 #27 |
| Blind-spot chat, ToT borné, self-review | #35 |
| Side-stories/dézoom/contre-perspective, slots | #23 #36 |
| Storyteller, plan/angles, preuve et multi-container | #36 |
| Débriefer/proofreader/freeze | #38 |
| Bootstrap Open Canvas, diff/versions/provenance | #37 |
| Choix formats, QA/download réel | #30 #38 |
| Runtime/reprise/CI/permissions | #26 #29 |
| Workload 22h et 03h/04h/05h | #40 |
| Retex, token discipline, tests par impact | #31 #19 #39 #40 |
| Packaging multi-workspace / cloud optionnel | #32 |
Les onze BN-00..BN-10 du plan initial sont #22..#32 : tous retrouvés. Huit compléments sont #34..#41. #33 est une PR, pas un ticket d'implémentation supplémentaire.
Les références historiques suggérant #35..#38 avant cette revue ne correspondaient pas à des issues alors existantes dans ce dépôt ; ne pas affirmer qu'elles étaient déjà logguées. Les exigences utiles sont désormais couvertes par cette matrice.
