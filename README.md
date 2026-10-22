# Decision Notes & Storytelling

> **A governed decision-note skill, not an installed research platform.** This repository owns research methodology, evidence and claim lineage, narrative decisions, versioned templates, counter-perspective QA, bridge proposals and bounded learning. Rendering is downstream. As of 2026-10-22 the workflow is specified/documented; it does **not** ship a React runtime, GitHub webhook service, Obsidian connector, four-format export API, or autonomous agent orchestration.

## Start here — human or agent (five bounded reads)

1. [AGENTS.md](AGENTS.md) — ownership of evidence, stage boundaries and change policy.
2. [SKILL.md](SKILL.md) — generation mode, analysis dimension, template, stage rules.
3. [templates/manifest.json](templates/manifest.json) and [modes/manifest.json](modes/manifest.json) — **canonical machine-readable** status, versions and fixtures. Do not use a prose table as authority over these.
4. [references/workflow.md](references/workflow.md) — active procedure and red-team/dreaming stop conditions. Open only the current stage.
5. The chosen `templates/<id>.md` and its declared QA fixture; read [references/bridges-integration-and-run-memory.md](references/bridges-integration-and-run-memory.md) if transferring/reusing prior research.

**Working boundaries**: one problem/subject and decision question per run; no general scan of all examples or archived notes; source claims carry ID, scope, temporal status and locator; a written claim does not become verified simply by being reused. Claims graph light is a method/schema, not an installed multi-user database.

## What the current repository actually provides

| Component | Authority / implementation status |
|---|---|
| Skill instruction and research→claims→note stages | [SKILL.md](SKILL.md), [references/workflow.md](references/workflow.md) — **documented** |
| Modes & versioned templates | [src/template_types.py](src/template_types.py), [templates/manifest.json](templates/manifest.json), [modes/manifest.json](modes/manifest.json) — **contract/fixtures verified by CI** |
| Evidence fragments, claims, light graph, composition and output spec | [contracts](contracts) — **schemas**, not an installed retrieval service |
| Side stories, bridges, red-team and dreaming | [references](references) — **governed methodology**, run loop remains process-driven |
| DOCX boundary | [contracts/docx-runtime-interface.schema.json](contracts/docx-runtime-interface.schema.json) — **interface to external renderer**, not built-in Word service |
| Validation | [scripts/validate_contracts.py](scripts/validate_contracts.py), [GitHub QA](.github/workflows/qa.yml) — **contract/manifest checks**, not live web/React/PDF E2E |
| React, Obsidian, GitHub webhook, run store, export APIs | **not implemented**; see draft [Workbench proposal](docs/workbench-proposal/00-GAP-ANALYSIS.md) |

## Select a template (manifest snapshot 2026-10-22)

The status here mirrors the manifest; the manifest remains authoritative on future changes.

| Template ID | Decision task | Pages | Manifest lifecycle |
|---|---|---:|---|
| `architecture-note` | Architecture, system/capability, tradeoffs, risks and economics | 5–10 | **candidate** |
| `one-pager` | Executive orientation to one decision | 1 | validated |
| `two-pager` | Compact company/product/person/strategy evaluation | 2 | validated |
| `benchmarking` | Compare alternatives against common criteria | 2–6 | candidate |
| `buy-side-gap-analysis` | Adopt / replace / complement / partner | 4–8 | candidate |
| `diagnostic-reco-sellside` | Positioning and GTM diagnostic | 5–9 | validated |
| `opportunity-note-icp` | Credibility of an account / opportunity | 4–8 | validated |
| `integration-note` | Build / buy / partner / coexist / defer | 3–7 | candidate |
| `strategic-market-note` | Business strategic market view and options | 5–7 | candidate |

### Three primary lenses (not interchangeable tags)

- **Business** — strategy, governance, organization, economics, client model, transformation.
- **Product** — jobs to be done, user journeys, use cases, competitive positioning, adoption and product operating model.
- **Technical** — architecture, data, APIs, dependency control, security, runtime, observability and cost.

Select one *primary* lens prior to template composition. Secondary lenses may inform comparisons; they must not override the decision spine. Dimension-specific support is **not uniformly declared for all nine templates** in the current manifest; a future filterable catalog must validate it per template instead of guessing. See [template catalog](references/template-catalog.md).

## Choose one generation mode

| Mode | Current lifecycle | Boundary |
|---|---|---|
| `from-scratch` | validated | research → atomic fragments → claims → decision narrative |
| `iterative` | validated | preserve canonical baseline and claim ledger, selective delta, regression |
| `feedback-dreaming` | validated | inspect multiple runs and propose candidate improvements, no automatic promotion |
| `retro-engineering` | **todo** | reverse-engineer a document; no production operation claimed |

## Reasoning and QA pipeline

```text
Select mode / primary dimension / template
  → Context and decision question
  → Research (account truth != product truth)
  → Source-addressable fragments
  → Claims / contradictions / unknowns (graph light)
  → Evidence rerank + hard gates
  → Dimension-specific scaffold
  → Draft from evidence + bounded side stories
  → Source validation + counter-perspective
  → Content freeze / layout / renderer and visual QA if output needed
  → Decision & next-step bridge
  → Lightweight dreaming + candidate change request (if reusable)
```

A `claim` with a citation is not sufficient if the source is out-of-scope or stale. Side stories cannot manufacture proof. The counter-perspective tests material conclusions; maximum one repair and one verification before reopen targeted. `NO_REUSABLE_DELTA` is a valid learning result.

## Working across subjects and templates

Carry a bounded run context — subject identity, cutoff, evidence ledger, claim IDs, unknowns, contradictions, rejected alternatives, hard gates, decision, counter-perspective verdict, output and template versions. Prior evidence remains *prior evidence*, not fresh truth. [Bridges & run memory](references/bridges-integration-and-run-memory.md) explicitly separate seller/product truth from company/account truth.

### Where to store results today

This repo is **public**. It contains authorized methods, fixtures and examples only. Do not add private contacts, client/source raw captures, API tokens or proprietary research documents to this Git history. For a new run, track source and claim IDs as governed artifacts and use a private workspace for sensitive captures. **Obsidian local persistence and graph rebuild are planned, not yet available in this repository.**

## Git contribution protocol

```text
feature branch from dev → PR to dev → QA GREEN + human review
→ merge into dev → dev-to-main PR → QA GREEN → promote
→ resynchronize dev
```

Changes to template/mode schema require version/fixture updates, runtime and evidence boundaries require negative tests, and promotion remains human approved. See [versioning](references/versioning-and-lifecycle.md), [QA checklist](tests/QA_CHECKLIST.md). The current CI is intentionally narrow; do not infer that a Word/PDF was rendered just because schema tests passed.

## Workbench / React cockpit — design branch only

**Proposal and change requests; not an operational UI.**

- [Gap analysis with Hivest & Candidatures Nice](docs/workbench-proposal/00-GAP-ANALYSIS.md)
- [Runtime & anti-compaction design](docs/workbench-proposal/01-ARCHITECTURE.md)
- [React UX and editorial ToC](docs/workbench-proposal/02-REACT-UX.md)
- [GitHub webhooks, actions and local Obsidian](docs/workbench-proposal/03-GITHUB-WEBHOOKS-OBSIDIAN.md)
- [Delivery plan BN-00…BN-10](docs/workbench-proposal/04-DELIVERY-PLAN.md)
- [React source demonstration](prototypes/workbench-react/README.md) — nine illustrative templates, search and three dimension filters, reordering and depth stars, local overlay download. **No source research nor real document export**.
- [Parent Epic #21](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/21)

**Core design decision**: a React UI may propose a `RunOverlay` (template SHA, sections, ordering, depth), but it cannot override the canonical template/evidence controls. A local service, only with PC permission, will coordinate Obsidian evidence, generated graph-light view, transactional stages, and optional GitHub branches/CI.
