# Module 4 — Notes API (Best-of-N)

## Goal

Generate **two independent** candidate Notes APIs from the *same* prompt, score them side-by-side on the 3-criterion rubric, and ship the winner. Keep the loser — it is evidence of the lift.

## Scenario

A small team needs a Notes service. One Claude answer is just *one sample* from a noisy process — the second answer is often meaningfully better or worse. Best-of-N turns that variance into a better artefact: produce N candidates, score, pick. You will do **N = 2** here (the minimum that lets you compare); N = 3 is the real-world sweet spot.

## Starter instructions

Follow these steps in order. The whole point is that the two candidates are produced **independently** — they must never see each other.

### Step 1 — Pick a track and make the folders

- **Track A — Python**: FastAPI + Pydantic v2 + sqlite3 stdlib.
- **Track B — Node + TypeScript**: Hono + Zod + better-sqlite3.

```bash
mkdir -p module-04/candidate-a module-04/candidate-b module-04/winner
```

### Step 2 — Produce Candidate A

1. Open a **new** Claude Code chat (or run `claude` in a clean terminal).
2. Paste the prompt from *"Claude Code prompt to use"* below **exactly** — do not edit it.
3. Save whatever Claude generates into `module-04/candidate-a/`.
4. **Do not** ask follow-up questions or iterate. One shot = one candidate.

### Step 3 — Produce Candidate B (independently)

1. Open a **second, separate** chat — *not* the same one. (Closing and reopening, a new tab, or a different model such as Sonnet vs Opus all work.) This independence is what makes the comparison meaningful; reusing the same chat just gives you an *iteration*, not a second candidate.
2. Paste the **identical** prompt.
3. Save the output into `module-04/candidate-b/`.

> Why independence matters: in the same chat, the model sees its earlier answer and tends to repeat it. Separate chats sample the model fresh, so A and B genuinely differ — which is the whole value of Best-of-N.

### Step 4 — Score and compare (see *Manual validation steps*)

Run both candidates through the same curl smoke test, fill in `module-04/scoring.md`, then copy the winner into `module-04/winner/`.

## Claude Code prompt to use

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

> `scoring.md` is a file **you create** — it is not shipped in the repo. For a complete filled-in model, see [`solution/scoring.example.md`](solution/scoring.example.md).

## Manual validation steps

### Step 4a — Smoke-test each candidate

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

### Step 4b — Compare side-by-side

Put both scores in one table so the winner is obvious. Example of a filled-in comparison:

| Criterion (0–3) | Candidate A | Candidate B |
|---|---|---|
| Correctness | 3 — all 7 curls pass | 3 — all 7 curls pass |
| Simplicity  | 3 — one readable file | 2 — split across 3 files |
| Fit         | 2 — 404 body is `{"detail":…}` | 3 — returns bare `{"error":"not found"}` |
| **Total**   | **8 / 9** | **8 / 9** |

When totals tie, the **tie-breaker is the simpler source**. Write one paragraph in `scoring.md` saying *why* the winner won — "both correct, but B matched the spec's 404 shape" is exactly the kind of concrete reason to capture.

### Step 4c — Ship the winner

```bash
cp -R module-04/candidate-b/* module-04/winner/   # copy the winner (example: B won)
```

Leave the losing candidate folder in place — do **not** delete it.

## Expected deliverable

```text
module-04/
├── candidate-a/
├── candidate-b/
├── scoring.md       # rubric scores for A and B + the side-by-side table + one paragraph on why the winner won
└── winner/          # exact copy of the winning candidate
```

A reference solution lives at `solution/` (Python and Node tracks) once the lab is complete.

## Definition of done

- [ ] Both candidates exist and were generated **independently** (two separate chats).
- [ ] `scoring.md` has rubric scores for A and B, the side-by-side table, and a one-paragraph justification.
- [ ] `winner/` runs end-to-end against the curl commands above.
- [ ] The losing candidate is archived, not deleted.

## Stretch challenge

Add a **third** independent candidate (`candidate-c/`) — N = 3 is the real Best-of-N sweet spot. Re-score all three; note whether the third run beat your first two and by how much. That delta is the "lift" Best-of-N buys you.

## Troubleshooting

| Symptom | Fix |
|---|---|
| Both candidates feel identical | Use *separate* chats — same chat = iteration, not BoN. |
| Tied total scores | Tie-breaker: simpler source wins. |
| Track B: better-sqlite3 native build fails | Ensure Node 20 LTS, not 21+; on macOS `xcode-select --install`. |
| Track A: Pydantic v1 imports | Re-prompt with "Pydantic v2" reinforced. |
| `404` returns `{"detail":{"error":"not found"}}` not `{"error":"not found"}` | FastAPI wraps `detail`. A candidate that fixes this scores higher on **Fit** — see the solution's Review gotcha. |
