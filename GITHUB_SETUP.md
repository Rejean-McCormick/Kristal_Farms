# GitHub Setup

Kristal Farms is intended to be a **public working repository**.

## Create the repository

```bash
git init
git add -A
git commit -m "Realign Kristal Farms repository to current public wiki"
git branch -M main
```

Create an empty **public** GitHub repository, then:

```bash
git remote add origin <REPOSITORY_URL>
git push -u origin main
```

With GitHub CLI:

```bash
gh repo create kristal-farms-docs --public --description "Kristal Farms — northern infrastructure model bringing compute to renewable energy, exporting digital value by fibre, and reusing heat." --source=. --remote=origin --push
```

## GitHub Wiki

The source for the public wiki is in `public-wiki/`. Follow `public-wiki/WIKI_SETUP.md` to publish it to the separate `.wiki.git` repository.

## Before pushing new material

Review:

- `docs/00-control/PUBLICATION_POLICY.md`
- `docs/00-control/CONTENT_SANITATION.md`
- `docs/00-control/CLAIMS_TO_VALIDATE.md`
- `docs/00-control/DOCUMENT_AUTHORITY.md`

Do not commit secrets, private tenant/customer data, personal information, legally restricted material or concrete operational-security details that create a credible risk.
