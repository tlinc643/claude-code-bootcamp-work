---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 6"
footer: "Luca Berton · Git Workflows for Safe AI Development"
---

# Part 6
## Git Workflows for Safe AI Development

**Duration:** 30 min · **Format:** Demo + hands-on workflow
**Deliverable:** Feature branch + reviewed diff + clean commit history

---

## Why Git Matters MORE with AI

AI changes a lot of code, fast.
Git is your **undo button**, your **review surface**, and your **collaboration contract**.

> No branch = no safety net.

---

## Feature Branches

```bash
git checkout -b feat/notes-tagging
# ... claude code session ...
git diff main...HEAD          # review
git add -p                    # stage selectively
git commit -m "feat(notes): add tagging + search"
git push -u origin feat/notes-tagging
```

Treat every Claude session as a **proposed change**, not a fait accompli.

---

## Commit Discipline

- One logical change per commit
- Imperative mood: *"add"*, *"fix"*, *"refactor"*
- Conventional Commits: `feat:`, `fix:`, `test:`, `docs:`, `chore:`
- Body explains **why**, not what
- Co-author Claude when relevant

---

## Reviewing Claude-Generated Diffs

Always read:
- New files in full
- Deleted lines (often the bug)
- Files **you didn't expect** to change
- Test files (are they real tests or placebos?)

> Trust the diff, not the chat summary.

---

## Safe Rollback

```bash
git revert <sha>           # safe public undo
git reset --hard <sha>     # local nuke (caution)
git stash                  # park work-in-progress
git restore <file>         # undo unstaged changes
```

Worktrees keep failed experiments **out of your main checkout**.

---

## Parallel Work with Worktrees

```bash
git worktree add ../notes-api-experiment-A feat/exp-a
git worktree add ../notes-api-experiment-B feat/exp-b
```

Run **two Claude sessions in parallel** without conflict.
Compare outcomes before choosing.

---

## Keeping AI Experiments Isolated

- Prefix branches: `ai/`, `exp/`, `spike/`
- Never let AI commit directly to `main`
- Squash-merge spikes; rebase clean features
- Tag known-good states: `v0.1-notes-api`

---

## Mini Project 6 — Feature Branch Workflow

**Task:** Add tagging + search to the Notes API.

1. `git checkout -b feat/notes-tagging`
2. Prompt Claude to plan + implement
3. Review diff line-by-line
4. Run tests
5. Commit in **logical chunks**
6. Merge to `main` with clean history

---

## Deliverable Checklist ✅

- [ ] Feature branch pushed
- [ ] Commit history readable: `git log --oneline`
- [ ] At least **2 logical commits** (impl + tests)
- [ ] Diff review notes saved in `reports/part-06-review.md`
- [ ] Tests still green on merge
- [ ] One worktree experiment created and removed

---

## Definition of Done

- Branch fast-forwards or rebases cleanly
- `main` always green
- Diff review notes mention at least one **rejected change**
- Commits follow Conventional Commits
- A peer can rebuild the change from `git log` alone

---

## Review Checkpoint 🔎

Pair review the PR-style diff:
- Spot one risky change
- Spot one unnecessary change
- Approve only after both are addressed.

---

## Break 2 — 10 minutes ☕

---

## Next Up

**Part 7 — Multimodal Prompting: Screenshot to UI**
You'll turn a wireframe into a working dashboard.
