# AGENTS.md

## Repository purpose
Govern evidence-grounded document composition, generation modes and reusable note templates.

## Required stage boundaries
Do not merge research, claims, narrative and rendering into one opaque pass.

```text
mode
→ research → fragments → claims graph light → rerank → scaffold
→ fill → side stories → sourcing → layout → DOCX QA → nudging
→ feedback/dreaming (optional)
```

## Supported modes
- `from-scratch`: full pipeline from a blank canonical baseline.
- `iterative`: delta-first update against a resolved canonical baseline.
- `feedback-dreaming`: system improvement after delivery/QA.
- `retro-engineering`: TODO only; documented reverse workflow, not production-ready.

## Change policy
- Contract change: add or update a regression fixture.
- Template change: update `templates/manifest.json`.
- Mode change: update `modes/manifest.json`.
- New template: starts candidate, then human approval + passing fixture may validate it.
- Promotion to main: integration branch `dev` must be green.
- Any DOCX-related output must satisfy `tests/QA_CHECKLIST.md`.
- Any skill or shared editorial-rule change must include a transverse mention review: link the shared contract from applicable skills, scope research quotas correctly, and record coverage/follow-up.

## Evidence policy
Side stories are composition artifacts and cannot originate unsupported claims. Account/buyer reality and seller/product truth remain independent until an explicit fit stage.


## Architecture commune — revue documentaire du 13 novembre 2026

Lire [l’index des décisions](docs/architecture/README.md), puis seulement l’ADR pertinent : routage et méthodes (1001), connaissance (1002), narration et rendu (1003), RUN/BUILD et contexte (1004), loopback et validation (1005), autorités et convergence (1006). Les principes sont approuvés ; les capacités réelles restent définies par les contrats et manifests au SHA du run. Cette publication documentaire ne migre aucun enum ni template. [Couverture des 14 ADR historiques](docs/architecture/ADR-REVIEW-2026-11-13.md).


## Hygiène des artefacts RUN et BUILD

Conserver les livrables de run, corpus privés, exports temporaires et captures dans leur destination de travail ou de livraison. Versionner dans le dépôt les méthodes, contrats, documentation de projet et fixtures de régression explicitement curatées. Un exemple public doit être minimal, attribué et autorisé, ou synthétique ; une sortie de run brute ne devient pas une fixture par simple déplacement. Cette règle encadre les nouveaux apports ; les éventuelles migrations de contenus historiques gardent leurs références et reçus.


## S3 domain skills

For new S3 studies, select the domain skill and its method by question, then the template by audience and use. Use the [domain analysis contract](references/domain-analysis.md). RUN pins the published BUILD and writes to the private case boundary. BUILD starts from dev with synthetic fixtures. Resume a legacy case on its recorded route and keep its private storage. Use a separate worktree for each activity when executing both.

## New-case executable boundary
For new independent full-workflow runs use `python scripts/case_runtime.py check`, then `init --case <id> --input intake.json`.
The active route is `workflow/case-process.json`; new RUN files live in ignored `data/cases/<id>/`.
Call begin/complete for A0 evidence, A1 typed graph, A2 scaffold, A3 composition, A4 review.
Each call consumes the emitted I/O/context packet; preserve pins, attempts and execution events.
Do not infer an old run completed these stages. Keep legacy programme gates and histories explicit.
For material incidents call loopback with the hashed proposal; diagnose architecture, bugfix, CI,
runtime or skill, then apply an authorized BUILD with regression proof and ADR disposition.

## Entrées S3 et documents de décision

Choisir dès l’entrée : **skill directe** pour un format court et un périmètre borné ; **brief puis A0–A4** pour une étude approfondie ou une recherche multi-source. La skill de domaine possède les constats et aide à choisir le format par lecteur et usage. Le sélecteur narratif reçoit uniquement les claims utiles, avec leurs preuves. A3 reçoit un paquet par section ; A4 retourne les écarts vers leur propriétaire. Voir [cartographie des skills, agents et statuts](references/s3-operations.md).

Maintenir le PRD canonique dans la [documentation versionnée](docs/specifications/) ou dans le board projet avec une version traçable. Le ticket maître lie cet emplacement et pointe ses dépendances et sa recette. Chaque ADR applicable lie le PRD et le ticket et distingue la décision, la preuve d’implémentation et la validation humaine. Les captures de conversation peuvent éclairer le contexte. Le code, les contrats et la documentation de projet matérialisent les décisions.
