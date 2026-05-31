# Module 08 — Architecture

## Overview

A minimal REST API for managing plain-text notes. It runs as a single-process
FastAPI application with no external dependencies beyond FastAPI and Uvicorn.
All data lives in memory; there is no database or file persistence.

## File layout

```
module-08/after/
├── app.py              # Application code (schema, storage, routes)
├── requirements.txt    # fastapi + uvicorn
├── pytest.ini          # pytest root / testpaths config
└── tests/
    └── test_notes_api.py
```

## Key components in app.py

### `NoteIn` (Pydantic model)
Validates incoming request bodies for both `POST /notes` and `PUT /notes/{id}`.
The `must_not_be_blank` validator rejects titles or bodies that are empty or
whitespace-only, returning HTTP 422 before the route handler is reached.

### `Note` (TypedDict)
Documents the shape of a stored note: `id`, `title`, `body`, `created_at`,
`updated_at`. Used only for type annotations; it has no runtime cost.

### `NoteStore`
Encapsulates the in-memory dict and auto-incrementing ID counter.
- `create(title, body)` — builds a new note dict, stores it, advances the counter.
- `list_all()` — returns notes in insertion order (dict ordering is preserved in Python 3.7+).
- `get(note_id)` — returns the note or `None`.
- `update(note_id, title, body)` — mutates in place, refreshes `updated_at`, returns the note or `None`.
- `delete(note_id)` — removes the entry, returns `True` on success or `False` if not found.
- `reset()` — clears state; called by the test fixture.

Route handlers only do two things: call a `NoteStore` method and translate a
`None` / `False` return into an HTTP 404.

### Module-level `store`
A single `NoteStore` instance shared across all requests within the process.

## Endpoints

| Method | Path              | Status | Description                      |
|--------|-------------------|--------|----------------------------------|
| GET    | /health           | 200    | Liveness probe                   |
| POST   | /notes            | 201    | Create a note                    |
| GET    | /notes            | 200    | List all notes                   |
| GET    | /notes/{note_id}  | 200    | Get a note by ID                 |
| PUT    | /notes/{note_id}  | 200    | Replace title and body of a note |
| DELETE | /notes/{note_id}  | 204    | Delete a note                    |

All 404 responses carry `{"detail": "Note not found"}`.  
All 422 responses are produced automatically by Pydantic validation.

## Data flow

```
HTTP request
  → FastAPI routing
    → Pydantic validates NoteIn (POST / PUT only)
      → NoteStore method
        → return dict (or None / False)
          → route handler converts None → HTTPException(404)
            → FastAPI serialises dict → HTTP response
```

## Known limitations

- **No persistence** — all notes are lost when the process restarts.
- **No concurrency safety** — simultaneous writes from multiple threads (e.g.,
  Uvicorn with `--workers > 1`) can produce duplicate IDs or lost updates. The
  app must run as a single worker.
- **No pagination** — `GET /notes` returns all notes in memory; large stores
  will produce large responses.
- **Sequential IDs** — IDs increment monotonically and are never reused after
  deletion, which leaks deletion history to clients.
- **No authentication or authorisation** — any client can read or modify any note.
