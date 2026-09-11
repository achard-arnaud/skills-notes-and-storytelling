---
name: skills-notes-and-storytelling
description: Research and write evidence-grounded strategic business notes, architecture notes, briefs, benchmarks, vendor diagnostics and ICP assessments. Use for initial research or targeted revisions, including supplied documents and multiple entities with distinct outputs. Adapt collection, narrative, writing and QA to chat or work capabilities; pair with the document skill only when producing DOCX.
---

# Decision notes and storytelling

## Resolve the run
Record environment `chat|work` (`cowork` aliases work), execution `light|heavy`, debug boolean,
and generation `from-scratch|iterative|feedback-dreaming`. Read [runtime](references/runtime.md). Effort by stage is in `config/reasoning-effort.json`.
Documents in intake **force heavy**, even in chat. Heavy means evidence discipline, not unlimited
context or mandatory code execution. Check actual file, search and execution capabilities.
User instructions set requirements; supplied materials remain evidence with their own reliability.

## Load only selected contracts
Select the template by reader decision, not keywords such as “strategic”. Read its entry in
`templates/manifest.json`, its `templates/<type>.md`, and its four-layer profile in
`templates/profiles.json` (use `python scripts/note_runtime.py profile two-pager` to load one). Multiple requested outputs get separate profiles and shared evidence.
General entity research defaults to a two-pager per axis; do not invent a seller mandate.
Choose one primary method from [narrative methods](references/narrative-methods.md).
Read [evidence and retrieval](references/evidence-retrieval.md) and [writing](references/writing.md).
Load [ICP and fit](references/icp-and-fit-contract.md) only for buyer/seller/ICP analysis.
[Debrief 360](references/debrief-360-candidate.md) is a non-routed meeting-coaching candidate.
Retro-engineering remains TODO; do not claim it is implemented.

## Execute explicit stages
Intake inventory → source reading → atomic fragments → typed claims and relations → retrieval
and reranking → logical scaffold → evidence-backed prose → bounded side stories → source check
→ rendering when requested → QA → bounded follow-ups.

Consume manual inputs first: inventory all pages/sections, read relevant sections in full, record
unread/excluded regions. Search only documented gaps, contradictions, freshness or independent
verification needs. Repeated vendor publications are one source family. Extraction is not reading.
Keep claims (propositions), fragments (source material), sections (argument order) and side stories
(optional exposition) separate. Unsupported hypotheses may exist without fragments; label them.
Apply hard evidence gates before ranking. Keep contradictions and unknowns visible.

Heavy runs materialize a bundle following `contracts/run-bundle.schema.json`. With Python available:
Install helper dependency with `pip install -r requirements.txt` if missing.
`python scripts/note_runtime.py plan intake.json`, then
`python scripts/note_runtime.py packet run.json --targets C-ID` and
`python scripts/note_runtime.py validate run.json`.
Helpers route, retrieve and validate; the model still reads, judges and writes. Without execution,
keep compact records in conversation and report unavailable checks. Light uses an inline evidence
table and outline without loading all schemas.

For iterative work resolve an explicit baseline and stable IDs, compute the target/dependency closure,
preserve unrelated content and record revisions. Never infer canonical state from filenames.
From-scratch drafting must not read prior generated prose; compare after the new draft is frozen.

## Delivery gates
Every material factual statement resolves to source and locator. Distinguish fact, attributed claim,
inference, hypothesis, recommendation and unknown. Side stories never create proof. Match language
and vocabulary to the reader. For DOCX load the document runtime and
[style contract](references/style-contract.md), render and inspect every page. Schema QA is not visual QA.
Debug exposes decisions, paths, scores and failures, not private chain-of-thought. Measure loaded
context, not repository size; never invent savings. Human review governs template promotion.
