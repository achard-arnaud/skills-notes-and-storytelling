---
title: "AstraForge Wedge — DevFactory"
analysis_dimension: "product"
generation_mode: "FROM_SCRATCH"
template: "ONE_PAGER"
maturity: "first-wedge"
source_date: "2026-09-18"
---

# DevFactory
## Software delivery acceleration under control

> **Status:** AstraForge's explicit **First Wedge**  
> **Job to be done:** Let AI workers participate in software delivery end-to-end without surrendering enterprise control.  
> **Primary value:** Faster software delivery with inspectable artifacts, approval gates and full execution traceability.

## Problem

Coding agents can already write code, tests and migrations. The enterprise problem begins when those agents must act over real repositories, files, pipelines and release processes.

The operational questions become:

- What may the agent access?
- Which work can run autonomously?
- Which changes require approval?
- How is parallel agent work coordinated?
- What evidence proves what happened?
- Can the run be reproduced or audited later?

## AstraForge pattern

```text
Epic / request
   ↓
Planning Agent
   ↓
Scoped task graph
   ↓
SWE Swarm
 ├─ Frontend
 ├─ Backend
 └─ DBA
   ↓
Review Agent
   ↓
Approval Gate
   ↓
Deploy Agent
   ↓
Release artifact + audit trail
```

The public product example exposes artifacts such as `tasks.json`, `ui_components.tsx`, `api_routes.ts`, `migration_04.sql`, `review.md` and `release.tar`.

## Core capabilities used

- agent sandboxing;
- scoped access / RBAC;
- parallel specialized agents;
- workflow orchestration;
- artifact generation;
- review dependency handling;
- human approval gates;
- audit logs;
- shared execution memory.

## Typical use cases

DevFactory is the umbrella wedge for:

1. **Operational Automation**
2. **Runbook Execution**
3. **Incident Handling**

It can also logically cover — **inference, not separately named on the public site** — feature implementation, migration work, test generation, refactoring and release preparation where the same controlled execution pattern applies.

## Buyer / user hypothesis

**Economic buyer:** CTO, VP Engineering, Platform Engineering leadership, Head of AI Platform.  
**Users:** software engineers, platform teams, DevOps/SRE, engineering managers.

## Value equation

```text
delivery speed
+ parallel agent execution
+ reduced repetitive engineering effort
+ lower supervision burden
+ controlled production risk
= DevFactory value
```

## Hard gate

DevFactory only differentiates materially if AstraForge governs **real execution** rather than merely planning work that is then performed elsewhere.

## Evidence status

**Fact:** DevFactory is explicitly named by AstraForge as the "First Wedge".  
**Fact:** The site shows Planning Agent → SWE Swarm → Review Agent → Deploy Agent.  
**Inference:** The broader feature/refactor/migration envelope follows from the demonstrated primitives but is not separately named as a marketed SKU.

**Primary source:** https://astraforgeos.ai/ — accessed 2026-09-18.
