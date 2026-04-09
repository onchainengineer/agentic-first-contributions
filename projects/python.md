# Python Agentic AI Projects

Beginner-friendly Python projects in the agentic AI space. All are actively maintained, use clear contribution workflows, and tag good first issues.

## Agent Frameworks

### [langchain-ai/langchain](https://github.com/langchain-ai/langchain)

The foundational framework for building LLM applications in Python. Huge ecosystem, active community, frequent releases.

- **Good for**: Contributing to core, integrations, docs, tests
- **Labels to check**: `good first issue`, `help wanted`, `documentation`
- **Dev setup**: `pip install -e ".[dev]"` in a subpackage
- **Why start here**: Massive project, many entry points at every skill level

### [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)

Graph-based orchestration for stateful AI agents. Part of the LangChain ecosystem but a separate project.

- **Good for**: Examples, docs, integration adapters
- **Smaller than LangChain**, easier to understand the whole codebase

### [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)

Role-based multi-agent orchestration. Define agents with goals and tools, then let them collaborate.

- **Good for**: Example agents, docs, integrations
- **Active community**, responsive maintainers
- **Labels**: `good first issue`, `documentation`

### [microsoft/autogen](https://github.com/microsoft/autogen)

Multi-agent conversation framework from Microsoft. Now being merged with Semantic Kernel into Microsoft Agent Framework.

- **Good for**: Examples, integrations, tests
- **Note**: Check the migration status before contributing core changes

### [run-llama/llama_index](https://github.com/run-llama/llama_index)

Data framework for LLM applications. The go-to for RAG pipelines.

- **Good for**: Integrations (readers, loaders), docs, examples
- **Huge integration surface area** — pick a data source and add support

### [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)

Type-safe agent framework from the Pydantic team. Clean Pythonic API.

- **Good for**: Examples, tests, docs
- **Smaller codebase** — easier to understand end-to-end
- **Production-focused**: values type safety and testability

### [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

Programming language model pipelines. Declarative, not prompt-based.

- **Good for**: Examples, benchmarks, docs
- **Research-heavy**: academic tone, but welcoming to engineers

## Memory and RAG

### [mem0ai/mem0](https://github.com/mem0ai/mem0)

Memory layer for AI agents. Stores and retrieves user-specific context across sessions.

- **Good for**: Integrations, examples, docs
- **Approachable codebase** — smaller than LangChain

### [getzep/zep](https://github.com/getzep/zep)

Long-term memory for AI assistants. Go backend with Python/TS clients.

- **Good for**: Client library improvements, docs
- **Language**: Core is Go, clients are Python/TS

### [chroma-core/chroma](https://github.com/chroma-core/chroma)

Vector database for AI applications. One of the most popular open source vector DBs.

- **Good for**: Python client, integrations, docs
- **Active maintenance**: frequent releases

## Visual / Low-Code Builders

### [langflow-ai/langflow](https://github.com/langflow-ai/langflow)

Visual builder for LangChain flows. Drag and drop agent design.

- **Stack**: Python backend, TypeScript/React frontend
- **Good for**: Both backend and frontend contributors
- **Very active**: 40k+ stars, many open issues

### [langgenius/dify](https://github.com/langgenius/dify)

LLMOps platform with visual workflow builder.

- **Stack**: Python + TypeScript
- **Enterprise-friendly features**
- **Many good first issues**

## LLM Tooling

### [vllm-project/vllm](https://github.com/vllm-project/vllm)

High-throughput LLM inference engine. Used in production by many companies.

- **Good for**: Examples, benchmarks, docs, small optimizations
- **Note**: Deep technical knowledge needed for core changes

### [BerriAI/litellm](https://github.com/BerriAI/litellm)

Unified API for 100+ LLM providers. Drop-in replacement for OpenAI API.

- **Good for**: Adding provider support, docs, tests
- **Low barrier**: each new provider is a self-contained PR

### [guidance-ai/guidance](https://github.com/guidance-ai/guidance)

Programming paradigm for controlled LLM output.

- **Good for**: Examples, docs, tests
- **Smaller community**, more direct maintainer attention

## Coding Agents

### [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands)

Open source autonomous coding agent. Formerly OpenDevin.

- **Good for**: Examples, tool integrations, docs
- **Very active development**

### [Aider-AI/aider](https://github.com/Aider-AI/aider)

AI pair programming in your terminal.

- **Good for**: Language support, examples, docs
- **Approachable architecture**

### [stitionai/devika](https://github.com/stitionai/devika)

Agentic AI software engineer.

- **Good for**: Examples, prompts, docs
- **Fast-moving project**

## Evals and Observability

### [langfuse/langfuse](https://github.com/langfuse/langfuse)

Open source LLM engineering platform with evals, tracing, and prompts.

- **Stack**: TypeScript + Python SDK
- **Good for**: Python SDK, docs, examples
- **Professional team** — clear processes

### [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)

CLI for testing and evaluating LLM outputs.

- **Good for**: Test cases, providers, docs
- **Stack**: TypeScript core, but accepts Python contributions via providers

### [comet-ml/opik](https://github.com/comet-ml/opik)

LLM evaluation platform.

- **Good for**: SDK, docs, integrations

## How to Choose

**Never contributed to open source?** Start with docs on LangChain or CrewAI. The communities are large and welcoming.

**Want a smaller codebase?** Try mem0, pydantic-ai, or guidance.

**Like benchmarks and metrics?** Try vLLM or promptfoo.

**Like building integrations?** Try LiteLLM (one provider per PR) or LangChain integrations.

**Like frontend work?** Try Langflow or Dify.

## Next Steps

- Read [How to Evaluate Projects](../guides/how-to-evaluate.md) before committing time
- Check [`projects/live-status.md`](live-status.md) for current open issue counts
- Pick an issue and follow [Making Your First Contribution](../guides/first-contribution.md)
