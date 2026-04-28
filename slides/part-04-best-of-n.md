---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 4"
footer: "Luca Berton · Build Real Apps Faster with Best-of-N"
---

# Part 4
## Build Real Apps Faster with Best-of-N

**Duration:** 35 min · **Format:** Demo + hands-on build
**Deliverable:** A working **Notes App API** chosen from N designs

---

## The "First Answer Wins" Trap

The first solution Claude offers is rarely the best.
It's the most **probable**, not the most **suitable**.

Best-of-N: ask for **multiple approaches**, compare, choose.

---

## What Best-of-N Looks Like

```
Prompt: "Propose 3 different backend designs for a Notes API.
For each: stack, data model, endpoints, trade-offs."

→ Option A: Express + SQLite
→ Option B: FastAPI + Postgres
→ Option C: Flask + JSON file (lightweight)

You: pick + justify + (optionally) merge strengths
```

---

## How to Compare Trade-offs

| Axis | Questions to ask |
|---|---|
| Simplicity | Lines of code, dependencies |
| Performance | Concurrency, latency |
| Testability | Easy to mock & isolate? |
| Maintainability | Conventions, idiomatic? |
| Fit | Matches CLAUDE.md constraints? |

---

## Combining the Best Parts

You're not forced to pick **one** design.

> *"Take A's routing, B's validation layer, and C's storage abstraction. Produce a unified plan."*

Claude is a great **synthesizer** when given explicit instructions.

---

## When NOT to Use Best-of-N

- Trivial bug fixes
- Pure refactors with one obvious shape
- Time-critical hotfixes
- When constraints already pin the design

Don't burn tokens on solved problems.

---

## Mini Project 4 — Notes App API

**Required endpoints**
- `POST /notes` — create
- `GET /notes` — list
- `GET /notes/:id` — read
- `PUT /notes/:id` — update
- `DELETE /notes/:id` — delete

**Validation:** title required, body ≤ 10k chars

---

## Build Process

1. Ask Claude for **3 design options**
2. Document trade-offs in `02-notes-api/DESIGN.md`
3. Choose (or merge) — explain the **why**
4. Implement chosen design
5. Smoke-test with `curl` or HTTP client

---

## Skills Practiced

- API design
- Prompt comparison
- Solution evaluation
- REST endpoints
- Basic validation

---

## Deliverable Checklist ✅

- [ ] `02-notes-api/` with running server
- [ ] All 5 CRUD endpoints
- [ ] Input validation
- [ ] `DESIGN.md` documenting **all N options**
- [ ] Decision rationale section
- [ ] Manual test transcript (curl/HTTPie)

---

## Definition of Done

- `curl` round-trip for all 5 endpoints succeeds
- Invalid input returns proper 4xx with messages
- DESIGN.md has ≥ 3 options + chosen one
- Reader can answer: *"Why this design over the others?"*

---

## Review Checkpoint 🔎

Pair-review:
- Read each other's DESIGN.md
- Challenge the rationale: *"What would change with 1M notes?"*
- Each suggests **one** thing the chosen design missed.

---

## Next Up

**Part 5 — Testing, Debugging & Self-Review**
You will harden the Notes API and catch its bugs.
