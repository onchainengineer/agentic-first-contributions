# TypeScript / JavaScript Agentic AI Projects

Beginner-friendly TypeScript and JavaScript projects in the agentic AI space.

## Agent Frameworks

### [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs)

The JavaScript version of LangChain. Same ecosystem, same patterns, TypeScript-first.

- **Good for**: Integrations, docs, tests
- **Active parity with Python version**
- **Labels**: `good first issue`, `help wanted`

### [mastra-ai/mastra](https://github.com/mastra-ai/mastra)

TypeScript agent framework focused on developer experience. Newer project, rapidly growing.

- **Good for**: Examples, docs, integrations
- **Smaller community**, more direct feedback

### [vercel/ai](https://github.com/vercel/ai)

The Vercel AI SDK. Powers many production LLM apps. React hooks, streaming, tool calling.

- **Good for**: Framework integrations (Svelte, Vue, Solid), examples
- **High quality standards** — review process is strict but educational

## Coding Agents

### [cline/cline](https://github.com/cline/cline)

Autonomous coding agent for VS Code. Formerly Claude Dev.

- **Stack**: TypeScript, VS Code extension
- **Good for**: Tool providers, examples, docs
- **Very active**, fast iteration

### [continuedev/continue](https://github.com/continuedev/continue)

Open source alternative to GitHub Copilot. VS Code and JetBrains extensions.

- **Stack**: TypeScript, Kotlin (JetBrains)
- **Good for**: Model providers, context providers, docs
- **Well-structured codebase**

### [TabbyML/tabby](https://github.com/TabbyML/tabby)

Self-hosted AI coding assistant.

- **Stack**: Rust core, TypeScript UI
- **Good for**: UI work, docs, examples

## Visual / Low-Code Builders

### [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)

Drag-and-drop UI to build LLM flows. Node.js + React.

- **Good for**: Node types, integrations, docs
- **Many good first issues**
- **Smaller team** — maintainers read every issue

### [n8n-io/n8n](https://github.com/n8n-io/n8n)

Workflow automation with AI nodes. 400+ integrations.

- **Stack**: TypeScript + Vue
- **Good for**: New nodes (one per PR), docs, translations
- **Very welcoming to contributors**

## LLM Tooling

### [BerriAI/litellm](https://github.com/BerriAI/litellm)

Python-first but has a proxy server and TypeScript usage. Provider support accepts JS contributions.

### [sindresorhus/llm-cli](https://github.com/sindresorhus/llm-cli)

Small CLI for working with LLMs. Easy entry point for Node.js contributors.

## MCP (Model Context Protocol)

### [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

Reference implementations of MCP servers. Mix of TypeScript and Python.

- **Good for**: New server implementations, bug fixes, docs
- **Many directions to contribute**: GitHub, filesystem, databases, APIs
- **Each server is self-contained**

### [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

Official TypeScript SDK for building MCP servers and clients.

- **Good for**: SDK improvements, examples, docs
- **Core infrastructure** — high standards but high impact

## Agent Runtimes

### [browser-use/browser-use](https://github.com/browser-use/browser-use)

Make websites accessible for AI agents. Playwright under the hood.

- **Good for**: Examples, docs, integration patterns
- **Fast-moving project**

### [stagehand-dev/stagehand](https://github.com/stagehand-dev/stagehand)

Browser automation for AI agents. TypeScript-first.

- **Good for**: Examples, docs, new browser actions
- **Professional team**

## Evals and Observability

### [langfuse/langfuse](https://github.com/langfuse/langfuse)

LLM engineering platform. TypeScript backend with Python and JS SDKs.

- **Stack**: Next.js + tRPC + PostgreSQL
- **Good for**: UI work, SDK improvements, docs
- **Enterprise-quality**

### [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)

CLI for testing LLM outputs. TypeScript core.

- **Good for**: Providers, assertion types, docs, examples
- **Very accessible for beginners**

### [helicone/helicone](https://github.com/helicone/helicone)

Open source LLM observability.

- **Stack**: TypeScript
- **Good for**: Provider support, docs, UI

## How to Choose

**React / Next.js developer?** Start with vercel/ai or langfuse.

**VS Code extension developer?** Try cline or continue.

**Backend developer?** Try LangChain.js or mastra.

**Want fast feedback loops?** Flowise maintainers are very responsive.

**Interested in protocols?** Contribute an MCP server — each one is a self-contained project.

## Next Steps

- Read [How to Evaluate Projects](../guides/how-to-evaluate.md) first
- Check the live status file for current open issue counts
- See [Making Your First Contribution](../guides/first-contribution.md) for the workflow
