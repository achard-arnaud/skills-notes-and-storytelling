---
artifact_type: format-crosswalk-proposal
source_repo: achard-arnaud/Business-ptf-analysis
source_ref: 22439881e61bcc65adf8a193b26c53c7e3258db7
target_template: two-pager
target_version: 1.3.0
status: review-only
---

# Three-page business diagnostic → two-page business mix and execution

## Harvest scope and evidence

Read-only harvest at Business-ptf-analysis commit `22439881e61bcc65adf8a193b26c53c7e3258db7` (tree `eb92e1de517afdd002af84471059ad4682d6c075`). Focused reads:

- `templates/THREE_PAGER_EXEC_v0.3.md` — three-page editorial contract.
- `contracts/three-pager-exec.schema.json` and `templates/registry.json` — payload/registry capability.
- `examples/three-pagers/greenyellow/README.md`, `analysis.md`, `three-pager.md` — documentary business/backlog example.

The reference template and three-pager example are explicitly candidate/demo-only; the registry lists the exec profile as `demo_only`, not production-validated. The GreenYellow example says it is public-source, non-approved and not a schema-conforming payload. Use its structure as a design reference, not its company facts or claims as reusable content.

## What the three-page structure contributes

| Page | Business question | Material content |
|---|---|---|
| **1 — Business model and drivers** | Where does the company create value, and what determines its economics? | Signalétique, business mix, customer/offer economics, value drivers, counter-thesis, SWOT → TOWS. |
| **2 — Value-chain execution** | Where do activities, frictions, and value transfers occur? | Activities and handoffs, operating model, current tooling/capabilities, constraints, baselines and evidence gaps. |
| **3 — Priority backlog** | Which initiatives could change value, and what must be proven first? | Three to five strategic themes or initiatives, value mechanism, KPI/baseline, owner/gates/dependencies, sequencing and takeaways. |

The third page carries traceability from value-chain activity to initiative priority; the first two pages explain why those priorities matter. Its detailed 9-activity Porter layout, star ratings, Magic Quadrant and initiative ranking are profile-specific mechanisms, not required elements for the two-page format.

## Two-page compression contract

| Two-pager page | Required spine | Carry-forward from three-page pattern |
|---|---|---|
| **P1 — Business mix and value creation** | Entity/scale, markets and geography, products/services, customers and commercial/delivery mix where disclosed, group/entity boundary, economic logic, value drivers, 24-month newsflow, evidence-backed SWOT → conditional TOWS. | Compress page 1's signalétique and drivers. Keep units, periods and denominators. Do not infer revenue mix from a service catalogue. |
| **P2 — Execution and competitive position** | Value-chain activities and handoffs, strategy-to-execution evidence, product/use-case delivery, competitive comparison, moat mechanisms/erosion, three to five business takeaways. | Compress page 2's activity/friction map and page 3's relevant 3–5 backlog items. Include initiative baselines, owners and gates only when the user's question includes a backlog or transformation decision. |

### Compression rules

1. Preserve the causal path: **business mix → value mechanism → activity/constraint → execution evidence → strategic implication**.
2. A metric without period, unit, perimeter or denominator is labelled and bounded; group figures never silently become entity figures.
3. Separate announced intent, funded work, delivery evidence and measured outcome.
4. Retain a value-chain item only if it explains economics, differentiation, risk or execution.
5. Compress a larger backlog to at most five themes; do not transfer the three-page star/rank/quadrant machinery automatically.
6. State missing mix, margin, customer concentration, baseline, owner or moat evidence as unknown; do not fill from a role advertisement.
7. Keep competitive archetypes distinct from sourced named competitors. A comparison without normalized scope is only a hypothesis.
8. **Business-analysis boundary:** do not introduce a candidate, François, recruiter, job-posting narrative, employer-fit score or application decision into the company description. If requested, candidate fit is a separate analysis and separate output variant.

## Distinction between the two formats

The three-pager supports a fuller diagnosis and a traceable backlog. The two-pager is the executive compression: page 1 establishes the company's business mix and value logic; page 2 shows whether and how that logic is executed, where the business may be differentiated, and what the strongest evidence supports. It is not a three-page backlog squeezed into smaller type.

## Source pointers

- [Business-ptf-analysis / three-page contract](https://github.com/achard-arnaud/Business-ptf-analysis/blob/22439881e61bcc65adf8a193b26c53c7e3258db7/templates/THREE_PAGER_EXEC_v0.3.md)
- [Registry capability status](https://github.com/achard-arnaud/Business-ptf-analysis/blob/22439881e61bcc65adf8a193b26c53c7e3258db7/templates/registry.json)
- [GreenYellow example description and limitations](https://github.com/achard-arnaud/Business-ptf-analysis/blob/22439881e61bcc65adf8a193b26c53c7e3258db7/examples/three-pagers/greenyellow/README.md)
- [GreenYellow three-page structure](https://github.com/achard-arnaud/Business-ptf-analysis/blob/22439881e61bcc65adf8a193b26c53c7e3258db7/examples/three-pagers/greenyellow/three-pager.md)
