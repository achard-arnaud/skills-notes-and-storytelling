# Decision Notes & Storytelling

Reusable skill for evidence-grounded decision notes, architecture notes, one-pagers, two-pagers, benchmarks, buy-side analyses, sell-side diagnostics ICP opportunity notes and post-call 360 debriefs.

## Canonical skill
- **Skill:** `decision-notes-and-storytelling`
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

## Template catalog

| Template | Version | Status |
|---|---:|---|
| `architecture-note` | 1.1.0 | validated |
| `one-pager` | 1.0.0 | validated |
| `two-pager` | 1.1.0 | validated |
| `benchmarking` | 0.2.0 | candidate |
| `buy-side-gap-analysis` | 0.2.0 | candidate |
| `diagnostic-reco-sellside` | 1.0.0 | validated |
| `opportunity-note-icp` | 1.0.0 | validated |\n| `debrief-360` | 0.1.0 | candidate |

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

Every new `.doc` / `.docx` decision note uses this skill together with the runtime DOCX creation/editing skill and the final render-and-inspect gate.

## Personal branding

Branding is selected independently from the output template through `branding/profiles.json`. The default profile is `francois`; additional people are atomic registry entries. Header and footer behavior is defined in `references/personal-branding.md`.
