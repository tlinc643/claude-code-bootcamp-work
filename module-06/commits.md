# Commit Plan — Module 06 Git Workflow

## Commit 1: Add GET /health endpoint

**Message:**
```
Add GET /health endpoint to Notes API
```

**Files:**
- `module-06/app.py` — new `health_check` route returning `{"status": "ok", "service": "notes-api"}`
- `module-06/tests/test_notes_api.py` — `test_health` covering the new route
- `module-06/README.md` — Health check section under Endpoints

**Why one commit:**
The route, its test, and its documentation are a single logical unit. Splitting them
would leave the branch in a state where the code and docs are out of sync.
