# Cross-template bridges, integration note and run memory

## Principle

A delivered note is a decision node, not a terminal artifact. After its decision is stable, the run evaluates whether the evidence already collected supports a bounded next decision. This is **nudging by bridge**: reuse validated context without silently extending the conclusion.

Bridges are optional outputs of every template, but bridge evaluation is mandatory. Zero bridge is a valid result.

## Run memory / provenance contract

Persist or carry forward a compact `RunContext` independent from document layout:

- decision question and active persona/audience;
- source ledger with source class, date, authority and access status;
- atomic fragments and evidence status;
- claims, contradictions, unknowns and typed graph edges;
- rejected alternatives and hard-gate decisions;
- scoring/reranking criteria and sensitivity assumptions;
- selected recommendation, confidence and falsifiers;
- entities/products/accounts studied;
- lock-in map by value-chain / technical-stack layer;
- unresolved questions and validation experiments;
- template + workflow + fixture versions;
- bridge candidates and their evidence coverage.

A downstream note imports this context as **prior evidence**, not as fresh truth. Time-sensitive claims are revalidated; inferred claims keep their status; rejected alternatives remain visible so the next run does not rediscover them as novel.

## Source classification

At minimum classify evidence as:

`primary_vendor | primary_regulatory | primary_repo | customer_or_partner | analyst_or_research | community | supplied_context | internal_inference`

Also classify its analytical role:

`account_truth | product_truth | market_peer | technical_dependency | commercial_model | ownership_or_distribution | risk_or_constraint`.

This allows retrieval/reranking by the next template without flattening all research into prose.

## Bridge contract

A bridge contains:

- `from_template` and originating decision;
- `to_template`;
- `why_next`;
- evidence/claim IDs reused;
- new evidence required;
- assumptions that must not be promoted to fact;
- decision question for the next note;
- stop condition / falsifier;
- estimated effort: `light | standard | deep`.

Default rule: prefer the **smallest reversible next decision**. Do not generate a new report merely because another template exists.

## Default bridge map

| From | Typical next bridge |
|---|---|
| Architecture note | benchmarking for alternatives; integration note for implementation/partner path; one-pager for executive decision |
| One-pager | deeper source template only when the compressed decision exposes a material unknown |
| Two-pager | opportunity note for target fit; integration note for concrete partnership/integration; sell-side diagnostic for GTM work |
| Benchmarking | buy-side gap analysis for winner vs incumbent; integration note for coexistence/complementarity; architecture note for unresolved technical feasibility |
| Buy-side gap analysis | integration note for `buy/build/partner` execution; architecture note for migration design; one-pager for approval |
| Sell-side diagnostic | opportunity note for a named ICP/account; benchmarking for competitive validation; integration note for co-distribution/partner strategy |
| Opportunity note ICP | integration note for pilot/partnership; buy-side analysis when buyer adoption becomes the question; two-pager for meeting preparation |
| Integration note | architecture note for deep implementation; opportunity note for partner/account validation; one-pager for go/no-go approval |
| Closing | opportunity/company research when mandate truth is weak; updated closing after debrief; opportunity note for a validated target; no bridge after explicit no-go |

`CLOSING` is also a common destination from a company/architecture note, two-pager, opportunity note or sell-side diagnostic when a specific consequential conversation is scheduled. Carry evidence lineage and unknowns; do not turn the prior note's inference into a conversation fact.

## Integration note

### Purpose

Turn a validated relationship between two or more products, companies or internal capabilities into a concrete `BUILD | BUY | PARTNER | COEXIST | DEFER` decision. It is the canonical destination for ecosystem/complementarity findings and for many post-benchmark nudges.

### Three lenses

**Technical**
- integration boundary and control points;
- APIs/events/data/auth/runtime dependencies;
- deployment, sovereignty and security;
- observability, support and failure ownership;
- migration/coexistence/rollback;
- lock-in location in the stack and exit path.

**Product**
- combined use cases and user journey;
- capability overlap vs complementarity;
- who owns UX, workflow and product roadmap;
- onboarding/adoption implications;
- proof/pilot and acceptance criteria;
- cannibalization or product-boundary risk.

**Business**
- build/buy/partner/co-distribute options;
- ICP and channel overlap;
- value capture, pricing/revenue-share and services;
- GTM motion and ownership of customer relationship;
- strategic moat vs dependency;
- ownership/investor/distribution links when evidenced.

### Decision spine

1. decision and recommended relationship;
2. starting truths for each party/capability;
3. complementarity thesis and explicit overlap;
4. technical integration path;
5. product/use-case integration path;
6. business/GTM integration path;
7. lock-in and sovereignty map by stack/value-chain layer;
8. build/buy/partner/coexist/defer alternatives;
9. economics and operating ownership;
10. risks, conflicts and falsifiers;
11. smallest reversible pilot;
12. bridge to the next decision if evidence supports it.

### Hard gates

Do not recommend integration when a critical security/sovereignty constraint, unsupported technical dependency, incompatible commercial incentive, unclear data/control ownership or unowned operating responsibility remains unresolved.

## Lock-in mapping

Do not reduce lock-in to a single high/medium/low score. Locate it.

Technical layers may include:
`data | schema | identity | API/protocol | workflow/orchestration | runtime | model | observability | deployment/cloud | admin/UI`.

Value-chain layers may include:
`IP | product experience | implementation/services | distribution/channel | customer relationship | pricing/billing | support/SLA | capital/ownership`.

For each material lock-in record:
- control point;
- switching asset/cost;
- portability mechanism;
- contractual/licensing constraint;
- credible exit path;
- medium/long-term sovereignty implication.

## Dreaming is part of the normal run

After delivery and bridge evaluation, execute a lightweight dreaming pass even when the user did not request it. It must not silently mutate canonical behavior.

The pass asks:
1. What failed, surprised or required manual correction?
2. What successful adaptation appears reusable?
3. Is the delta case-specific, template-specific or workflow-wide?
4. Which existing fixture would have caught it?
5. Is a new regression fixture or candidate patch justified?

Output may be `NO_REUSABLE_DELTA`. Promotion remains human-governed.
