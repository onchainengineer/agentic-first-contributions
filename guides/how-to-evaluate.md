# How to Evaluate an Open Source Project

Before you invest time contributing, check if the project is worth it. A bad project wastes your effort. A good one multiplies it.

## The 10-Minute Health Check

Spend 10 minutes on these checks before you pick an issue:

### 1. Recent Activity (1 min)

Look at the GitHub repo's activity:

- **Recent commits**: Is there a commit in the last 30 days? Preferably the last 7.
- **Recent PRs**: Are PRs being merged? Check the "Pull requests" tab.
- **Recent issues**: Are new issues being opened? Are they being triaged?

Red flag: Last commit 6+ months ago, even if it has 50k stars.

### 2. Maintainer Responsiveness (2 min)

Click into 5 recent PRs and 5 recent issues:

- Are maintainers responding?
- How long between a PR opening and first review?
- Are questions answered?

Red flag: PRs sitting for months with no response.

### 3. CONTRIBUTING.md Quality (2 min)

Open `CONTRIBUTING.md` and read it:

- Does it explain the setup steps clearly?
- Does it describe the PR workflow?
- Does it mention tests?
- Does it have a "good first issue" section?

Red flag: No CONTRIBUTING.md, or one that is just "open a PR".

### 4. Good First Issue Label (1 min)

Go to the issues tab and filter by `label:"good first issue"`:

- Are there any?
- How many are open?
- Are they well described (clear problem, clear definition of done)?
- Are they recent?

Red flag: Zero good first issues, or all of them are from 2022.

### 5. Test Suite (2 min)

Clone the repo and try to run the tests:

```bash
git clone https://github.com/org/repo.git
cd repo
# Follow the test command from README or CONTRIBUTING
```

- Do the tests pass on `main`?
- How long do they take?
- Are there clear failures?

Red flag: Tests do not run, fail on main, or take hours.

### 6. Community Signals (2 min)

Check for community health signs:

- Does the project have a Discord, Slack, or forum?
- Is the maintainer responsive on those platforms?
- Is there a CODE_OF_CONDUCT?
- Are contributor credits visible (all-contributors, CONTRIBUTORS.md)?

## The Star Count Trap

High star counts mean the project was popular at some point. They do **not** mean:

- The project is active
- Maintainers respond to PRs
- Your contribution will be accepted
- The code is good

**Ignore stars as your primary signal.** Look at commit frequency and PR merge rate instead.

## Good Signs

### Healthy Maintainer Engagement

- PRs reviewed within a week
- Questions answered within a few days
- Clear decisions on proposals (accept, reject, or reason)
- Thank you notes to contributors

### Clear Governance

- Documented decision-making process
- Defined maintainer roles
- CODE_OF_CONDUCT enforced
- Public roadmap or project board

### Beginner Friendly Culture

- Detailed CONTRIBUTING.md
- Issue templates that guide beginners
- "good first issue" and "help wanted" labels actively used
- Documentation is welcoming, not just reference

### Good Development Practices

- CI running on every PR
- Linting and formatting enforced
- Tests cover new features
- Code reviews happen publicly on PRs

## Red Flags

### Slow or No Maintenance

- Commits sparse, more than a month between them
- PRs sitting for months unreviewed
- Issues unanswered
- "Looking for maintainers" notice in README

### Poor Contributor Experience

- No CONTRIBUTING.md, or very short one
- No issue templates
- Maintainer dismisses questions as "just read the code"
- Hostile tone in issues or PRs

### Technical Debt Signals

- CI broken on main
- Many duplicate issues
- Massive PRs with no reviews
- Tests missing or broken

### Abandoned but Popular

- Many stars
- Last commit 6+ months ago
- "Archived" notice coming soon
- Forks with more activity than the original

If you see these, look for a maintained fork or pick a different project.

## The "Am I Welcome?" Test

Read the last 10 closed PRs. For each:

- Was it merged or closed?
- If closed without merge, was there a clear reason?
- How were new contributors treated?
- Was feedback constructive?

If you see maintainers being curt, dismissive, or impatient with beginners, find a different project. Your experience will be similar.

## When in Doubt, Start Small

The safest first contribution is a **typo fix**. If a typo PR:

- Gets merged within a few days
- Gets friendly feedback
- Uses a clear process

...then the project is probably a good fit for larger contributions.

If your typo PR sits for weeks or gets closed without explanation, move on.

## Next Steps

- [Finding Your First Issue](finding-issues.md) — pick an issue to work on
- [Making Your First Contribution](first-contribution.md) — the PR workflow
