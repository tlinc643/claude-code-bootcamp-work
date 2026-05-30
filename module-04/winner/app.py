from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator

app = FastAPI(title="Notes API")

_store: dict[int, dict] = {}
_next_id = 1


class NoteCreate(BaseModel):
    title: str
    body: str

    @field_validator("title", "body")
    @classmethod
    def not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("must not be empty")
        return v


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


@app.post("/notes", status_code=201)
def create_note(payload: NoteCreate) -> dict:
    global _next_id
    now = _now()
    note = {
        "id": _next_id,
        "title": payload.title,
        "body": payload.body,
        "created_at": now,
        "updated_at": now,
    }
    _store[_next_id] = note
    _next_id += 1
    return note


@app.get("/notes")
def list_notes() -> list[dict]:
    return list(_store.values())


@app.get("/notes/{note_id}")
def get_note(note_id: int) -> dict:
    if note_id not in _store:
        raise HTTPException(status_code=404, detail="Note not found")
    return _store[note_id]


@app.put("/notes/{note_id}")
def update_note(note_id: int, payload: NoteCreate) -> dict:
    if note_id not in _store:
        raise HTTPException(status_code=404, detail="Note not found")
    note = _store[note_id]
    note["title"] = payload.title
    note["body"] = payload.body
    note["updated_at"] = _now()
    return note


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int) -> None:
    if note_id not in _store:
        raise HTTPException(status_code=404, detail="Note not found")
    del _store[note_id]
