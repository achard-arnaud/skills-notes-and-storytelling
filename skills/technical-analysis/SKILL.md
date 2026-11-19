---
name: technical-analysis
description: Analyze a system, its architecture, integration, runtime, reliability, data flow, technical economics or proof of concept. Use for engineering decisions and technical reviews. Route user adoption to product-analysis, enterprise economics to business-analysis and legal applicability to regulatory-bootstrap.
---

# Technical analysis

1. Determine the system boundary, affected actors, interfaces, constraints, stage and decision. Separate observed behavior, target behavior, estimate and unknown.
2. Read the [method manifest](manifest.json) and the [shared analysis contract](../../references/domain-analysis.md). Select the applicable [decision profile](../../references/technical-decisions.md) by decision type and criticality, with the output format chosen independently. For a descriptive mandate, analyze the mechanism and failure modes without inventing an adoption decision.
3. Make the inputs, output, dependencies, ownership and error paths explicit. State which alternative or condition would overturn the conclusion. Preserve evidence scope, measurements, confidence limits and rollback facts.
4. Use the same analytical result in an ADR, integration note or technical section. Validate profile-specific constraints using the existing checker where relevant. Apply the [shared editorial and research review](../../references/editorial-and-research-quality.md), then verify the support actually delivered.

## Choose the support after analysis

For a short deliverable, stay in the direct path and choose a format for the reader with the [S3 route map](../../references/s3-operations.md). Reuse the [narrative selector](../selecting-narrative-schema/SKILL.md) for decision structure when useful. Supply a scoped findings packet, not the study corpus. A complete study starts from a brief and passes the same findings to A2. In either path, route each material gap to the evidence or method owner with a reference and an exit test. Keep editorial approval with the human.
