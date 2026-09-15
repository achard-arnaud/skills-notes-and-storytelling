# Feedback / dreaming / self-healing governance

## Purpose

Dreaming is the governed loopback that converts real runs into reusable improvements without letting a single output silently rewrite canonical behavior.

It must answer three different questions:

1. **run quality** — did this output fail, surprise, or outperform expectations in a reusable way?
2. **counter-perspective** — what assumption, framing, winner, bridge, or operating pattern would a skeptical reviewer try to invalidate?
3. **system learning** — does the evidence justify a candidate fixture, patch, contract change, or workflow change?

Dreaming is not a second drafting pass and is not permission to add architecture. Its purpose is to detect reusable deltas with the smallest sufficient intervention.

## Tiered loopback

Every run receives one dreaming tier. Higher tiers include the checks of lower tiers.

### Tier 0 — `NO_REUSABLE_DELTA`

Valid outcome when the run closes cleanly and no reusable learning is evidenced.

Record only:
- decision/output type;
- QA status;
- bridge status;
- `NO_REUSABLE_DELTA`.

### Tier 1 — mandatory lightweight run check

Default for every normal run after decision, counter-perspective QA and bridge evaluation.

Ask:
- did a source, claim, layout, bridge, lock-in or QA issue recur or require a non-obvious adaptation?
- did the counter-perspective expose a material weakness that was repaired?
- did a successful adaptation look reusable beyond this case?

Outputs:
- `NO_REUSABLE_DELTA`; or
- one bounded candidate delta with affected template/workflow and evidence from the run.

Tier 1 never triggers broad refactoring.

### Tier 2 — targeted red-team loopback

Use when one of the following is true:
- the recommendation depends on a material assumption or weak evidence;
- a benchmark winner, integration thesis, architecture choice or bridge can reasonably be overturned;
- QA found a defect that could recur across a document family;
- the user explicitly asks to challenge, red-team, contre-analyser, or inspect failure modes;
- Tier 1 finds a candidate delta with potentially structural impact.

Procedure:
1. define the proposition to falsify;
2. identify the strongest credible counter-perspective, not a straw man;
3. search for disconfirming evidence, category errors, hidden hard gates, path dependence, lock-in and operating consequences;
4. test whether the conclusion survives, narrows, pivots or reopens;
5. separate a business-decision correction from a reusable system correction;
6. create regression coverage only for the reusable part.

Valid verdicts:
- `SURVIVES_RED_TEAM`;
- `SURVIVES_WITH_NARROWING`;
- `PIVOT_REQUIRED`;
- `REOPEN_TARGETED`.

### Tier 3 — explicit `FEEDBACK_DREAMING` / multi-run system review

Use for deeper improvement across multiple runs, repeated feedback, repeated QA defects, a newly discovered document family, or a candidate patch that would change canonical routing/contracts/templates.

Tier 3 must compare multiple observations where possible and should inspect:
- recurrence rate;
- whether the same failure appears across different templates or domains;
- whether the proposed fix changes behavior outside the observed cases;
- backward compatibility and migration impact;
- rollback path;
- test/fixture sufficiency.

Tier 3 may propose a branch/PR but still cannot autonomously promote canonical behavior.

## Counter-perspective contract

A counter-perspective is an explicit attempt to invalidate a material proposition before delivery or promotion.

It must be:
- **specific** — name the claim, recommendation, winner, bridge or assumption under attack;
- **credible** — use the strongest alternative explanation or failure path supported by evidence;
- **decision-relevant** — ignore objections that cannot change the decision or confidence;
- **bounded** — stop when the falsifier is resolved or the decision is reopened;
- **traceable** — link to claim/source/unknown IDs where available.

Preferred attack lenses:
- wrong problem framing;
- category mismatch;
- missing alternative or baseline;
- evidence asymmetry;
- hidden hard gate;
- incentive or ownership conflict;
- temporal staleness;
- lock-in/control migration;
- operational burden or failure ownership;
- reversibility/exit-path weakness;
- user/process adoption failure;
- second-order ecosystem consequence.

Do not create artificial balance. If the best counter-perspective is weak, record that and move on.

## Procedure

1. Capture QA defects, surprises, user feedback, counter-perspective findings and successful adaptations.
2. Separate case-specific content from reusable research/content/layout/contract/routing rules.
3. Include bridge quality: did the next-step recommendation reuse context correctly, preserve evidence status and avoid unnecessary research?
4. Include lock-in reasoning quality when material: was dependency located at the right stack/value-chain/process control point with an exit path?
5. Include process/habit lock-in when an admin surface, workflow or partner changes where humans perform canonical work.
6. Identify affected template/workflow and current versions.
7. Create a candidate patch only when a reusable delta exists.
8. Add/update regression fixture coverage.
9. Produce a delta note: why, scope, compatibility, QA impact, rollback, evidence tier and counter-perspective result.
10. Request human validation before promotion.

## Benchmark → integration closure learning

When a benchmark has identified a sufficiently good, reversible candidate and the remaining unknowns can only be resolved through implementation or pilot evidence, stop broad peer discovery.

Use one of:
- `CLOSED` — decision sufficiently established;
- `CLOSED_WITH_CHALLENGE_GATE` — selected path should be red-teamed against real implementation before execution;
- `REOPEN_TARGETED` — reopen only the specific failed hard gate or uncertainty.

Rules:
- preserve the native/no-tool baseline as fallback;
- convert unresolved implementation questions into pilot questions rather than new benchmark axes;
- prohibit adding peers after closure unless a named hard gate requires it;
- carry falsifiers, exit path and challenge gates into the Integration Note or Architecture Note.

## Integration-note learning

Reusable candidates exposed by real integration runs include:
- distinguish **strategic decision** (`BUILD | BUY | PARTNER | COEXIST | DEFER`) from **integration posture** (`embedded capability | admin surface | projection | runtime dependency | channel/partner | coexistence layer`);
- require a bounded pilot contract for every positive recommendation;
- map **operational habit/process lock-in** in addition to technical and commercial lock-in;
- recognize `projection / admin surface` as an integration pattern that does not create a new system of record.

These are canonical only after promotion evidence. A single real run can justify candidate coverage; cross-domain confirmation should be preferred before broadening the template.

## Promotion evidence

A reusable change normally requires at least one real output plus QA/user evidence. Promotion strength increases with tier:
- Tier 1: candidate note or fixture;
- Tier 2: candidate patch + regression fixture when the red-team finding is concrete and falsifiable;
- Tier 3: canonical change proposal with compatibility and rollback analysis.

A single run may justify a candidate fixture or patch when the gap is concrete and falsifiable, but not autonomous canonical promotion.

## Hard rule

The system may propose, branch, test, render, report and open a draft PR. A human decides promote, revise, reject or retire.

## Bridge learning

Dreaming should preferentially improve the reusable bridge contract rather than hard-code a one-off next step. Examples:
- benchmark complementarity repeatedly leads to integration analysis;
- sell-side diagnostics repeatedly expose named ICP targets suited to opportunity notes;
- architecture decisions repeatedly need a compact executive approval artifact.

Record the originating decision, reused claim/source IDs, new evidence required, counter-perspective result and whether the bridge produced useful information. This makes bridge quality testable over time.
