# Template — Integration note

## Purpose
Turn a validated relationship between products, companies or internal capabilities into a concrete `BUILD | BUY | PARTNER | COEXIST | DEFER` decision without confusing attractive synergy with executable integration.

Use after benchmark/opportunity/architecture/sell-side work when enough prior evidence exists. Reuse RunContext; do not restart broad research.

## Preflight
1. state the originating decision/bridge and reused claim/source IDs;
2. establish independent truth for every party/capability;
3. distinguish `overlap | complement | dependency | substitute | channel/partner`;
4. declare the **integration posture** separately from the strategic decision when useful: `embedded capability | admin surface | projection | runtime dependency | channel/partner | coexistence layer | other`;
5. list new evidence required before recommendation.

## Decision spine
1. recommendation + confidence + condition;
2. independent starting truths;
3. complementarity thesis and explicit overlap/conflict;
4. technical integration path;
5. product/use-case integration path;
6. business/GTM integration path;
7. operating model and responsibility boundaries;
8. lock-in/sovereignty map by stack, value-chain and process/control point;
9. `BUILD | BUY | PARTNER | COEXIST | DEFER` option matrix;
10. economics/value capture and dependency trade-off;
11. risks, unknowns and falsifiers;
12. smallest reversible pilot with acceptance/stop criteria;
13. counter-perspective verdict on the recommended path;
14. optional one-pass repair/narrowing + verification;
15. bridge to next decision only when material;
16. dreaming handoff: reusable integration/QA delta or `NO_REUSABLE_DELTA`.

## Technical lens
Capture:
- integration boundary and interfaces: API/event/file/DB/MCP or other evidenced mechanism;
- data ownership, schema, identity/auth and secrets;
- runtime/deployment and sovereignty;
- observability, support/SLA and failure ownership;
- migration/coexistence/rollback;
- lock-in location and credible exit path.

Do not invent an integration because both products expose APIs. Identify the exact control handoff and untested interface.

## Projection / admin-surface pattern

When the integration exists only to expose or administer a governed core, treat `projection / admin surface` as a distinct posture:
- the canonical system of record remains external to the integration surface;
- canonical IDs remain authoritative;
- schema mapping is explicit and versioned;
- provider-specific row/object IDs do not become business identity;
- writes are proposals or bounded mutations behind a merge/validation gate unless the architecture explicitly establishes otherwise;
- the core must remain operable when the projection/admin surface is removed.

Do not promote an admin surface into a new system of record by convenience.

## Product lens
Capture:
- combined user journey and 2–4 strongest joint use cases;
- overlap vs complementarity;
- UX/workflow ownership;
- onboarding/adoption;
- roadmap and release dependency;
- proof/acceptance mechanics;
- cannibalization or boundary confusion.

## Business lens
Capture:
- ICP/channel overlap and anti-fit;
- customer relationship and account ownership;
- build/buy/partner/co-distribution model;
- pricing, revenue share, services and value capture;
- GTM responsibilities and support obligations;
- moat gained vs strategic dependency created;
- evidenced distribution, ownership/investor or ecosystem links.

## Lock-in lens

Map technical and commercial lock-in, plus **operational habit/process lock-in** where humans may move canonical work into a more convenient external surface.

For every material control point capture:
- current owner/control point;
- control after integration;
- switching asset/cost;
- portability/exit mechanism;
- process or human habit that could make the dependency sticky even if data is exportable.

## Option matrix
Compare at least the plausible subset of:
`BUILD | BUY | PARTNER | COEXIST | DEFER`.

Criteria should normally include time-to-value, cost, control/sovereignty, capability gain, operating burden, reversibility, commercial upside and dependency risk. Hard gates precede scoring.

## Pilot contract
Every positive recommendation ends with a bounded pilot:
- hypothesis;
- representative use case;
- owner on each side;
- interface/boundary tested;
- success metric;
- acceptance threshold;
- stop condition;
- rollback/exit;
- evidence needed for scale decision.

The pilot is not optional prose: it is the mechanism that converts unresolved integration questions into testable evidence.

## Counter-perspective gate

Before delivery, challenge the recommended path against:
- native/no-tool or incumbent baseline;
- strongest rejected option;
- hidden operating burden;
- control migration / lock-in;
- failure ownership;
- one plausible reason the integration should not exist at all.

Return `SURVIVES_RED_TEAM | SURVIVES_WITH_NARROWING | PIVOT_REQUIRED | REOPEN_TARGETED`.

Loopback rules:
- `SURVIVES_RED_TEAM` → continue;
- `SURVIVES_WITH_NARROWING` → narrow once, then verify once;
- `PIVOT_REQUIRED` → change strategic decision or integration posture and return to the smallest affected option set;
- `REOPEN_TARGETED` → reopen only the failed hard gate or unresolved interface, not the entire upstream benchmark by default.

After a repair/narrowing pass, one verification pass is allowed. If it still fails materially, stop and escalate to targeted reopen or Tier 3 dreaming.

Create a dreaming loopback event only when the red-team finding or repair appears reusable beyond the current integration.

## Gates
Reject or defer when a critical security/sovereignty constraint, unsupported dependency, incompatible incentive, unclear data/customer/control ownership or unowned operating responsibility remains unresolved.

## Side stories
- `comparator`: another ecosystem pattern;
- `false_lead`: apparent synergy rejected at a concrete break point;
- `analytical_focus`: economics, control point or lock-in mechanism;
- `dezoom`: ecosystem/portfolio consequence;
- `method`: evidence boundary or untested interface.
