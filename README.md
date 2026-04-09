# Agentic First Contributions

**Your launchpad into the agentic AI open source ecosystem.** A guide + curated list of beginner-friendly projects in LLM agents, multi-agent frameworks, MCP servers, agent tooling, and AI developer tools.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## Why This Repo?

Agentic AI is moving fast. Every week brings new frameworks, protocols, and tools. If you want to contribute to this space, the hardest part is knowing where to start.

This repo gives you:

1. **A guide** on how to find and evaluate agentic AI projects worth contributing to
2. **Curated project lists** organized by language and topic
3. **A live script** that fetches current "good first issue" counts from GitHub
4. **Weekly updates** via GitHub Actions so the lists stay fresh

---

## Quick Start

Want to contribute to an agentic AI project **right now**? Pick one of these well-maintained, beginner-friendly repos:

| Project | Language | What It Is | Why Start Here |
|---------|----------|-----------|---------------|
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | The foundational LLM agent framework | Huge community, many docs/tests issues |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Python | Role-based multi-agent orchestration | Active maintainers, good first issue label |
| [langflow-ai/langflow](https://github.com/langflow-ai/langflow) | Python + TS | Visual agent builder | Great if you like frontend + AI |
| [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) | TypeScript | Drag-and-drop LLM flows | Node.js + React, lots of features to add |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Python | Memory layer for AI agents | Smaller repo, approachable codebase |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | TS + Python | Reference MCP server implementations | New protocol, lots of servers to build |
| [cline/cline](https://github.com/cline/cline) | TypeScript | Autonomous coding agent (VS Code) | Fast-moving project |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Python | Multi-agent conversation framework | Backed by Microsoft, stable |

For the full list, see [projects/](projects/).

---

## Guides

Start here if you are new to open source or new to agentic AI:

| Guide | What You Learn |
|-------|---------------|
| [How to Find Projects](guides/how-to-find-projects.md) | Search strategies, filters, platforms |
| [How to Evaluate Projects](guides/how-to-evaluate.md) | Signs of a healthy project, red flags to avoid |
| [Making Your First Contribution](guides/first-contribution.md) | Fork, clone, branch, PR workflow |
| [Contributing to AI Projects Specifically](guides/ai-specific-tips.md) | Testing LLM code, working with API costs, evals |
| [Finding Your First Issue](guides/finding-issues.md) | GitHub search filters, labels, tools |

---

## Curated Project Lists

### By Language

| List | Focus |
|------|-------|
| [Python](projects/python.md) | LangChain, CrewAI, AutoGen, LlamaIndex, DSPy, Pydantic AI, and more |
| [TypeScript / JavaScript](projects/typescript.md) | LangChain.js, Mastra, Vercel AI SDK, Flowise, Cline |
| [Rust](projects/rust.md) | Rig, llm, SmartCore, Candle-based tools |
| [Go](projects/go.md) | LangChainGo, Ollama, Eino, agent CLIs |

### By Topic

| List | Focus |
|------|-------|
| [Agent Frameworks](projects/agent-frameworks.md) | LangChain, CrewAI, AutoGen, LlamaIndex, Semantic Kernel |
| [Visual / No-Code Builders](projects/visual-builders.md) | Langflow, Flowise, Dify, n8n |
| [MCP (Model Context Protocol)](projects/mcp.md) | Protocol spec, reference servers, community servers |
| [Memory & RAG](projects/memory-and-rag.md) | Mem0, Zep, Chroma, LanceDB, Weaviate |
| [Agent Runtimes & Coding Agents](projects/coding-agents.md) | Cline, Aider, OpenHands, Continue, Cursor alternatives |
| [LLM Tooling](projects/llm-tooling.md) | llama.cpp, vLLM, Ollama, LiteLLM, Guidance |
| [Evals & Observability](projects/evals-observability.md) | Langfuse, Helicone, Braintrust, promptfoo |
| [Agent Protocols](projects/protocols.md) | A2A, MCP, ACP, OpenAI function calling standards |

### Live Status (Auto-Updated)

The [`projects/live-status.md`](projects/live-status.md) file is updated weekly by a GitHub Action. It shows the current "good first issue" count for every project in the curated lists.

---

## How to Use This Repo

### If you are looking for a project to contribute to

1. Read [How to Find Projects](guides/how-to-find-projects.md)
2. Browse the [language](projects/) or [topic](projects/) lists that match your interests
3. Check [`projects/live-status.md`](projects/live-status.md) for current open issues
4. Read [How to Evaluate Projects](guides/how-to-evaluate.md) before committing time
5. Follow [Making Your First Contribution](guides/first-contribution.md) to submit a PR

### If you want to add a project to the list

Open a PR following the rules in [CONTRIBUTING.md](CONTRIBUTING.md). We accept projects that are:

- Actively maintained (commits in the last 3 months)
- Open source (OSI-approved license)
- Welcoming to contributors (CONTRIBUTING.md, issue templates, labels)
- Related to agentic AI, LLMs, MCP, or AI developer tools

### If you want to run the update script locally

```bash
cd scripts
pip install requests pyyaml
export GITHUB_TOKEN=your_personal_access_token
python fetch-issues.py
```

This updates `projects/live-status.md` with fresh issue counts.

---

## Resources

External resources for finding agentic AI projects:

| Resource | Description |
|----------|-------------|
| [goodfirstissue.dev](https://goodfirstissue.dev) | Aggregates good first issues across repos |
| [goodfirstissues.com](https://goodfirstissues.com) | Alternative aggregator with filters |
| [Up For Grabs](https://up-for-grabs.net) | Projects with tasks for new contributors |
| [First Timers Only](https://www.firsttimersonly.com) | Issues reserved for first-time contributors |
| [GitHub Topic: good-first-issue](https://github.com/topics/good-first-issue) | Raw GitHub topic search |
| [GitHub Topic: ai-agents](https://github.com/topics/ai-agents) | AI agent projects on GitHub |
| [GitHub Topic: llm](https://github.com/topics/llm) | LLM-related projects |
| [GitHub Topic: mcp](https://github.com/topics/mcp) | Model Context Protocol projects |

Other awesome lists focused on AI agents:

- [kyrolabs/awesome-agents](https://github.com/kyrolabs/awesome-agents) — broad AI agent list
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — autonomous agents
- [kaushikb11/awesome-llm-agents](https://github.com/kaushikb11/awesome-llm-agents) — LLM agent frameworks
- [Jenqyang/Awesome-AI-Agents](https://github.com/Jenqyang/Awesome-AI-Agents) — autonomous agents powered by LLMs
- [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) — 500 agent use cases

These lists are broader. This repo is narrower: every project here is vetted for beginner-friendliness.

---

## Who Is This For?

- **Developers** looking to break into agentic AI by contributing to real projects
- **Students** building a portfolio with meaningful open source work
- **AI enthusiasts** who want to move from using tools to building them
- **Career switchers** who need signal on what is worth learning in the current landscape

---

## License

MIT. See [LICENSE](LICENSE).
