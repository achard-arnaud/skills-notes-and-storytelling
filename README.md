# Decision Notes & Storytelling

Evidence-grounded analysis and document composition, from a concise decision note to a detailed business narrative.

The project connects source material, typed claims, analytical methods, narrative structure and document review. It combines reusable skills with Python validation and execution tools so that an analysis can be inspected, revised and resumed across sessions.

**Repository review · 17 November 2026.** Template lifecycles and executable capabilities are defined by the manifests at the revision used for a run.

## Product value

| User outcome | Product capability | Engineering mechanism |
| --- | --- | --- |
| Explain a recommendation and its limits | Trace a conclusion to source material, scope and counter-evidence | Stable source, fragment and claim IDs, locators, typed relations and validation |
| Reuse research across different outputs | Produce business, product and technical views from an explicit evidence base | Analytical outputs, synthesis, scaffold and format-specific bindings |
| Revise a long report consistently | Identify what a source correction affects and retain unrelated work | Dependency analysis, invalidation plans and regression coverage |
| Resume work after a session ends | Reconstruct the next task from stored artifacts | Scoped context packets, checkpoints, hashes and version checks |
| Extend formats and decision methods | Select a profile and load the required references | Versioned manifests, schemas, fixtures and shared runtime |
| Improve the system from observed failures | Turn an incident into a bounded, testable correction | Loopback receipts, ADR references, BUILD issues and regression tests |

The design addresses several sources of complexity together — source reliability, evolving knowledge, selective context loading, multi-format composition, long-running studies and human review.

## Start with a bounded case

1. Read [AGENTS.md](AGENTS.md) for evidence rules, stage boundaries and contribution policy.
2. Read [SKILL.md](SKILL.md) for generation mode, analytical dimension and routing.
3. Select the output using [templates/manifest.json](templates/manifest.json), [templates/profiles.json](templates/profiles.json) and the chosen template reference.
4. Read [case execution and recovery](references/case-process.md) for the executable A0–A4 route.
5. For detailed studies, read the [long-report workspace guide](diagnostic-complet/README.md) and the [interface contract](diagnostic-complet/docs/INTERFACES.md).

The repository carries BUILD assets such as methods, contracts, code and curated fixtures. New case data belongs in the ignored `data/cases/<case-id>/` workspace. Private sources and client deliverables stay in their authorized working destination.

## From evidence to a reviewed narrative

| Stage | Result | Boundary enforced by the runtime |
| --- | --- | --- |
| **A0 — Evidence acquisition** | Source captures, dates, locators and reading coverage | Source references and scoped regions are checked |
| **A1 — Typed evidence graph** | Sources, fragments, claims and relations | Identity, provenance, graph types and references are validated |
| **A2 — Narrative scaffold** | Question, decision structure, objections and section-to-claim mapping | Required fields and references are checked against the selected profile |
| **A3 — Composition** | Section prose, bounded side stories and optional renderer payload | Claim mappings and payload contracts are checked |
| **A4 — Review** | Evidence, content and delivery reviews, plus render receipts when requested | Required artifacts and their hashes are verified |

The agent or operator performs research, analysis and writing. The Python engine validates submitted artifacts and records transitions, attempts and rejections. The source-to-prose meaning and the quality of a recommendation remain explicit review responsibilities.

The [process manifest](workflow/case-process.json), its [schema](contracts/case-process.schema.json) and [case artifact contracts](contracts/case-artifacts.schema.json) define the current implementation. The [engine release](workflow/engine-release.json) pins shared files by hash.

## Skills, analytical methods and templates

The canonical method favors small, focused skills and selective reference loading. Analytical methods answer bounded questions. Storytelling skills organize their outputs for a reader. Templates determine the delivery structure and its constraints.

Three analytical dimensions are available — **business**, **product** and **technical**. Pedagogical learning sheets and regulatory analysis add specialized content and review contracts. Support is resolved per template and branch.

The long-report workspace includes methods for market and competition, industry value chains, corporate functions, data foundations, AI capabilities, economics, governance and adoption. Their findings feed narrative design and typed side stories. The [skills map](diagnostic-complet/docs/SKILLS-MAP.md) and [operational catalog](diagnostic-complet/docs/SKILLS-CATALOG.md) describe entry points and ownership.

### Output families

| Output family | Typical purpose | Canonical reference |
| --- | --- | --- |
| One-pager and two-pager | Executive orientation, company analysis and a compact decision | [Template catalog](references/template-catalog.md) |
| Architecture and integration notes | Alternatives, dependencies, risk, economics and reversibility | [Architecture template](templates/architecture-note.md), [integration template](templates/integration-note.md) |
| Benchmarks, buy-side and sell-side analyses | Compare options, qualify fit and explain value | [Template manifest](templates/manifest.json) |
| Strategic market notes | Market mechanisms, positioning and options | [Market template](templates/strategic-market-note.md) |
| Detailed business narratives | A main argument enriched by sourced side stories | [Narrative contract](diagnostic-complet/docs/NARRATIVE.md) |
| Pedagogical learning sheets | Structured learning content, use cases and exercises | [Pedagogical skill](skills/pedagogical-ai-learning/SKILL.md) |
| Regulatory notes — integration candidate on dev | Sector-specific analysis and traceable regulatory implications | [Candidate contract on dev](https://github.com/achard-arnaud/skills-notes-and-storytelling/blob/dev/templates/regulatory-note.md) |

Manifest states distinguish candidate and validated templates. A fixture, a successful test and reader acceptance each provide a different type of evidence. The canonical branch currently declares ten templates. The integration branch also carries the regulatory candidate.

Generation modes are `from-scratch`, `iterative` and `feedback-dreaming`. Their lifecycle is declared in [modes/manifest.json](modes/manifest.json). The reverse-engineering mode remains at `todo`.

## Graph, ontology and knowledge lifecycle

Two related representations serve different tasks.

- The evidence graph connects source fragments, claims, contradictions, hypotheses and the document sections that use them. Unknowns retain their status throughout composition.
- The documentary knowledge base preserves sources, deduplicated atoms and distinct occurrences with locators. An ontology constrains node and relation types and supports consistency analysis.

The implementation provides ingestion, ontology validation, relation checks, profile-aware classification and a controlled Graph1 projection. Typed interfaces preserve the distinction between an observed statement, an attributed claim, an inference and a hypothesis.

This structure makes evidence reuse and impact analysis possible. For example, an updated source can require review of one finding and its dependent paragraphs while leaving another branch of the study intact. Cross-study reuse requires explicit scope and provenance.

The graph is file-based and the retrieval helpers are local Python tools. Knowledge coverage and correctness are assessed through provenance, tests and review.

Useful entry points include [KB ingestion](diagnostic-complet/kb.py), [ontology](diagnostic-complet/ontology.py), [ontology definitions](diagnostic-complet/ontology/ontology-v1.json), [context protocol](diagnostic-complet/docs/CONTEXT-PROTOCOL.md) and [Graph1 projection](diagnostic-complet/project.py).

## Runtime, context and recovery

The runtime keeps execution state separate from reusable methods.

- **Case isolation** scopes each new run to its declared subject and sources.
- **Context packets** load the references and artifacts needed for the next stage.
- **Dependency pins** bind the run to its methods, contracts and input revisions.
- **Attempts and events** retain failed boundaries and subsequent retries.
- **Checkpoint validation** rejects missing, modified or incompatible dependencies.
- **Invalidation** follows declared dependencies and preserves prior attempts.
- **Atomic writes and local locking** protect case state during concurrent operations.

The canonical engine enforces A0–A4 case boundaries. The detailed-study workspace also contains analytical envelopes, synthesis-to-writing bindings and selective impact logic. The active branch and its contracts determine which path is used.

A fresh-process regression verifies reconstruction from stored artifacts, including partial analysis, changed-source rejection and changed-engine rejection. The [comparison protocol](diagnostic-complet/docs/CONVERGENCE-TRIAL-PROTOCOL.md) extends that mechanical check to the proposed real-study evaluation.

## Loopback and technical decisions

The case loopback records an incident, its evidence, the affected state and the relevant ADR. It routes the diagnosis across architecture, bugfix, CI, runtime and skill concerns. A proposed change carries a falsifiable hypothesis, a test, a stopping condition and a rollback path.

A separate [KB reinforcement operation](diagnostic-complet/operational-skills/reinforce-kb-loopback/SKILL.md) examines a declared knowledge-base update and returns proposals for review.

Seven [technical decision profiles](references/technical-decisions.md) share the runtime — architecture rupture, debt and risk, migration/TCO, ecosystem impact, bootstrap/DX, run readiness and PoC verdict. Their contracts require alternatives, assumptions, evidence or explicit unknowns, and decision-specific checks. Observed measurements resolve to hashed evidence. The `Adopt` verdict requires the declared thresholds to pass on observed values.

The [architecture register](docs/architecture/README.md) explains the rationale for routing, evidence, narrative artifacts, RUN/BUILD separation, learning and governance. [ADR-1008](docs/architecture/ADR-1008-executable-cases-and-decision-profiles.md) connects these principles to the executable case engine and decision profiles.

## TDD, CI and delivery evidence

BUILD corrections use bounded acceptance criteria, a failing regression when applicable, implementation and verification at the resulting commit. Synthetic fixtures exercise both successful paths and adversarial cases such as stale inputs, invalid references, modified evidence and unsupported decisions.

The [skill-qa workflow](.github/workflows/qa.yml) runs on pull requests and pushes to `dev` and `main`.

| CI job | Checks actually defined |
| --- | --- |
| `validate` | Install declared dependencies, validate contracts, check the case process and run the root test suite |
| `runtime-convergence` | Run the `diagnostic-complet` test suite after validation succeeds |
| [Pedagogical render](.github/workflows/pedagogical-render.yml) | On relevant changes, run specialized tests, render the Perception sheet and verify the generated output |

CI covers contracts, runtime behavior and selected rendering paths. Analytical substance, narrative quality, visual inspection and human acceptance keep their own review results.

SDD prepares implementation-ready units from the current backlog. TDD consumes eligible units, records ownership and attaches tests and CI evidence to exact commits. Repository automation follows the current [shared SDLC contract](https://github.com/achard-arnaud/Skills-SDLC-superpower/blob/main/README.md). The [convergence epic](https://github.com/achard-arnaud/skills-notes-and-storytelling/issues/294) tracks the remaining integration and evaluation work.

## Architecture comparisons in progress — main, S2 and S3

The evaluation programme compares how different skill architectures deliver the same analytical task.

| Comparison cohort | Architecture under examination | Evaluation question |
| --- | --- | --- |
| **main — canonical reference** | Small focused skills, reusable methods and selectively loaded references | What quality, execution cost and recovery behavior does the canonical approach provide? |
| **S2 — consolidation variant** | Group related behavior around business, product, technical, pedagogical and regulatory families, with templates carried by manifests and internal references | Does consolidation improve routing and consistency while controlling context and dependency costs? |
| **S3 — long-workflow convergence variant** | Connect evidence, typed analytical results, synthesis, narrative composition and recovery for a detailed report | Can a richer workflow retain analytical depth and reliable revisions at an acceptable execution cost? |

These labels identify comparison cohorts. The S1/S2/S3 work units in older tickets also identify implementation stages. Each evaluation therefore freezes the actual Git revisions, method versions, source set and renderer before execution.

An [experimental branch](https://github.com/achard-arnaud/skills-notes-and-storytelling/tree/experiment/narrative-procedure-ab-20261113) preserves earlier work. The current target is developed through bounded units on `dev`. The [trial protocol](diagnostic-complet/docs/CONVERGENCE-TRIAL-PROTOCOL.md) defines comparable inputs, fresh-session recovery and separate quality verdicts.

Performance evaluation is intended to record wall-clock duration, stage timings, loaded context, exposed token usage, tool/skill calls, retries and available cost measurements. Missing host metrics remain unknown. Quality evaluation examines mandate fidelity, evidence coverage, analytical contribution, narrative comprehension and delivered output.

The current synthetic recovery tests establish mechanical behavior. Comparative performance and runtime results across the three cohorts are still being organized. A real-study trial and an independent reserve case are part of the remaining evaluation.

## Renderers and delivery

Rendering capabilities are specialized and selected through the declared profile.

- [Two-pager renderer](renderers/two_pager_nice/README.md) provides a dedicated layout and content contract.
- [Pedagogical renderer](renderers/pedagogical/) provides a six-page landscape path with a specialized content schema and CI.
- [Detailed-study renderer](diagnostic-complet/render.py) produces reader views from a study.
- The [DOCX interface](contracts/docx-runtime-interface.schema.json) defines the handoff to a document runtime.

For an A0–A4 run requesting rendering, the profile must declare an available adapter and its pinned dependencies. The runtime records the actual invocation, output hashes and QA receipt. Renderer coverage varies by format.

## Local verification

Python 3.12 is the version used by CI. From the repository root, install the declared dependencies and run the checks.

```bash
python3 -m pip install -r requirements.txt
python3 scripts/validate_contracts.py
python3 scripts/case_runtime.py check
python3 -m unittest discover -s tests -v
(cd diagnostic-complet && python3 -m unittest discover -s tests -v)
```

For a new case, prepare an intake matching [the intake contract](contracts/case-artifacts.schema.json) and choose a template declared in the active process manifest.

```bash
python3 scripts/case_runtime.py init --case example-study --input intake.json
python3 scripts/case_runtime.py begin --case example-study --stage A0 --actor manual_agent
python3 scripts/case_runtime.py status --case example-study
```

## Contribution and project bootstrap

Start from the current integration branch, read the applicable ADR and reserve a bounded file scope. Reuse the existing source-of-truth manifests and validators. Contract changes include regression fixtures. Template changes update the template manifest. New templates begin as candidates.

The delivery path is feature branch → PR to `dev` → review and green CI → integration → reviewed promotion to `main`. A documentation-only forward-port can update the project entry point while functional changes retain their integration status.

For a first contribution, follow one scenario end to end — its input, contract, transformation, output and verification. Keep private case data in its authorized workspace. The [historical Workbench proposal](https://github.com/achard-arnaud/skills-notes-and-storytelling/tree/design/business-notes-workbench-20261022/docs/workbench-proposal) remains a design reference for a future cockpit.
