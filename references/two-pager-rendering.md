# Two-pager rendering and flexible content binding

## Separation of concerns

- Business analysis lives in source-addressable claims and the business content contract.
- Page composition is bound from JSON in the caller's chosen module order.
- HTML supplies semantic structure; CSS supplies layout and design tokens.
- Theme JSON owns typography, spacing, page geometry and palette reference.
- PNG/PDF output is downstream evidence; it never replaces the content source.

The reusable implementation is in renderers/two_pager_nice. It transfers the internal two-pager-nice HTML/CSS print system without carrying its WaveMaker example or business facts.

## Flexible binding

Use the existing page contract as a reusable layout with business meaning supplied by the case data, not as a fixed narrative questionnaire. The two-page frame and renderer's outer slot order are stable; within them, bind only evidence-backed modules and vary labels, payloads, card types and column order as supported by the JSON contract.

Typical page 1 slots: headline/gate, signal cards, value-creation flow, company / market / operating-model columns, strategic newsflow, SWOT/TOWS and source/unknown note.

Typical page 2 slots: strategy-to-execution flow, product/use-case modules, competition/moat, execution evidence, decision takeaways and next-step block.

Optional content inside cards and lists may be omitted or re-ordered when immaterial or unavailable. The current renderer still expects its outer frame (header/gate, three top cards, flow, lower layout and footer); it does not yet collapse whole outer blocks. Map the distinct prior-24-month newsflow to a dedicated lower column/card, with its own title and dated items. A missing metric, leadership profile, funding event or customer split should be omitted from payloads, not filled with an invented placeholder or forced SWOT. Keep the prior-24-month newsflow container distinct when the time-bound review was requested; if no material event is evidenced, state that coverage found no qualifying signal and define source/cutoff.

The renderer's current structural contract uses a document object (title, language, theme) and two page objects. Each page binds a kicker, subtitle, decision gate, three top cards, one flow, a page layout and a closing strip. The lower layout can be three columns or due diligence. Reuse those blocks for business meaning through labels and payload; do not hard-code company, employer, product or candidate facts into templates. Adding an independently collapsible block, a new layout family or a native diagram component requires an explicit schema/template/CSS change and a regression fixture.

## CSS and design tokens

Change tokens in themes/business-corporate.json or palettes/business-corporate.json. Keep semantic colors stable: green for verified evidence, orange for company claims/inference, red for unknown/contradiction. Never convey evidence status by color alone.

The shared CSS keeps A4 landscape, page/card grid, hierarchy, print rules, card padding and type floors independent of case content. Change layout classes only when the same improvement benefits multiple cases. Do not shrink text or use absolute placement to fix a one-off overflow; shorten content, alter grid ratios or add a layout variant with an explicit contract.

Minimums: 9 pt body text and padding, 11 pt preferred body text, no clipping/overlap/out-of-page content, one or two pages as requested, tables no wider than five columns. Business modules may use shorter labels but may not weaken evidence distinction.

## Schema Flow Master harvest

Choose one diagram only when it resolves a structure question. Use organization chart for evidenced reporting lines; C4 context for ecosystem boundaries; a simple hierarchy/table for product segmentation; a flow for value creation or execution. Store editable Mermaid separately from any rendered image. The current renderer has no native Mermaid slot: map a diagram to a supported card/list or add a tested diagram block before embedding it. Keep unknown connections dashed/labeled as hypotheses; do not claim renderer support for a diagram family until tested in the target environment.

## Commands and verification

From repository root:

- Build: python renderers/two_pager_nice/scripts/cli.py build <content.json> --output build/two-pager --name artifact
- QA: python renderers/two_pager_nice/scripts/cli.py qa build/two-pager/artifact.html --report build/two-pager/artifact_qa.json --screenshots build/two-pager/qa
- All: python renderers/two_pager_nice/scripts/cli.py all <content.json> --output build/two-pager --name artifact

Chromium is the reference renderer. Verify its availability, then render; inspect both page images at 100% and 150%; check PDF page count separately. If a supported runtime cannot launch Chromium, an equivalent browser may be used and identified in the receipt; do not report Chromium QA as passed. The current repository CI covers contracts/manifests, not live PDF visual QA.
