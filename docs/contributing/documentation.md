# Documentation workflow

## Local docs site

The repository uses MkDocs configuration in `mkdocs.yml`.

Recommended documentation dependencies:

```text
mkdocs
mkdocs-material
pymdown-extensions
```

Run:

```bash
mkdocs serve
```

## What requires documentation

Update docs when changing:

- architecture;
- data semantics;
- APIs/contracts;
- permissions;
- publication behavior;
- scenario assumptions/results;
- user-visible map semantics;
- deployment/runbooks.

## ADRs

Durable architectural choices should be recorded in `docs/adr/` rather than buried in PR comments.

## Machine contracts

When prose changes a rule represented in `contracts/`, update both in the same pull request.
