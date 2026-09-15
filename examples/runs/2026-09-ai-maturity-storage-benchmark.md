---
template_type: benchmarking
template_version: 0.2.0
fixture_version: 0.2.0
workflow_version: 1.1.0
run_type: real_case_qa
source_project: achard-arnaud/ai-maturity-diagnostic
---

# Real-case QA — storage backend benchmark for AI Maturity Diagnostic

## Decision question
Select a low-cost, low-friction persistence/admin option for a vibe-coded mini-CRM with roughly 5,000 records across about 10–15 entity families, while preserving portability and avoiding unnecessary infrastructure.

## Baseline facts to verify before scoring
- The project is local-first and currently exposes a lightweight Python HTTP control plane.
- The repository persists important business truth in structured files and generated artifacts; persistence is explicitly still a productization gate.
- At this scale, raw database capacity is not the limiting factor. The decision is primarily about canonical persistence, CRUD/admin ergonomics, integration effort, portability, and license/hosting constraints.
- Never assume an existing SQLite deployment merely because another analysis says so: inspect the repository and distinguish current code from proposed architecture.

## Default hard gates
1. Cost suitable for a small internal / early-stage deployment.
2. Integration must be realistic for the current Python/local-first stack.
3. License and redistribution constraints must be explicitly classified: OSI open source, source-available/fair-code, or proprietary.
4. Data must remain exportable through standard formats or a standard relational database.
5. Operational burden must be proportionate to ~5,000 records.

## Weighted criteria after gates
| Criterion | Weight |
|---|---:|
| Integration effort / time-to-working | 35% |
| Total cost at target scale | 30% |
| Admin / CRUD ergonomics for non-developers | 15% |
| Portability / sovereignty / self-hostability | 10% |
| Migration path and ecosystem fit | 10% |

## Mandatory candidate families
The research pass must cover, at minimum:
- native SQLite with a deliberately small admin layer or generated CRUD;
- managed PostgreSQL with a free/cheap tier;
- spreadsheet-like open-source database/admin products (for example Baserow, Grist, Teable where fit is credible);
- backend-as-a-service candidates such as PocketBase or Supabase only when their extra capabilities justify their operational cost;
- source-available candidates such as NocoDB or Directus only with current license and database-support verification.

## Required challenge of supplied baseline answer
A supplied comparator answer recommends Directus on top of an existing SQLite database, with managed PostgreSQL as fallback. QA must independently verify:
- whether the repository actually has the asserted SQLite database and what it stores;
- whether the current Directus release supports SQLite as a production database and can wrap an arbitrary existing SQLite schema without migration;
- the current Directus license category;
- whether an admin UI is truly the primary problem or whether canonical persistence/schema consolidation is still missing;
- whether simpler options (native SQLite + SQLModel/SQLAlchemy + a tiny admin, Grist/Baserow/Teable, PocketBase) dominate on effort and cost.

## Expected output shape
1. Correct the problem statement before comparing tools.
2. Separate `storage engine`, `admin/UI`, and `backend platform`; do not compare them as if they were identical product categories.
3. Build the common comparison matrix only after category normalization.
4. Produce a shortlist with a clear best-fit path for the present state plus a migration trigger for the next architecture.
5. Include one explicit falsifier per shortlisted option.
6. Finish with an auto-critique pass: missing peers, weak claims, sensitivity to assumptions, and what additional repository evidence would change the recommendation.

## Regression checks
- identical criteria across shortlisted options;
- hard gates before weighted scoring;
- current primary-source verification for license, database support, limits and pricing;
- facts from the target repository distinguished from assumptions and from proposed future architecture;
- recommendation remains valid if record count changes from 5,000 to 50,000 unless a stated trigger is crossed;
- no feature-rich platform wins merely because it has more capabilities than the use case needs;
- recommendation includes fallback path and falsifier;
- auto-critique can downgrade the initial winner when a critical baseline claim is disproved.
