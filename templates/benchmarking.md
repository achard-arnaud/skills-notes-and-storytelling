# Template — Benchmarking

## Purpose
Compare 2+ credible options for a concrete decision without allowing category mismatch, feature breadth or weak evidence to manufacture a winner.

## Benchmark profile
Declare one primary profile before research:
- `technical` — architecture, integration, operations, license, TCO, portability/sovereignty;
- `product` — use cases, UX/capabilities, positioning, pricing/value, 4P, ICP/GTM, moat;
- `business` — market, business model, value chain, Porter/RIOT/7S where decision-relevant, distribution, economics, moat.

Mixed benchmarks are allowed, but weights and hard gates must state which decision they serve.

## Decision spine
1. **Reframe the problem** — decision, horizon, constraints, current baseline and smallest useful scope.
2. **Axes proposal / HITL checkpoint** — propose research/comparison axes; request validation/completion when interaction is available. If not, record defaults as assumptions.
3. **Peer discovery** — direct alternatives first; then European/sovereign peers and adjacent substitutes where relevant.
4. **Category normalization** — classify candidates before scoring. Storage engine, admin UI and backend platform, for example, are not interchangeable categories.
5. **Hard gates** — eliminate or quarantine candidates that fail non-negotiables before weighted scoring.
6. **Evidence matrix** — identical criteria and evidence status for comparable candidates.
7. **Initial ranking** — transparent weights, confidence and missing evidence.
8. **Deep dive / adversarial pass** — challenge the apparent winner and strongest alternative; search for disconfirming evidence.
9. **Overlap test** — if candidates do not overlap enough for one fair matrix, split into clusters or fallback paths rather than force a winner.
10. **Lock-in / sovereignty map** — locate control points, switching assets, portability and exit path.
11. **Ecosystem / complementarity pass** — separate competitor/substitute ranking from potential technical, product, distribution or ownership complementarity.
12. **Recommendation** — best current path, fallback, migration/reevaluation trigger and falsifiers.
13. **Closure state** — decide `CLOSED | CLOSED_WITH_CHALLENGE_GATE | REOPEN_TARGETED`.
14. **Bridge** — integration note for complementarity/coexistence; buy-side gap for winner vs incumbent; architecture note for unresolved feasibility.
15. **Dreaming handoff** — record whether the red-team produced a reusable benchmark/closure improvement or only changed this decision.

## Closure discipline

A benchmark should stop when further peer discovery has lower information value than a bounded implementation or pilot.

Use:
- `CLOSED` when the decision is sufficiently established for the next action;
- `CLOSED_WITH_CHALLENGE_GATE` when a preferred option exists but should be red-teamed against real implementation before execution;
- `REOPEN_TARGETED` when one named hard gate or uncertainty invalidates the current conclusion.

After closure:
- preserve the native/no-tool or incumbent baseline as fallback;
- convert unresolved implementation questions into pilot questions;
- do not add more peers unless a named hard gate requires it;
- carry falsifiers, exit path and challenge gates into the downstream Integration or Architecture Note.

If the downstream implementation red-team returns `PIVOT_REQUIRED`, closure is revoked only for the invalidated decision dimension. Do not restart the full market scan by default.

## Counter-perspective / adversarial pass

The pass must attack the decision rather than merely list weaknesses.

At minimum challenge:
- the apparent winner;
- the strongest credible alternative or native baseline;
- one category/framing assumption;
- one hidden hard gate, lock-in or operating burden that could reverse the recommendation.

Return `SURVIVES_RED_TEAM | SURVIVES_WITH_NARROWING | PIVOT_REQUIRED | REOPEN_TARGETED`.

When `SURVIVES_WITH_NARROWING`:
- narrow once;
- verify once;
- then close or reopen.

When `PIVOT_REQUIRED` or `REOPEN_TARGETED`:
- name exactly which criterion, hard gate or category assumption failed;
- update only the affected shortlist/decision space;
- create a dreaming loopback event only if the failure suggests a reusable benchmark rule.

Do not keep exploring once the remaining uncertainty can only be resolved by code, pilot, migration rehearsal, procurement, customer discovery or another bounded experiment.

## Default research preferences — overridable
When the user has not supplied alternatives, prefer candidates that are credible for the stated context. For software/technical decisions, explicitly inspect:
- current license class and change risk; MIT/Apache-2.0 may be preferred when sovereignty/portability matters but are not universal hard gates;
- self-host/on-prem or credible export path when sovereignty matters;
- European peers when relevant to the decision;
- real use cases and moat, not feature lists;
- fit to organization size, operating capacity and time-to-value.

Do not hard-code company size, geography or license as universal exclusions.

## Scoring
Scores are heuristics unless an externally validated scale exists. Hard gates remain outside weighted scoring. Show sensitivity when a reasonable change in weights can reverse the winner.

## Required outputs
- decision and corrected problem statement;
- candidate/category map;
- hard gates;
- comparison matrix;
- shortlist + fallback;
- uncertainty/sensitivity;
- lock-in location + exit path where material;
- complementarity/ecosystem findings kept separate from ranking;
- recommendation + falsifiers + reevaluation trigger;
- counter-perspective verdict;
- closure state and exact reopen condition;
- red-team repair/verification result when applicable;
- dreaming loopback event or `NO_REUSABLE_DELTA`;
- auto-critique: missing peers, weak claims, category bias, evidence that could reverse the result.

Default comparison presentation is a table with density-aware widths.
