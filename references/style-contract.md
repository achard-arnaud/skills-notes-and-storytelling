# Visual and prose contract

## Prose

Follow the [shared editorial and research quality contract](editorial-and-research-quality.md).

- State the analytical point directly and affirmatively; give each sentence one job.
- Use short paragraphs of 2–5 sentences, bullets for lists of 3+ items, and tables for comparisons.
- Label facts, inferences, hypotheses, unknowns and recommendations explicitly.
- Replace compressed contrasts and disclaimers with separate evidence-based findings and their business meaning.
- Put analytical caveats and implications in the body. Keep footnotes and container endings for concise source or status legends.
- Run a dedicated semantic repetition review across every content container before delivery.

Example:

> This score is a decision heuristic. It prioritizes evidence for comparison.

## Tables

- Default comparison device.
- Prefer 3 columns; hard maximum 5 unless a landscape template explicitly allows more.
- Width allocation follows semantic density, not equal-width defaults.
- Give the longest explanatory column the most width.
- Keep labels compact and move nuance into the explanatory column.
- Repeat header rows across page breaks.
- Avoid split rows when possible.
- If a table becomes prose-heavy, split it into two tables or add a short analytical paragraph.

## Mermaid diagrams

Mermaid source is canonical; the rendered image is embedded into DOCX.

For each figure record:
- source Mermaid text;
- native render width/height;
- target page width/height;
- scale factor;
- orientation decision;
- visual QA result.

### 30% transposition gate

If the diagram must be reduced below 70% of native size to fit page width or available vertical space:
1. preserve the same nodes, edges and semantics;
2. transpose orientation (typically `LR → TB` or `TB → LR`);
3. rerender;
4. choose the orientation requiring the least reduction;
5. inspect labels and edge overlaps at 100%.

Never accept tiny text merely to preserve the original orientation.

## DOCX

Always pair this skill with the runtime DOCX skill.

Hard gates:
- body text >= 9 pt;
- diagram labels readable at 100%;
- no overlap, clipping, orphaned headings, broken tables or hidden content;
- page count coherent with template family;
- sources remain readable;
- section spacing is consistent;
- all final pages inspected after the last change.

## Template geometry

- Architecture note: portrait, prose + diagrams + analytical side stories.
- One-pager: landscape or portrait depending decision density; one dominant message.
- Two-pager: A4 landscape by default; dense but readable.
- Benchmarking: landscape preferred; comparison tables dominate.
- Buy-side gap analysis: portrait or landscape according to matrix density; executive recommendation on page 1.
