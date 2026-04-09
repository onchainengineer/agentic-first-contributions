# Model Context Protocol (MCP) Projects

MCP is an open standard from Anthropic for connecting AI assistants to external data and tools. It is one of the best ecosystems to contribute to right now because it is new, small, and gaining rapid adoption.

## Core Repos

### [modelcontextprotocol/specification](https://github.com/modelcontextprotocol/specification)

The MCP specification itself.

- **Good for**: Spec clarifications, examples, docs
- **High bar** — changes affect the whole ecosystem
- **Watch discussions** to understand where the protocol is heading

### [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

Reference implementations of MCP servers. The best place to start contributing to MCP.

- **Languages**: TypeScript and Python
- **Good for**: New server implementations, bug fixes, docs
- **Each server is self-contained** — you can pick one topic and own it

### [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)

Official TypeScript SDK.

- **Good for**: SDK improvements, examples, docs
- **Core infrastructure** — high standards

### [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)

Official Python SDK.

- **Good for**: SDK improvements, examples, docs
- **Similar standards to TypeScript SDK**

### [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)

Official Rust SDK. Early stage.

- **Good for**: Shaping the early API, examples
- **Strong positioning** — fewer contributors, more influence

### [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk)

Official Go SDK. Early stage.

- **Good for**: Idiomatic Go design, examples

### [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)

Developer tool for testing MCP servers. Web UI.

- **Stack**: TypeScript + React
- **Good for**: UI improvements, debugging features

## Community Servers

Beyond the reference servers, many community MCP servers exist. A few well-maintained ones:

### [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use)

Use MCP servers from Python, including LangChain integration.

### [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)

Curated list of MCP servers. Not a codebase but a great discovery tool.

## Why MCP Is a Great Place to Start

**New protocol.** First movers have outsized influence.

**Small codebases.** Each server is a few files. You can understand the whole thing quickly.

**Clear scope.** "Write a server for X" is a self-contained project.

**High demand.** Every database, API, and service needs an MCP server. Pick one that does not exist yet.

**Professional maintainers.** The core team is at Anthropic with strong engineering practices.

## Ideas for New Servers

If you want to write a new MCP server, pick a service you use:

- Databases: PostgreSQL variants, ClickHouse, DuckDB, MongoDB, Neo4j
- APIs: Stripe, Twilio, SendGrid, Linear, Notion, Airtable
- Infrastructure: Kubernetes, Docker, Terraform, Pulumi
- Data: Snowflake, BigQuery, Databricks, dbt
- Internal tools: Jira, Confluence, ServiceNow
- Dev tools: Sentry, Datadog, PagerDuty

**Check if a server already exists** before starting. Many of the obvious ones are done.

## How to Write a New MCP Server

Follow the [official quickstart](https://modelcontextprotocol.io/quickstart). The pattern:

1. Pick a language (TS, Python, Rust, Go)
2. Use the SDK to create a server
3. Define tools with JSON schemas
4. Implement tool handlers
5. Test with the MCP inspector
6. Submit to the community servers list

## Security Considerations

MCP servers often expose sensitive operations. When contributing:

- Use read-only credentials by default
- Validate all inputs
- Do not log secrets
- Provide an explicit allowlist or confirmation flow for destructive operations
- Document the security model in the README

## Next Steps

- Read [AI-Specific Tips](../guides/ai-specific-tips.md)
- Explore existing MCP servers to understand patterns
- Pick an unmet need and build a server
