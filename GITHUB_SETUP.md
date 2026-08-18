# GitHub Setup

Create the remote as **public**. Kristal Farms uses a public-by-default working-repository policy; review `PUBLICATION_POLICY.md` before committing any genuinely restricted material.

```bash
git init
git add .
git commit -m "Kristal Farms v3: platform, human infrastructure and international learning"
git branch -M main

# Create an empty public repository in GitHub, then:
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

If GitHub CLI is installed and authenticated:

```bash
gh repo create kristal-farms-docs --public --description "Kristal Farms: cold-climate infrastructure for using difficult-to-export renewable energy on site—secure compute, fibre export, heat reuse, harmonious community integration, northern capability building, and international learning." --source=. --remote=origin --push
```

Before publishing or pushing new source material, review:
- `docs/00-control/PUBLICATION_POLICY.md`
- `docs/00-control/DOCUMENT_AUTHORITY.md`
- `docs/00-control/DECISIONS_REQUIRED.md`
- `docs/00-control/CONTENT_SANITATION.md`
- `docs/00-control/SCOPE_BOUNDARIES.md`
- `docs/10-core/strategy/HUMAN_DIGNITY_FRAMEWORK_EN.md`
