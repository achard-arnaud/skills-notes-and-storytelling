# Visual and prose contract

## Prose

Prefer:
- direct affirmative statements;
- short paragraphs of 2–5 sentences;
- bullets for lists of 3+ items;
- tables for comparisons;
- explicit labels for facts, hypotheses, unknowns and recommendations.

Rewrite avoidable opposition patterns.

Instead of:
> This is not an objective measure, but a decision heuristic.

Prefer:
> This score is a decision heuristic. It prioritizes evidence for comparison.

Write direct, affirmative, concrete sentences. Express legal boundaries through their precise scope and conditions. Preserve exact quotations and necessary legal prohibitions. Split compressed rhetorical comparisons into separate substantive statements.

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

## Reader-facing analysis and method records

Use the body of each container for the substantive analysis. Keep execution accounting, reversibility of document production, QA outcomes and workflow commentary in run-method records. Explain industrial reversibility in the body when contracts, transferable assets or switching costs are material.

Reserve footers and container endings for page numbers, source references and extremely discreet illustrative legends defining symbols, units or figure scope. Place analytical conclusions in the body. Keep method commentary and self-evaluation in the sidecar records.

## Mandatory cross-container repetition review

After drafting and after the final render, map each material proposition to its primary location across introduction, diagram, table, prose, box, conclusion and footer. A repeated proposition must add a distinct mechanism, discriminating example or material exception. Keep the opening synthesis brief and let the body develop its evidence. Merge semantic duplicates and use compact cross-references for necessary reminders. Preserve legally material conditions.

Record proposition, locations, contribution and edit in the run’s editorial-review record. Check prose-versus-diagram, prose-versus-table and opening-versus-conclusion redundancy. Run a final scan for avoidable negative constructions and rhetorical oppositions in reader-facing prose. Rewrite inherited exclusions as positive qualification criteria while preserving exact quotations and legal prohibitions. Inspect every footer and container ending. Each container contributes identifiable information.
