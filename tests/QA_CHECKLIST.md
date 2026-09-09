# QA contract

A document passes only when all checks below are true.

## Mode / lifecycle
- [ ] generation mode declared;
- [ ] iterative runs identify canonical baseline and review scope;
- [ ] template version matches the manifest;
- [ ] linked QA fixture supports the same template major version;
- [ ] workflow compatibility is current;
- [ ] feedback/dreaming changes remain candidate until explicit human promotion;
- [ ] retro-engineering mode remains TODO unless its implementation gate is deliberately changed.

## Content
- [ ] executive answer present;
- [ ] every section answers a decision-relevant question;
- [ ] unsupported material claims absent;
- [ ] facts / inferences / hypotheses / recommendations distinguishable;
- [ ] account/buyer reality remains separate from seller/product truth until fit;
- [ ] side stories contain no new proof;
- [ ] next-step nudges are bounded and useful.

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
- [ ] ICP and anti-ICP explicit;
- [ ] proof/acceptance mechanics explicit;
- [ ] pricing/packaging and land-expand path explicit;
- [ ] competitive threat separated from migration opportunity;
- [ ] recommendations include owner, metric, falsifier or validation question.

### Opportunity note ICP
- [ ] target reality researched independently from product truth;
- [ ] hard gates evaluated before fit score;
- [ ] capability gaps mapped to product outcomes;
- [ ] alternatives considered;
- [ ] sponsor/terrain/veto lanes explicit or marked unknown;
- [ ] representative proof is reversible and measurable.

## Publication
- [ ] reusable changes include an updated regression fixture;
- [ ] template/mode manifest passes version checks;
- [ ] CI is green on the integration branch before promotion.
