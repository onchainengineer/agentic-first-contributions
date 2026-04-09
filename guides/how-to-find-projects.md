# How to Find Agentic AI Projects to Contribute To

Finding a good project is half the battle. Here is a structured approach.

## Strategy 1: Start with What You Use

The best project to contribute to is one you already use. If you have built something with LangChain, you already understand its API, its pain points, and its documentation gaps. Contributing back is a natural next step.

Ask yourself:

- What AI libraries do I import in my side projects?
- What tools have I wished worked differently?
- What bugs have I worked around instead of reporting?

Your "I wish X did Y" frustrations are contribution opportunities.

## Strategy 2: Search GitHub Directly

GitHub's search is powerful when you use the right filters.

### Find beginner-friendly agentic AI repos

```
topic:ai-agents label:"good first issue" is:open
topic:llm label:"good first issue" is:open
topic:langchain label:"good first issue" is:open
topic:mcp label:"good first issue" is:open
topic:rag label:"good first issue" is:open
```

### Find recently updated projects

Stale projects are a trap. Filter for recent activity:

```
topic:ai-agents pushed:>2026-03-01
```

### Find well-documented projects

Projects with good docs are easier to contribute to:

```
topic:ai-agents "contributing.md" in:path
```

## Strategy 3: Use Aggregator Platforms

Several platforms curate good first issues across repos:

- **[goodfirstissue.dev](https://goodfirstissue.dev)** — filter by language, includes many AI projects
- **[goodfirstissues.com](https://goodfirstissues.com)** — similar, different UI
- **[Up For Grabs](https://up-for-grabs.net)** — filter by language and tags
- **[First Timers Only](https://www.firsttimersonly.com)** — specifically reserved for first-timers
- **[CodeTriage](https://www.codetriage.com)** — daily email with a new issue

All of these include agentic AI projects.

## Strategy 4: Browse Curated Awesome Lists

Other maintainers have done the discovery work. Browse:

- [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents)
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)
- [kaushikb11/awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents)

These are broader than our curated lists. Use them to discover projects, then evaluate using our [How to Evaluate](how-to-evaluate.md) guide.

## Strategy 5: Follow the Ecosystem

Agentic AI moves fast. Stay current:

- **GitHub Trending**: [github.com/trending](https://github.com/trending?since=weekly) filtered by Python, TypeScript, or your language
- **Hacker News**: search "Show HN" for agent frameworks
- **X / Twitter**: follow LangChain, CrewAI, Anthropic, Hugging Face accounts
- **Anthropic, OpenAI, Google blogs**: new protocols and standards often emerge from these

New projects with small but active communities are often hungry for contributors.

## Strategy 6: Contribute to Dependencies

Look at the `requirements.txt` / `package.json` / `pyproject.toml` of your favorite agentic project. Every dependency is itself a project you could contribute to.

If you use LangChain, you could contribute to:
- LangChain itself
- langchain-community integrations
- langchain-core
- langgraph
- langsmith (observability)

Going up the dependency tree lets you contribute in the exact spot you understand best.

## What to Avoid

**Avoid hype-driven repos with 50k stars and no recent commits.** Popularity is not the same as activity. Many projects spike, then die.

**Avoid solo maintainer projects** unless you are prepared for slow reviews. One-person projects depend on one person's schedule.

**Avoid projects without CONTRIBUTING.md.** If they have not documented how to contribute, the process will be painful.

**Avoid "first PR just say hi" repos.** These do not build real experience. You want projects where your contribution matters.

## Next Steps

- [How to Evaluate Projects](how-to-evaluate.md) — decide if a project is worth your time
- [Finding Your First Issue](finding-issues.md) — the actual issue search workflow
- [Making Your First Contribution](first-contribution.md) — fork to merged PR
