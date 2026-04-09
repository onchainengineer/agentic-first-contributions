# Evals and Observability

Tools for testing, tracing, and monitoring LLM applications. Critical for production agents but often underinvested. Great contribution opportunities.

## Evaluation Frameworks

### [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)

CLI for testing and evaluating LLM outputs. Declarative test files.

- **Stack**: TypeScript
- **Good for**: New providers, assertion types, docs, examples
- **Very accessible for beginners**
- **Active community**

### [explodinggradients/ragas](https://github.com/explodinggradients/ragas)

Evaluation framework specifically for RAG pipelines.

- **Stack**: Python
- **Good for**: New metrics, examples, docs
- **Academic rigor**, practical focus

### [openai/evals](https://github.com/openai/evals)

Framework for evaluating LLMs. The original eval framework from OpenAI.

- **Stack**: Python
- **Good for**: New evals (each is self-contained), docs
- **Slower-moving** but foundational

### [confident-ai/deepeval](https://github.com/confident-ai/deepeval)

Unit testing for LLM outputs.

- **Stack**: Python
- **Good for**: New metrics, integrations, docs

### [stanford-crfm/helm](https://github.com/stanford-crfm/helm)

Holistic evaluation of language models.

- **Stack**: Python
- **Good for**: New scenarios, benchmarks, docs
- **Academic project** — higher bar, higher impact

## Observability Platforms

### [langfuse/langfuse](https://github.com/langfuse/langfuse)

Open source LLM engineering platform. Tracing, evals, prompt management.

- **Stack**: TypeScript + Next.js
- **Good for**: UI work, SDK improvements, integrations
- **Enterprise-quality codebase**
- **Professional team**

### [helicone/helicone](https://github.com/helicone/helicone)

Open source LLM observability with a proxy architecture.

- **Stack**: TypeScript
- **Good for**: Provider support, docs, UI

### [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)

ML observability in a notebook.

- **Stack**: Python + TypeScript
- **Good for**: Integrations, docs, examples

### [traceloop/openllmetry](https://github.com/traceloop/openllmetry)

OpenTelemetry-based observability for LLM apps.

- **Stack**: Python + TypeScript
- **Good for**: Instrumentation for new frameworks, docs

### [lunary-ai/lunary](https://github.com/lunary-ai/lunary)

Open source observability and analytics for LLM apps.

- **Stack**: TypeScript
- **Good for**: Features, docs

### [comet-ml/opik](https://github.com/comet-ml/opik)

LLM evaluation and observability.

- **Stack**: Python + TypeScript
- **Good for**: SDK improvements, integrations

## Prompt Management

### [langfuse/langfuse](https://github.com/langfuse/langfuse)
(also includes prompt management)

### [promptlayer/promptlayer-python](https://github.com/MagnivOrg/prompt-layer-library)

Prompt versioning and tracking.

## Why This Category Matters

LLM apps without observability are impossible to debug. Evals are the only way to know if a prompt change actually improves things. This is where production AI separates from demos.

## What to Contribute

**Integrations.** Each new LLM framework or vendor needs instrumentation.

**New metrics.** Novel eval metrics are genuinely useful research.

**Examples.** Show how to use the tool on real applications.

**Dashboards.** Better visualization of traces and metrics.

**Provider support.** Evals and observability tools need to work with every LLM.

## Challenges

**LLM non-determinism** makes tests hard. Your contributions should handle this gracefully.

**Cost sensitivity** — users run evals often. Efficiency matters.

**Privacy** — observability captures prompts and outputs. Handle PII carefully.

## Next Steps

- [AI-Specific Tips](../guides/ai-specific-tips.md) — how to work with evals
- [How to Evaluate Projects](../guides/how-to-evaluate.md)
