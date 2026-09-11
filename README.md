# Skills Notes & Storytelling

Reusable skill for evidence-grounded decision notes, architecture notes, one-pagers, two-pagers, benchmarks, buy-side analyses, sell-side diagnostics and ICP opportunity notes. Runs natively in both `chat` and `cowork` execution modes (see [references/execution-modes.md](references/execution-modes.md)).

## Canonical skill
- **Skill:** `skills-notes-and-storytelling`
- **Entry point:** [SKILL.md](SKILL.md)
- **Template enum + generation modes:** [src/template_types.py](src/template_types.py)
- **Workflow:** [references/workflow.md](references/workflow.md)
- **Modes:** [references/modes.md](references/modes.md)
- **Versioning:** [references/versioning-and-lifecycle.md](references/versioning-and-lifecycle.md)
- **Visual contract:** [references/style-contract.md](references/style-contract.md)
- **Side-story retrodocumentation:** [references/side-stories-retro.md](references/side-stories-retro.md)

## Generation modes

| Mode | Status | Purpose |
|---|---|---|
| `from-scratch` | validated | Full evidence → claims → scaffold → document run |
| `iterative` | validated | Delta-first update against a canonical baseline + full regression |
| `feedback-dreaming` | validated | Convert human feedback / QA deltas into candidate system upgrades |
| `retro-engineering` | **TODO** | Reverse-infer a template from a supplied document; vision-first, OCR fallback |

## Choose the note format

| Template | Reader / decision | Pages | Orientation | Status |
|---|---|---:|---|---|
| `architecture-note` | Technical or business sponsor: understand architecture, scale, risks and economics | 5–10 | portrait | validated |
| `one-pager` | Executive reader: gain rapid orientation on one decision | 1 | adaptive | validated |
| `two-pager` | Sponsor or prospect: assess a company, product, person or compact strategy | 2 | landscape | validated |
| `benchmarking` | Decision group: compare options consistently | 2–6 | landscape | candidate |
| `buy-side-gap-analysis` | Buyer: adopt, replace, complement or partner | 4–8 | adaptive | candidate |
| `diagnostic-reco-sellside` | Founder / commercial leader: improve positioning and sales motion | 5–9 | portrait | validated |
| `opportunity-note-icp` | Seller / partner lead: decide whether one target is credible | 4–8 | portrait | validated |

Read [the detailed template catalog](references/template-catalog.md) only after choosing the format.

## Core pipeline

```text
mode selection
→ research
→ atomic fragments
→ claims graph light
→ reranking
→ scaffold
→ fragment-grounded drafting
→ side-story insertion
→ fact-checking & sourcing
→ layout
→ DOCX render QA
→ next-step nudging
→ feedback/dreaming candidate
```

## Cross-version QA

Each template declares:
- semantic version;
- lifecycle;
- compatible modes;
- QA fixture;
- fixture version;
- workflow version.

CI rejects template/fixture major mismatches, stale workflow fixtures, enum/manifest drift, missing fixtures and accidental activation of the `retro-engineering` TODO.

## Git workflow

```text
feature branch
→ PR to dev
→ CI GREEN
→ merge into dev
→ PR dev → main
→ CI GREEN
→ promotion to main
→ fast-forward dev to main
```

Every new `.doc` / `.docx` decision note uses this skill together with the runtime DOCX creation/editing skill and the final render-and-inspect gate. Their boundary is versioned in [the DOCX runtime interface contract](contracts/docx-runtime-interface.schema.json): a layout-ready output specification goes in; a visual QA report comes back.

## Adaptive runtime v2

Resolve chat/work separately from light/heavy and debug. Documents always force heavy. Read only the
selected template's four-layer profile using `python scripts/note_runtime.py profile two-pager`.
Install helper requirements with `pip install -r requirements.txt`; then run
`python scripts/note_runtime.py plan intake.json`, `packet run.json --targets C-ID`, or `validate run.json`.
`search-plan` emits gap queries after manual coverage review; it does not execute searches.
`src.runtime.revise` returns a new baseline and rejects edits outside the requested impact closure.

The audit and harvest decisions are in [docs/ARCHITECTURE_V2.md](docs/ARCHITECTURE_V2.md).
Run `python -m unittest discover -s tests -v` in addition to contract QA. No model-cost savings are
claimed without measurements; reasoning settings are recommendations until applied by the host.
