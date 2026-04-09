# Tips for Contributing to AI Projects

Agentic AI projects have unique challenges that normal open source projects do not. Here is what to know.

## API Keys and Costs

### The Problem

Most LLM frameworks need an API key to run. Running tests can cost money. A full test suite might cost $5-50 per run.

### What to Do

**Check for free alternatives first:**

- **Local models**: many projects support Ollama, llama.cpp, or HuggingFace local models
- **Free tiers**: Together, Groq, Anthropic free tier, OpenAI free credits
- **Mock LLMs**: many frameworks have `FakeLLM`, `MockChatModel`, or similar for testing
- **VCR / cassettes**: projects may record LLM responses and replay them in tests

**Read the CONTRIBUTING.md for the project's recommended approach.** Some projects explicitly ask contributors to use `pytest -k 'not integration'` to skip expensive tests.

**Never commit API keys.** Check the `.gitignore`. If `.env` is not there, do not put your keys in one.

### Environment Variables

Most projects expect keys in environment variables:

```bash
export OPENAI_API_KEY=sk-...
export ANTHROPIC_API_KEY=sk-ant-...
```

Use a `.env` file that is gitignored:

```bash
# .env (never commit)
OPENAI_API_KEY=sk-...
```

Load it with `python-dotenv` or similar.

## Testing LLM Code

### The Problem

LLMs are non-deterministic. The same input can give different outputs. Traditional assertions like `assert output == "expected"` do not work.

### Strategies

**1. Test the structure, not the content.**

```python
# Bad
assert response == "The answer is 42"

# Good
assert "42" in response
assert len(response) > 0
assert isinstance(response, str)
```

**2. Use JSON mode or function calling for structured outputs.**

Structured outputs are testable:

```python
response = llm.with_structured_output(AnswerSchema).invoke(query)
assert response.confidence > 0.5
assert response.answer is not None
```

**3. Use evals, not assertions.**

For quality checks, use an LLM-as-judge:

```python
def test_summarization_quality():
    summary = summarize(long_text)
    score = judge_llm.evaluate(
        prompt=f"Rate this summary 1-10 for accuracy: {summary}",
        criteria="accuracy, conciseness"
    )
    assert score >= 7
```

**4. Mock the LLM for unit tests.**

For unit tests that do not actually need the LLM:

```python
from langchain.llms.fake import FakeListLLM

llm = FakeListLLM(responses=["canned response 1", "canned response 2"])
# Now test your agent logic without calling a real LLM
```

**5. Record and replay.**

Use `vcr.py` or similar to record real LLM responses once, then replay them in CI.

## Working with Evals

### What Evals Are

Evals are test suites for LLM behavior. They run the model on a set of inputs and measure outputs against expected criteria.

Examples:
- Accuracy on a benchmark
- Faithfulness to source documents (RAG)
- Tool call accuracy (agents)
- Latency and token usage

### Contributing Eval Changes

If your PR affects LLM behavior (prompt changes, model changes, tool changes):

1. **Run the evals before your change.** Record the baseline.
2. **Make your change.**
3. **Run the evals again.**
4. **Report both results in the PR description.**

Example:

```markdown
## Eval Results

### Before
- Accuracy: 78.2%
- Average latency: 1.2s
- Token usage: 340/query

### After
- Accuracy: 82.5% (+4.3%)
- Average latency: 1.3s (+0.1s)
- Token usage: 365/query (+25)
```

Transparency about tradeoffs matters.

### Regression Policy

Check the project's regression policy before submitting. Some projects block any accuracy regression. Others accept small regressions if latency improves. Ask in the issue or PR if unclear.

## Model Version Drift

LLMs change. The same model name can produce different outputs across versions.

### Symptoms

- Tests pass locally but fail in CI
- A maintainer says "this test was passing last week"
- Behavior differs between your machine and production

### Handling It

- **Pin model versions** when possible: `gpt-4o-2024-08-06` instead of `gpt-4o`
- **Document model versions** in test fixtures
- **Do not fix flaky tests by loosening assertions** — understand why they are flaky
- **Ask the maintainer** before making big changes to eval baselines

## Dependency Hell

AI projects pull in huge dependency trees. Installation is often painful.

### Tips

**Use virtual environments religiously.**

```bash
python -m venv venv
source venv/bin/activate
```

**Try `uv` or `pixi` for faster installs.**

```bash
uv pip install -e ".[dev]"
```

**Watch for conflicting CUDA / torch versions.** If you see CUDA errors, the project may need a specific PyTorch version.

**Read the project's Docker setup if one exists.** It is often the fastest way to get a working environment.

## Benchmarks and Claims

When contributing benchmark numbers or performance claims:

- **Specify the exact hardware.** "GPU: A100 80GB, batch size 32"
- **Specify the exact model version.** "gpt-4o-2024-08-06"
- **Specify the exact dataset and version.** "MMLU v1.0, 5-shot"
- **Include the raw numbers, not just the conclusion.**
- **Link to your reproduction script.**

Unreproducible benchmarks are worthless.

## Prompt Engineering Contributions

Changing a prompt is a code change. Treat it like one.

- Explain WHY the new prompt is better
- Show before/after examples
- Run evals and report results
- Consider edge cases (long inputs, empty inputs, non-English)

Do not submit prompt changes based on "it seems better". Measure it.

## Working with Maintainers

### Ask Before Building

Before you invest hours on a feature:

> I would like to add X. Before I start, could you confirm this fits the project direction?

This prevents wasted work on PRs maintainers will reject.

### Be Patient

AI projects are often hit with inexperienced contributors using AI to generate low-quality PRs. Maintainers may be skeptical at first. Build trust through small, high-quality contributions before tackling big changes.

### Document What You Learned

If you figured out something non-obvious during your contribution — how to set up the dev environment, how to run a specific test, how to debug an issue — consider contributing that as a docs PR too.

## Next Steps

- [Finding Your First Issue](finding-issues.md) — tools and filters
- Browse the [project lists](../projects/) to find where to contribute
