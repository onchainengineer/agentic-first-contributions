# Agent Protocols and Standards

Standards and protocols for agent interoperability. This is the most strategic area to contribute to right now — early influence on protocols shapes the whole ecosystem.

## Model Context Protocol (MCP)

Anthropic's open standard for connecting AI assistants to data and tools. See [MCP Projects](mcp.md) for the full list.

### Core MCP Repos

- [modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification) — the spec itself
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — reference implementations
- [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)
- [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
- [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)
- [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk)

MCP is the most active protocol ecosystem right now. See the dedicated [MCP Projects page](mcp.md).

## Agent-to-Agent (A2A)

Google's proposed protocol for agent interoperability.

### [google/a2a](https://github.com/google/a2a)

The A2A specification and reference implementations.

- **Stack**: Multiple
- **Good for**: Examples, SDK development, docs
- **Early stage** — shape the direction

## Agent Communication Protocol (ACP)

From IBM Research, focused on enterprise agent communication.

### Resources

- [Linux Foundation AI & Data](https://lfaidata.foundation/) projects related to agent standards
- [AGNTCY](https://github.com/agntcy) — multi-vendor agent collaboration working group

## OpenAI Function Calling Standards

The de facto standard for tool use, though not a formal protocol.

### [openai/openai-python](https://github.com/openai/openai-python)

Official OpenAI Python client. Widely used as a reference for tool calling.

- **Good for**: Examples, docs, type improvements

### [openai/openai-node](https://github.com/openai/openai-node)

Official OpenAI Node.js client.

## AgentOps Standards

Emerging standards for agent operations, safety, and governance.

### [OWASP-AI](https://github.com/OWASP/www-project-ai-security-and-privacy-guide)

OWASP's guide to AI security. Not a protocol but a standards document.

## Why Contribute to Protocols?

**High leverage.** A protocol contribution affects every tool that implements it.

**Strategic positioning.** Early contributors are seen as experts.

**Shapes the future.** The agent interoperability landscape is being defined right now.

**Fewer contributors.** Protocol work is less crowded than application-level work.

## What Makes Protocol Contributions Hard

**High bar for spec changes.** Any change affects all implementations.

**Long review cycles.** Decisions need broad community input.

**Backward compatibility.** Once something ships, it is hard to change.

**Governance.** Working groups, RFC processes, consensus building.

## Where to Start

**Do not start with spec changes.** Start with:

1. **Examples and tutorials** — show how to use the protocol
2. **Reference implementations** — bug fixes and small improvements
3. **SDKs** — adding features to language SDKs
4. **Integration libraries** — connect the protocol to popular frameworks
5. **Documentation** — every protocol needs better docs

Only once you understand the protocol deeply should you propose spec changes.

## Stay Informed

Follow these to understand protocol developments:

- [Anthropic MCP announcements](https://www.anthropic.com/news)
- [GitHub discussions on the protocol repos](https://github.com/modelcontextprotocol/specification/discussions)
- [Linux Foundation AI & Data events](https://lfaidata.foundation/)

## Next Steps

- [MCP Projects](mcp.md) — the most active protocol ecosystem
- [Agent Frameworks](agent-frameworks.md) — frameworks that implement protocols
