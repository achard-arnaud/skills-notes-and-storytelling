# Governed writing workflow

Workflow version: 1.3.1

## Common state machine

```text
MODE_SELECTED
→ CONTEXT_FRAMED
→ RESEARCHED
→ FRAGMENTED
→ CLAIMS_GRAPHED
→ RERANKED
→ SCAFFOLDED
→ DRAFTED
→ SIDE_STORIES_ROUTED
→ SOURCED
→ COUNTER_PERSPECTIVE_QA
→ RED_TEAM_REPAIRED (only when narrowing/repair is material)
→ RED_TEAM_VERIFIED (single verification pass)
→ LAID_OUT / RENDER_QA (when artifact requested)
→ DELIVERED
→ BRIDGE_EVALUATED
→ DREAMING_TIER_SELECTED
→ DREAMING_CHECKED
→ DREAMING_CANDIDATE (only when reusable delta exists)
```

Every normal run reaches `COUNTER_PERSPECTIVE_QA`, `BRIDGE_EVALUATED` and `DREAMING_CHECKED`. Counter-perspective depth is proportional to decision risk. Dreaming may legitimately return `NO_REUSABLE_DELTA`.

A red-team finding may trigger **one** repair/narrowing pass and **one** verification pass before dreaming. Do not loop indefinitely inside the run. A second material failure becomes `REOPEN_TARGETED` or Tier 3.

| Stage | Required input | Output | Gate |
|---|---|---|---|
| Mode selection | request + existing artifacts | mode declaration | baseline/new-work explicit |
| Context framing | request + trusted context | decision question, audience, horizon, constraints | supplied framing challenged where material |
| Research | decision question + scope | classified source ledger | sufficient or limits stated |
| Fragments | source ledger | atomic fragments | one evidence unit per fragment |
| Claims graph | fragments | claims + typed edges | every claim has lineage |
| Rerank | claims | ranked claim set | duplicates pruned; hard gates external to score |
| Scaffold | ranked claims | section skeleton | each section has purpose/payoff |
| Fill | scaffold + fragments | prose/bullets/tables | no unsupported material assertion |
| Side stories | coherent trunk | routed side stories | bounded + return anchor |
| Sourcing | draft | source-complete draft | material claims traceable |
| Counter-perspective QA | sourced draft + claims + unknowns | attack findings + verdict | strongest credible invalidation tested |
| Red-team repair | material narrowing/repair finding | revised proposition/output | at most one repair pass |
| Red-team verification | repaired proposition | verified verdict | at most one verification pass; otherwise reopen |
| Layout/render | content spec | artifact + QA when requested | template/version + visual gates |
| Bridge | delivered decision + RunContext | zero or more bounded bridge candidates | evidence-backed; smallest reversible next decision |
| Dreaming tier | complete run + QA/feedback | Tier 0–3 | depth proportional to reusable-risk signal |
| Dreaming check | complete run + counter-perspective + QA/feedback | `NO_REUSABLE_DELTA` or candidate delta | no silent promotion |

## RunContext

Maintain the compact provenance object defined in [bridges-integration-and-run-memory.md](bridges-integration-and-run-memory.md). It is the handoff between templates and prevents research, rejected options, sourcing decisions and uncertainty from being lost between notes.

Add when material:
- counter-perspective proposition attacked;
- strongest alternative explanation/failure path;
- counter-perspective verdict;
- repair/narrowing applied;
- verification verdict;
- loopback event type;
- dreaming tier and candidate delta status.

## Mode-specific preflight

### From scratch
Start with a blank decision spine. Material statements flow from sourced fragments into claims before the scaffold.

### Iterative
Resolve a canonical baseline before research. Record accepted content/evidence/layout, requested delta and any form-global review scope. Preserve accepted material outside scope and rerun regression QA on the final output.

### Feedback / dreaming
This explicit mode deepens the mandatory end-of-run dreaming check across one or more outputs. It updates the system, not the business conclusion. Candidate improvements require regression coverage and human promotion.

### Retro-engineering
Documented TODO; excluded from production routing until contracts and tests exist.

## Claims graph light

Node types: `fragment | claim | decision | recommendation | unknown`.

Edge types: `supports | contradicts | qualifies | causes | depends_on | compares_to | answers | motivates | integrates_with | substitutes | complements | enables`.

The graph supports retrieval, deduplication, reranking, bridge detection, ecosystem/complementarity analysis, counter-perspective selection and side-story placement without becoming a heavy ontology.

## Reranking

Default 0–5 dimensions:
- decision relevance 30%;
- evidence strength 25%;
- explanatory power 20%;
- novelty/non-redundancy 15%;
- audience fit 10%.

Hard gates, contradictions and critical unknowns remain outside weighted scoring.

## Scaffold rule

For each section define question answered, top claim IDs, payload type, maximum density, source coverage threshold and transition/return sentence.

## Counter-perspective / red-team QA

This is a bounded falsification pass, not a rewrite pass.

For each material decision or recommendation:
1. name the proposition that would most damage the conclusion if false;
2. select the strongest credible counter-perspective from evidence/unknowns/rejected alternatives;
3. inspect disconfirming evidence, hidden hard gates, category mismatch, lock-in/control migration, operating burden, reversibility and incentive conflict where relevant;
4. decide one of:
   - `SURVIVES_RED_TEAM`;
   - `SURVIVES_WITH_NARROWING`;
   - `PIVOT_REQUIRED`;
   - `REOPEN_TARGETED`;
5. if `SURVIVES_WITH_NARROWING` or a bounded repair can resolve the issue, apply one repair pass;
6. verify the repaired proposition once;
7. if verification still finds a material defect, stop and route to `REOPEN_TARGETED` or Tier 3 rather than iterating again.

Depth rules:
- low-risk descriptive note: one material counter-perspective maximum;
- decision note with reversible next step: challenge recommendation + main assumption;
- benchmark/integration/architecture/high-lock-in decision: challenge winner/path, baseline/fallback and at least one hidden hard gate.

Do not manufacture symmetry or objections. Stop when additional attack paths cannot change confidence, scope or decision.

## Review modes

Use three complementary review lenses when useful:

### 1. Conformance review
Checks whether the output follows contracts, evidence rules, template structure, sourcing, page constraints and explicit user scope.

### 2. Counter-perspective review
Checks whether the reasoning survives the strongest credible alternative explanation, failure mode or stakeholder/control-point perspective.

### 3. Reader/decision review
Checks whether the intended decision maker can see the answer, uncertainty, falsifier, next step and trade-offs without reconstructing the analysis.

A review finding should identify the lens that produced it. This prevents stylistic preferences from masquerading as factual or decision defects.

## Final QA sequence

1. mode/baseline QA;
2. context/problem-framing QA;
3. content-contract QA;
4. source and evidence-status QA;
5. lock-in/sovereignty/process-control location check when material;
6. counter-perspective/red-team QA;
7. optional single repair/narrowing pass;
8. single red-team verification pass;
9. stylistic/layout/render QA when applicable;
10. reader/decision QA;
11. decision + falsifier check;
12. bridge evaluation using preserved RunContext;
13. select dreaming tier using [dreaming-self-healing.md](dreaming-self-healing.md);
14. mandatory dreaming check;
15. if reusable delta exists, create candidate patch/fixture proposal for human approval.
