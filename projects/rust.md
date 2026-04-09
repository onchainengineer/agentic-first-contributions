# Rust Agentic AI Projects

Rust has a smaller but growing agentic AI ecosystem. Projects here are often smaller and more approachable than their Python equivalents.

## Agent Frameworks

### [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig)

Ergonomic library for building LLM applications in Rust. Small core, clean API.

- **Good for**: Provider integrations, examples, docs
- **Smaller codebase** — easier to read end-to-end
- **Active maintainers**

### [rustformers/llm](https://github.com/rustformers/llm)

Collection of Rust crates for running LLMs locally.

- **Good for**: Model support, examples, benchmarks
- **Systems-level work** — good if you like low-level details

## LLM Inference

### [huggingface/candle](https://github.com/huggingface/candle)

Minimalist ML framework in Rust. Used for local LLM inference and training.

- **Good for**: Examples, new model support, docs
- **Professional team** from Hugging Face
- **High bar for core contributions**, lower for examples

### [mistralrs/mistral.rs](https://github.com/EricLBuehler/mistral.rs)

Fast LLM inference in Rust with quantization support.

- **Good for**: Model support, examples, benchmarks
- **Active development**

## Agent Tools

### [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)

Official Rust SDK for the Model Context Protocol.

- **Good for**: Examples, SDK improvements, docs
- **Official protocol** — good for long-term positioning
- **Early stage** — contributions shape the direction

## Embeddings and Vector Search

### [lancedb/lancedb](https://github.com/lancedb/lancedb)

Vector database built on Lance. Rust core with Python and JS clients.

- **Good for**: Python/JS bindings, docs, examples
- **Production-grade**, used in real deployments

### [qdrant/qdrant](https://github.com/qdrant/qdrant)

Vector similarity search engine.

- **Good for**: Features, docs, integrations
- **Mature project** with clear contribution process

## Coding Agents

### [TabbyML/tabby](https://github.com/TabbyML/tabby)

Self-hosted AI coding assistant. Rust core, TypeScript UI.

- **Good for**: Rust core improvements, model support
- **Hybrid**: Rust for inference, TS for UI

## How to Choose

**Want to learn Rust and AI together?** Start with rig — small, well-structured, welcoming.

**Systems programming background?** Candle or mistral.rs will feel familiar.

**Want to shape a new ecosystem?** The MCP Rust SDK is early enough that contributions matter a lot.

**Vector DB interests?** LanceDB or Qdrant.

## Why Rust for AI?

- **Performance**: critical for inference and embedding
- **Memory safety**: fewer production bugs
- **Growing ecosystem**: fewer projects than Python, but less competition per issue
- **Tooling**: cargo and clippy make onboarding easier than Python's fragmented tools

## Next Steps

- Read [How to Evaluate Projects](../guides/how-to-evaluate.md) first
- See [Making Your First Contribution](../guides/first-contribution.md)
