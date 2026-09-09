# Versioning and crossed lifecycle

Template, workflow and QA fixtures evolve as a coordinated system.

## Semantic versioning

### PATCH
Use for backward-compatible:
- wording rules;
- visual spacing;
- minor QA checks;
- source formatting.

The fixture may keep its version when coverage is unchanged. Bump the fixture patch when the example itself changes.

### MINOR
Use for:
- new optional section;
- new side-story mapping;
- new supported generation mode;
- stronger non-breaking QA gate;
- new content payload option.

The linked QA fixture must bump at least MINOR and explicitly exercise the new behavior.

### MAJOR
Use for:
- required section changes;
- incompatible schema changes;
- changed decision semantics;
- removed payload types;
- changed evidence boundary.

The linked fixture must share the new MAJOR version.

## Cross-lifecycle invariant

Every template manifest entry declares:
- `version`;
- `lifecycle`;
- `qa_fixture`;
- `qa_fixture_version`;
- `supported_modes`;
- repository `workflow_version`.

A template cannot move to `validated` or `promoted` unless:
1. its fixture exists;
2. fixture front matter identifies the same template type;
3. fixture template major version equals the manifest template major;
4. fixture workflow version equals the manifest workflow version;
5. CI validator passes.

## Human feedback and version bump

A feedback/dreaming run records:
- originating artifact;
- current template version;
- issue/feedback;
- reusable delta;
- proposed bump;
- regression fixture delta;
- human decision.

## Historical snapshots

Old fixtures remain valid historical snapshots when a new major version is created. Do not rewrite a v1 fixture to masquerade as v2 evidence.
