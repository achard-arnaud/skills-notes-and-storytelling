# Visual, prose and language contract

## Output language

`output_language` is an E2E run variable.

Default:
- explicit user instruction when present;
- otherwise majority natural language of the conversation at skill invocation.

Ignore URLs, code, quoted sources, product names and isolated technical identifiers when detecting the majority language.

The same value must be present in the run context and output specification and must be checked again during final proofreading.

## Linguistic coherence and anti-jargon

Prefer:
- natural vocabulary in the selected language;
- direct affirmative statements;
- short paragraphs of 2–5 sentences;
- bullets for lists of 3+ items;
- tables for comparisons;
- explicit labels for facts, hypotheses, unknowns and recommendations.

Use foreign-language terms only when at least one condition is true:
- proper product, protocol, standard or code identifier;
- widely accepted domain acronym;
- source terminology whose translation would reduce precision;
- no concise natural equivalent exists.

When a foreign technical term is useful but avoidable ambiguity remains, define it on first use in the output language.

Examples for French:
- prefer `adaptation`, `capitalisation` or `inspiration` to `harvest`;
- prefer `rattrapage` to `catch-up`;
- prefer `accélération` to `speed-up`;
- prefer `critère bloquant` to `hard gate` in reader-facing prose;
- retain `ICP`, `SLA`, `API`, `MCP`, product names and code identifiers when useful.

Run `python scripts/language_lint.py --language <output_language> --docx <artifact.docx>` before delivery. Review flagged passages manually: the linter is a guardrail, not a semantic authority.

## Direct prose

Rewrite avoidable opposition patterns.

Instead of:
> This is not an objective measure, but a decision heuristic.

Prefer:
> This score is a decision heuristic. It prioritizes evidence for comparison.

Use a negative construction only when the negation itself prevents a material misunderstanding.

## Analysis/action boundary

Analytical templates may recommend a direction and the next validation. They should not silently turn into implementation roadmaps.

Avoid inside analytical templates:
- 30/60/90-day sequencing;
- detailed task backlogs;
- project calendars;
- owner-by-owner execution plans.

Route those artifacts to the future `action-plan` template after the analysis is accepted.

## Tables

- Default comparison device.
- Prefer 3 columns; hard maximum 5 unless a landscape template explicitly allows more.
- Width allocation follows semantic density.
- Give the longest explanatory column the most width.
- Repeat header rows across page breaks.
- Avoid split rows when possible.
- If a table becomes prose-heavy, split it or add a short analytical paragraph.

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

If the diagram must be reduced below 70% of native size:
1. preserve nodes, edges and semantics;
2. transpose orientation;
3. rerender;
4. choose the orientation requiring the least reduction;
5. inspect labels and edge overlaps at 100%.

## DOCX

Always pair this skill with the runtime DOCX skill.

Hard gates:
- body text >= 9 pt;
- diagram labels readable at 100%;
- no overlap, clipping, orphaned headings, broken tables or hidden content;
- page count coherent with template family;
- sources readable;
- section spacing consistent;
- language lint reviewed;
- all final pages inspected after the last change.
