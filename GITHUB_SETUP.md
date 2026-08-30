# GitHub Setup

Create the remote as **private** unless/until a public-release policy is approved.

```bash
git init
git add .
git commit -m "Kristal Farms v3: platform, human infrastructure and international learning"
git branch -M main

# Create an empty private repository in GitHub, then:
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

If GitHub CLI is installed and authenticated:

```bash
gh repo create kristal-farms-docs --private --description "Kristal Farms: cold-climate infrastructure for using difficult-to-export renewable energy on site—secure compute, fibre export, heat reuse, harmonious community integration, northern capability building, and international learning." --source=. --remote=origin --push
```

Before changing visibility, review:
- `docs/00-control/DOCUMENT_AUTHORITY.md`
- `docs/00-control/DECISIONS_REQUIRED.md`
- `docs/00-control/CONTENT_SANITATION.md`
- `docs/00-control/SCOPE_BOUNDARIES.md`
- `docs/10-core/strategy/HUMAN_DIGNITY_FRAMEWORK_EN.md`
