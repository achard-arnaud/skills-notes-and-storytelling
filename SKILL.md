---
name: decision-notes-and-storytelling
description: Create, revise, or industrialize evidence-grounded decision notes, architecture notes, one-pagers, two-pagers, benchmarks, buy-side gap analyses, sell-side diagnostic/recommendation notes, ICP opportunity notes and integration notes. Own research-to-claims-to-storytelling, evidence lineage, template bridges, lock-in mapping, next-step nudging and the governed dreaming loop. Pair with the runtime DOCX skill when a Word artifact is requested.
---

# Decision Notes & Storytelling

## Scope

This skill is a governed decision-note OS. It owns **context reconstruction, research, evidence lineage, claims, decision architecture, narrative composition, template routing, cross-template bridges and learning loops**. Rendering is a downstream concern.

Use the lightest output that closes the decision. Do not create a larger report when a one-pager, two-pager or bounded integration decision is sufficient.

## Generation mode

Select one mode from `GenerationMode` before the output template. Read [references/modes.md](references/modes.md).

- `FROM_SCRATCH` — no trusted canonical draft exists.
- `ITERATIVE` — preserve a canonical baseline and update only the declared factual/content scope before full regression QA.
- `FEEDBACK_DREAMING` — explicit system-improvement run over prior outputs/feedback.
- `RETRO_ENGINEERING` — **TODO / non-production**.

`FEEDBACK_DREAMING` remains an explicit mode for deep improvement work, but a **lightweight dreaming check is also mandatory at the end of every normal run**. The user does not need to request it. `NO_REUSABLE_DELTA` is a valid result; canonical behavior never changes without human approval.

## Template enum

Select exactly one primary template:

- `ARCHITECTURE_NOTE`
- `ONE_PAGER`
- `TWO_PAGER`
- `BENCHMARKING`
- `BUY_SIDE_GAP_ANALYSIS`
- `DIAGNOSTIC_RECO_SELL_SIDE`
- `OPPORTUNITY_NOTE_ICP`
- `INTEGRATION_NOTE`

Every template is versioned in `templates/manifest.json` with a QA fixture. Read [references/versioning-and-lifecycle.md](references/versioning-and-lifecycle.md).

## Canonical workflow

Follow [references/workflow.md](references/workflow.md). Stage boundaries remain explicit.

1. **Context & decision framing** — reconstruct the actual problem, audience, time horizon and constraints before accepting the supplied framing.
2. **Research** — collect evidence; separate account/company reality, product truth, market alternatives and dependencies.
3. **Fragments** — convert evidence into atomic source-addressable fragments.
4. **Claims graph light** — create claims, contradictions, unknowns and typed edges.
5. **Rerank** — prioritize decision relevance, evidence strength, explanatory value, novelty and audience fit.
6. **Scaffold** — build the decision spine before drafting.
7. **Fill** — draft only from attached fragments; preserve evidence status.
8. **Side stories** — add bounded analytical detours only after the core spine is coherent.
9. **Fact-check & source** — verify every material claim and source line.
10. **Layout / render QA** — when an artifact is requested, map to the template and run the appropriate rendering QA.
11. **Bridge / nudging** — evaluate the smallest evidence-backed next decision and route it to another template when useful. Zero bridge is valid.
12. **Dreaming** — always inspect the run for reusable QA/workflow/template improvements; propose, never silently promote.

## Evidence memory and bridges

Read [references/bridges-integration-and-run-memory.md](references/bridges-integration-and-run-memory.md).

Carry a compact run context across bridges: source ledger, source classes, fragments, claims, contradictions, unknowns, rejected alternatives, hard gates, scoring assumptions, decision, falsifiers, entities, lock-in map, template/workflow versions and open validation questions.

A downstream template may reuse prior evidence but must not launder it into fresh truth. Revalidate time-sensitive claims. Preserve `fact | inference | hypothesis | recommendation | unknown` and source lineage.

## Lock-in and sovereignty

Treat lock-in as a **location and control-point question**, not merely a severity score. Map material dependencies across technical stack and value chain, then identify switching asset/cost, portability mechanism, contractual/licensing constraint, exit path and medium/long-term sovereignty implication.

## Evidence and prose rules

- Lead with the decision, result or central thesis.
- Prefer direct affirmative formulations.
- Prefer bullets for enumerations of 3+ items and tables for structured comparisons.
- Label `fact | inference | hypothesis | recommendation | unknown`.
- Side stories never create new proof.
- Preserve lineage from source → fragment → claim → section → bridge.
- Apply hard gates before scoring or narrative ranking.
- Keep seller recommendations separate from buyer/account reality until the explicit fit stage.
- Prefer the smallest reversible validation step over speculative implementation depth.

## Side stories

Preferred kinds: `dezoom | method | false_lead | comparator | analytical_focus | callback`. Every side story has a stable ID, source claim IDs, purpose, insertion anchor and return-to anchor.

## Specialized templates

### BENCHMARKING
Compare 2+ options against identical criteria. Reconstruct the true problem before scoring, normalize unlike categories, apply hard gates, show uncertainty/sensitivity and end with falsifiers. Technical, product and business benchmarks share the evidence pipeline but use domain-specific criteria.

### BUY_SIDE_GAP_ANALYSIS
Evaluate adopt/replace/complement/partner from the buyer baseline, target state, hard gates, migration/coexistence and economics before feature richness.

### DIAGNOSTIC_RECO_SELL_SIDE
Advise a vendor/founder on positioning, ICP, proof, packaging, pricing, competition and sales motion. Keep diagnosis separate from recommendations.

### OPPORTUNITY_NOTE_ICP
Decide whether a concrete target/partner is credible. Keep target truth and product truth independent until fit; end with a reversible validation step.

### INTEGRATION_NOTE
Use when the next decision is how products, companies or internal capabilities should combine. Evaluate three lenses — **technical, product, business** — and decide `BUILD | BUY | PARTNER | COEXIST | DEFER`. Explicitly map complementarity, overlap, operating ownership, lock-in location, sovereignty, economics, GTM/customer ownership and exit path.

## Feedback / dreaming

Read [references/dreaming-self-healing.md](references/dreaming-self-healing.md). Every normal run performs the lightweight check. An explicit `FEEDBACK_DREAMING` run deepens it across outputs and feedback.

A reusable change requires evidence from a real run, separation of case-specific vs reusable deltas, a candidate patch, regression coverage and human approval. Never silently mutate the canonical template catalog.
