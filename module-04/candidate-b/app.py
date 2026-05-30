from datetime import datetime, timezone
from uuid import UUID, uuid4

from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, field_validator

app = FastAPI(title="Notes API")

_store: dict[UUID, dict] = {}


class NoteCreate(BaseModel):
    title: str
    body: str

    @field_validator("title", "body")
    @classmethod
    def not_blank(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("must not be blank")
        return v


class NoteUpdate(BaseModel):
    title: str | None = None
    body: str | None = None

    @field_validator("title", "body")
    @classmethod
    def not_blank(cls, v: str | None) -> str | None:
        if v is not None and not v.strip():
            raise ValueError("must not be blank")
        return v


class Note(BaseModel):
    id: UUID
    title: str
    body: str
    created_at: datetime
    updated_at: datetime


def _now() -> datetime:
    return datetime.now(timezone.utc)


@app.post("/notes", response_model=Note, status_code=201)
def create_note(payload: NoteCreate) -> Note:
    now = _now()
    note = {
        "id": uuid4(),
        "title": payload.title,
        "body": payload.body,
        "created_at": now,
        "updated_at": now,
    }
    _store[note["id"]] = note
    return Note(**note)


@app.get("/notes", response_model=list[Note])
def list_notes() -> list[Note]:
    return [Note(**n) for n in _store.values()]


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: UUID) -> Note:
    note = _store.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return Note(**note)


@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: UUID, payload: NoteUpdate) -> Note:
    note = _store.get(note_id)
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    if payload.title is not None:
        note["title"] = payload.title
    if payload.body is not None:
        note["body"] = payload.body
    note["updated_at"] = _now()
    return Note(**note)


@app.delete("/notes/{note_id}", status_code=204)
def delete_note(note_id: UUID) -> Response:
    if note_id not in _store:
        raise HTTPException(status_code=404, detail="Note not found")
    del _store[note_id]
    return Response(status_code=204)
