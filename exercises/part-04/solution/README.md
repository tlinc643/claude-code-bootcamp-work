# Reference solution — Module 4

> **Stop**: only open this after you have produced your own two candidates, filled in `scoring.md`, and chosen a winner.

Two parallel tracks ship under this directory. Pick the one matching your stack and diff your work against it:

| Track | Path | Run |
|---|---|---|
| Python (FastAPI + SQLite) | [`python/`](python/) | `pip install -r python/requirements.txt && uvicorn python.app:app --reload` |
| Node.js (Hono + better-sqlite3) | [`node/`](node/) | `cd node && npm i && npm start` |

## What a good `scoring.md` looks like

The reference run produced **two candidates** from the same prompt in two separate chats: **Candidate A** kept everything in one `app.py`; **Candidate B** split the route layer out from persistence. Both passed the curl smoke test, so the rubric — not "it works" — decided the winner:

| Criterion (0–3) | Candidate A (single file) | Candidate B (split) |
|---|---|---|
| Correctness | 3 — all 7 curls pass | 3 — all 7 curls pass |
| Simplicity  | 3 — ~12 lines shorter, one glance | 2 — three files to follow |
| Fit         | 2 — 404 body is `{"detail":…}` | 3 — isolates persistence, returns bare `{"error":"not found"}` |
| **Total**   | **8 / 9** | **8 / 9** |

This is a deliberate tie (8–8) to show the **tie-breaker in action**. Two equally defensible calls:

- **Ship A** on the "simpler source wins" tie-breaker — fewer files to maintain on day one.
- **Ship B** because its **Fit** edge (correct 404 shape, testable persistence layer) matters more for a service that will grow.

Either is acceptable *if your one-paragraph justification names the trade-off this concretely*. A vague "B looks cleaner" is not. If your `scoring.md` doesn't articulate the trade-off, refine the rationale before submitting.

A complete, filled-in model lives at [`scoring.example.md`](scoring.example.md) — copy its shape into your own `module-04/scoring.md`.

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
