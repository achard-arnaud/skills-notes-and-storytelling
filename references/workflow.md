# Governed writing workflow

## Common state machine

```text
MODE_SELECTED
→ RESEARCHED
→ FRAGMENTED
→ CLAIMS_GRAPHED
→ RERANKED
→ SCAFFOLDED
→ DRAFTED
→ SIDE_STORIES_ROUTED
→ SOURCED
→ LAID_OUT
→ DOCX_QA_PASSED
→ DELIVERED
→ NUDGED
→ FEEDBACK_CAPTURED (optional)
→ DREAMING_CANDIDATE (optional)
```

Each transition has an input contract, output contract and stop condition.

| Stage | Required input | Output | Gate |
|---|---|---|---|
| Mode selection | request + existing artifacts | mode declaration | baseline/new-work status explicit |
| Research | decision question + scope | source ledger | sources sufficient or limits stated |
| Fragments | source ledger | atomic fragments | one idea/evidence unit per fragment |
| Claims graph light | fragments | claims + typed edges | every claim has lineage |
| Rerank | claims | ranked claim set | low-value duplicates pruned |
| Scaffold | ranked claims | section skeleton | each section has purpose/payoff |
| Fill | scaffold + fragments | prose/bullets/tables | no unsupported material assertion |
| Side stories | coherent trunk | routed side stories | detours bounded + return anchor |
| Sourcing | complete draft | source-complete draft | material claims traceable |
| Layout | content spec | DOCX-ready spec | template/version contract satisfied |
| DOCX QA | DOCX | QA report | every page visually clean |
| Nudging | delivered decision | next-step set | bounded, decision-relevant follow-ups |
| Feedback | output + human/QA delta | feedback ledger | reusable vs case-specific separated |
| Dreaming | feedback ledger + fixtures | candidate patch | human promotion required |

## Mode-specific preflight

### From scratch
Start with a blank decision spine. Every material statement must flow from sourced fragments into claims before it reaches the scaffold.

### Iterative
Resolve a canonical baseline before research. Record:
- accepted content;
- accepted evidence status;
- accepted layout/template version;
- requested delta;
- **form-global changes** that make an entire section or document span review-eligible.

An iterative run preserves accepted material outside the declared review scope and reruns regression QA on the full final document. A form-global style/storytelling change may legitimately reopen every paragraph in scope while preserving its factual approval.

### Feedback / dreaming
Runs after delivery or after repeated QA/manual corrections. It updates the **system**, not the business conclusion. Candidate improvements require a fixture and a versioned delta note.

### Retro-engineering
See [references/modes.md](modes.md). This mode is documented as TODO and excluded from production routing until its tests and contracts exist.

## Claims graph light

Use a lightweight graph.

Node types:
- `fragment`
- `claim`
- `decision`
- `recommendation`
- `unknown`

Edge types:
- `supports`
- `contradicts`
- `qualifies`
- `causes`
- `depends_on`
- `compares_to`
- `answers`
- `motivates`

The graph improves retrieval, deduplication, bridge detection, reranking and side-story placement. It remains small enough for manual inspection.

## Reranking

Default score dimensions, each 0–5:
- decision relevance: 30%
- evidence strength: 25%
- explanatory power: 20%
- novelty / non-redundancy: 15%
- audience fit: 10%

The score is a prioritization heuristic. Hard gates for contradictions, weak evidence and critical unknowns remain outside the weighted score.

## Scaffold rule

Define headings and payload type before prose.

For each section define:
- question answered;
- top claim IDs;
- preferred payload: prose | bullets | table | diagram | side story;
- maximum density;
- source coverage threshold;
- return/transition sentence.

## Final QA sequence

1. mode/baseline QA;
2. content-contract QA;
3. source QA;
4. stylistic lint;
5. diagram-fit check;
6. DOCX render;
7. inspect every page at 100%;
8. fix overlap/clipping/density/table widths;
9. rerender;
10. confirm template + fixture version compatibility;
11. deliver;
12. capture reusable feedback for dreaming.
