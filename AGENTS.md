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

## Evidence policy
Side stories are composition artifacts and cannot originate unsupported claims. Account/buyer reality and seller/product truth remain independent until an explicit fit stage.


## Architecture commune — revue documentaire du 13 novembre 2026

Lire [l’index des décisions](docs/architecture/README.md), puis seulement l’ADR pertinent : routage et méthodes (1001), connaissance (1002), narration et rendu (1003), RUN/BUILD et contexte (1004), loopback et validation (1005), autorités et convergence (1006). Les principes sont approuvés ; les capacités réelles restent définies par les contrats et manifests au SHA du run. Cette publication documentaire ne migre aucun enum ni template. [Couverture des 14 ADR historiques](docs/architecture/ADR-REVIEW-2026-11-13.md).
