# Agentic First Contributions

## Overview

A guide + curated list repository that helps developers find beginner-friendly agentic AI open source projects. Pure documentation with one Python script for automated status updates.

## Tech Stack

- Markdown (all guides and lists)
- Python 3.12 (single script for fetching GitHub API data)
- YAML (project list configuration)
- GitHub Actions (weekly status updates + CI)

## Commands

```bash
# Run the status update script locally
cd scripts
pip install requests pyyaml
export GITHUB_TOKEN=your_token
python fetch-issues.py

# Lint markdown
npx markdownlint-cli2 "**/*.md"
```

## Structure

- `guides/` — How-to guides for finding and contributing to projects
- `projects/` — Curated lists organized by language and topic
  - `live-status.md` — Auto-updated weekly by GitHub Actions
- `scripts/` — Python script and project list for live status
- `.github/workflows/` — CI and weekly status update

## Conventions

- American English, second person, active voice
- ATX headings, one idea per paragraph
- Every curated project must include: repo link, stack, what it is good for
- When adding a project, verify it meets the criteria in CONTRIBUTING.md
- Conventional commits: `docs:`, `feat:`, `fix:`, `chore:`

## Things to Avoid

- Do not add projects that are unmaintained (no commits in 3+ months)
- Do not add projects without CONTRIBUTING.md or good first issue labels
- Do not use hype language ("revolutionary", "game-changing")
- Do not add application code — this is a curation repo
- Do not remove the live-status.md file (it is generated, but tracked)
