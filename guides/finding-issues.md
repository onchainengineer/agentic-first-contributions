# Finding Your First Issue

Once you have picked a project, you need to find an issue to work on. Here is the playbook.

## Method 1: Good First Issue Label

Every healthy project tags beginner-friendly issues with `good first issue`. On any GitHub repo:

1. Go to the Issues tab
2. Click the "Labels" filter
3. Select `good first issue`

URL pattern:
```
https://github.com/OWNER/REPO/issues?q=is:open+label:"good first issue"
```

Also check these related labels:
- `help wanted`
- `beginner`
- `beginner-friendly`
- `first-timers-only`
- `hacktoberfest`

## Method 2: Issue Type Filters

Different issue types have different difficulty levels.

### Easiest: Documentation

```
label:documentation
```

Docs fixes are low-risk: broken links, typos, unclear explanations. You do not need to understand the codebase.

### Next Easiest: Tests

```
label:tests
```

Adding missing test coverage is a great way to learn the codebase without changing behavior.

### Medium: Bug Fixes

```
label:bug label:"good first issue"
```

Reproducing a bug teaches you the codebase. Fixing it teaches you the architecture.

### Medium: Small Features

Look for features labeled `enhancement` and `good first issue` together.

### Harder: Architecture and Design

Avoid issues labeled `discussion`, `design`, or `rfc` as your first contribution. These require deep project context.

## Method 3: Search Within a Repo

GitHub's issue search supports powerful queries:

```
is:open is:issue label:"good first issue" no:assignee
```

Useful modifiers:
- `no:assignee` — nobody has claimed it yet
- `updated:>2026-03-01` — recently updated
- `comments:<3` — not already discussed to death
- `linked:pr` — has a related PR (read it for context)

## Method 4: Aggregator Platforms

Platforms that search across many repos:

### [goodfirstissue.dev](https://goodfirstissue.dev)

Filter by language. Shows current open issues across popular repos.

### [goodfirstissues.com](https://goodfirstissues.com)

Similar to the above. Different set of projects.

### [Up For Grabs](https://up-for-grabs.net)

Filter by tags (python, javascript, web, etc.).

### [First Timers Only](https://www.firsttimersonly.com)

Issues specifically reserved for people making their first contribution.

### [CodeTriage](https://www.codetriage.com)

Sign up and get a different open issue emailed to you every day.

## Method 5: AI-Specific Labels

Agentic AI projects sometimes use custom labels:

```
label:rag
label:agent
label:tools
label:mcp
label:eval
label:docs-tutorial
```

Look at the full label list in each repo for project-specific categories.

## What Makes a Good First Issue

A good first issue has:

**Clear problem statement.** You can read it once and understand what needs to happen.

**Clear definition of done.** You know when you are finished.

**Scoped to a few files.** Not "refactor the entire agent module".

**No architectural decisions.** The approach is clear, you just need to execute.

**Maintainer attention.** Recent comments from a maintainer saying "happy to help if you pick this up".

## Red Flags in Issues

**Stale.** Last activity 6+ months ago. Project may have moved on.

**Debated.** 30+ comments with contributors arguing about approach. Stay out.

**Already assigned.** Someone else is working on it. Pick another.

**Vague.** "Make X better." You cannot tell if you succeeded.

**Massive.** "Add support for Y." That is not a first issue.

**Duplicate.** The issue is linked to 5 closed PRs. The problem is harder than it looks.

## The Claim Pattern

Once you find an issue:

1. **Read the full issue and all comments**
2. **Check for an assignee** — if someone is assigned, pick another issue
3. **Comment on the issue**:

   > Hi, I would like to work on this. Could you assign it to me or confirm it is still open?

4. **Wait for response** — do not start coding yet
5. **Once confirmed, start work**
6. **Ask clarifying questions if needed**

## If You Cannot Find an Issue

Sometimes the "good first issue" label is empty. Here is what to do:

**Look for docs gaps.** Read the README and run the quickstart. If anything is unclear or outdated, propose a docs fix.

**Look for missing tests.** Run the coverage report. Find an uncovered function and add tests.

**Look for TODO comments in code.**

```bash
grep -r "TODO\|FIXME\|XXX" src/
```

Not every TODO is a good issue, but some are.

**Look at Dependabot PRs.** If a dependency update broke something, fixing it is a contribution.

**Ask the maintainers.** Open a discussion:

> I am new to the project and would like to contribute. Is there a small issue you could suggest?

## Progression

Your contribution journey should look like:

1. **First contribution**: Typo or small docs fix
2. **Second contribution**: Missing test or small bug
3. **Third contribution**: Small feature or medium bug
4. **Fourth+ contributions**: Anything you want

Each successful contribution builds maintainer trust. Over time, you get assigned harder work.

## Next Steps

- [Making Your First Contribution](first-contribution.md) — the PR workflow
- [AI-Specific Tips](ai-specific-tips.md) — unique challenges of AI projects
- Browse the [project lists](../projects/) for specific recommendations
