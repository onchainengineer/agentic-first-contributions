# Memory and RAG Projects

Retrieval-Augmented Generation (RAG) and persistent memory are core building blocks of production agents. These projects power the "remembers what we talked about" and "knows your docs" parts of agentic apps.

## Memory Systems

### [mem0ai/mem0](https://github.com/mem0ai/mem0)

Memory layer for AI agents. Stores user-specific context across sessions.

- **Stack**: Python
- **Good for**: Integrations (LLMs, vector stores), examples, docs
- **Approachable codebase**

### [getzep/zep](https://github.com/getzep/zep)

Long-term memory for AI assistants. Go backend with Python/TS clients.

- **Stack**: Go core, Python + TS clients
- **Good for**: Client library improvements, docs

### [letta-ai/letta](https://github.com/letta-ai/letta)

Stateful LLM agent framework with memory. Formerly MemGPT.

- **Stack**: Python
- **Good for**: Examples, memory strategies, docs

## Vector Databases

### [chroma-core/chroma](https://github.com/chroma-core/chroma)

Popular open source vector database. Embeddable or self-hosted.

- **Stack**: Python + Rust
- **Good for**: Python client, integrations, docs

### [qdrant/qdrant](https://github.com/qdrant/qdrant)

Vector similarity search engine. Rust core with multi-language clients.

- **Stack**: Rust + Python/TS clients
- **Good for**: Features, docs, client improvements

### [weaviate/weaviate](https://github.com/weaviate/weaviate)

Vector search engine with hybrid search and generative modules.

- **Stack**: Go
- **Good for**: Modules, docs, integrations

### [lancedb/lancedb](https://github.com/lancedb/lancedb)

Vector database built on Lance. Fast, embedded-friendly.

- **Stack**: Rust core, Python + JS clients
- **Good for**: Client bindings, examples, docs

### [milvus-io/milvus](https://github.com/milvus-io/milvus)

Cloud-native vector database. Production-grade.

- **Stack**: Go
- **Good for**: Docs, clients, integrations

## RAG Frameworks

### [run-llama/llama_index](https://github.com/run-llama/llama_index)

The most popular RAG framework in Python.

- **Good for**: Data loaders, query engines, docs
- **Huge integration surface**

### [explodinggradients/ragas](https://github.com/explodinggradients/ragas)

Evaluation framework for RAG pipelines.

- **Stack**: Python
- **Good for**: New metrics, examples, docs
- **Active development**

### [neuml/txtai](https://github.com/neuml/txtai)

All-in-one semantic search and RAG platform.

- **Stack**: Python
- **Good for**: Examples, integrations, docs

## Embedding Models and Tools

### [huggingface/text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference)

Fast inference for open embedding models.

- **Stack**: Rust
- **Good for**: Model support, benchmarks, docs

### [nomic-ai/nomic](https://github.com/nomic-ai/nomic)

Nomic's open embedding models and tooling.

- **Good for**: Examples, integrations

## Document Processing

### [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)

Extract and clean text from documents for LLM pipelines.

- **Stack**: Python
- **Good for**: New file format support, docs

### [opendatalab/MinerU](https://github.com/opendatalab/MinerU)

PDF to structured data extraction for RAG.

- **Stack**: Python
- **Good for**: Model improvements, examples

## How to Choose

**Want to start small?** mem0, Chroma Python client, or ragas are approachable.

**Systems background?** LanceDB, Qdrant, or milvus.

**Love data pipelines?** LlamaIndex or Unstructured.

**Interested in evals?** Ragas is the go-to.

## Contributing Ideas

**Add support for a new file format** in Unstructured or MinerU.

**Add a new data loader** to LlamaIndex.

**Write benchmark scripts** comparing vector DBs on real workloads.

**Add retrieval strategies** to ragas.

**Build integration examples** showing how to connect memory systems to agent frameworks.

## Next Steps

- [How to Evaluate Projects](../guides/how-to-evaluate.md)
- [Agent Frameworks](agent-frameworks.md) — combine memory with agent frameworks
