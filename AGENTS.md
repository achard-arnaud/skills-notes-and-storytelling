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

## Runtime / artifact policy
- Runs are execution outputs, not source code.
- Never commit run outputs, generated notes, generated PDFs/DOCX/PPTX, temporary artifacts, screenshots, exported reports or customer-specific deliverables into this repository.
- Store deliverables outside the repository source tree through the conversation artifact mechanism, CI artifacts, or another explicit artifact store.
- If a run reveals a reusable improvement, commit only the generalized rule, template, fixture or documentation patch required to reproduce that improvement; do not commit the run itself.
- `examples/` may contain stable fixtures and minimal illustrative samples only when they are intentionally curated regression assets, not live run output.

## Change policy
- Contract change: add or update a regression fixture.
- Template change: update `templates/manifest.json`.
- Mode change: update `modes/manifest.json`.
- New template: starts candidate, then human approval + passing fixture may validate it.
- Promotion to main: integration branch `dev` must be green.
- Any DOCX-related output must satisfy `tests/QA_CHECKLIST.md`.

## Evidence policy
Side stories are composition artifacts and cannot originate unsupported claims. Account/buyer reality and seller/product truth remain independent until an explicit fit stage.
