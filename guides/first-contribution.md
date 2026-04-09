# Making Your First Contribution

You found a project. You picked an issue. Now make the contribution.

## The Workflow

```
1. Fork       → Copy the repo to your GitHub account
2. Clone      → Download your fork to your machine
3. Branch     → Create a feature branch
4. Code       → Make your changes
5. Test       → Verify nothing broke
6. Commit     → Save changes with a good message
7. Push       → Upload your branch to your fork
8. PR         → Open a Pull Request on GitHub
9. Review     → Respond to feedback
10. Merged    → Celebrate
```

## Step-by-Step

### 1. Claim the Issue

Before you write any code, comment on the issue:

> Hi, I would like to work on this. Could you assign it to me?

This prevents two people from working on the same thing. Wait for a maintainer response before starting.

### 2. Fork the Repo

Click the "Fork" button on GitHub. This creates a copy under your account.

### 3. Clone Your Fork

```bash
git clone https://github.com/YOUR-USERNAME/project-name.git
cd project-name
```

### 4. Add the Upstream Remote

So you can pull in changes from the original repo:

```bash
git remote add upstream https://github.com/ORIGINAL-ORG/project-name.git
git remote -v  # Verify
```

### 5. Create a Branch

```bash
git checkout -b fix-typo-in-readme
```

Use a descriptive name. `fix-login-bug` is better than `patch-1`.

### 6. Set Up the Development Environment

Follow the project's CONTRIBUTING.md or README for setup. For Python projects, this usually means:

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

For Node projects:

```bash
npm install
# or pnpm install / bun install
```

### 7. Make Your Changes

Write the code. Follow the project's conventions. Look at recent merged PRs to see the style.

### 8. Test Your Changes

Run the project's test suite:

```bash
# Python
pytest

# Node
npm test
```

If you added new functionality, add tests for it. If you fixed a bug, add a regression test.

### 9. Run the Linter

```bash
# Python
ruff check .

# Node
npm run lint
```

Fix any issues.

### 10. Commit

```bash
git add .
git commit -m "fix: correct typo in README installation section"
```

Write a clear message. The convention is usually:

```
type: short description

Longer explanation if needed.

Fixes #123
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.

### 11. Push to Your Fork

```bash
git push origin fix-typo-in-readme
```

### 12. Open a Pull Request

Go to the original repo on GitHub. GitHub will show a banner asking if you want to create a PR from your branch.

Write a clear description:

```markdown
## What

Fixes the typo in the README installation section where "depenencies" should be "dependencies".

## Why

Closes #123. The typo was flagged by a user in the issue.

## Testing

- Ran `npm run lint` — clean
- Built the docs locally — renders correctly
```

Reference the issue with `Closes #123` so GitHub auto-closes it when merged.

### 13. Respond to Review

A maintainer will review your PR. They might:

- **Approve it** — you are done, wait for merge
- **Request changes** — make the changes and push new commits
- **Ask questions** — answer them
- **Close it** — try to understand why and learn

Push new commits to the same branch. The PR updates automatically.

### 14. After Merge

Your contribution is public and permanent. Congratulations.

Clean up:

```bash
git checkout main
git pull upstream main
git push origin main
git branch -d fix-typo-in-readme
git push origin --delete fix-typo-in-readme
```

## Special Considerations for AI Projects

### API Keys and Costs

Many agentic AI projects need an LLM API key to run tests. Check:

- Does the project accept a mock / fake LLM for tests?
- Is there a free tier (local Ollama, free HuggingFace models)?
- Are integration tests gated behind a flag so you can skip them?

**Never commit API keys.** Check `.gitignore` includes `.env`.

### Eval-Based Changes

For changes that affect LLM behavior:

- Run existing evals before your change
- Run them again after
- Report both results in your PR
- Explain any regressions

### Model Version Drift

LLM output changes between model versions. If a test fails because "GPT-4o-2024-11-20 gives different output than GPT-4o-2024-08-06", that is a model drift issue, not your bug. Document it and ask the maintainer for guidance.

## Common Mistakes

**Giant PRs.** Keep PRs small. One issue, one PR.

**No description.** Reviewers need context. Explain what and why.

**Ignoring CONTRIBUTING.md.** Every project has its own rules. Read them.

**Not running tests.** CI will catch failures. Why make the reviewer wait?

**Pushing to `main`.** Always use a feature branch.

**Getting discouraged by feedback.** Review comments are normal. Even experienced engineers get feedback. It is not personal.

## Next Steps

- [AI-Specific Tips](ai-specific-tips.md) — testing LLM code, managing costs, working with evals
- Browse the [project lists](../projects/) to find your next contribution
