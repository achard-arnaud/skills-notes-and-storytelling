---
template_type: architecture-note
template_version: 1.2.0
fixture_version: 1.0.0
workflow_version: 1.3.1
analysis_dimension: business
fixture_role: nrt
drift_policy: bounded
case: ODDO BHF AI/Data strategy and operating model
---

# Business architecture note NRT — ODDO BHF

## Purpose

Replay this fixture when changing `SKILL.md`, `templates/architecture-note.md`, template routing, business-dimension scaffolding, diagram/render rules, evidence handling or iterative compression. It is a business-dimension non-regression test, not a canonical source of current ODDO BHF facts.

Time-sensitive facts MUST be revalidated on replay. The fixture protects the analytical shape and decision value, not stale claims.

## Required run mode

- `GenerationMode`: `FROM_SCRATCH` for full replay; `ITERATIVE` for regression against a prior output.
- `analysis_dimension`: `business`.
- `template`: `ARCHITECTURE_NOTE`.
- reader-facing artifact: DOCX when artifact rendering is exercised.

## Decision thesis to preserve

The note must test whether the company is building a standalone AI vertical or a transverse Data/AI capability embedded in strategy, transformation, IT/platforms, businesses and control functions. The answer may change with new evidence, but the run must explicitly resolve this organizational question.

## Mandatory business spine

The replay must contain, when evidence remains available:

1. executive thesis and why-now;
2. multi-year Data/AI trajectory rather than a flat use-case inventory;
3. functional organizational architecture with official-vs-inferred boundaries;
4. people-as-evidence: named leaders only when their mandates/background explain strategy, decision rights or operating model;
5. capability stack from data/knowledge foundations through platform/governance/adoption to assistants/agents and process/service redesign;
6. distinct transformation fronts for employee augmentation, process redesign and client/service differentiation;
7. client/growth/organizational-model implications;
8. governance as operating capability, including agent identity, permissions, observability, HITL, lifecycle and value ownership when agentic scope is material;
9. economics/value attribution and the move beyond use-case counts;
10. hard gates covering decision rights, agent/tool proliferation, lock-in/sovereignty, adoption/process redesign and value attribution;
11. strongest counter-perspective with an explicit verdict;
12. open questions required to move from public strategic reading to operating-model audit;
13. sources and evidence-status boundaries.

## Diagram NRT

A business replay should normally generate at least three decision-bearing diagrams when evidence supports them:

- trajectory: foundations -> industrialisation -> scale -> redesign;
- functional operating model: executive sponsorship -> transformation/Data-AI -> Data/Digital/Data Office/IT -> businesses and control functions;
- capability stack: data/knowledge -> platform/governance -> adoption/portfolio -> assistants/agents -> process/service redesign.

Diagram source may be Mermaid or equivalent graph source. In reader-facing DOCX, render diagrams as images; do not expose raw Mermaid as the primary artifact. Every figure needs a caption and must remain legible at normal page scale.

## Content-preservation NRT

An `ITERATIVE` replay fails if formatting, compression or template migration silently removes a material canonical claim without one of:

- explicit scope instruction;
- evidence invalidation;
- contradiction resolution;
- deliberate replacement by a stronger claim preserving the same decision function.

In particular, do not lose trajectory, organizational architecture, people-as-evidence, transformation fronts, client/growth implications, governance, hard gates, counter-perspective or open validation questions merely to reduce page count.

## Evidence and people NRT

- Exact HR reporting lines must not be invented from functional proximity.
- Public role/mandate = fact when sourced.
- Functional placement without explicit reporting evidence = inference.
- Biography must be pruned unless it changes interpretation of strategy, ownership, capability or risk.
- Current roles and time-sensitive strategy claims must be refreshed on replay.

## Storytelling NRT

The note must read as a causal business story, not as disconnected sections:

`data foundations -> governance/platform -> leadership/operating model -> adoption -> agents -> process/service redesign -> client/growth implications -> orchestration hard gates`.

Bounded side stories may deepen the argument (`dezoom`, `analytical_focus`, `false_lead`, `comparator`) but may not create proof.

## Reader-facing style NRT

When rendered as DOCX:

- portrait strategic-note layout by default;
- strong executive thesis and bottom-line blocks;
- restrained navy/teal semantic palette;
- author/template metadata in header when configured;
- repository attribution in footer when configured;
- diagrams executed as images;
- tables used for parallel decision facts, prose for causal reasoning;
- no orphan source-only page when avoidable without destructive compression;
- sources remain compact and auditable.

## Failure conditions / drift alarms

Fail or flag the replay when any of the following occurs:

- business mode falls back to component/runtime architecture as the dominant spine;
- output becomes a use-case catalogue;
- people section becomes an executive biography directory;
- functional reconstruction is presented as an official org chart;
- agentic strategy omits identity/permissions/orchestration/observability/value ownership;
- client/growth implications disappear despite material evidence;
- counter-perspective becomes generic risk boilerplate;
- diagrams become decorative rather than decision-bearing;
- iterative compression removes material claims without an evidence/scope reason;
- current facts are reused from this fixture without revalidation.

## Expected closure

The replay should end with:

- a bounded strategic bottom line;
- explicit uncertainty;
- a counter-perspective verdict;
- the smallest set of questions/evidence needed for the next operating-model audit.

The exact company conclusion is NOT frozen. The decision architecture and evidence discipline are.