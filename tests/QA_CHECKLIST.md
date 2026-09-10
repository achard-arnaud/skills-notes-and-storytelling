# QA contract

A document passes only when all checks below are true.

## Run context / lifecycle
- [ ] generation mode declared;
- [ ] output_language resolved from explicit user choice or conversation-majority default;
- [ ] the same output_language is present in run context, scaffold, output spec and final QA;
- [ ] iterative runs identify canonical baseline, accepted language and review scope;
- [ ] template version matches the manifest;
- [ ] linked QA fixture supports the same template major version;
- [ ] workflow compatibility is current;
- [ ] feedback/dreaming changes remain candidate until explicit human promotion;
- [ ] retro-engineering remains TODO;
- [ ] action-plan remains TODO and cannot be invoked implicitly.

## Content
- [ ] executive answer present;
- [ ] every section answers a decision-relevant question;
- [ ] unsupported material claims absent;
- [ ] facts / inferences / hypotheses / recommendations distinguishable;
- [ ] account/target reality remains separate from product/seller truth until fit;
- [ ] hard gates precede scoring when fit is evaluated;
- [ ] side stories contain no new proof;
- [ ] analytical templates end with bounded validation/discussion options rather than implementation roadmaps.

## ICP / fit when material
- [ ] seven dimensions covered: problem, maturity, workflow, technical, organization, economics, timing;
- [ ] anti-ICP explicit;
- [ ] hard gates use PASS | OPEN | FAIL;
- [ ] sponsor / terrain / technical / veto lanes are explicit or unknown;
- [ ] at least one credible alternative considered;
- [ ] positive fit includes a falsifier.

## Language and terminology
- [ ] final prose remains coherent with output_language;
- [ ] avoidable foreign jargon replaced with natural equivalents;
- [ ] retained foreign technical terms are product names, standards, acronyms or precision-critical terms;
- [ ] first-use explanation added where a foreign term may confuse the reader;
- [ ] language_lint.py executed on the final DOCX and findings reviewed;
- [ ] harvest, catch-up, speed-up and hard gate are localized in French reader-facing prose unless explicitly justified.

## Style
- [ ] direct affirmative language preferred;
- [ ] 3+ item enumerations use bullets unless a table is stronger;
- [ ] comparisons use tables by default;
- [ ] table widths reflect content density;
- [ ] repeated rhetorical "not X but Y" constructions removed.

## Diagrams
- [ ] Mermaid source retained where Mermaid is used;
- [ ] rendered image embedded;
- [ ] labels readable at 100%;
- [ ] no node/edge overlap;
- [ ] scale factor >=0.70 OR orientation transposed and rerendered;
- [ ] diagram meaning unchanged after transposition.

## DOCX visual
- [ ] every page rendered;
- [ ] every PNG inspected at 100%;
- [ ] no clipping/overlap;
- [ ] no broken rows/tables;
- [ ] no orphan headings;
- [ ] body >=9 pt;
- [ ] sources readable;
- [ ] final render performed after last edit.

## Template-specific
### Diagnostic/reco sell-side
- [ ] diagnosis precedes recommendations;
- [ ] seven-dimensional ICP and anti-ICP explicit;
- [ ] proof/acceptance mechanics explicit;
- [ ] pricing/packaging and expansion logic explicit;
- [ ] competitive threat separated from migration opportunity;
- [ ] recommendations include rationale, evidence and validation question/falsifier;
- [ ] no 30/60/90 implementation plan.

### Opportunity note ICP
- [ ] target reality researched independently from product truth;
- [ ] hard gates evaluated before fit score;
- [ ] partnership scenarios use a consistent scenario canvas when relevant;
- [ ] capability gaps mapped to outcomes;
- [ ] alternatives considered;
- [ ] sponsor/terrain/veto lanes explicit or unknown;
- [ ] next step is a bounded demo/workshop/validation rather than an implementation roadmap.

## Publication
- [ ] reusable changes include an updated regression fixture;
- [ ] template/mode manifest passes version checks;
- [ ] CI is green on the integration branch before promotion.
