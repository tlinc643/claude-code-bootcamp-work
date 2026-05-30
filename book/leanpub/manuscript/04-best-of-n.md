# 04. Best-of-N

Module 04 · 30 min

## Build Faster with Best-of-N

**The first answer is rarely the best. Generate three; score; ship the winner.**

### Theory · Best-of-N (4 min)

> **Generate N independent candidates → score on a rubric → pick the winner.** N = 3 is the sweet spot.

- **Independent** — each candidate gets its own fresh prompt context. *Not* "now improve it" (that's iteration).
- **Score on a rubric**, not vibes. Three criteria:
  - **Correctness** — passes the manual test plan?
  - **Simplicity** — could a junior maintain it?
  - **Fit** — matches `CLAUDE.md` conventions and repo style?

**Without the rubric you pick by gut and the lift disappears. Correctness gates everything.**

### Best-of-N, scored

![Best-of-N: generate N candidates, score on Correctness, Simplicity, Fit, pick the winner](resources/04-bon-scoring.png)

Generate **N** independent candidates → score on **Correctness · Simplicity · Fit** → keep the winner.

### Reference · The 3-criterion scorecard

| Criterion | Question | Weight |
|---|---|---|
| **Correctness** | Does it pass every step of the manual test plan? | Gate — fail here = out |
| **Simplicity** | Could a junior maintain it next quarter? | High |
| **Fit** | Does it follow `CLAUDE.md` + repo style? | Medium |

Record a one-paragraph justification per candidate in `scoring.md`. **Never delete losers before scoring.**

### Reference · Common mistakes

- One candidate + "improve it" ×3 (iteration, not BoN).
- Skipping the rubric → picking by vibe → no lift.
- Choosing the "elegant" one that fails the test plan (correctness is the gate).

### Live demo · Three candidates, one winner (6 min)

**The reusable prompt — paste it verbatim for A, B, and C:**

```text
GOAL: A REST Notes API: create, list, get, delete a note.
CONSTRAINTS: Python 3.11 + FastAPI; persist to SQLite ./notes.db;
  return JSON; 404 on missing id; no other third-party deps.
OUTPUT: one runnable app + a curl test plan covering all 4 routes.
EXAMPLES: POST /notes {"text":"hi"} -> 201 + id;
  GET /notes/999 (missing) -> 404 {"error":"not found"}.
```

`/clear` before **each** candidate → paste the **same** prompt → save to `candidate-a|b|c/`. Then score side-by-side and commit the winner.

> Variance must come from the model, **not** the prompt. Never say "now do it differently."

### Your turn · Notes API, Best-of-3 (13 min)

**Exercise**: [`exercises/part-04/README.md`](#hands-on-exercise--module-04)

Build a Notes API (SQLite `notes.db`), then generate **3 candidates** and score them:

```text
POST /notes · GET /notes?q= · GET /notes/:id · PATCH /notes/:id · DELETE /notes/:id
Status: 201 create · 200 read/update · 204 delete · 404 missing · 422 invalid
```

Track A: Python (FastAPI + Pydantic v2). Track B: Node (Hono + Zod + better-sqlite3).

**Deliverables**: `candidate-{a,b,c}/`, `scoring.md` (scores + justification), `winner/` (clean copy).

**Success signal**: all five endpoints respond with correct status codes via curl.

### Done & next (1 min)

**Definition of done**

- [ ] Three candidates in `module-04/candidate-{a,b,c}/`.
- [ ] `scoring.md` with scores + one-paragraph justification each.
- [ ] `winner/` runs end-to-end; losers archived (not deleted).

**Next** — we trust the winner only after we *test* it and review like a stranger's PR.
**Module 5 — Testing, Debugging & Self-Review.**

## Hands-on exercise — Module 04 {#hands-on-exercise--module-04}

> **Companion repository** — Work this exercise from the live files in the [Claude Code Bootcamp repository](https://github.com/lucab85/Claude-Code-Bootcamp): [`exercises/part-04/README.md`](https://github.com/lucab85/Claude-Code-Bootcamp/blob/main/exercises/part-04/README.md).
> Reference solution: [`exercises/part-04/solution/README.md`](https://github.com/lucab85/Claude-Code-Bootcamp/blob/main/exercises/part-04/solution/README.md).

## Module 4 — Notes API (Best-of-N)

### Goal

Generate **two independent** candidate Notes APIs from the *same* prompt, score them side-by-side on the 3-criterion rubric, and ship the winner. Keep the loser — it is evidence of the lift.

### Scenario

A small team needs a Notes service. One Claude answer is just *one sample* from a noisy process — the second answer is often meaningfully better or worse. Best-of-N turns that variance into a better artefact: produce N candidates, score, pick. You will do **N = 2** here (the minimum that lets you compare); N = 3 is the real-world sweet spot.

### Starter instructions

Follow these steps in order. The whole point is that the two candidates are produced **independently** — they must never see each other.

#### Step 1 — Pick a track and make the folders

- **Track A — Python**: FastAPI + Pydantic v2 + sqlite3 stdlib.
- **Track B — Node + TypeScript**: Hono + Zod + better-sqlite3.

```bash
mkdir -p module-04/candidate-a module-04/candidate-b module-04/winner
```

#### Step 2 — Produce Candidate A

1. Open a **new** Claude Code chat (or run `claude` in a clean terminal).
2. Paste the prompt from *"Claude Code prompt to use"* below **exactly** — do not edit it.
3. Save whatever Claude generates into `module-04/candidate-a/`.
4. **Do not** ask follow-up questions or iterate. One shot = one candidate.

#### Step 3 — Produce Candidate B (independently)

1. Open a **second, separate** chat — *not* the same one. (Closing and reopening, a new tab, or a different model such as Sonnet vs Opus all work.) This independence is what makes the comparison meaningful; reusing the same chat just gives you an *iteration*, not a second candidate.
2. Paste the **identical** prompt.
3. Save the output into `module-04/candidate-b/`.

> Why independence matters: in the same chat, the model sees its earlier answer and tends to repeat it. Separate chats sample the model fresh, so A and B genuinely differ — which is the whole value of Best-of-N.

#### Step 4 — Score and compare (see *Manual validation steps*)

Run both candidates through the same curl smoke test, fill in `module-04/scoring.md`, then copy the winner into `module-04/winner/`.

### Claude Code prompt to use

```text
GOAL
Build a small Notes API persisting to SQLite.

CONSTRAINTS
- Track A: Python 3.11 with FastAPI + Pydantic v2 + the sqlite3 stdlib module.
- Track B: TypeScript on Node 20 with Hono + Zod + better-sqlite3.
- One process. No migrations framework — initialise the schema at startup.
- HTTP status codes: 201 on create, 200 on read/update, 204 on delete, 404 on missing, 422 on invalid body.
- Timestamps in ISO 8601 UTC.

OUTPUT FORMAT
- A runnable project (single source file is fine) plus a 5-line README with the run command.

EXAMPLES
- POST /notes {"title":"a","body":"b"} → 201 {"id":1,"title":"a","body":"b","created_at":"...","updated_at":"..."}
- GET /notes?q=spec → 200 [matching notes]
- GET /notes/999 → 404 {"error":"not found"}
```

Then score **each** candidate with this block (one per candidate) in `module-04/scoring.md`:

```text
Candidate: [a|b]
Correctness (0–3): can I exercise all five endpoints with curl?
Simplicity   (0–3): is the source single-glance readable?
Fit          (0–3): does it follow CLAUDE.md conventions?
Total: __ / 9
Notes:
```

> `scoring.md` is a file **you create** — it is not shipped in the repo. For a complete filled-in model, see `solution/scoring.example.md`.

### Manual validation steps

#### Step 4a — Smoke-test each candidate

For **each** candidate (`candidate-a`, then `candidate-b`), start its server and run the same script. Adjust the port to whatever that candidate chose.

```bash
curl -X POST localhost:8000/notes -H 'content-type: application/json' \
  -d '{"title":"hi","body":"there"}'                  # 201
curl localhost:8000/notes                             # 200
curl 'localhost:8000/notes?q=hi'                      # 200
curl localhost:8000/notes/1                           # 200
curl -X PATCH localhost:8000/notes/1 -H 'content-type: application/json' \
  -d '{"body":"world"}'                               # 200
curl -X DELETE localhost:8000/notes/1                 # 204
curl localhost:8000/notes/999                         # 404
```

#### Step 4b — Compare side-by-side

Put both scores in one table so the winner is obvious. Example of a filled-in comparison:

| Criterion (0–3) | Candidate A | Candidate B |
|---|---|---|
| Correctness | 3 — all 7 curls pass | 3 — all 7 curls pass |
| Simplicity  | 3 — one readable file | 2 — split across 3 files |
| Fit         | 2 — 404 body is `{"detail":…}` | 3 — returns bare `{"error":"not found"}` |
| **Total**   | **8 / 9** | **8 / 9** |

When totals tie, the **tie-breaker is the simpler source**. Write one paragraph in `scoring.md` saying *why* the winner won — "both correct, but B matched the spec's 404 shape" is exactly the kind of concrete reason to capture.

#### Step 4c — Ship the winner

```bash
cp -R module-04/candidate-b/* module-04/winner/   # copy the winner (example: B won)
```

Leave the losing candidate folder in place — do **not** delete it.

### Expected deliverable

```text
module-04/
├── candidate-a/
├── candidate-b/
├── scoring.md       # rubric scores for A and B + the side-by-side table + one paragraph on why the winner won
└── winner/          # exact copy of the winning candidate
```

A reference solution lives at `solution/` (Python and Node tracks) once the lab is complete.

### Definition of done

- [ ] Both candidates exist and were generated **independently** (two separate chats).
- [ ] `scoring.md` has rubric scores for A and B, the side-by-side table, and a one-paragraph justification.
- [ ] `winner/` runs end-to-end against the curl commands above.
- [ ] The losing candidate is archived, not deleted.

### Stretch challenge

Add a **third** independent candidate (`candidate-c/`) — N = 3 is the real Best-of-N sweet spot. Re-score all three; note whether the third run beat your first two and by how much. That delta is the "lift" Best-of-N buys you.

### Troubleshooting

| Symptom | Fix |
|---|---|
| Both candidates feel identical | Use *separate* chats — same chat = iteration, not BoN. |
| Tied total scores | Tie-breaker: simpler source wins. |
| Track B: better-sqlite3 native build fails | Ensure Node 20 LTS, not 21+; on macOS `xcode-select --install`. |
| Track A: Pydantic v1 imports | Re-prompt with "Pydantic v2" reinforced. |
| `404` returns `{"detail":{"error":"not found"}}` not `{"error":"not found"}` | FastAPI wraps `detail`. A candidate that fixes this scores higher on **Fit** — see the solution's Review gotcha. |

## Solution — Module 04 {#solution--module-04}

## Reference solution — Module 4

> **Stop**: only open this after you have produced your own two candidates, filled in `scoring.md`, and chosen a winner.

Two parallel tracks ship under this directory. Pick the one matching your stack and diff your work against it:

| Track | Path | Run |
|---|---|---|
| Python (FastAPI + SQLite) | `python/` | `pip install -r python/requirements.txt && uvicorn python.app:app --reload` |
| Node.js (Hono + better-sqlite3) | `node/` | `cd node && npm i && npm start` |

### What a good `scoring.md` looks like

The reference run produced **two candidates** from the same prompt in two separate chats. Both are shipped so you can read them:

| | Candidate A | Candidate B |
|---|---|---|
| Source | `python/candidates/candidate-a/notes_api.py` | `python/candidates/candidate-b/app.py` |
| Shape | single-file, modern `lifespan`, partial `PATCH`, blank-title validator | split helpers, but uses `PUT` and skips validation |

Running the **same** curl smoke test against both is what separated them — "it works" was not enough:

| Criterion (0–3) | Candidate A | Candidate B |
|---|---|---|
| Correctness | 3 — all 6 codes match spec | 1 — `PATCH`→405 (implemented `PUT`); blank title→201 not 422 |
| Simplicity  | 3 — one readable file | 2 — clean, but repeats row→Note mapping per route |
| Fit         | 2 — 404 body is `{"detail":…}` | 1 — wrong update verb, no validation, deprecated `on_event` |
| **Total**   | **8 / 9** | **4 / 9** |

**Winner: A (8 vs 4)** — not a tie. B fails two spec requirements outright: the `PATCH` partial-update route and the 422 on a blank title. This is exactly the variance Best-of-N exists to catch: same prompt, but one run silently dropped a verb and all input validation. Keep B as evidence of the lift — do not delete it.

The full worked write-up is at `python/candidates/scoring.md`; a copy-ready template is at `scoring.example.md`. Copy either shape into your own `module-04/scoring.md`.

### Verification run (what "PASS" looks like)

A real verification of a winning FastAPI + sqlite3 candidate. Cold start, then every endpoint and edge case exercised:

| # | Case | Result |
|---|---|---|
| 1 | `POST /notes {"title":"a","body":"b"}` | `201` + full JSON with ISO-8601 UTC `created_at`/`updated_at` |
| 2 | `GET /notes?q=a` | `200` `[{…note 1…}]` |
| 3 | `GET /notes/999` | `404` |
| 4 | `PATCH /notes/1 {"title":"updated"}` | `200`; body preserved, `updated_at` advanced, `created_at` unchanged |
| 5 | `DELETE /notes/1` | `204`, empty body |
| 6 | `POST` blank title `"  "` | `422` "title must not be blank" |
| 7 | `POST` missing title field | `422` "Field required" |
| 8 | `PATCH /notes/1` after delete | `404` (tombstone) |
| 9 | `GET /notes` (empty store) | `200` `[]` |
| 10 | `GET /notes?q=zzznomatch` | `200` `[]` |

#### Gotcha to catch in Review — the 404 body shape

The spec example shows `GET /notes/999 → 404 {"error":"not found"}`. But raising `HTTPException(status_code=404, detail={"error": "not found"})` makes FastAPI **wrap** `detail`, so the wire shape is actually:

```json
{"detail": {"error": "not found"}}
```

…not the bare `{"error": "not found"}` in the spec. Two valid fixes — pick one and be consistent:

- **Match the spec literally:** raise with a plain string (`detail="not found"`) and let callers read `detail`, or add a custom exception handler that returns `JSONResponse({"error": "not found"}, status_code=404)`.
- **Accept FastAPI's envelope:** update the spec/examples to show `{"detail": …}` and have callers unwrap `detail`.

This is a classic Best-of-N differentiator: a candidate that *notices* and resolves the envelope mismatch should score higher on **Fit** than one that silently ships `{"detail":{…}}`.

### Running it (environment note)

The README's `pip install fastapi uvicorn` line assumes a healthy system Python. If `pip3`/system Python is broken (e.g. a `pyexpat` dylib mismatch on a freshly upgraded macOS Python), use [`uv`](https://docs.astral.sh/uv/) instead — no global install needed:

```bash
uv run --with fastapi --with uvicorn uvicorn notes_api:app --port 8765
```

### Definition of done

See `../README.md`. Note: at least **two distinct candidates** are required — variants of the same approach don't count, and they must come from **two separate chats**, not follow-up turns in one.
