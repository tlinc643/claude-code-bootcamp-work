---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 9"
footer: "Luca Berton · Automation: Commands, Hooks & Reusable Workflows"
---

# Part 9
## Automation: Commands, Hooks & Reusable Workflows

**Duration:** 30 min · **Format:** Concept walkthrough + practical lab
**Deliverable:** A **personal Claude Code command library**

---

## Why Automate?

You'll repeat the same prompts hundreds of times:
- *"Review this diff."*
- *"Generate tests for X."*
- *"Write release notes since last tag."*

Stop retyping. **Save them as commands.**

---

## Reusable Command Patterns

A command = a parametrized prompt template:

```md
# /review
Review the staged diff against our review rubric.
Output: severity-ranked list with file:line and proposed fix.
Constraint: do not modify code yet.
```

Stored once, invoked everywhere.

---

## Command Library Categories

| Category | Examples |
|---|---|
| Review | `/review`, `/security-review`, `/perf-review` |
| Testing | `/gen-tests`, `/coverage-gaps` |
| Docs | `/handoff`, `/release-notes`, `/changelog` |
| Refactor | `/find-dup`, `/rename-suggest` |
| Ops | `/ci-check`, `/deps-audit` |

---

## Custom Commands — File Layout

Commands live as Markdown files in your project:

```
.claude/
└── commands/
    ├── audit.md          → /audit
    ├── review.md         → /review
    └── write_tests.md    → /write_tests
```

Filename = command name. **Restart Claude Code** after adding one.

---

## Example: `/audit`

```md
Audit project dependencies:

1. Run `npm audit` to list vulnerable packages
2. Run `npm audit fix` to apply safe updates
3. Run the test suite to verify nothing broke
4. Summarize remaining risks
```

One file → repeatable, consistent multi-step workflow.

---

## Commands with Arguments — `$ARGUMENTS`

```md
Write comprehensive tests for: $ARGUMENTS

Conventions:
* Vitest + React Testing Library
* Place tests in __tests__ next to source
* Name files [filename].test.ts(x)
* Use @/ import prefix

Cover: happy path, edge cases, error states.
```

Invoke:

```
/write_tests src/hooks/use-auth.ts
```

---

## Hooks — Lifecycle Events

Hooks run **before** or **after** Claude uses a tool.

| Hook | Fires | Can block? |
|---|---|---|
| `PreToolUse` | before a tool call | ✅ exit `2` |
| `PostToolUse` | after a tool call | ❌ feedback only |
| `Stop` | response finished | — |
| `UserPromptSubmit` | on each user prompt | — |
| `SessionStart` / `SessionEnd` | session lifecycle | — |
| `PreCompact` | before `/compact` | — |

Configured in `.claude/settings.json` (or `settings.local.json`).

---

## Hook Config — Example

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Read|Grep",
      "hooks": [{
        "type": "command",
        "command": "node $PWD/.claude/hooks/block-env.js"
      }]
    }]
  }
}
```

- `matcher` — tool name, regex-style (`|` = OR, `*` = any)
- `command` — receives JSON on **stdin**, controls flow via exit code

---

## Hook Script — Block `.env` Reads

```js
const chunks = [];
for await (const chunk of process.stdin) chunks.push(chunk);
const { tool_input } = JSON.parse(Buffer.concat(chunks).toString());

const path = tool_input?.file_path || tool_input?.path || "";
if (path.includes(".env")) {
  console.error("Blocked: .env is off-limits");
  process.exit(2);   // 2 = block + send stderr to Claude
}
process.exit(0);     // 0 = allow
```

---

## Sharing Hooks Safely — `$PWD`

Hooks should use **absolute paths** (security best practice).
But absolute paths break when shared across machines.

**Pattern:**
1. Commit `settings.example.json` with `$PWD` placeholders
2. `npm run setup` runs an `init-claude.js` script
3. The script substitutes `$PWD` → real absolute path
4. Output: `.claude/settings.local.json` (gitignored)

Result: shareable + secure.

---

## High-Value Hook Ideas

| Hook | Effect |
|---|---|
| `PostToolUse` on `Edit\|Write` → run `tsc --noEmit` | Type errors fed back instantly |
| `PostToolUse` on `Edit` in `./queries/` → SDK review | Detect duplicate DB queries |
| `PreToolUse` on `Read\|Grep` → block secrets | Protect `.env`, keys |
| `PostToolUse` on `Write` → run formatter | Auto-format every edit |
| Catch-all `"matcher": "*"` → `jq . > log.json` | Inspect hook payloads |

---

## MCP Servers — Extending Claude's Tools

MCP = **Model Context Protocol**. External tools Claude can call.

Add the Playwright browser server (run **outside** Claude Code):

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

Pre-approve permissions in `.claude/settings.local.json`:

```json
{
  "permissions": {
    "allow": ["mcp__playwright"],
    "deny": []
  }
}
```

Note the **double underscores** in `mcp__playwright`.

---

## MCP in Practice

> "Open `localhost:3000`, generate a component, review the styling,
> then update `@src/lib/prompts/generation.tsx` so future
> components use warmer gradients and asymmetric layouts."

Claude **sees the rendered UI** — not just the code — and improves
its own prompts. Other servers: DBs, APIs, filesystem, cloud.

---

## GitHub Integration — `/install-github-app`

Run inside Claude Code:

```
/install-github-app
```

Walks you through:
1. Installing the Claude Code GitHub App
2. Adding your API key as a secret
3. Auto-generating a PR with workflow files in `.github/workflows/`

Two default workflows ship with it.

---

## GitHub Workflows You Get

**Mention action** — `@claude` in any issue or PR
- Plans the task, executes with codebase access, replies inline

**PR action** — runs on every pull request
- Reviews changes, posts a detailed report

Customize with `custom_instructions`, `mcp_config`, and
`allowed_tools` (every tool **must** be explicitly listed).

---

## Claude Code SDK

Run Claude Code **programmatically** (TS / Python / CLI):

```ts
import { query } from "@anthropic-ai/claude-code";

for await (const m of query({
  prompt: "Find duplicate queries in ./src/queries",
  options: { allowedTools: ["Edit"] },
})) {
  console.log(m);
}
```

Default permissions are **read-only**. Use it inside hooks,
git hooks, CI, or one-Claude-reviews-another patterns.

---

## Subagents (Concept)

A subagent = a focused, task-scoped helper:
- **Reviewer subagent** — only reviews diffs
- **Tester subagent** — only writes tests
- **Doc subagent** — only writes docs

Specialization → fewer mistakes, less context drift.

---

## Mini Project 9 — Command Library

Create `commands/` with at minimum:

- `review.md` — diff review against your rubric
- `gen-tests.md` — generate tests for a file/module
- `docs.md` — produce/refresh README + handoff
- `refactor.md` — safe-refactor with constraints
- `release-notes.md` — notes since last tag

---

## Skills Practiced

- Reusable prompt design
- Parametrization
- Workflow automation thinking
- Subagent / hook concepts

---

## Deliverable Checklist ✅

- [ ] `commands/` folder committed
- [ ] **5 commands** above, each with: purpose, inputs, outputs, example
- [ ] Each command tested on a real prior project (1–8)
- [ ] `commands/README.md` indexes them
- [ ] One command demo recorded in notes

---

## Definition of Done

- Commands are **copy-pasteable** into a Claude session
- Each produces consistent output across runs
- A peer can run any command on **their** repo with no edits
- Library is reusable beyond this workshop

---

## Review Checkpoint 🔎

Swap libraries with a peer:
- Run their `/review` on **your** code
- Run yours on **theirs**
- Each finds **one** improvement to the other's command.

---

## Break 3 — 10 minutes ☕

---

## Next Up

**Part 10 — Production Readiness**
Security, CI, deployment, and human judgment.
