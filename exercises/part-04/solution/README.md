# Reference solution — Module 4

> **Stop**: only open this after you have produced your own two candidates, filled in `scoring.md`, and chosen a winner.

Two parallel tracks ship under this directory. Pick the one matching your stack and diff your work against it:

| Track | Path | Run |
|---|---|---|
| Python (FastAPI + SQLite) | [`python/`](python/) | `pip install -r python/requirements.txt && uvicorn python.app:app --reload` |
| Node.js (Hono + better-sqlite3) | [`node/`](node/) | `cd node && npm i && npm start` |

## What a good `scoring.md` looks like

The reference run produced **two candidates** from the same prompt in two separate chats. Both are shipped so you can read them:

| | Candidate A | Candidate B |
|---|---|---|
| Source | [`python/candidates/candidate-a/notes_api.py`](python/candidates/candidate-a/notes_api.py) | [`python/candidates/candidate-b/app.py`](python/candidates/candidate-b/app.py) |
| Shape | single-file, modern `lifespan`, partial `PATCH`, blank-title validator | split helpers, but uses `PUT` and skips validation |

Running the **same** curl smoke test against both is what separated them — "it works" was not enough:

| Criterion (0–3) | Candidate A | Candidate B |
|---|---|---|
| Correctness | 3 — all 6 codes match spec | 1 — `PATCH`→405 (implemented `PUT`); blank title→201 not 422 |
| Simplicity  | 3 — one readable file | 2 — clean, but repeats row→Note mapping per route |
| Fit         | 2 — 404 body is `{"detail":…}` | 1 — wrong update verb, no validation, deprecated `on_event` |
| **Total**   | **8 / 9** | **4 / 9** |

**Winner: A (8 vs 4)** — not a tie. B fails two spec requirements outright: the `PATCH` partial-update route and the 422 on a blank title. This is exactly the variance Best-of-N exists to catch: same prompt, but one run silently dropped a verb and all input validation. Keep B as evidence of the lift — do not delete it.

The full worked write-up is at [`python/candidates/scoring.md`](python/candidates/scoring.md); a copy-ready template is at [`scoring.example.md`](scoring.example.md). Copy either shape into your own `module-04/scoring.md`.

## Verification run (what "PASS" looks like)

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

### Gotcha to catch in Review — the 404 body shape

The spec example shows `GET /notes/999 → 404 {"error":"not found"}`. But raising `HTTPException(status_code=404, detail={"error": "not found"})` makes FastAPI **wrap** `detail`, so the wire shape is actually:

```json
{"detail": {"error": "not found"}}
```

…not the bare `{"error": "not found"}` in the spec. Two valid fixes — pick one and be consistent:

- **Match the spec literally:** raise with a plain string (`detail="not found"`) and let callers read `detail`, or add a custom exception handler that returns `JSONResponse({"error": "not found"}, status_code=404)`.
- **Accept FastAPI's envelope:** update the spec/examples to show `{"detail": …}` and have callers unwrap `detail`.

This is a classic Best-of-N differentiator: a candidate that *notices* and resolves the envelope mismatch should score higher on **Fit** than one that silently ships `{"detail":{…}}`.

## Running it (environment note)

The README's `pip install fastapi uvicorn` line assumes a healthy system Python. If `pip3`/system Python is broken (e.g. a `pyexpat` dylib mismatch on a freshly upgraded macOS Python), use [`uv`](https://docs.astral.sh/uv/) instead — no global install needed:

```bash
uv run --with fastapi --with uvicorn uvicorn notes_api:app --port 8765
```

## Definition of done

See `../README.md`. Note: at least **two distinct candidates** are required — variants of the same approach don't count, and they must come from **two separate chats**, not follow-up turns in one.
