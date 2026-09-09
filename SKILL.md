---
name: decision-notes-and-storytelling
description: Create, revise, or industrialize evidence-grounded .doc/.docx business notes, architecture notes, one-pagers, two-pagers, benchmarks, and buy-side gap analyses. Own the research-to-claims-to-storytelling workflow, template selection, side-story routing, sourcing gates, next-step nudging, and human-reviewed template learning. Always pair with the runtime DOCX creation/editing skill for rendering and visual QA.
---

# Decision Notes & Storytelling

## Scope

This skill replaces the narrow `two-pagers-nice` concept with one governed document system. It owns **content architecture and narrative composition**. The runtime DOCX skill owns **Word generation, rendering, and file-level QA**.

Use this skill whenever the requested output is a `.doc` or `.docx` note, brief, comparison, architecture memo, one-pager, two-pager, benchmark, or buy-side analysis.

## Template enum

Select exactly one value from `OutputTemplateType` in `src/template_types.py`:

- `ARCHITECTURE_NOTE`
- `ONE_PAGER`
- `TWO_PAGER`
- `BENCHMARKING`
- `BUY_SIDE_GAP_ANALYSIS`

A new family starts as `CANDIDATE` in the dreaming loop and requires human approval before catalog promotion.

## Canonical workflow

Follow [references/workflow.md](references/workflow.md). Do not collapse stages.

1. **Research** — collect source evidence; separate company/account truth from product truth.
2. **Fragments** — convert evidence into atomic, source-addressable fragments.
3. **Claims graph light** — create claim nodes and typed edges without overbuilding a knowledge graph.
4. **Rerank** — score decision relevance, evidence strength, novelty, explanatory value and audience fit.
5. **Scaffold** — build a section skeleton from ranked claims before drafting prose.
6. **Fill** — draft only from fragments attached to claims; preserve evidence status.
7. **Side stories** — insert bounded detours after the core causal spine is coherent.
8. **Layout** — map content to the selected template; prefer bullets and comparison tables.
9. **Fact-check & source** — verify every material claim and source line.
10. **DOCX QA** — invoke the DOCX skill; render every page; visually inspect and iterate.
11. **Next-step nudging** — expose bounded follow-ups, open questions and highest-value deeper dives.
12. **Dreaming** — if the run created a genuinely new document pattern, create a candidate template update; human review decides promotion.

## Evidence and prose rules

- Lead with the decision, result, or central thesis.
- Prefer direct affirmative formulations.
- Use contrast only when the contrast itself carries analytical value.
- Prefer bullets for enumerations of 3+ items.
- Prefer tables for structured comparisons.
- Label `fact | inference | hypothesis | recommendation | unknown`.
- Side stories never create new proof.
- Preserve source lineage from fragment → claim → section → side story.
- A failed evidence gate cannot be averaged away by narrative confidence.

## Visual rules

Apply [references/style-contract.md](references/style-contract.md).

Key gates:
- body text target 10.5–11 pt; hard minimum 9 pt;
- no clipping, overlap or out-of-bounds content;
- tables use column widths proportional to semantic density;
- comparisons default to tables;
- Mermaid diagrams are rendered to images;
- if fitting a Mermaid to page width would reduce either dimension by more than **30%**, rerun the same logic in a vertical orientation;
- every final DOCX passes render → page-by-page inspection → correction → rerender.

## Side stories

Use [references/side-stories-retro.md](references/side-stories-retro.md). Preferred business-note kinds:

- `dezoom` — broader operating/model implication;
- `method` — method or evidence caveat;
- `false_lead` — tempting analogy rejected with reasons;
- `comparator` — bounded comparison;
- `analytical_focus` — deeper mechanism or conjecture;
- `callback` — return to a previously introduced decision thread.

Every side story has a stable ID, source claim IDs, purpose, insertion anchor and return-to anchor.

## Buy-side gap analysis

Use `BUY_SIDE_GAP_ANALYSIS` when the reader is evaluating whether to adopt, replace, complement, or partner with a product/vendor.

Required sections:
1. decision and target operating context;
2. incumbent / alternative baseline;
3. capability and operating-model comparison;
4. migration/replacement feasibility;
5. hard gates and missing evidence;
6. commercial model and TCO logic;
7. implementation and change risks;
8. prioritized gap matrix;
9. recommendation and reversible next step.

Use side stories to distinguish:
- comparator: nearest credible alternative;
- false_lead: apparent equivalence that breaks under implementation;
- analytical_focus: economic or architectural mechanism;
- dezoom: portfolio/operating-model consequence;
- method: evidence and scoring limits.

## Dreaming / self-healing

Read [references/dreaming-self-healing.md](references/dreaming-self-healing.md). A new template can be learned only after:
- at least one real output exists;
- QA findings are recorded;
- reusable deltas are separated from case-specific content;
- a candidate contract/template change is proposed;
- a human explicitly approves promotion.

Never silently mutate the canonical template after a single run.
