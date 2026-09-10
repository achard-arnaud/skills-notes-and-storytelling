# Governed writing workflow

## Common state machine

```text
RUN_CONTEXT_SET
→ RESEARCHED
→ FRAGMENTED
→ CLAIMS_GRAPHED
→ RERANKED
→ SCAFFOLDED
→ DRAFTED
→ SIDE_STORIES_ROUTED
→ SOURCED
→ LANGUAGE_QA_PASSED
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
| Run context | request + conversation | mode + output_language + decision + audience | output language resolved |
| Research | decision question + scope | source ledger | sources sufficient or limits stated |
| Fragments | source ledger | atomic fragments | one evidence unit per fragment |
| Claims graph light | fragments | claims + typed edges | every claim has lineage |
| Rerank | claims | ranked claim set | low-value duplicates pruned |
| Scaffold | ranked claims + output_language | section skeleton | each section has purpose/payoff |
| Fill | scaffold + fragments | prose/bullets/tables | no unsupported material assertion; language preserved |
| Side stories | coherent trunk | routed side stories | bounded + return anchor |
| Sourcing | complete draft | source-complete draft | material claims traceable |
| Language QA | draft + output_language | lint/review result | linguistic coherence + anti-jargon reviewed |
| Layout | content spec | DOCX-ready spec | template/version/language contract satisfied |
| DOCX QA | DOCX | QA report | every page visually clean |
| Nudging | delivered analysis | next analytic validation | no hidden action-plan expansion |
| Feedback | output + human/QA delta | feedback ledger | reusable vs case-specific separated |
| Dreaming | feedback ledger + fixtures | candidate patch | human promotion required |

## Language continuity

Set `output_language` once in the run context.

Default resolution:
1. explicit user instruction;
2. otherwise majority natural language of the conversation when the skill is called.

Ignore URLs, code, quoted source blocks, proper product names and isolated technical identifiers.

Propagate the same language value through:
- run context;
- scaffold;
- output spec;
- draft;
- language lint;
- final DOCX proofreading;
- QA report.

A language change requires an explicit user instruction or a new run context.

## Analysis/action boundary

The current production templates are analytical.

They may end with:
- decision;
- recommendation;
- discussion scenario;
- validation question;
- falsifier;
- demo/workshop/proof suggestion;
- next analytical artifact.

They must not automatically emit:
- 30/60/90-day plans;
- project calendars;
- task backlogs;
- owner-by-owner delivery plans.

Those belong to the future `ACTION_PLAN` template, derived only after an upstream analysis is accepted.

## Mode-specific preflight

### From scratch
Start with a blank decision spine. Every material statement flows from sourced fragments into claims before the scaffold.

### Iterative
Resolve a canonical baseline before research. Record:
- accepted content;
- accepted evidence status;
- accepted layout/template version;
- accepted output language;
- requested delta;
- form-global changes.

Preserve accepted material outside review scope and rerun full final QA.

### Feedback / dreaming
Runs after delivery or repeated QA/manual corrections. It updates the system, not the business conclusion. Candidate improvements require a fixture and a versioned delta note.

### Retro-engineering
Documented as TODO and excluded from production routing.

## Claims graph light

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

## Reranking

Default score dimensions:
- decision relevance: 30%
- evidence strength: 25%
- explanatory power: 20%
- novelty/non-redundancy: 15%
- audience fit: 10%

Hard gates remain outside weighted scoring.

## Scaffold rule

For each section define:
- question answered;
- top claim IDs;
- preferred payload;
- maximum density;
- source coverage threshold;
- transition/return sentence;
- output language.

## Final QA sequence

1. run-context/mode QA;
2. content-contract QA;
3. ICP/gate QA when relevant;
4. source QA;
5. language coherence + anti-jargon lint;
6. stylistic lint;
7. diagram-fit check;
8. DOCX render;
9. inspect every page at 100%;
10. fix overlap/clipping/density/table widths/language drift;
11. rerender;
12. confirm template + fixture + workflow compatibility;
13. deliver;
14. capture reusable feedback.
