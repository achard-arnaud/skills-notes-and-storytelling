# Template — Architecture / strategic note

Use for deep architecture analysis where the decision may be primarily **technical, product or business**. Select one `analysis_dimension` before scaffolding; secondary dimensions may support the spine but must not silently replace it.

## Analysis dimensions

### `technical`
Use when the central question is system architecture, runtime, data flow, scalability, security, observability, sovereignty or technical economics.

Default sequence:
1. executive thesis;
2. system boundary;
3. component architecture;
4. runtime / event / data flow;
5. scalability and failure modes;
6. governance / security / audit;
7. operating model and economics;
8. open-source/private conjectures;
9. moat / strategic implications;
10. questions and next steps;
11. sources.

### `product`
Use when the central question is product strategy, user/job architecture, capabilities, use cases, adoption, differentiation, packaging or product operating model.

Default sequence:
1. executive thesis and product boundary;
2. user / client / job reality;
3. product capability architecture;
4. use-case portfolio and value paths;
5. adoption / workflow integration;
6. data / AI / platform dependencies;
7. governance and product ownership;
8. differentiation, alternatives and lock-in;
9. roadmap / strategic implications;
10. questions and next steps;
11. sources.

### `business`
Use when the central question is enterprise strategy, organizational design, transformation, governance, operating model, client model or capability building. This is the default dimension for a strategy note on a company’s AI/Data transformation when the architecture is primarily organizational rather than software-centric.

Default sequence:
1. **executive thesis** — one strategic reading, not an executive summary catalogue;
2. **why now / strategic context** — external and internal trigger, including dated transformation signals;
3. **trajectory** — reconstruct the sequence of capability building over time; preserve the difference between foundations, industrialization, scale and redesign;
4. **organizational architecture** — executive sponsorship, transformation axis, Data/AI/Digital core, IT/platform, businesses, control functions and decision rights;
5. **people as strategic evidence** — deepen only leaders whose mandate, prior experience or public signals explain the operating model; biography without explanatory value is removed;
6. **capability / operating-model architecture** — data, platform, governance, skills/adoption, portfolio/value management, agent/process orchestration, client/product layer;
7. **business transformation fronts** — separate employee augmentation, process redesign and client/product/service transformation when material;
8. **client / growth model** — explain how Data/AI connects to segmentation, distribution, service model, cross-business integration, revenue or differentiation;
9. **governance, sovereignty and economics** — decision rights, risk/legal/compliance/cyber, provider/model portability, value attribution, funding and ownership;
10. **counter-perspective / hard gates** — strongest credible failure paths: matrix complexity, proliferation, weak benefit ownership, adoption, lock-in/control migration, regulatory or sovereignty constraints;
11. **strategic implications / next phase** — state what phase the company is entering, what must become true, falsifiers and bounded next questions;
12. **sources**.

Business notes should reconstruct the company as a **capability system**, not a list of AI use cases. When evidence supports it, use a narrative such as `foundation → governance → platform → adoption → AI/GenAI → agents → process/service redesign`; do not force this sequence onto cases where the evidence contradicts it.

## Visual / diagram rules

- Use diagrams when they compress causal or organizational logic better than prose.
- For business notes, preferred diagram families are: transformation trajectory, functional operating model, capability stack, value-flow / client-model bridge, and governance/control plane.
- Render Mermaid/graph diagrams to images before Word insertion; never leave Mermaid source code in the reader-facing DOCX.
- Keep diagram labels short and move explanatory prose into the surrounding narrative or caption.
- Use vertical Mermaid orientation whenever the 30% transposition gate is triggered or horizontal scaling would materially reduce readability.
- Diagrams are evidence-backed analytical views. Mark reconstructed organization charts as `functional reconstruction` when reporting lines are not fully public.

## Business-note quality gates

A business-dimension note fails QA if it:
- reduces strategy to a use-case catalogue;
- names executives without explaining why their mandate or prior experience matters;
- confuses an inferred functional operating model with an official HR organization chart;
- omits the transformation trajectory or why-now when the evidence is time-dependent;
- discusses agents without identity, permissions, observability, ownership and value attribution when those are material;
- treats governance only as compliance instead of examining it as an operating capability;
- claims strategic differentiation without connecting it to client, operating or economic consequences;
- compresses away material evidence from an earlier canonical note during an iterative run.
