# GitHub Wiki Setup

GitHub stores the wiki as a separate Git repository ending in `.wiki.git`.

After the main GitHub repository exists and the Wiki feature is enabled, clone the wiki repository and copy these Markdown files into it.

Example:

```bash
git clone https://github.com/OWNER/REPOSITORY.wiki.git
cp /path/to/kristal-farms-public-wiki-en-rebuilt/*.md REPOSITORY.wiki/
cd REPOSITORY.wiki
git add .
git commit -m "Rebuild public Kristal Farms wiki"
git push
```

Replace `OWNER/REPOSITORY` with the actual GitHub repository.
