---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 1"
footer: "Luca Berton · Welcome, Setup & AI-First Mindset"
---

# Part 1
## Welcome, Setup & AI-First Development Mindset

**Duration:** 20 min · **Format:** Instructor demo + guided setup
**Deliverable:** A working AI Coding Workspace

---

## Workshop Promise

By the end of this 5-hour workshop you will:

- Use Claude Code as an **AI development partner** (not autocomplete)
- Ship **10 real-world projects** end-to-end
- Walk away with a **repeatable workflow** + a **certificate**

---

## Learning Outcomes for Part 1

After this part you can:

1. Explain how Claude Code differs from autocomplete tools
2. Set up Claude Code for professional AI-assisted development
3. Initialize a clean workshop workspace with Git
4. Describe the Claude Code loop: **Plan → Implement → Test → Review → Commit**

---

## Claude Code ≠ Autocomplete

| Autocomplete | Claude Code |
|---|---|
| Single-line suggestions | End-to-end task delegation |
| Reactive | Proactive (plans first) |
| No memory of project | Reads files, runs tests, edits multi-file |
| You drive every keystroke | You drive **intent**, Claude drives execution |

---

## AI-First Mindset

- **Delegate tasks**, not snippets
- **Trust, but verify** — every diff is reviewed
- **Plan before code** — make Claude write the plan first
- **Fast feedback loops** — small, testable steps
- **Safe delegation ≠ blind trust**

---

## The Claude Code Workflow

```
        ┌────────┐
        │  PLAN  │
        └───┬────┘
            ▼
     ┌────────────┐
     │ IMPLEMENT  │
     └──────┬─────┘
            ▼
        ┌────────┐
        │  TEST  │
        └───┬────┘
            ▼
       ┌────────┐
       │ REVIEW │
       └───┬────┘
           ▼
       ┌────────┐
       │ COMMIT │
       └────────┘
```

---

## Recommended Folder Structure

```
claude-code-workshop/
├── CLAUDE.md
├── .gitignore
├── README.md
├── 01-cli-task-manager/
├── 02-notes-api/
├── 03-dashboard/
├── commands/
└── reports/
```

One folder per project. One Git repo overall.

---

## Mini Project 1 — AI Coding Workspace Setup

**Goal:** Create a clean local workspace ready for the next 9 projects.

**Steps**

1. Install / authenticate Claude Code
2. `mkdir claude-code-workshop && cd claude-code-workshop`
3. `git init` and add `.gitignore`
4. Create the folder structure above
5. First commit: `chore: scaffold workshop workspace`

---

## Deliverable Checklist ✅

- [ ] Claude Code installed and authenticated
- [ ] Git repository initialized with first commit
- [ ] Workshop project folder structure created
- [ ] `README.md` with your name + workshop date
- [ ] `.gitignore` configured for your stack

---

## Definition of Done

- `git log` shows ≥ 1 commit
- `claude --version` (or equivalent) works
- Folder layout matches the recommended structure
- You can run a Claude Code session inside the repo

---

## Review Checkpoint 🔎

Pair with a peer and verify:

- Both repos boot cleanly
- Both can launch a Claude Code session
- Both committed their scaffold

> If anything fails here, **stop and fix** — every later part depends on it.

---

## Next Up

**Part 2 — Prompting Claude Code Like a Tech Lead**
You will build the **CLI Task Manager** using "big prompts."
