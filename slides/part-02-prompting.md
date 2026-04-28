---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 2"
footer: "Luca Berton · Prompting Claude Code Like a Tech Lead"
---

# Part 2
## Prompting Claude Code Like a Tech Lead

**Duration:** 30 min · **Format:** Demo + hands-on prompt lab
**Deliverable:** A working **CLI Task Manager**

---

## Why "Like a Tech Lead"?

Tech leads don't write tickets that say *"add a button."*
They write briefs with **context, constraints, acceptance criteria**.

Claude Code performs best when prompted the same way.

---

## Small Prompts vs Big Prompts

| Small Prompt | Big Prompt |
|---|---|
| "Write a function to add a task" | "Build a CLI task manager with add/list/complete/delete, JSON storage, tests, and a README. Plan first." |
| Reactive, snippet-level | Goal-level, end-to-end |
| Many round-trips | Few, high-leverage prompts |

---

## Anatomy of a Big Prompt

1. **Goal** — what we're building & why
2. **Context** — language, framework, existing files
3. **Constraints** — style, deps, performance, security
4. **Acceptance criteria** — observable, testable
5. **Expected output** — files, format, commands
6. **Plan-first instruction** — *"propose a plan before writing code"*

---

## Example Brief

> **Goal:** Build a Python CLI task manager.
> **Context:** Python 3.11, single repo, no external DB.
> **Constraints:** stdlib only, ≤300 LOC, type hints.
> **Acceptance:** `task add|list|complete|delete` work; tasks persist to `tasks.json`; `pytest` passes.
> **Output:** plan first, then files + tests + README.
> **Plan first.** Wait for my approval before coding.

---

## Hands, Eyes, and Ears

Use Claude Code as your:
- **Hands** — writing & editing files
- **Eyes** — reading logs, diffs, test output
- **Ears** — listening to your intent and reflecting it back

Ask it to **summarize what it heard** before it codes.

---

## Intervene Without Micromanaging

- Approve / reject the **plan**, not every line
- Push back with *"why this approach over X?"*
- Course-correct early; don't wait until 500 LOC are written
- Use **Stop → Re-prompt** instead of editing by hand

---

## Better Feedback Loops

- Short tasks → quick verification → commit
- Always run tests after a change
- Ask: *"What did you change and why?"*
- Ask: *"What did you NOT change?"*

---

## Mini Project 2 — CLI Task Manager

**Build:** a command-line task manager.

**Required commands**
- `task add "<title>"`
- `task list`
- `task complete <id>`
- `task delete <id>`

**Storage:** local JSON file
**Tests:** at least one per command

---

## Skills Practiced

- Structured (big) prompting
- Acceptance criteria
- Iterative refinement
- Basic testing

---

## Deliverable Checklist ✅

- [ ] Working CLI in `01-cli-task-manager/`
- [ ] All 4 commands functional
- [ ] `tasks.json` persistence
- [ ] `README.md` with usage examples
- [ ] At least 4 passing tests
- [ ] The original "big prompt" saved in `prompts/`

---

## Definition of Done

- `task add "Buy milk"` then `task list` shows it
- `task complete 1` flips status; `task list` reflects it
- Tests pass: `pytest` (or stack equivalent) green
- README runs end-to-end for a new user

---

## Review Checkpoint 🔎

Pair-review:
- Read each other's "big prompt"
- Run each other's CLI
- Each finds **one improvement** in the other's prompt

---

## Next Up

**Part 3 — Project Context with CLAUDE.md**
You will give Claude Code a **persistent brain** for this project.
