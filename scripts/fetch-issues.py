#!/usr/bin/env python3
"""
Fetch good-first-issue counts for tracked projects and update projects/live-status.md.

Usage:
    export GITHUB_TOKEN=your_token_here
    pip install requests pyyaml
    python fetch-issues.py

The script reads projects.yaml, queries the GitHub API for each project,
and writes a sorted markdown table to projects/live-status.md.
"""

from __future__ import annotations

import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
import yaml

GITHUB_API = "https://api.github.com"
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
PROJECTS_FILE = SCRIPT_DIR / "projects.yaml"
OUTPUT_FILE = REPO_ROOT / "projects" / "live-status.md"


def get_token() -> str:
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("ERROR: GITHUB_TOKEN environment variable not set", file=sys.stderr)
        print("Create a token at https://github.com/settings/tokens", file=sys.stderr)
        sys.exit(1)
    return token


def gh_get(url: str, token: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    resp = requests.get(url, headers=headers, params=params, timeout=30)
    if resp.status_code != 200:
        print(f"WARN: {url} returned {resp.status_code}: {resp.text[:200]}", file=sys.stderr)
        return {}
    return resp.json()


def count_issues(repo: str, label: str, token: str) -> int:
    """Count open issues with the given label using the search API."""
    url = f"{GITHUB_API}/search/issues"
    query = f'repo:{repo} is:issue is:open label:"{label}"'
    data = gh_get(url, token, params={"q": query, "per_page": 1})
    return int(data.get("total_count", 0))


def get_repo_info(repo: str, token: str) -> dict[str, Any]:
    """Get basic repo info: stars, last push, default branch."""
    data = gh_get(f"{GITHUB_API}/repos/{repo}", token)
    return {
        "stars": data.get("stargazers_count", 0),
        "pushed_at": data.get("pushed_at", ""),
        "archived": data.get("archived", False),
        "url": data.get("html_url", f"https://github.com/{repo}"),
    }


def format_stars(n: int) -> str:
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def format_relative(iso_time: str) -> str:
    if not iso_time:
        return "unknown"
    try:
        dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    except ValueError:
        return iso_time
    now = datetime.now(timezone.utc)
    delta = now - dt
    days = delta.days
    if days == 0:
        return "today"
    if days == 1:
        return "1 day ago"
    if days < 30:
        return f"{days} days ago"
    if days < 365:
        return f"{days // 30} mo ago"
    return f"{days // 365}y ago"


def load_projects() -> list[dict[str, str]]:
    with PROJECTS_FILE.open() as f:
        data = yaml.safe_load(f)
    return data["projects"]


def fetch_all(projects: list[dict[str, str]], token: str) -> list[dict[str, Any]]:
    results = []
    for i, project in enumerate(projects, 1):
        repo = project["repo"]
        print(f"[{i}/{len(projects)}] Fetching {repo}...", file=sys.stderr)
        info = get_repo_info(repo, token)
        if not info:
            continue
        gfi = count_issues(repo, "good first issue", token)
        hw = count_issues(repo, "help wanted", token)
        docs = count_issues(repo, "documentation", token)
        results.append({
            "repo": repo,
            "category": project.get("category", ""),
            "language": project.get("language", ""),
            "stars": info["stars"],
            "pushed_at": info["pushed_at"],
            "archived": info["archived"],
            "url": info["url"],
            "good_first_issue": gfi,
            "help_wanted": hw,
            "documentation": docs,
        })
    return results


def render_markdown(results: list[dict[str, Any]]) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines: list[str] = []
    lines.append("# Live Status")
    lines.append("")
    lines.append(f"**Last updated**: {now}")
    lines.append("")
    lines.append(
        "Current open issue counts for every tracked project. "
        "Sorted by good first issue count, descending."
    )
    lines.append("")
    lines.append("See the [guides](../guides/) before picking a project. High issue counts do not always mean healthy projects.")
    lines.append("")

    # Sort by good-first-issue count descending, then by stars
    sorted_results = sorted(
        results, key=lambda r: (r["good_first_issue"], r["stars"]), reverse=True
    )

    lines.append("## All Projects")
    lines.append("")
    lines.append("| Project | Category | Language | Stars | Good First Issue | Help Wanted | Docs | Last Push |")
    lines.append("|---------|----------|----------|-------|------------------|-------------|------|-----------|")
    for r in sorted_results:
        archived_note = " (archived)" if r["archived"] else ""
        lines.append(
            f"| [{r['repo']}]({r['url']}){archived_note} "
            f"| {r['category']} "
            f"| {r['language']} "
            f"| {format_stars(r['stars'])} "
            f"| {r['good_first_issue']} "
            f"| {r['help_wanted']} "
            f"| {r['documentation']} "
            f"| {format_relative(r['pushed_at'])} |"
        )
    lines.append("")

    # Top 10 by good first issue
    lines.append("## Top 10 by Good First Issue Count")
    lines.append("")
    top = [r for r in sorted_results if r["good_first_issue"] > 0][:10]
    if top:
        lines.append("| Project | Good First Issue | Link |")
        lines.append("|---------|------------------|------|")
        for r in top:
            lines.append(
                f"| {r['repo']} | {r['good_first_issue']} | [{r['good_first_issue']} open issues]({r['url']}/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) |"
            )
    else:
        lines.append("_No projects with open good first issues in this update._")
    lines.append("")

    # Freshness
    lines.append("## Freshness")
    lines.append("")
    stale = [r for r in sorted_results if "mo ago" in format_relative(r["pushed_at"]) or "y ago" in format_relative(r["pushed_at"])]
    if stale:
        lines.append(f"**{len(stale)} projects have not been pushed to recently.** Consider removing from the curated list if they remain stale.")
        lines.append("")
        for r in stale:
            lines.append(f"- {r['repo']} — last push: {format_relative(r['pushed_at'])}")
    else:
        lines.append("All tracked projects have been updated recently.")
    lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(
        "_Generated by [`scripts/fetch-issues.py`](../scripts/fetch-issues.py). "
        "To update manually: `cd scripts && python fetch-issues.py`._"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    token = get_token()
    projects = load_projects()
    print(f"Fetching status for {len(projects)} projects...", file=sys.stderr)
    results = fetch_all(projects, token)
    markdown = render_markdown(results)
    OUTPUT_FILE.write_text(markdown)
    print(f"Wrote {OUTPUT_FILE}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
