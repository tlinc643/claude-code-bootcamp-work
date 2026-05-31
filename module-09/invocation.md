# Invoking the notes-api-smoke Skill

## Slash-command invocation

Type this in the Claude Code prompt:

```
/notes-api-smoke
```

Claude will follow the steps in `skill/SKILL.md` automatically.

---

## Natural-language invocation

Any of these prompts will trigger the same skill:

```
Smoke-test the Notes API and tell me what passes.
```

```
Run a quick health check on the Notes API — I want a pass/fail summary.
```

```
Check that all five CRUD operations work on the Notes API.
```

---

## What to expect

Claude will:

1. Locate `notes_api.py` in the current module.
2. Run `pytest tests/ -v` and capture the output.
3. Optionally hit `GET /health` if a live server is detected.
4. Print a formatted pass/fail table covering Create, List, Get, Update, and
   Delete endpoints.

Claude will **not** modify any application or test files during the smoke test.

---

## Example session

```
You:    /notes-api-smoke

Claude: Running smoke test for module-09/notes_api.py …

        Step 1 — App file found: module-09/notes_api.py ✓
        Step 2 — Dependencies present ✓
        Step 3 — pytest output:
                   12 passed in 0.42s

        === Notes API Smoke Test Results ===
        App file found     PASS   module-09/notes_api.py
        Test suite ran     PASS   12/12 passed
        Health endpoint    SKIP   Server not running
        Create note        PASS
        List notes         PASS
        Get note           PASS
        Update note        PASS
        Delete note        PASS

        Overall: PASS
```
