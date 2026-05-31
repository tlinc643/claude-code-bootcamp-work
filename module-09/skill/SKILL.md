# Skill: notes-api-smoke

Smoke-test the FastAPI Notes API in this module and report a clear pass/fail
summary. Do **not** modify application code unless the user explicitly asks.

---

## Trigger

This skill fires when the user types `/notes-api-smoke` or asks you to
"smoke-test the Notes API."

---

## Steps

### 1 — Identify the app file

Search for the FastAPI application entry point:

```bash
find . -name "*.py" | xargs grep -l "FastAPI()" 2>/dev/null
```

Expected result: `module-09/notes_api.py`.  
If not found, stop and tell the user which directory to run from.

### 2 — Check dependencies are installed

```bash
pip show fastapi httpx pytest pytest-asyncio 2>&1 | grep -E "^(Name|WARNING)"
```

If any package is missing, print the install command but do **not** run it
without user approval.

### 3 — Run the test suite

```bash
cd module-09 && python -m pytest tests/ -v --tb=short 2>&1
```

Capture the full output. Note which tests passed, which failed, and any errors.

### 4 — Check the health endpoint (live server optional)

If the server is already running (`ps aux | grep uvicorn`), hit the health
endpoint:

```bash
curl -s http://127.0.0.1:8000/health
```

Expected: `{"status":"ok","service":"notes-api"}`

If the server is not running, skip this step and note it in the summary —
do **not** start the server automatically.

### 5 — Verify CRUD behaviour via the test results

Map the pytest output to these five behaviours:

| Behaviour | What to look for in test output |
|-----------|--------------------------------|
| **Create** | `test_create_note` PASSED / FAILED |
| **List**   | `test_list_notes` PASSED / FAILED |
| **Get**    | `test_get_note` PASSED / FAILED |
| **Update** | `test_update_note` PASSED / FAILED |
| **Delete** | `test_delete_note` PASSED / FAILED |

Any test whose name does not match a row is listed under "Other".

### 6 — Summarise results

Print a table in this format:

```
=== Notes API Smoke Test Results ===

Check               Status   Notes
------------------  -------  ---------------------------
App file found      PASS     module-09/notes_api.py
Test suite ran      PASS     12/12 passed
Health endpoint     SKIP     Server not running
Create note         PASS
List notes          PASS
Get note            PASS
Update note         PASS
Delete note         PASS

Overall: PASS  (or FAIL — list failing checks)
```

### 7 — Guard rails

- Report findings only; do **not** edit `notes_api.py` or any test file.
- If a test fails, quote the relevant error lines verbatim so the user can
  act on them.
- If the whole suite is skipped due to a missing dependency, say so and stop.
