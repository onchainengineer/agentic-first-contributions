# Live Status

This file is automatically updated weekly by a GitHub Action. It shows the current number of open "good first issue" labels across all curated projects.

**Last updated**: Not yet run. The first update will happen when the GitHub Action runs for the first time.

To update manually:

```bash
cd scripts
pip install requests pyyaml
export GITHUB_TOKEN=your_token_here
python fetch-issues.py
```

## Tracked Projects

See [`scripts/projects.yaml`](../scripts/projects.yaml) for the list of projects tracked.

## How It Works

The script queries the GitHub API for each project and counts:

- Total open issues
- Open issues with `good first issue` label
- Open issues with `help wanted` label
- Open issues with `documentation` label

Results are sorted by good first issue count, descending.

## Reading the Status

High count is not always better. A project with 50 open good first issues may mean:

- **Good**: Active project with clear beginner pathway
- **Bad**: Maintainers cannot keep up with their own backlog

Use this data as a starting signal, then apply the checks from [How to Evaluate Projects](../guides/how-to-evaluate.md).

---

## Current Status

_The table below will be populated by the next GitHub Action run._

| Project | Language | Stars | Good First Issues | Help Wanted | Last Commit |
|---------|----------|-------|-------------------|-------------|-------------|
| _pending first run_ | | | | | |
