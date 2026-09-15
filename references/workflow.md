# Governed writing workflow

Workflow version: 1.2.0

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
→ LAID_OUT / RENDER_QA (when artifact requested)
→ DELIVERED
→ BRIDGE_EVALUATED
→ DREAMING_CHECKED
→ DREAMING_CANDIDATE (only when reusable delta exists)
```

Every normal run reaches `BRIDGE_EVALUATED` and `DREAMING_CHECKED`. Both may legitimately return `NONE` / `NO_REUSABLE_DELTA`.

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
| Layout/render | content spec | artifact + QA when requested | template/version + visual gates |
| Bridge | delivered decision + RunContext | zero or more bounded bridge candidates | evidence-backed; smallest reversible next decision |
| Dreaming check | complete run + QA/feedback | `NO_REUSABLE_DELTA` or candidate delta | no silent promotion |

## RunContext

Maintain the compact provenance object defined in [bridges-integration-and-run-memory.md](bridges-integration-and-run-memory.md). It is the handoff between templates and prevents research, rejected options, sourcing decisions and uncertainty from being lost between notes.

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

The graph supports retrieval, deduplication, reranking, bridge detection, ecosystem/complementarity analysis and side-story placement without becoming a heavy ontology.

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

## Final QA sequence

1. mode/baseline QA;
2. context/problem-framing QA;
3. content-contract QA;
4. source and evidence-status QA;
5. lock-in/sovereignty location check when material;
6. stylistic/layout/render QA when applicable;
7. decision + falsifier check;
8. bridge evaluation using preserved RunContext;
9. mandatory lightweight dreaming check;
10. if reusable delta exists, create candidate patch/fixture proposal for human approval.
