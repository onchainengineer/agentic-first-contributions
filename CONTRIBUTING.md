# Contributing

Thanks for helping improve this guide! There are three main ways to contribute:

1. **Add a project** to the curated lists
2. **Improve a guide** with clearer explanations or examples
3. **Fix the script** that updates live status

## Adding a Project

Projects must meet all of these criteria:

- **Agentic AI related**: LLM agents, multi-agent frameworks, MCP, memory, RAG, coding agents, LLM tooling, evals
- **Actively maintained**: commits within the last 3 months
- **Open source**: OSI-approved license
- **Beginner friendly**: has a CONTRIBUTING.md and uses `good first issue` or `help wanted` labels
- **Accessible codebase**: clear structure, documented setup

### How to Add

1. Pick the appropriate file in `projects/` (language or topic)
2. Add a new entry following the existing format:

```markdown
### [owner/repo](https://github.com/owner/repo)

One-line description.

- **Stack**: language + framework
- **Good for**: what kinds of contributions
- **Why start here**: why a beginner should care
```

3. Add the project to `scripts/projects.yaml`:

```yaml
- repo: owner/repo
  category: agent-framework  # or another valid category
  language: Python
```

4. Open a PR explaining why the project fits

### Valid Categories

- `agent-framework` — LLM agent libraries and frameworks
- `visual-builder` — No-code/low-code agent builders
- `coding-agent` — AI coding assistants and agents
- `memory-rag` — Memory systems, vector DBs, RAG tools
- `llm-tooling` — Inference engines, unified APIs, runtime tools
- `mcp` — Model Context Protocol projects
- `evals-observability` — Testing, tracing, monitoring

### Removing a Project

If a project becomes unmaintained:

1. Open an issue explaining why (no commits in 6+ months, archived, etc.)
2. Wait 7 days for community input
3. If no objections, open a PR to remove it from both the list file and `projects.yaml`

## Improving a Guide

The guides should be clear, accurate, and welcoming. Improvements we love:

- Fixing outdated information
- Adding concrete examples
- Clarifying confusing explanations
- Adding new sections with valuable content

## Fixing the Script

The fetch script lives in `scripts/fetch-issues.py`. When making changes:

- Test locally first with your GitHub token
- Verify the script produces valid markdown
- Check that rate limits are respected

## Writing Style

- Second person ("you"), active voice
- Short sentences, short paragraphs
- Define jargon on first use
- American English
- No marketing language
- No em dashes

## Commit Convention

Use Conventional Commits:

- `docs:` — documentation changes
- `feat:` — new feature or curated project
- `fix:` — fix an error
- `chore:` — CI, config, maintenance

Examples:
- `feat: add Mastra to TypeScript agent frameworks`
- `docs: clarify MCP server setup in mcp.md`
- `fix: correct broken link in first-contribution guide`
- `chore: update fetch-issues.py to handle rate limits`

## Code of Conduct

Be kind. Be specific. Assume good intent. Avoid gatekeeping.

If you see behavior that violates these principles, open an issue or contact the maintainers.
