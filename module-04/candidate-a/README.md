# Notes API — Candidate A

Simple in-memory Notes API built with FastAPI.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app:app --reload
```

The server starts at `http://127.0.0.1:8000`.

## Endpoints

### Create a note
```bash
curl -s -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "First note", "body": "Hello, world!"}' | python3 -m json.tool
```

### List all notes
```bash
curl -s http://localhost:8000/notes | python3 -m json.tool
```

### Get one note
```bash
curl -s http://localhost:8000/notes/1 | python3 -m json.tool
```

### Update a note
```bash
curl -s -X PUT http://localhost:8000/notes/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated title", "body": "Updated body."}' | python3 -m json.tool
```

### Delete a note
```bash
curl -s -X DELETE http://localhost:8000/notes/1 -o /dev/null -w "%{http_code}\n"
```

Returns `204 No Content` on success, `404` if the note does not exist.
