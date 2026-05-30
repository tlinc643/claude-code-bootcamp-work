# Reference solution — Module 4

> **Stop**: only open this after you have produced your own `candidates.md` and chosen a winner.

Two parallel tracks ship under this directory. Pick the one matching your stack and diff your work against it:

| Track | Path | Run |
|---|---|---|
| Python (FastAPI + SQLite) | [`python/`](python/) | `pip install -r python/requirements.txt && uvicorn python.app:app --reload` |
| Node.js (Hono + better-sqlite3) | [`node/`](node/) | `cd node && npm i && npm start` |

## What to compare in `candidates.md`

The reference run produced **two candidates**: one with the route layer split out and one with everything in `app.py`. The winner (the split version) was picked against the 3-criterion rubric:

| Criterion | Weight | Why split version won |
|---|---|---|
| Correctness | 0.4 | Both pass the smoke script; tied. |
| Maintainability | 0.4 | Split version isolates persistence from routing → easier tests. |
| Speed-to-ship | 0.2 | Single-file version was 12 lines shorter; minor win. |

If your `candidates.md` doesn't articulate the trade-off this concretely, refine the rationale before submitting.

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

See `../README.md`. Note: at least **two distinct candidates** are required — variants of the same approach don't count.
