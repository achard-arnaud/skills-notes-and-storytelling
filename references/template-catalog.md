# Template catalog

| Enum | Primary decision | Orientation | Default length | Core payloads |
|---|---|---:|---:|---|
| ARCHITECTURE_NOTE | understand architecture, scale, risks, economics | portrait | 5–10 pp | diagrams, prose, side stories, tables |
| ONE_PAGER | fast executive orientation | portrait/landscape | 1 p | thesis, 3–5 facts, recommendation |
| TWO_PAGER | company/product/person or compact strategy | landscape | 2 pp | dense cards, comparison, CTA |
| BENCHMARKING | compare multiple options consistently | landscape | 2–6 pp | matrices, scoring, sensitivity |
| BUY_SIDE_GAP_ANALYSIS | adopt / replace / complement / partner | portrait/landscape | 4–8 pp | baseline, gap matrix, migration, TCO, risks |

## Architecture note
Use for technical architecture + operating model + scalability + business model. Put the strongest architecture diagram early. Use `analytical_focus` for conjectures and `method` for public/private evidence limits.

## One-pager
One dominant decision. Avoid a miniature report.

## Two-pager
Retains the existing "nice" philosophy: dense but readable, strong hierarchy, diagrams before weak prose, tables <=5 columns.

## Benchmarking
Requires identical evaluation criteria and evidence status per option. Scores remain heuristics unless externally validated.

## Buy-side gap analysis
Starts from the buyer's incumbent state. Evaluate replacement feasibility and organizational consequences before feature richness.

Required matrix rows should normally include:
- trigger/orchestration model;
- execution environment;
- integration surface;
- exception handling;
- observability and audit;
- identity/security;
- human-in-the-loop;
- deployment/sovereignty;
- migration effort;
- commercial model;
- operating ownership;
- proof required before scale.
