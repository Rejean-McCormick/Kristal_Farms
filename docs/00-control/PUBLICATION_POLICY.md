# Publication Policy — Public by Default

**Status:** repository control decision  
**Effective:** 2026-08-17

## Principle

Kristal Farms is developed as a **public working project**. The repository may openly contain:

- strategic vision and evolving project architecture;
- preliminary site, hydro, climate and infrastructure screening;
- working economic models and assumptions;
- unresolved decisions and competing hypotheses;
- partner-document drafts and superseded versions;
- research that still needs stronger sourcing, provided its limitations are explicit;
- public datasets and derived analysis;
- technical specifications that are appropriate for open review;
- community, dignity, language, education and governance frameworks under development.

Public visibility is not equivalent to validation, endorsement, engineering approval, investment approval, permitting approval or legal advice. Status labels and caveats remain part of the substance of the repository.

## What stays out of the public repository

Only material with a concrete restriction should be excluded, especially:

1. credentials, passwords, API keys, tokens, private keys and other secrets;
2. personal information that should not be publicly disclosed;
3. confidential third-party information received under NDA, contract or another legal restriction;
4. non-public tenant/customer data, models, logs or security credentials;
5. detailed operational-security information where disclosure would create a credible physical, cyber or infrastructure risk;
6. information a host community or rights-holder has lawfully provided on a confidential basis;
7. material whose copyright or licence does not permit repository publication.

Such material should never be committed and should live outside the repository or in an explicitly ignored local path.

## Working research and imperfect citations

A file can be **public but not publication-ready**. For example, a research note containing assistant-era citation tokens may remain visible for provenance and collaborative cleanup, but claims from it must not be promoted into an authoritative partner, engineering, regulatory or investor document until re-sourced.

Use labels such as:

- `WORKING DRAFT`;
- `PRELIMINARY SCREENING`;
- `HYPOTHESIS`;
- `SOURCE HYGIENE REQUIRED`;
- `NOT ENGINEERING-VALIDATED`;
- `SUPERSEDED`;
- `CURRENT CONTROL`.

## Site and map data

Site, hydro and map screening data are public by default when they are derived from public or publishable sources. Exact future security layouts, access-control systems, tenant security configurations, unpublished critical-infrastructure vulnerabilities or confidential rights-holder information are not.

## Economics

Working economics may be public. Every material numeric claim should carry its assumptions, source/provenance and an `as-of` date when time-sensitive. Public availability must not be mistaken for an investment representation or validated business case.

## Public wiki

`public-wiki/` is the plain-language public entry point. It should summarize the current project faithfully while clearly separating:

- established design principles;
- current working choices;
- long-term vision;
- hypotheses still requiring evidence.

## Licence

A public GitHub repository is viewable by everyone, but public visibility does not automatically grant reuse rights. A separate licence decision is required before representing the documentation, data or code as open-source/open-content.
