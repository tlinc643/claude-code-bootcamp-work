# Module 08 — Handoff

## Quick start

```bash
cd module-08/after
pip install -r requirements.txt
uvicorn app:app --reload
```

The API is then available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

## Running the tests

```bash
cd module-08/after
pip install -r requirements.txt
pytest
```

Expected output: **14 passed** with no warnings.

## Running tests verbosely

```bash
pytest -v
```

## Running a single test

```bash
pytest tests/test_notes_api.py::test_create_note -v
```

## Checking the live API manually

```bash
# Health check
curl http://localhost:8000/health

# Create a note
curl -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello", "body": "World"}'

# List all notes
curl http://localhost:8000/notes

# Get a specific note
curl http://localhost:8000/notes/1

# Update a note
curl -X PUT http://localhost:8000/notes/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated", "body": "New body"}'

# Delete a note
curl -X DELETE http://localhost:8000/notes/1
```

## Notes

- State is in-memory only. Restarting the server clears all notes.
- No authentication is required.
- The `before/` directory contains the original unrefactored version for comparison.
