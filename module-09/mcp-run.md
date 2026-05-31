# MCP Dry Run: Notes API Smoke Test

This is a conceptual walkthrough of how the Model Context Protocol (MCP) could
be used to smoke-test the Notes API. **No external service is connected here.**

---

## What MCP adds

Without MCP, Claude issues Bash commands to run curl or pytest and reads the
text output. With MCP, a dedicated server can expose the Notes API operations
as typed tools that Claude calls directly — no shell escaping, structured
responses, and the ability to compose checks programmatically.

---

## Hypothetical MCP server: `notes-api-mcp`

Imagine a small MCP server (`notes_api_mcp.py`) that wraps the running Notes
API and exposes five tools:

| MCP Tool           | HTTP call it makes            | Returns                     |
|--------------------|-------------------------------|-----------------------------|
| `health_check`     | `GET /health`                 | `{ status, service }`       |
| `create_note`      | `POST /notes`                 | created `Note` object       |
| `list_notes`       | `GET /notes`                  | array of `Note` objects     |
| `get_note`         | `GET /notes/{id}`             | single `Note` or 404 detail |
| `delete_note`      | `DELETE /notes/{id}`          | 204 or 404 detail           |

The MCP server is registered in `.claude/settings.json`:

```json
{
  "mcpServers": {
    "notes-api": {
      "command": "python",
      "args": ["module-09/notes_api_mcp.py"],
      "env": { "NOTES_API_BASE": "http://127.0.0.1:8000" }
    }
  }
}
```

---

## Dry-run conversation

```
You:    /notes-api-smoke   (MCP variant)

Claude: [calls mcp__notes-api__health_check]
        → { "status": "ok", "service": "notes-api" }
        Health check: PASS ✓

        [calls mcp__notes-api__create_note  { title: "smoke", body: "test" }]
        → { "id": 1, "title": "smoke", "body": "test", ... }
        Create note: PASS ✓

        [calls mcp__notes-api__list_notes]
        → [ { "id": 1, ... } ]
        List notes (1 item): PASS ✓

        [calls mcp__notes-api__get_note  { id: 1 }]
        → { "id": 1, "title": "smoke", ... }
        Get note: PASS ✓

        [calls mcp__notes-api__delete_note  { id: 1 }]
        → 204 No Content
        Delete note: PASS ✓

        === MCP Smoke Test Results ===
        Health check    PASS
        Create note     PASS
        List notes      PASS
        Get note        PASS
        Delete note     PASS

        Overall: PASS
```

---

## Advantages over pure Bash

| Concern              | Bash + curl approach          | MCP approach                        |
|----------------------|-------------------------------|-------------------------------------|
| Response parsing     | grep / jq on raw text         | Structured dict returned directly   |
| Error handling       | Check exit codes manually     | MCP surface returns typed errors    |
| Composability        | String concatenation          | Pass tool outputs as typed values   |
| Audit trail          | Shell history                 | MCP call log in Claude session      |

---

## Why this is a dry run

- The `notes_api_mcp.py` file does not exist in this module.
- The MCP server is not registered in any real settings file.
- No network calls are made.

This document exists to illustrate the *pattern* — connecting Claude to a
running service via MCP so that API checks become first-class tool calls rather
than shell commands.
