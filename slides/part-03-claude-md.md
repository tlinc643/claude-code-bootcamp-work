---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 3"
footer: "Luca Berton · Project Context with CLAUDE.md"
---

# Part 3
## Project Context with CLAUDE.md

**Duration:** 25 min · **Format:** Instructor explanation + guided lab
**Deliverable:** A reusable **CLAUDE.md** for the task manager

---

## Why Claude Code Needs Project Context

Without context, Claude Code:
- Re-discovers conventions every session
- Picks inconsistent patterns
- Touches files it shouldn't
- Wastes tokens on rediscovery

`CLAUDE.md` = **the project brain** loaded with every prompt.

---

## What Goes Inside CLAUDE.md

- **Architecture notes** — what lives where
- **Coding conventions** — style, naming, formatting
- **Testing commands** — how to run tests
- **Security rules** — secrets, boundaries
- **"Do not touch" areas** — generated files, vendored code
- **Workflow** — branch naming, commit style

---

## CLAUDE.md Skeleton

```md
# Project: CLI Task Manager

## Stack
Python 3.11, stdlib only, pytest

## Commands
- Run tests: `pytest -q`
- Lint: `ruff check .`
- Run CLI: `python -m taskmgr`

## Conventions
- Type hints everywhere
- Functions ≤ 30 lines
- snake_case modules

## Security
- Never log task titles in errors
- No network calls

## Do Not Touch
- /vendor, /generated, tasks.json
```

---

## Keeping It Concise

- Token budget matters → trim ruthlessly
- One source of truth — link to docs, don't duplicate
- Refresh when conventions change
- Keep examples **short** but **canonical**

Target: **< 200 lines** for most projects.

---

## Layered Context

```
~/.claude/CLAUDE.md        ← personal defaults
repo/CLAUDE.md             ← project rules
repo/feature/CLAUDE.md     ← optional, scoped
```

Specific overrides general.

---

## Mini Project 3 — Project Brain

**Goal:** Author a `CLAUDE.md` for your CLI Task Manager.

**Steps**
1. Draft the skeleton in repo root
2. Fill each section from your real project
3. Run a test prompt: *"Add a `task search <query>` command."*
4. Compare results **with vs without** CLAUDE.md
5. Iterate the file based on what was missed

---

## Deliverable Checklist ✅

- [ ] `CLAUDE.md` committed at project root
- [ ] Sections: Stack, Commands, Conventions, Security, Do Not Touch
- [ ] At least one *workflow* example
- [ ] Side-by-side note: "Before vs After CLAUDE.md"
- [ ] File is ≤ 200 lines

---

## Definition of Done

- New Claude Code session uses your conventions automatically
- Claude follows the **Do Not Touch** rules
- Test commands in CLAUDE.md actually work
- A peer can onboard from CLAUDE.md alone

---

## Review Checkpoint 🔎

Swap CLAUDE.md with a peer:
- Can they understand the project in 2 minutes?
- Is anything missing? Anything redundant?
- Each provides 2 concrete edits.

---

## Break 1 — 10 minutes ☕

Stretch, hydrate, and skim your CLAUDE.md once more.

---

## Next Up

**Part 4 — Build Real Apps Faster with Best-of-N**
You will generate **multiple designs** for a Notes API and pick the best.
