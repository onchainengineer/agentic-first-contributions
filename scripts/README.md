# Scripts

Automation scripts for the repo.

## fetch-issues.py

Queries the GitHub API for each project in `projects.yaml` and updates `projects/live-status.md` with current issue counts.

### Usage

```bash
# Install dependencies
pip install requests pyyaml

# Set your GitHub token
export GITHUB_TOKEN=ghp_...

# Run
python fetch-issues.py
```

### Getting a Token

Create a personal access token at [github.com/settings/tokens](https://github.com/settings/tokens). The script only needs **read access to public repos** — no special scopes required. A classic token with no scopes works, or a fine-grained token with "Public repositories (read-only)".

### Rate Limits

The GitHub API allows:

- **60 requests/hour** without a token
- **5,000 requests/hour** with a token

Each project requires 4 API calls (repo info, 3 label searches), so fetching ~50 projects uses ~200 calls. Well under the token limit.

### Automation

The script is run automatically weekly by the GitHub Action in `.github/workflows/update-status.yml`. It commits the updated `projects/live-status.md` to the repo.

## projects.yaml

The list of tracked projects. To add a project:

1. Verify it meets the [contribution criteria](../CONTRIBUTING.md)
2. Add an entry with `repo`, `category`, and `language`
3. Open a PR

Example entry:

```yaml
- repo: owner/name
  category: agent-framework
  language: Python
```

Valid categories:
- `agent-framework`
- `visual-builder`
- `coding-agent`
- `memory-rag`
- `llm-tooling`
- `mcp`
- `evals-observability`
