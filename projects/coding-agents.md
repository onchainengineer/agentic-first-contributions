# Coding Agents

Agents that write, edit, and run code. This is the fastest-moving segment of agentic AI right now — contributions here have high visibility.

## Top Projects

### [cline/cline](https://github.com/cline/cline)

Autonomous coding agent in VS Code. Plans multi-step changes, edits files, runs commands, uses the browser.

- **Stack**: TypeScript, VS Code extension
- **Good for**: Tool providers, docs, examples
- **Very active** — new features ship weekly

### [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)

Open source autonomous coding agent. Formerly OpenDevin. Runs in a sandboxed environment.

- **Stack**: Python + TypeScript
- **Good for**: Tool integrations, agent strategies, docs
- **Academic-industry collaboration**

### [Aider-AI/aider](https://github.com/Aider-AI/aider)

AI pair programming in your terminal.

- **Stack**: Python
- **Good for**: Language support (more tree-sitter grammars), docs, examples
- **Beloved by users**, responsive maintainer

### [continuedev/continue](https://github.com/continuedev/continue)

Open source autocomplete and chat. VS Code and JetBrains.

- **Stack**: TypeScript + Kotlin
- **Good for**: Model providers, context providers, docs
- **Well-architected**, clear contribution path

### [TabbyML/tabby](https://github.com/TabbyML/tabby)

Self-hosted AI coding assistant.

- **Stack**: Rust core + TypeScript UI
- **Good for**: UI, docs, examples

### [block/goose](https://github.com/block/goose)

Open source AI agent that automates software engineering tasks. From Block (Square).

- **Stack**: Rust + TypeScript
- **Good for**: Extensions (MCP servers), docs, examples

### [cognition-ai/devin-swe](https://github.com/cognition-ai)

Cognition Labs publishes some open source components of their SWE agent work.

## Smaller / Emerging

### [princeton-nlp/SWE-agent](https://github.com/princeton-nlp/SWE-agent)

Research-focused coding agent from Princeton. Used in SWE-bench.

- **Stack**: Python
- **Good for**: Evals, benchmark improvements, docs
- **Academic tone**, research focused

### [stitionai/devika](https://github.com/stitionai/devika)

Agentic AI software engineer.

- **Stack**: Python + TypeScript
- **Good for**: Prompts, tools, docs

### [RooVetGit/Roo-Code](https://github.com/RooVetGit/Roo-Code)

VS Code coding agent based on Cline.

- **Stack**: TypeScript
- **Good for**: Fork-specific features, docs

## Why This Category Matters

Coding agents are eating software development. The projects here will shape how developers work in 5 years. Early contributions are a strong signal.

## What to Contribute

**Tool integrations.** Coding agents need tools for search, git, shell, browsers. Each tool is self-contained.

**Language support.** Better tree-sitter grammars, better syntax highlighting, better refactoring for specific languages.

**Prompts and strategies.** Improving how agents plan and execute. Requires evals.

**Benchmarks.** SWE-bench, HumanEval, and custom evals.

**Docs and examples.** New users constantly need guidance.

## Challenges

**Non-determinism.** Coding agent tests are flaky. Contributions need to handle this.

**API costs.** Tests that actually run the agent cost money. Many projects mock or skip these.

**Rapid change.** The SOTA shifts weekly. Your contribution may be outdated by merge time. Focus on foundations over trendy features.

## Next Steps

- [AI-Specific Tips](../guides/ai-specific-tips.md) — critical reading for this category
- [How to Evaluate Projects](../guides/how-to-evaluate.md)
