# Module 4 — Python Reference Solution

Notes API on FastAPI + Pydantic v2 + `sqlite3` stdlib.

## Install

```bash
pip install fastapi uvicorn pydantic
```

## Run

```bash
uvicorn app:app --reload
```

## Smoke test

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

State persists in `notes.db` (SQLite).

## Best-of-N worked run

`app.py` above is the canonical reference. The [`candidates/`](candidates/) folder
holds a real two-candidate Best-of-N run so you can see how scoring played out:

- [`candidates/candidate-a/notes_api.py`](candidates/candidate-a/notes_api.py) — winner (8/9): partial `PATCH`, blank-title 422.
- [`candidates/candidate-b/app.py`](candidates/candidate-b/app.py) — loser (4/9): uses `PUT`, skips validation.
- [`candidates/scoring.md`](candidates/scoring.md) — the filled-in rubric and decision.
