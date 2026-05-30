# Project Purpose

This is my personal Claude Code Bootcamp working repository. I use it to practice
and document hands-on exercises as I work through each course module.

# Stack

- **Python 3.11+** — primary language for exercises (stdlib only unless noted)
- **JSON** — lightweight persistence (e.g., `tasks.json`)
- **Markdown** — notes, READMEs, slides
- **Bash** — helper scripts under `scripts/`
- **Mermaid / SVG** — diagrams in select modules

# Repo Structure

```
module-XX/   ← one folder per course module (active work lives here)
exercises/   ← reference exercises and solutions provided by the course
slides/      ← course slide decks (Markdown source)
scripts/     ← repo-level build and validation helpers
skills/      ← reusable Claude Code skill definitions
specs/       ← project specs and planning documents
archive/     ← old or superseded material
```

Each module must be self-contained. Do not share state or imports across modules.

# Working Rules

- **Do not modify completed modules** unless I explicitly ask you to.
- **Keep each module self-contained** — no cross-module imports or shared files.
- **Prefer simple, readable Python** — clarity beats cleverness.
- **Use the Python standard library** unless the module's README explicitly lists
  extra dependencies.
- **Explain your plan before making changes** — one short paragraph is enough.
- **After making changes, provide exact test commands** I can copy and run.
- **Do not create files outside the current module** unless I instruct you to.

# Git Rules

- Commit work module by module — one logical unit per commit.
- Keep commits small and easy to understand.
- **Do not run `git commit`** unless I explicitly ask you to.
- Do not push to any remote unless I ask.

# Do Not

- Do not touch modules or files unrelated to the current task.
- Do not access corporate, sensitive, or personal data.
- Do not add dependencies that aren't required by the task.
- Do not overwrite existing files without warning me first and getting confirmation.
