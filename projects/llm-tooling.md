# LLM Tooling and Infrastructure

Lower-level projects that power agentic AI: inference engines, model servers, unified APIs, and runtime tools.

## Inference Engines

### [ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)

LLM inference in C/C++. The foundation of local model running.

- **Stack**: C/C++ with many language bindings
- **Good for**: Bindings, examples, docs
- **High bar for core**, accessible for bindings

### [vllm-project/vllm](https://github.com/vllm-project/vllm)

High-throughput LLM inference engine. Used in production by many companies.

- **Stack**: Python + CUDA
- **Good for**: Examples, benchmarks, docs, small optimizations
- **Deep GPU knowledge** needed for core

### [huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference)

Production inference server from Hugging Face.

- **Stack**: Rust + Python
- **Good for**: Model support, examples, docs

### [EricLBuehler/mistral.rs](https://github.com/EricLBuehler/mistral.rs)

Fast LLM inference in Rust with quantization.

- **Stack**: Rust
- **Good for**: Model support, benchmarks

## Local Model Runners

### [ollama/ollama](https://github.com/ollama/ollama)

Run LLMs locally with a simple API. One of the biggest projects in the space.

- **Stack**: Go
- **Good for**: Model support, docs, clients
- **Massive community**

### [LM-Studio](https://github.com/lmstudio-ai)

Desktop app for running local models. Has an open core.

- **Good for**: Docs, model examples

### [Mozilla-Ocho/llamafile](https://github.com/Mozilla-Ocho/llamafile)

Distribute and run LLMs as a single file.

- **Stack**: C++ + cosmopolitan libc
- **Good for**: Docs, examples, model packaging

## Unified APIs

### [BerriAI/litellm](https://github.com/BerriAI/litellm)

Unified API for 100+ LLM providers. Drop-in OpenAI replacement.

- **Stack**: Python
- **Good for**: Adding provider support, docs, tests
- **Low barrier**: each provider is a self-contained PR

### [simonw/llm](https://github.com/simonw/llm)

CLI and Python library for interacting with LLMs.

- **Stack**: Python
- **Good for**: Plugins (each is a separate package), docs
- **Very responsive maintainer** (Simon Willison)

## Structured Output

### [guidance-ai/guidance](https://github.com/guidance-ai/guidance)

Programming paradigm for controlled LLM output.

- **Good for**: Examples, docs, tests

### [outlines-dev/outlines](https://github.com/outlines-dev/outlines)

Structured text generation.

- **Stack**: Python
- **Good for**: Grammar support, examples, docs

### [dottxt-ai/regex](https://github.com/dottxt-ai)

Constrained generation research and tools.

## Prompt Management

### [BerriAI/litellm](https://github.com/BerriAI/litellm)
(listed above, also handles prompt management)

### [mirascope/mirascope](https://github.com/mirascope/mirascope)

Pythonic prompt management and LLM calls.

- **Good for**: Provider support, examples, docs

## Serving and Deployment

### [bentoml/BentoML](https://github.com/bentoml/BentoML)

Framework for building and deploying ML services, including LLMs.

- **Stack**: Python
- **Good for**: Examples, docs, integrations

### [replicate/cog](https://github.com/replicate/cog)

Containers for machine learning.

- **Stack**: Go + Python
- **Good for**: Docs, examples

## How to Choose

**Low-level systems work?** llama.cpp, vllm, text-generation-inference.

**Want a low-barrier first PR?** Add a provider to LiteLLM or a plugin to simonw/llm.

**Like Rust?** mistral.rs or text-embeddings-inference.

**Like Go?** Ollama.

**Focused on production?** BentoML or Cog.

## What to Contribute

**Provider integrations** are the easiest. Pick an LLM API and add support.

**Model support** for inference engines is self-contained.

**Benchmarks** are undervalued. Well-designed benchmarks get cited and used.

**Docs** are always needed. Inference engines change fast and docs lag.

**Bindings** for languages not yet supported. llama.cpp has many but always needs more.

## Next Steps

- [Agent Frameworks](agent-frameworks.md) — projects built on top of this tooling
- [How to Evaluate Projects](../guides/how-to-evaluate.md)
