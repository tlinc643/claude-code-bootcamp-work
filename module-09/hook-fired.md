# Hook: What It Does and How to Know It Fired

## What the hook is intended to do

The hook defined in `.claude/hooks.json` is a `PreToolUse` hook that watches
every Bash tool call Claude makes.

**Trigger condition:** the Bash command string contains `git commit`.

**Action when triggered:**

1. The hook shell script runs `python -m pytest tests/ -q --tb=no` inside
   `module-09/`.
2. If pytest **passes** (exit 0), the hook exits cleanly and the commit
   proceeds normally.
3. If pytest **fails** (exit non-zero), the hook prints:

   ```
   HOOK BLOCKED: pytest failed (exit 1). Fix tests before committing.
   ```

   and exits with code `2`.  Claude Code treats any non-zero hook exit as a
   block: the Bash tool call is cancelled and the error message is surfaced
   to the user.

This enforces a simple rule: **you cannot commit while tests are red**.

---

## Evidence that the hook fired

### Scenario A — tests pass (hook allows the commit)

You would see normal pytest output followed by the commit completing:

```
$ # Claude attempts: git commit -m "..."
[hook runs pytest silently — 12 passed]
[main abc1234] your commit message
```

No visible hook message means the hook ran and let it through.

### Scenario B — tests fail (hook blocks the commit)

Claude Code would display something like:

```
Tool call blocked by PreToolUse hook.

Hook output:
HOOK BLOCKED: pytest failed (exit 1). Fix tests before committing.

FAILED tests/test_notes_api.py::test_create_note - AssertionError
```

The `git commit` Bash call never executes. The commit does not appear in
`git log`.

### Quick manual verification (without a real commit)

You can simulate the hook locally by running the hook script directly:

```bash
# Simulate a failing test environment, then call the hook logic
CLAUDE_TOOL_INPUT="git commit -m test" bash -c '
  if echo "$CLAUDE_TOOL_INPUT" | grep -q "git commit"; then
    cd module-09 && python -m pytest tests/ -q --tb=no
    STATUS=$?
    if [ $STATUS -ne 0 ]; then
      echo "HOOK BLOCKED: pytest failed (exit $STATUS). Fix tests before committing."
      exit 2
    fi
  fi
'
echo "Exit code: $?"
```

If tests are green, exit code is `0`. If tests are red, exit code is `2` and
the blocked message appears — exactly what Claude Code would see.

---

## Important notes

- This hook file lives in `module-09/.claude/hooks.json` and is for **learning
  purposes only**.
- It does not affect any real global Claude Code configuration.
- Real production hooks would be placed in `~/.claude/settings.json` (global)
  or `.claude/settings.json` (project root), not in a sub-directory.
