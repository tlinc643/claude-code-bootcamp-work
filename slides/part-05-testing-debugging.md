---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 5"
footer: "Luca Berton · Testing, Debugging & Self-Review"
---

# Part 5
## Testing, Debugging & Self-Review

**Duration:** 35 min · **Format:** Guided lab + code review checkpoint
**Deliverable:** Tests + bug fixes + a **review rubric**

---

## Testing Mindset with AI

AI writes code fast. **Tests are the brake pedal.**

Without tests, AI velocity = AI risk velocity.

---

## Getting Meaningful Tests

Bad: *"Write tests."*
Good:

> *"For each endpoint, write tests for: happy path, missing fields, oversized body, non-existent ID, malformed JSON, and concurrent updates. Use AAA format and table-driven where it helps."*

Specify **categories**, not counts.

---

## Asking Claude to Find Its Own Bugs

> *"Review the code you just wrote. List 5 likely bugs, ranked by severity. Prove or disprove each with a test."*

This works because Claude is a better **critic** than **author** in a fresh context.

---

## Review Rubrics

A rubric forces consistent reviews. Example:

1. Correctness — does it satisfy acceptance criteria?
2. Edge cases — empty, max, malformed, concurrent
3. Error handling — fail loudly, fail safely
4. Security — input validation, secrets, authz
5. Tests — coverage on **behavior**, not lines
6. Readability — names, structure, comments

---

## Debugging Loop with Claude

```
1. Reproduce — minimal failing case
2. Show — paste error + relevant code
3. Hypothesize — ask Claude for top 3 causes
4. Test — verify each hypothesis
5. Fix — smallest possible change
6. Regression test — lock the bug out
```

---

## When NOT to Trust AI Code

- Auth, crypto, payments → human review mandatory
- Migrations, deletes, irreversible ops
- Code touching production secrets
- "Confident" code with **no tests**
- Anything you don't understand line-by-line

---

## Human Checkpoints

Always insert human review at:
- **Plan approval** — before any code
- **Diff review** — before commit
- **Pre-merge** — before main
- **Pre-deploy** — before prod

---

## Mini Project 5 — Test & Debug the Notes API

1. Generate test suite (unit + integration)
2. Ask Claude to self-review against your rubric
3. Triage findings → fix top 3 bugs
4. Add regression tests for each
5. Commit `test(notes-api): harden CRUD with edge cases`

---

## Skills Practiced

- Unit testing
- Debugging
- Test coverage
- AI-assisted code review
- Rubric-based evaluation

---

## Deliverable Checklist ✅

- [ ] Test suite in `02-notes-api/tests/`
- [ ] ≥ 1 test per category (happy, missing, oversized, 404, malformed)
- [ ] At least **3 documented bugs** with fixes
- [ ] Regression test per bug
- [ ] `REVIEW_RUBRIC.md` committed
- [ ] All tests passing on `main`

---

## Definition of Done

- `pytest` (or equiv.) green
- Coverage on every endpoint
- Rubric reusable on later projects
- Each bug has: *symptom → cause → fix → test*

---

## Review Checkpoint 🔎

Swap rubrics with a peer:
- Apply their rubric to your code
- Apply yours to theirs
- Each finds **one issue** the other missed.

---

## Next Up

**Part 6 — Git Workflows for Safe AI Development**
Branches, diffs, and worktrees as your safety net.
