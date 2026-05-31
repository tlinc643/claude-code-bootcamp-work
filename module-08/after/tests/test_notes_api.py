import pytest
from fastapi.testclient import TestClient

import app as notes_app
from app import app


@pytest.fixture(autouse=True)
def reset_store():
    """Reset the in-memory store and ID counter before each test."""
    notes_app.store.reset()
    yield


client = TestClient(app)


def test_health():
    """GET /health returns 200 with status ok and service name."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "notes-api"}


def test_create_note():
    """POST /notes returns 201 with the new note's fields."""
    response = client.post("/notes", json={"title": "Hello", "body": "World"})
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Hello"
    assert data["body"] == "World"
    assert "created_at" in data
    assert "updated_at" in data


def test_list_notes_empty():
    """GET /notes returns an empty list when no notes exist."""
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == []


def test_list_notes_returns_all():
    """GET /notes returns all created notes."""
    client.post("/notes", json={"title": "First", "body": "One"})
    client.post("/notes", json={"title": "Second", "body": "Two"})
    response = client.get("/notes")
    assert response.status_code == 200
    notes = response.json()
    assert len(notes) == 2
    assert notes[0]["title"] == "First"
    assert notes[1]["title"] == "Second"


def test_get_note_by_id():
    """GET /notes/{id} returns the correct note."""
    client.post("/notes", json={"title": "My Note", "body": "Content"})
    response = client.get("/notes/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "My Note"
    assert data["body"] == "Content"


def test_update_note():
    """PUT /notes/{id} updates title and body and refreshes updated_at."""
    client.post("/notes", json={"title": "Old Title", "body": "Old Body"})
    original = client.get("/notes/1").json()

    response = client.put("/notes/1", json={"title": "New Title", "body": "New Body"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["body"] == "New Body"
    assert data["created_at"] == original["created_at"]
    assert data["updated_at"] >= original["updated_at"]


def test_delete_note():
    """DELETE /notes/{id} removes the note and returns 204."""
    client.post("/notes", json={"title": "To Delete", "body": "Gone"})
    response = client.delete("/notes/1")
    assert response.status_code == 204

    get_response = client.get("/notes/1")
    assert get_response.status_code == 404


def test_get_missing_note_returns_404():
    """GET /notes/{id} for a non-existent ID returns 404."""
    response = client.get("/notes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"


def test_update_missing_note_returns_404():
    """PUT /notes/{id} for a non-existent ID returns 404."""
    response = client.put("/notes/999", json={"title": "X", "body": "Y"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"


def test_delete_missing_note_returns_404():
    """DELETE /notes/{id} for a non-existent ID returns 404."""
    response = client.delete("/notes/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"


def test_create_note_empty_title_rejected():
    """POST /notes with a blank title returns 422."""
    response = client.post("/notes", json={"title": "   ", "body": "Valid body"})
    assert response.status_code == 422


def test_create_note_empty_body_rejected():
    """POST /notes with a blank body returns 422."""
    response = client.post("/notes", json={"title": "Valid title", "body": ""})
    assert response.status_code == 422


def test_update_note_empty_title_rejected():
    """PUT /notes/{id} with a blank title returns 422."""
    client.post("/notes", json={"title": "Good", "body": "Good"})
    response = client.put("/notes/1", json={"title": "", "body": "Valid"})
    assert response.status_code == 422


def test_update_note_empty_body_rejected():
    """PUT /notes/{id} with a blank body returns 422."""
    client.post("/notes", json={"title": "Good", "body": "Good"})
    response = client.put("/notes/1", json={"title": "Valid", "body": "   "})
    assert response.status_code == 422
