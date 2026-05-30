# Module 3 — Project Context with CLAUDE.md

## Goal

Author a `CLAUDE.md` for a real repo and prove Claude follows it on the next prompt.

## Scenario

You inherit a repo. Every time you prompt Claude, you re-explain stack, conventions, and "do nots". That waste is what `CLAUDE.md` exists to remove. Today you commit one — and earn it back.

## What you'll do (overview)

In one sentence: **draft a `CLAUDE.md`, commit it to a real repo, then prove in a fresh chat that Claude actually obeys one of its rules.** The five numbered steps below walk you through it.

## Starter instructions

1. Pick a repo: your module-2 work, or any personal repo you trust to commit to.
2. `cd` into it.
3. Create `module-03/` in your submission directory (this is where your two deliverables go).
4. Open `skills/claude-md-template/SKILL.md` for the template and section guidance.

## Claude Code prompt to use

This is **Step 1 — draft CLAUDE.md**. Run this prompt from the **root** of the repo you picked:

```text
You are drafting CLAUDE.md for the repo at the current working directory.
Read the repo first. Then propose a CLAUDE.md with these sections:

# Stack       — languages, package managers, runtime versions
# Conventions — naming, file layout, lint/format rules
# Commands    — exact commands for build, test, run, lint
# Do-not      — things you must never do (e.g., add deps without asking)
# Glossary    — domain terms only this team uses

Each line must change your behavior on a future prompt. If a line is just
documentation, omit it. Keep the whole file under 80 lines.
```

## Manual validation steps

Work through Steps 2–5 below, then run the final checks.

### Step 2 — Save and commit it

1. Save Claude's proposal as `CLAUDE.md` at the **repo root** (not inside `module-03/`).
2. Read every line. Delete any line that is just documentation and would not change Claude's behaviour.
3. Commit it to the repo: `git add CLAUDE.md && git commit -m "Add CLAUDE.md"`.
4. Copy the committed file into your submission folder: `cp CLAUDE.md module-03/CLAUDE.md`.

### Step 3 — Prove Claude obeys it

1. Open a **fresh** Claude Code chat in the same repo (so the new `CLAUDE.md` is loaded).
2. Ask one prompt whose correct answer depends on a line in your `Conventions` section — for example, ask Claude to create a new file or function and watch whether it follows your naming rule.
3. Confirm Claude follows the convention **without you re-stating it**.
4. Screenshot that obedient response and save it as `module-03/proof.png`.

> **Example prompt.** Notice it never mentions any convention — that is the point; you are testing whether `CLAUDE.md` silently steers the output:
>
> ```text
> Create module-03/greet.py: a small CLI with a subcommand `hello <name>`
> that prints "Hello, <name>!". Add a `--upper` flag that uppercases it.
> ```
>
> **Claude obeyed** if, without being asked, it: starts with `#!/usr/bin/env python3`, uses `argparse` subcommands, gives each function a one-line docstring, and exits `0`/`1` per your rules. **Claude ignored** the file if you see multi-line docstrings, hand-rolled `sys.argv` parsing, or no shebang (recheck you're in a fresh chat at repo root).
>
> For the most unmistakable single-line proof, target one high-signal rule instead:
>
> ```text
> Add a function to module-03/greet.py that logs the current time.
> ```
>
> Obeys → `datetime.now(timezone.utc).isoformat()` (ISO-8601 UTC). Ignored → `datetime.now()` (local, no tz) or `time.time()`. That one-line diff is the easiest thing to capture as `proof.png`.

### Step 4 — Run the trim test

The *trim test* checks that every section actually earns its place:

1. Temporarily delete one section from `CLAUDE.md` (start with `Conventions`).
2. Re-ask a prompt that depended on it in a fresh chat.
3. Observe whether Claude's behaviour drifts (e.g., wrong naming, wrong commands).
4. Restore the section. Be ready to **name one line you could delete and why** — that is part of the Definition of done.

### Step 5 — Validate

1. `wc -l CLAUDE.md` → ≤ 80.
2. Confirm all five H1 sections are present: `Stack`, `Conventions`, `Commands`, `Do-not`, `Glossary`.
3. Confirm `CLAUDE.md` is committed to the underlying repo (`git log -- CLAUDE.md` shows your commit).
4. Confirm `module-03/CLAUDE.md` and `module-03/proof.png` both exist.

## Expected deliverable

```text
module-03/
├── CLAUDE.md      # copy of the file you committed to the underlying repo
└── proof.png      # screenshot of Claude obeying one convention
```

## Definition of done

- [ ] File is committed to the underlying repo (not just sitting in the submission folder).
- [ ] All five H1 sections present.
- [ ] ≤ 80 lines total.
- [ ] `proof.png` shows Claude obeying.
- [ ] You can name one line you deleted in the trim test, and why.

## Stretch challenge

Extend the trim test to *every* section: delete each one in turn, re-prompt, and observe the drift. Document which section caused the largest behaviour regression in `module-03/trim-notes.md`.

## Troubleshooting

| Symptom | Fix |
|---|---|
| File over 80 lines | Trim ruthlessly — every line must change behavior. |
| Claude ignores the file | Confirm it's at repo root and you're in a fresh chat. |
| Proof screenshot is unconvincing | Re-pick a convention that produces a visible diff in output. |
