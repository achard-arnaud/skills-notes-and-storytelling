# AGENTS.md

## Repository purpose
Govern evidence-grounded document composition and reusable note templates.

## Required stage boundaries
Do not merge research, claims, narrative and rendering into one opaque pass.

```text
research → fragments → claims graph light → rerank → scaffold
→ fill → side stories → sourcing → layout → DOCX QA → nudging
```

## Change policy
- Contract change: add or update a regression fixture.
- Template change: update `templates/manifest.json`.
- New template: lifecycle starts at `candidate`.
- Promotion: requires explicit human approval.
- Any DOCX-related output must satisfy `tests/QA_CHECKLIST.md`.

## Evidence policy
Side stories are composition artifacts and cannot originate unsupported claims.
