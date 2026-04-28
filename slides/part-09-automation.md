---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 9"
footer: "Luca Berton · Automation: Commands, Hooks & Reusable Workflows"
---

# Part 9
## Automation: Commands, Hooks & Reusable Workflows

**Duration:** 30 min · **Format:** Concept walkthrough + practical lab
**Deliverable:** A **personal Claude Code command library**

---

## Why Automate?

You'll repeat the same prompts hundreds of times:
- *"Review this diff."*
- *"Generate tests for X."*
- *"Write release notes since last tag."*

Stop retyping. **Save them as commands.**

---

## Reusable Command Patterns

A command = a parametrized prompt template:

```md
# /review
Review the staged diff against our review rubric.
Output: severity-ranked list with file:line and proposed fix.
Constraint: do not modify code yet.
```

Stored once, invoked everywhere.

---

## Command Library Categories

| Category | Examples |
|---|---|
| Review | `/review`, `/security-review`, `/perf-review` |
| Testing | `/gen-tests`, `/coverage-gaps` |
| Docs | `/handoff`, `/release-notes`, `/changelog` |
| Refactor | `/find-dup`, `/rename-suggest` |
| Ops | `/ci-check`, `/deps-audit` |

---

## Hooks (Concept)

Hooks = scripts triggered by Claude Code lifecycle events:
- Before a session — load context
- After a tool call — log or validate
- Pre-commit — run lint/tests/audit

Hooks make safety **automatic**, not optional.

---

## Subagents (Concept)

A subagent = a focused, task-scoped helper:
- **Reviewer subagent** — only reviews diffs
- **Tester subagent** — only writes tests
- **Doc subagent** — only writes docs

Specialization → fewer mistakes, less context drift.

---

## MCP-Style Extensions (Concept)

MCP-style integrations let Claude reach:
- Your issue tracker
- Your CI logs
- Your DB read replica
- Your monitoring dashboards

> Pattern: *"Claude as the orchestrator, tools as the hands."*

---

## Mini Project 9 — Command Library

Create `commands/` with at minimum:

- `review.md` — diff review against your rubric
- `gen-tests.md` — generate tests for a file/module
- `docs.md` — produce/refresh README + handoff
- `refactor.md` — safe-refactor with constraints
- `release-notes.md` — notes since last tag

---

## Skills Practiced

- Reusable prompt design
- Parametrization
- Workflow automation thinking
- Subagent / hook concepts

---

## Deliverable Checklist ✅

- [ ] `commands/` folder committed
- [ ] **5 commands** above, each with: purpose, inputs, outputs, example
- [ ] Each command tested on a real prior project (1–8)
- [ ] `commands/README.md` indexes them
- [ ] One command demo recorded in notes

---

## Definition of Done

- Commands are **copy-pasteable** into a Claude session
- Each produces consistent output across runs
- A peer can run any command on **their** repo with no edits
- Library is reusable beyond this workshop

---

## Review Checkpoint 🔎

Swap libraries with a peer:
- Run their `/review` on **your** code
- Run yours on **theirs**
- Each finds **one** improvement to the other's command.

---

## Break 3 — 10 minutes ☕

---

## Next Up

**Part 10 — Production Readiness**
Security, CI, deployment, and human judgment.
