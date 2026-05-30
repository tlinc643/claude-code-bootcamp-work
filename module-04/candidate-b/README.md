# Notes API — Candidate B

A simple in-memory Notes REST API built with FastAPI and Pydantic.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app:app --reload
```

The server listens on `http://127.0.0.1:8000` by default.
Interactive docs: `http://127.0.0.1:8000/docs`

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/notes` | Create a note |
| GET | `/notes` | List all notes |
| GET | `/notes/{id}` | Get one note |
| PUT | `/notes/{id}` | Update a note |
| DELETE | `/notes/{id}` | Delete a note |

## curl Examples

### Create a note

```bash
curl -s -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "First note", "body": "Hello, world!"}' | python -m json.tool
```

### List all notes

```bash
curl -s http://127.0.0.1:8000/notes | python -m json.tool
```

### Get one note

```bash
# Replace <id> with the UUID returned by the create call
curl -s http://127.0.0.1:8000/notes/<id> | python -m json.tool
```

### Update a note

```bash
curl -s -X PUT http://127.0.0.1:8000/notes/<id> \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated title"}' | python -m json.tool
```

### Delete a note

```bash
curl -s -X DELETE http://127.0.0.1:8000/notes/<id> -w "%{http_code}\n"
# Expect: 204
```

### Validation error (blank title)

```bash
curl -s -X POST http://127.0.0.1:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "  ", "body": "oops"}' | python -m json.tool
# Expect: 422 Unprocessable Entity
```
