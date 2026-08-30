# GitHub Setup

Recommended repository name: `kristal-farms-docs`

Recommended visibility: **Private**. The repository contains internal and diligence material in addition to external-facing partner documents.

## Create and push with GitHub CLI

From the repository directory:

```bash
git init -b main
git add .
git commit -m "Initial Kristal Farms documentation repository"
gh repo create kristal-farms-docs --private --source=. --remote=origin --push
```

## Or connect to an existing GitHub repository

```bash
git init -b main
git add .
git commit -m "Initial Kristal Farms documentation repository"
git remote add origin git@github.com:YOUR_ORG_OR_USERNAME/kristal-farms-docs.git
git push -u origin main
```

Before changing the repository to public visibility, review `docs/internal/`, `source-material/`, due-diligence documents, and any NDA-preferred materials identified in `docs/partners/markdown/14_Data_Room_Index.md`.
