---
name: decision-notes-and-storytelling
description: Create, revise, or industrialize evidence-grounded .doc/.docx business notes, architecture notes, one-pagers, two-pagers, benchmarks, buy-side gap analyses, sell-side diagnostic/recommendation notes, and ICP opportunity notes. Own research-to-claims-to-storytelling, generation mode, output language, template selection, ICP/fit contracts, side-story routing, sourcing gates, next-step nudging, and human-reviewed template learning. Always pair with the runtime DOCX creation/editing skill for rendering and visual QA.
---

# Decision Notes & Storytelling

## Scope

This skill is the governed document OS for **analysis and decision notes**. It owns content architecture, evidence lineage, narrative composition, template contracts, output-language continuity and learning loops. The runtime DOCX skill owns Word generation, rendering and file-level QA.

Use this skill whenever the requested output is a `.doc` or `.docx` note, brief, comparison, architecture memo, one-pager, two-pager, benchmark, buy-side analysis, sell-side diagnostic or ICP opportunity note.

## Run context and language

Create a run context conforming to `contracts/run-context.schema.json`.

Set `output_language` before research starts:
1. explicit user language instruction wins;
2. otherwise use the **majority natural language of the conversation at the moment the skill is invoked**;
3. ignore URLs, code, quoted source blocks, product names and isolated technical terms when determining the majority language.

Carry the same `output_language` through:
`run context → scaffold → output specification → drafting → language QA → DOCX proofreading`.

Do not silently switch languages between sections. Preserve product names, standards and technical identifiers where translation would reduce precision. Prefer a natural equivalent in the output language for avoidable jargon.

## Generation mode

Select one mode from `GenerationMode` before selecting the output template. Read [references/modes.md](references/modes.md).

- `FROM_SCRATCH` — no trusted canonical draft exists; execute the complete evidence → claims → scaffold → draft pipeline.
- `ITERATIVE` — a canonical prior output exists; establish the accepted baseline, compute the delta, update only the required evidence/content/layout scope, then regression-check preserved material.
- `FEEDBACK_DREAMING` — post-run improvement loop; convert repeated feedback and QA defects into candidate changes to contracts/templates with explicit human promotion.
- `RETRO_ENGINEERING` — **TODO / non-production**.

## Template enum

Select exactly one value from `OutputTemplateType`:

- `ARCHITECTURE_NOTE`
- `ONE_PAGER`
- `TWO_PAGER`
- `BENCHMARKING`
- `BUY_SIDE_GAP_ANALYSIS`
- `DIAGNOSTIC_RECO_SELL_SIDE`
- `OPPORTUNITY_NOTE_ICP`
- `ACTION_PLAN` — **TODO / non-production**

Every template is versioned in `templates/manifest.json` with its QA fixture and workflow compatibility.

## Analysis/action boundary

The current production templates are **analysis templates**. They may end with:
- a decision;
- conditions and falsifiers;
- open questions;
- discussion options;
- a bounded next validation;
- a request for a demo, workshop or additional evidence.

They do **not** generate an implementation roadmap, 30/60/90-day plan, task backlog or operational action plan by default.

An action plan is a **post-analysis derivative artifact**. The future `ACTION_PLAN` template is documented as TODO and remains blocked from production routing until explicitly promoted.

## Canonical workflow

Follow [references/workflow.md](references/workflow.md).

1. **Run context** — mode, output language, decision, audience, scope.
2. **Research** — collect source evidence; separate account/company reality, product truth and market alternatives.
3. **Fragments** — convert evidence into atomic, source-addressable fragments.
4. **Claims graph light** — create claim nodes and typed edges.
5. **Rerank** — prioritize decision relevance, evidence strength, explanatory value, novelty and audience fit.
6. **Scaffold** — build a section skeleton from ranked claims before drafting.
7. **Fill** — draft only from fragments attached to claims; preserve evidence status and output language.
8. **Side stories** — insert bounded detours after the core decision spine is coherent.
9. **Layout** — map content to the selected template; prefer bullets and comparison tables.
10. **Fact-check & source** — verify every material claim and source line.
11. **Language QA** — anti-jargon + linguistic-coherence check using the run-context language.
12. **DOCX QA** — invoke the runtime DOCX skill; render every page; inspect and iterate.
13. **Next-step nudging** — expose bounded follow-ups or the next analytic artifact; do not synthesize an action plan unless that template is explicitly available and requested.
14. **Feedback/dreaming** — create candidate reusable changes; human review decides promotion.

## Evidence and ICP rules

- Lead with the decision, result or central thesis.
- Label `fact | inference | hypothesis | recommendation | unknown`.
- Side stories never create new proof.
- Preserve source lineage from fragment → claim → section → side story.
- Apply hard evidence gates before scoring.
- Keep account/buyer reality separate from product/seller truth until the explicit fit stage.
- When ICP is material, use [references/icp-and-fit-contract.md](references/icp-and-fit-contract.md): seven dimensions, anti-ICP, `PASS | OPEN | FAIL` hard gates, sponsor/terrain/veto lanes and explicit falsifiers.

## Prose and visual rules

Apply [references/style-contract.md](references/style-contract.md).

Key gates:
- direct affirmative formulations;
- bullets for enumerations of 3+ items;
- tables for structured comparisons;
- body text target 10.5–11 pt; hard minimum 9 pt;
- no clipping, overlap or out-of-bounds content;
- Mermaid source remains canonical and rendered diagrams are embedded as images;
- if fitting a Mermaid would reduce either dimension by more than 30%, transpose the same semantic graph and rerender;
- every final DOCX passes language lint + render → page-by-page inspection → correction → rerender.

## Specialized templates

### BUY_SIDE_GAP_ANALYSIS
Start from buyer baseline, hard gates and migration reality before feature richness.

### DIAGNOSTIC_RECO_SELL_SIDE
Advise a vendor/founder on positioning, ICP, proof, packaging, pricing, competitive threats and commercial motion. The note ends with prioritised recommendations, validation questions and discussion options. Operational sequencing belongs to the future action-plan template.

### OPPORTUNITY_NOTE_ICP
Decide whether a concrete target account, partner or internal platform is a plausible opportunity. Build target truth and product truth independently, apply ICP/hard gates, map gaps to outcomes, compare alternatives and end with a reversible validation or discussion step.

### ACTION_PLAN
TODO. Derive implementation sequencing only **after** a validated analysis artifact exists.

## Feedback / dreaming

Read [references/dreaming-self-healing.md](references/dreaming-self-healing.md). A reusable change requires:
- at least one real output;
- QA findings or explicit user feedback;
- separation of case-specific vs reusable deltas;
- a candidate contract/template/mode patch;
- a version-linked regression fixture;
- human approval before promotion.

Never silently mutate the canonical template after a single run.
