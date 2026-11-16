# Reusable two-pager renderer

This package provides the HTML/CSS binding and print pipeline for the business two-pager. It is case-agnostic: all facts, labels, card bodies, flow steps and section titles arrive in JSON. The reusable business spine is specified in references/business-two-pager.md; binding and tokens are specified in references/two-pager-rendering.md.

## Layout and tokens

- templates/document.html.j2: composition and semantic content slots.
- assets/theme.css.j2: shared layout, print rules, evidence colors and typography.
- themes/business-corporate.json: page geometry, font and spacing tokens.
- palettes/business-corporate.json: evidence-aware semantic colors.
- scripts: build, PDF/PNG render and DOM layout QA.

Use three cards and a flow plus three columns on page 1; use a due-diligence layout on page 2 only when the question requires it. Re-label and re-order content through JSON. Do not add named employers, vendors, products, customers or candidate data to this package.

## Run

Install requirements in an isolated project environment, ensure Chromium is available, and run from the repository root:

python renderers/two_pager_nice/scripts/cli.py all <content.json> --output build/two-pager --name artifact

The content JSON contract follows the generic shape used by the document template. Treat the CSS tokens as the reusable design surface and the JSON as case binding; do not fork CSS for each company.

The renderer has not been connected to a CI browser job. Contract/manifest checks do not prove PDF rendering or visual QA.
