---
name: decision-notes-and-storytelling
description: Create, revise, or industrialize evidence-grounded decision notes, architecture notes, one-pagers, two-pagers, benchmarks, buy-side gap analyses, sell-side diagnostic/recommendation notes, ICP opportunity notes and integration notes. Own research-to-claims-to-storytelling, evidence lineage, template bridges, counter-perspective QA, lock-in mapping, next-step nudging and the governed tiered dreaming loop. Pair with the runtime DOCX skill when a Word artifact is requested.
---

# Decision Notes & Storytelling

## Scope

This skill is a governed decision-note OS. It owns **context reconstruction, research, evidence lineage, claims, decision architecture, narrative composition, template routing, cross-template bridges, counter-perspective QA and learning loops**. Rendering is a downstream concern.

Use the lightest output that closes the decision. Do not create a larger report when a one-pager, two-pager or bounded integration decision is sufficient.

## Runtime artifacts and repository hygiene

Runs are execution outputs, not source assets. Never store a live run, generated note, generated PDF/DOCX/PPTX, temporary export, screenshot, customer-specific deliverable or other run artifact in this repository. Deliver them through the conversation artifact mechanism, CI artifacts, or another explicit artifact store outside the source tree.

When a run reveals a reusable improvement, promote only the generalized rule, template, fixture, contract or documentation patch required to reproduce the improvement. Do not commit the run itself. Curated examples are allowed only when they are stable regression fixtures or intentionally maintained minimal samples; they must not be raw run dumps.

## Generation mode

Select one mode from `GenerationMode` before the output template. Read [references/modes.md](references/modes.md).

- `FROM_SCRATCH` — no trusted canonical draft exists.
- `ITERATIVE` — preserve a canonical baseline and update only the declared factual/content scope before full regression QA. **Content-preservation gate:** an iterative run must ledger material claims/sections from the canonical baseline and may remove them only when they are stale, contradicted, explicitly out of scope or replaced by stronger evidence. Compression alone is not a valid reason to lose decision value.
- `FEEDBACK_DREAMING` — explicit system-improvement run over prior outputs/feedback.
- `RETRO_ENGINEERING` — **TODO / non-production**.

`FEEDBACK_DREAMING` remains an explicit mode for deep improvement work, but a lightweight dreaming check is mandatory at the end of every normal run. The user does not need to request it. `NO_REUSABLE_DELTA` is valid; canonical behavior never changes without human approval.

## Analysis dimension

After generation mode and before template scaffolding, select one primary `analysis_dimension`:

- `technical` — architecture, runtime, data flow, security, scalability, observability, infrastructure, technical economics;
- `product` — users/jobs, capabilities, use cases, workflow/adoption, product differentiation, packaging and product operating model;
- `business` — enterprise strategy, organizational design, transformation, governance, capability building, client model, operating model and economics.

The three dimensions share the evidence pipeline but **do not share the same decision spine**. A note may use secondary lenses, but the primary dimension governs research reranking, scaffold, side stories, counter-perspective and visual architecture. Do not default a company AI-strategy request to a technical architecture merely because AI technology is present.

For `ARCHITECTURE_NOTE`, read the dimension-specific contract in [templates/architecture-note.md](templates/architecture-note.md). For other templates, use the same dimension distinction when relevant until their contracts are explicitly generalized.

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

1. **Context & decision framing** — reconstruct the actual problem, audience, time horizon and constraints before accepting the supplied framing; select primary analysis dimension.
2. **Research** — collect evidence; separate account/company reality, product truth, market alternatives and dependencies. Rerank source classes to the selected dimension.
3. **Fragments** — convert evidence into atomic source-addressable fragments.
4. **Claims graph light** — create claims, contradictions, unknowns and typed edges.
5. **Rerank** — prioritize decision relevance, evidence strength, explanatory value, novelty, audience fit and dimension fit.
6. **Scaffold** — build the dimension-specific decision spine before drafting.
7. **Fill** — draft only from attached fragments; preserve evidence status and, in `ITERATIVE`, the canonical content ledger.
8. **Side stories** — add bounded analytical detours only after the core spine is coherent.
9. **Fact-check & source** — verify every material claim and source line.
10. **Counter-perspective QA** — attack the material conclusion with the strongest credible alternative explanation, hidden hard gate, lock-in/control shift or failure path. Do not manufacture artificial balance.
11. **Layout / render QA** — when an artifact is requested, map to the template and run the appropriate rendering QA. Reader-facing DOCX diagrams must be rendered images, not source markup.
12. **Reader/decision QA** — verify that the intended reader can see decision, uncertainty, falsifier and next step without reconstructing the analysis.
13. **Bridge / nudging** — evaluate the smallest evidence-backed next decision and route it to another template when useful. Zero bridge is valid.
14. **Dreaming tier selection** — select Tier 0–3 based on the strength and reusability of the run signal.
15. **Dreaming** — inspect the run for reusable QA/workflow/template improvements; propose, never silently promote.

## Review lenses

Keep three review lenses distinct:

- **Conformance review** — contracts, evidence rules, scope, sourcing, template and rendering constraints.
- **Counter-perspective review** — strongest credible challenge to the reasoning or recommendation.
- **Reader/decision review** — clarity, decision usefulness, trade-offs, uncertainty, falsifier and next action.

Do not let stylistic preferences masquerade as factual or decision defects.

## Evidence memory and bridges

Read [references/bridges-integration-and-run-memory.md](references/bridges-integration-and-run-memory.md).

Carry a compact run context across bridges: source ledger, source classes, fragments, claims, contradictions, unknowns, rejected alternatives, hard gates, scoring assumptions, decision, falsifiers, entities, lock-in map, template/workflow versions, analysis dimension, open validation questions, counter-perspective verdict and dreaming tier when material.

A downstream template may reuse prior evidence but must not launder it into fresh truth. Revalidate time-sensitive claims. Preserve `fact | inference | hypothesis | recommendation | unknown` and source lineage.

## Lock-in and sovereignty

Treat lock-in as a **location and control-point question**, not merely a severity score. Map material dependencies across technical stack, value chain and human/process control points, then identify switching asset/cost, portability mechanism, contractual/licensing constraint, exit path and medium/long-term sovereignty implication.

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
- Stop broad research when remaining uncertainty can only be resolved by a bounded experiment, implementation, procurement, migration rehearsal or customer discovery.

## Side stories

Preferred kinds: `dezoom | method | false_lead | comparator | analytical_focus | callback`. Every side story has a stable ID, source claim IDs, purpose, insertion anchor and return-to anchor.

## Specialized templates

### ARCHITECTURE_NOTE
Use for deep technical, product or business architecture when a system/capability model and its implications must be reconstructed. The selected `analysis_dimension` controls the sequence and diagram family. A business architecture note treats organization, governance, capability building, client model and transformation as architecture; it must not be forced into a software-component narrative. Read [templates/architecture-note.md](templates/architecture-note.md).

### BENCHMARKING
Compare 2+ options against identical criteria. Reconstruct the true problem before scoring, normalize unlike categories, apply hard gates, show uncertainty/sensitivity and end with falsifiers. Technical, product and business benchmarks share the evidence pipeline but use domain-specific criteria. Close explicitly as `CLOSED | CLOSED_WITH_CHALLENGE_GATE | REOPEN_TARGETED`; do not keep adding peers after closure unless a named hard gate requires it.

### BUY_SIDE_GAP_ANALYSIS
Evaluate adopt/replace/complement/partner from the buyer baseline, target state, hard gates, migration/coexistence and economics before feature richness.

### DIAGNOSTIC_RECO_SELL_SIDE
Advise a vendor/founder on positioning, ICP, proof, packaging, pricing, competition and sales motion. Keep diagnosis separate from recommendations.

### OPPORTUNITY_NOTE_ICP
Decide whether a concrete target/partner is credible. Keep target truth and product truth independent until fit; end with a reversible validation step.

### INTEGRATION_NOTE
Use when the next decision is how products, companies or internal capabilities should combine. Evaluate three lenses — **technical, product, business** — and decide `BUILD | BUY | PARTNER | COEXIST | DEFER`. Distinguish strategic decision from integration posture when useful. Explicitly map complementarity, overlap, operating ownership, lock-in location, sovereignty, economics, GTM/customer ownership, process/habit lock-in and exit path. Every positive recommendation requires a bounded pilot and a counter-perspective verdict.

## Counter-perspective / red-team

Read [references/workflow.md](references/workflow.md) and [references/dreaming-self-healing.md](references/dreaming-self-healing.md).

Use red-team as bounded falsification, not as theatrical opposition. Attack the proposition most capable of reversing the decision. Preferred lenses include wrong framing, category mismatch, missing baseline, evidence asymmetry, hidden hard gate, incentive/ownership conflict, staleness, lock-in/control migration, operating burden, reversibility and user/process adoption failure.

Valid outcomes:
- `SURVIVES_RED_TEAM`;
- `SURVIVES_WITH_NARROWING`;
- `PIVOT_REQUIRED`;
- `REOPEN_TARGETED`.

## Feedback / dreaming

Read [references/dreaming-self-healing.md](references/dreaming-self-healing.md). Every normal run performs the lightweight check; higher tiers deepen the loopback when the signal is structural.

Tiering:
- Tier 0 — `NO_REUSABLE_DELTA`;
- Tier 1 — mandatory lightweight run check;
- Tier 2 — targeted red-team loopback for material/structural uncertainty;
- Tier 3 — explicit `FEEDBACK_DREAMING` multi-run system review.

A reusable change requires evidence from a real run, separation of case-specific vs reusable deltas, a candidate patch, regression coverage and human approval. Never silently mutate the canonical template catalog.
