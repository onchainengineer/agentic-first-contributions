# Go Agentic AI Projects

Go is underrepresented in the agentic AI space but has a few strong projects, especially around infrastructure and tooling.

## Agent Frameworks

### [tmc/langchaingo](https://github.com/tmc/langchaingo)

LangChain for Go. Community-maintained port of the Python library.

- **Good for**: Provider support, examples, docs
- **Smaller community** — direct maintainer contact
- **Great learning project** if you know Go and want to learn agents

### [cloudwego/eino](https://github.com/cloudwego/eino)

LLM application framework from ByteDance's CloudWeGo team.

- **Good for**: Examples, docs, provider integrations
- **Professional team**, production focus

## LLM Inference and Tooling

### [ollama/ollama](https://github.com/ollama/ollama)

Run LLMs locally with a simple API. One of the most popular projects in the space.

- **Good for**: Model support, docs, examples
- **Massive community** — many good first issues
- **Well-documented contribution process**

### [k8sgpt-ai/k8sgpt](https://github.com/k8sgpt-ai/k8sgpt)

Uses LLMs to diagnose Kubernetes issues. CNCF sandbox project.

- **Good for**: Analyzers, integrations, docs
- **Mature governance** — CNCF standards apply
- **Great for DevOps backgrounds**

## MCP and Agent Protocols

### [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk)

Official Go SDK for the Model Context Protocol.

- **Good for**: Examples, SDK improvements, docs
- **Early stage** — strong positioning for contributions

## Agent Infrastructure

### [substratusai/substratus](https://github.com/substratusai/substratus)

Cross-cloud substrate for training and serving ML models.

- **Good for**: Operators, examples, docs
- **Kubernetes-focused**

### [berops/claudie](https://github.com/berops/claudie)

Multi-cloud Kubernetes platform. Not agent-focused but used for running agent infrastructure.

## How to Choose

**Know Go and want to learn AI?** Start with langchaingo — the ported API is a great teacher.

**Infrastructure background?** Ollama, k8sgpt, or Claudie play to your strengths.

**Like protocols and RPC?** The MCP Go SDK is early enough to shape.

**Want high visibility?** Ollama has huge reach — any contribution is seen by many users.

## Why Go for AI?

- **Deployment simplicity**: single binary, easy to ship
- **Concurrency**: goroutines fit agent coordination naturally
- **CLI ergonomics**: best-in-class for tools and daemons
- **Cloud native**: native fit with Kubernetes and DevOps tooling

## Next Steps

- Read [How to Evaluate Projects](../guides/how-to-evaluate.md) first
- See [Making Your First Contribution](../guides/first-contribution.md)
