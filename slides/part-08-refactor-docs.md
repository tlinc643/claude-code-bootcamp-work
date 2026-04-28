---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 8"
footer: "Luca Berton · Refactoring & Documentation at Scale"
---

# Part 8
## Refactoring & Documentation at Scale

**Duration:** 25 min · **Format:** Instructor demo + hands-on refactor
**Deliverable:** Refactored dashboard + developer handoff docs

---

## Refactoring Mindset

Refactoring = changing **shape**, not **behavior**.
Tests are your guarantee that behavior didn't drift.

> No tests, no refactor.

---

## Asking Claude to Refactor Safely

> *"Refactor `Dashboard.tsx` to extract reusable components. Do not change behavior. Run tests after each step. Stop and report after each extraction."*

Constraints make refactors safe:
- Behavior preserved
- Tests run between steps
- Smallest viable changes

---

## What to Look For

- **Duplication** — three uses = extract
- **Long functions** — split by responsibility
- **Bad names** — rename ruthlessly
- **God components** — split by region
- **Magic numbers** — name them
- **Dead code** — delete confidently (Git remembers)

---

## Detecting Duplication with Claude

> *"Scan the dashboard codebase. List the top 5 instances of duplication or near-duplication. For each: file paths, lines, and a proposed extraction."*

Then refactor **one item at a time**, committing between.

---

## Documentation that Earns Its Keep

Bad docs: explain syntax.
Good docs: explain **decisions** & **non-obvious behavior**.

| Layer | Audience |
|---|---|
| README | First-time users |
| ARCHITECTURE.md | New maintainers |
| Code comments | Future-you |
| HANDOFF.md | Next dev on the project |

---

## Auto-generating Handoff Docs

> *"Write `HANDOFF.md` for this dashboard. Cover: how to run, key components, state model, known limitations, next 3 improvements, and where each lives."*

Then **edit by hand** — never ship docs you haven't read.

---

## Mini Project 8 — Refactor & Document

1. Run tests → must be green before starting
2. Ask Claude for top duplications
3. Refactor in small commits
4. Rename for clarity
5. Generate `ARCHITECTURE.md` and `HANDOFF.md`
6. Update `README.md`

---

## Deliverable Checklist ✅

- [ ] Tests still green after refactor
- [ ] At least **3 refactor commits** with clear messages
- [ ] `ARCHITECTURE.md` committed
- [ ] `HANDOFF.md` committed
- [ ] Updated `README.md`
- [ ] Duplication report saved in `reports/`

---

## Definition of Done

- No behavior change observable from outside
- Diff is readable and reversible
- A new dev could be productive from the docs alone
- Component tree is cleaner than the start

---

## Review Checkpoint 🔎

Swap repos with a peer:
- Read **only** their `HANDOFF.md`
- Try to run the project
- Note every blocker → feedback to author.

---

## Next Up

**Part 9 — Automation: Commands, Hooks & Reusable Workflows**
You'll build a **personal command library**.
