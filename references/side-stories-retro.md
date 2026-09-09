# Side stories — retrodocumentation and business-note adaptation

This pattern is harvested from `tourisme-etude-historico-geographique/skills/composing-side-stories`.

## Original invariant retained

A side story is a **composition artifact, never new proof**.

It survives outside the causal trunk because it improves interpretation, comparison, method transparency or reader navigation.

Lifecycle:
`candidate → validated → promoted → retired`

Every promoted side story has:
- stable ID;
- kind;
- purpose/payoff;
- lineage to existing claims/fragments/sources;
- insertion anchor;
- return-to anchor;
- evidence status;
- reader eligibility.

## Adaptation used in the Plasma / AstraForge notes

The current note format implicitly created six useful classes:

### dezoom
Moves from the local mechanism to a wider operating-model or business-model consequence.

Typical payload:
- platform implication;
- organizational implication;
- portfolio consequence;
- second-order effect.

### analytical_focus
A bounded deep dive on a mechanism, conjecture or architectural/economic implication.

Use when:
- the mechanism matters to the decision;
- it is too narrow for a full section;
- it requires explicit caveats and evidence status.

### false_lead
Captures a tempting analogy, then identifies the exact point where it fails.

Business examples:
- "event-triggered workflow" ≠ "event-native choreography";
- "open source" ≠ "zero switching cost";
- "proof of done" ≠ "business outcome proof".

### comparator
A bounded product/vendor comparison attached to the same decision criterion.

Requires:
- common criterion;
- starting-condition differences;
- major confounders;
- explicit takeaway.

### method
Explains scoring, source limits, or research method.

Use for:
- heuristic scoring caveat;
- incomplete public-runtime evidence;
- vendor-claimed metrics;
- pricing assumptions.

### callback
Reconnects a later finding to a thread introduced earlier.

Use sparingly to maintain continuity in long notes.

## Routing rule

Core decision claim?
→ main spine.

Mechanism necessary to explain a core claim?
→ bridge or analytical focus.

Useful comparison that does not alter the core conclusion?
→ comparator.

Tempting but invalid equivalence?
→ false lead.

Wider consequence?
→ dezoom.

Evidence/scoring caveat?
→ method.

## Buy-side mapping

For `BUY_SIDE_GAP_ANALYSIS`:
- `false_lead`: rejects superficial feature parity;
- `comparator`: compares incumbent and challenger on one operating criterion;
- `analytical_focus`: TCO, migration or control-plane mechanism;
- `dezoom`: enterprise portfolio / operating-model effect;
- `method`: confidence, unknown pricing, vendor evidence;
- `callback`: returns to purchase or replacement decision.

Side stories must never upgrade conjecture into fact.
