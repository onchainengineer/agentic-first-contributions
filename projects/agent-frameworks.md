# Agent Frameworks

Libraries and frameworks for building LLM-powered agents. These are the core building blocks of the agentic AI ecosystem.

## Top Picks

### [langchain-ai/langchain](https://github.com/langchain-ai/langchain)
The foundational framework. Modular components for chains, agents, memory, retrieval, and tool use. Python.

### [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
Role-based multi-agent orchestration. Define agents with goals and tools, let them collaborate. Python.

### [microsoft/autogen](https://github.com/microsoft/autogen)
Multi-agent conversation framework from Microsoft. Being merged with Semantic Kernel into Microsoft Agent Framework. Python.

### [run-llama/llama_index](https://github.com/run-llama/llama_index)
Data framework for LLM applications. Best for RAG-heavy agents. Python.

### [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
Type-safe agent framework with Pythonic API. Clean, production-ready. Python.

### [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)
Programming language model pipelines. Declarative, optimization-driven. Python.

### [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)
Enterprise-focused agent framework. Python, C#, Java.

### [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs)
TypeScript port of LangChain. JavaScript/TypeScript.

### [mastra-ai/mastra](https://github.com/mastra-ai/mastra)
TypeScript-first agent framework. Newer, growing fast.

### [vercel/ai](https://github.com/vercel/ai)
The Vercel AI SDK. Powers many production LLM apps. Streaming, tool use, React hooks.

### [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)
Graph-based orchestration for stateful agents. Part of the LangChain ecosystem.

### [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig)
Rust agent framework with a clean API.

### [tmc/langchaingo](https://github.com/tmc/langchaingo)
LangChain port for Go.

## Choosing a Framework

| If you... | Pick |
|-----------|------|
| Want the biggest ecosystem | LangChain |
| Like role-based multi-agent | CrewAI |
| Want type safety | Pydantic AI |
| Build RAG heavy apps | LlamaIndex |
| Are a TypeScript developer | Vercel AI SDK or Mastra |
| Want enterprise backing | Semantic Kernel |
| Like declarative optimization | DSPy |
| Want graph-based state machines | LangGraph |
| Write Rust | rig |
| Write Go | langchaingo |

## Contributing Strategies

**Integrations are the easiest entry point.** Most frameworks need new LLM providers, vector stores, tools, and data loaders. Each integration is a self-contained PR.

**Docs and examples are high-impact.** Frameworks move fast — examples get outdated. Updating or adding examples is valuable work.

**Tests are valuable.** Many agent frameworks have weak test coverage for edge cases. Adding tests builds maintainer trust.

**Avoid core architecture changes as a first PR.** These require deep knowledge of the framework's philosophy.

## Next Steps

- [How to Evaluate Projects](../guides/how-to-evaluate.md)
- [Python Projects](python.md) | [TypeScript Projects](typescript.md) | [Rust Projects](rust.md) | [Go Projects](go.md)
