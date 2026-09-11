# Adaptive business skill v2 — audit and decisions

## Baselines and correction of the earlier assessment
Business baseline: 18ae0deac4d9eef89431b7515a0694f53b1b2b59.
Historical baseline: fb83e0e759d1fef78bbb2cca766fecbb23eda8d5.
The historical repository already implements much of the previously recommended architecture.
The prior assessment did not sufficiently inspect it. This change reuses its design patterns;
it does not claim to have invented them or to port its domain-specific pipeline wholesale.

| Improvement | Historical implementation inspected | Business baseline | v2 disposition |
|---|---|---|---|
| Scoped context | scripts/audit_context_budget.py, build_story_scaffold.py | no runtime budget audit | explicit read-slice audit; packet budgets |
| Scaffold versus material | scripts/build_drafting_packets.py | described, no materializer | separate claims/fragments/sections in bundle and packets |
| Input lineage | scripts/audit_intake_lineage.py | fragments only | source origin/family/coverage and manual-first gap planner |
| Local drafting | scripts/build_drafting_packets.py | iterative prose instructions | ID/section/fragment retrieval and impact closure |
| Canonical baseline | scripts/output_state.py | baseline described | explicit run_id, parent baseline and scoped immutable revision |
| Side-story return | scripts/return_target_resolution.py | return_to nullable without semantic QA | resolved section IDs; method exception |
| Multiple business logics | causal arc design | typed edges already declared | preserve edge repertoire, mechanism requirement for causes |
| Language/ICP | business feat/icp-language-analysis-boundary | unmerged branch | reuse language_lint and ICP contract selectively |
| Consulting narrative | business feat/debrief-360 | unmerged branch | shared narrative registry; meeting-specific candidate stays unrouted |
| Debug/light/heavy | not a single inherited routing switch | absent | independent profile controls; document override |

No historical content corpus, run-specific repair scripts, or historical ontology is imported.
The installed skill ships runtime references/contracts, not audit logs, old research, tests or repository history.

## Four layers
Every existing template has a profile in templates/profiles.json: objective/collection/length,
narrative strategy, scaffold/retrieval/versioning, writing/language/notes. Template selection remains
in the enum and manifest. General four-entity research uses separate outputs, not a seller advisory
unless the user actually asks to advise the seller. No new validated template was necessary for Rivard.

## Runtime versus instructions
SKILL.md instructs a model; scripts perform deterministic work only when called by a tool-capable host.
Reading a skill is not executing it. The v1 run did not leave auditable fragment/claim/packet artifacts;
calling it a fully executed pipeline was too strong. The v2 replay must report actual artifact checks.
The helpers are not a miniature operating system, autonomous researcher, embedding service or model router.
Reasoning level is recommended, never asserted as applied. JSON validation cannot establish truth.

## Chat and work
Environment and execution depth are independent. Chat usually benefits from compact inline records;
work can persist reusable files and run validators if available. Documents force heavy in either,
with smaller successive packets in chat. Actual available capabilities take precedence over UI names.
Debug adds bounded traces and decisions, not private reasoning or an expanded evidence standard.

## Downsizing and cost
Smaller models can benefit from explicit inputs, contracts and deterministic checks. This does not
establish equivalent reasoning quality. Route routine extraction/formatting cheaply only when the host
allows it; reserve difficult inference and source conflicts for stronger review. An evaluation needs
multiple tasks, repeated runs, equal QA gates, actual model/token/time data, and correction costs.
No billed-cost telemetry or controlled multi-model benchmark was available in this refactor.
Any earlier percentage savings or proportion of 'OS versus skill' was unmeasured and should be withdrawn.
SKILL.md word/byte reduction alone measures entry size, not total run cost. Audit selected references,
source packets, outputs and retries separately. The historical audit correctly makes this distinction.

## QA boundaries and remaining work
Runtime tests exercise failure cases, source lineage, hypothesis handling, contradictory evidence,
intake order, selective revisions and budget overflow. CI also preserves legacy enum/fixture/DOCX gates.
Word and language checks are heuristic. Narrative quality, actual source accuracy, manual reading and
visual layout still require review. No learned reranker or automatic semantic truth validator is claimed.
See TODO.md for candidate work; no branch was blindly merged over newer main fixes.
