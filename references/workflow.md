# Governed writing workflow

## State machine

```text
RESEARCHED
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
→ DREAMING_CANDIDATE (optional)
```

Each transition has an input contract, output contract and stop condition.

| Stage | Required input | Output | Gate |
|---|---|---|---|
| Research | decision question + scope | source ledger | sources sufficient or limits stated |
| Fragments | source ledger | atomic fragments | one idea/evidence unit per fragment |
| Claims graph light | fragments | claims + typed edges | every claim has lineage |
| Rerank | claims | ranked claim set | low-value duplicates pruned |
| Scaffold | ranked claims | section skeleton | each section has purpose/payoff |
| Fill | scaffold + fragments | prose/bullets/tables | no unsupported material assertion |
| Side stories | coherent trunk | routed side stories | detours bounded + return anchor |
| Sourcing | complete draft | source-complete draft | material claims traceable |
| Layout | content spec | DOCX-ready spec | template contract satisfied |
| DOCX QA | DOCX | QA report | every page visually clean |
| Nudging | delivered decision | next-step set | bounded, decision-relevant follow-ups |
| Dreaming | run + QA deltas | candidate template patch | human promotion required |

## Claims graph light

Use a lightweight graph, not a full ontology.

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

The graph exists to improve retrieval, deduplication, bridge detection and reranking. It remains small enough to inspect manually.

## Reranking

Default score dimensions, each 0–5:
- decision relevance: 30%
- evidence strength: 25%
- explanatory power: 20%
- novelty / non-redundancy: 15%
- audience fit: 10%

Treat the score as a prioritization heuristic. Preserve explicit hard gates for contradictions, weak evidence and critical unknowns.

## Scaffold rule

Draft headings and payload type before prose.

For each section define:
- question answered;
- top claim IDs;
- preferred payload: prose | bullets | table | diagram | side story;
- maximum density;
- source coverage threshold;
- return/transition sentence.

## Final QA sequence

1. content-contract QA;
2. source QA;
3. stylistic lint;
4. diagram-fit check;
5. DOCX render;
6. inspect every page at 100%;
7. fix overlap/clipping/density/table widths;
8. rerender;
9. confirm contract compliance;
10. deliver.
