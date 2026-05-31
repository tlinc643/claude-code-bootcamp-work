from datetime import datetime, timezone
from typing import TypedDict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------

class NoteIn(BaseModel):
    title: str
    body: str

    @field_validator("title", "body")
    @classmethod
    def must_not_be_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("must not be empty")
        return v


class Note(TypedDict):
    id: int
    title: str
    body: str
    created_at: str
    updated_at: str


# ---------------------------------------------------------------------------
# Storage
# ---------------------------------------------------------------------------

class NoteStore:
    """In-memory store for notes. Owns the ID counter and the note dict."""

    def __init__(self) -> None:
        self._notes: dict[int, Note] = {}
        self._next_id: int = 1

    def reset(self) -> None:
        """Clear all notes and reset the ID counter (used in tests)."""
        self._notes.clear()
        self._next_id = 1

    def create(self, title: str, body: str) -> Note:
        now = _utc_now()
        note: Note = {
            "id": self._next_id,
            "title": title,
            "body": body,
            "created_at": now,
            "updated_at": now,
        }
        self._notes[self._next_id] = note
        self._next_id += 1
        return note

    def list_all(self) -> list[Note]:
        return list(self._notes.values())

    def get(self, note_id: int) -> Note | None:
        return self._notes.get(note_id)

    def update(self, note_id: int, title: str, body: str) -> Note | None:
        note = self._notes.get(note_id)
        if note is None:
            return None
        note["title"] = title
        note["body"] = body
        note["updated_at"] = _utc_now()
        return note

    def delete(self, note_id: int) -> bool:
        if note_id not in self._notes:
            return False
        del self._notes[note_id]
        return True


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------

store = NoteStore()
app = FastAPI(title="Notes API")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "notes-api"}


@app.post("/notes", status_code=201)
def create_note(payload: NoteIn) -> dict:
    return store.create(payload.title, payload.body)


@app.get("/notes")
def list_notes() -> list[dict]:
    return store.list_all()


@app.get("/notes/{note_id}")
def get_note(note_id: int) -> dict:
    note = store.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.put("/notes/{note_id}")
def update_note(note_id: int, payload: NoteIn) -> dict:
    note = store.update(note_id, payload.title, payload.body)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: int) -> None:
    if not store.delete(note_id):
        raise HTTPException(status_code=404, detail="Note not found")
