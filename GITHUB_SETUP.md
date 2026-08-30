# GitHub Setup

Canonical repository: `Kristal_Farms` (local repository name `kristal-farms`).

For a new clone, use the normal GitHub workflow:

```bash
git clone https://github.com/Rejean-McCormick/Kristal_Farms.git
cd Kristal_Farms
git status
```

For an existing local worktree without a remote:

```bash
git remote add origin https://github.com/Rejean-McCormick/Kristal_Farms.git
git branch -M main
git push -u origin main
```

Normal updates:

```bash
git add .
git commit -m "Describe the change"
git push
```

Before publishing or changing repository visibility, review:

- `SECURITY.md`;
- `LICENSING.md`;
- `docs/00-control/DOCUMENT_AUTHORITY.md`;
- `docs/00-control/SCOPE_BOUNDARIES.md`;
- `docs/00-control/QA_REPORT.md`.

The GitHub Wiki is maintained separately from the canonical repository.
