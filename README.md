# Claude Code Bootcamp Work

This repository contains my completed work from the **Claude Code Bootcamp** by Packt / Luca Berton.

The goal of this repo is to document my hands-on practice using Claude Code for AI-assisted software development, including project setup, prompt-driven implementation, testing, Git workflow, refactoring, reusable skills, hooks, and production-readiness review.

## Repository Purpose

This is a training and portfolio repository. It demonstrates how I used Claude Code to:

* create small applications from structured requirements;
* use `CLAUDE.md` as persistent project context;
* compare multiple AI-generated implementations;
* test and debug generated code;
* manage changes safely with Git;
* refactor code under explicit constraints;
* create reusable Claude Code skill and hook examples;
* assess a project for production readiness.

## Module Summary

| Module      | Topic                            | What It Demonstrates                                                                                           |
| ----------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `module-01` | Environment and workflow notes   | Captures local development environment and explains the Plan → Implement → Test → Review → Commit workflow.    |
| `module-02` | CLI Task Manager                 | Builds a simple Python command-line task manager with add, list, done, and delete operations.                  |
| `module-03` | Project context with `CLAUDE.md` | Creates a persistent project instruction file so Claude Code follows repo-specific rules.                      |
| `module-04` | Best-of-N Notes API              | Generates two independent FastAPI Notes API implementations, compares them, scores them, and selects a winner. |
| `module-05` | Testing and self-review          | Adds real pytest coverage for the Notes API and documents testing lessons learned.                             |
| `module-06` | Git workflow exercise            | Practices feature-branch development, PR-style review notes, and safe AI-assisted change management.           |
| `module-07` | Screenshot to UI                 | Uses a visual wireframe to generate a simple Streamlit dashboard UI.                                           |
| `module-08` | Refactoring and documentation    | Refactors the Notes API under explicit constraints and adds architecture and handoff documentation.            |
| `module-09` | Skills, hooks, and MCP dry run   | Creates a reusable Claude Code skill, example hook configuration, and MCP dry-run explanation.                 |
| `module-10` | Production readiness report      | Reviews the final project for security, observability, deployment, runbooks, rollback, risks, and readiness.   |

## Main Technical Artifacts

Key artifacts in this repo include:

* `CLAUDE.md` — persistent Claude Code project context.
* `module-04/winner/` — selected Notes API implementation.
* `module-05/tests/` — pytest coverage for the Notes API.
* `module-06/pr.md` — PR-style review summary.
* `module-07/app.py` — Streamlit dashboard generated from a wireframe.
* `module-08/after/` — refactored Notes API.
* `module-08/ARCHITECTURE.md` — architecture documentation.
* `module-08/HANDOFF.md` — handoff and run instructions.
* `module-09/skill/SKILL.md` — reusable Claude Code skill example.
* `module-09/.claude/hooks.json` — demonstration hook configuration.
* `module-10/production-readiness-report.md` — production readiness assessment.

## Notes API Overview

Several modules use a small FastAPI-based Notes API as the working application.

The API supports:

* health check;
* create note;
* list notes;
* get note by ID;
* update note by ID;
* delete note by ID.

The project intentionally uses simple in-memory storage because the bootcamp focus is Claude Code workflow, testing, review, and refactoring rather than production database design.

## How to Run the Refactored Notes API

The refactored version is located in:

```text
module-08/after/
```

From the repository root:

```bash
cd module-08/after
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

The API should then be available at:

```text
http://127.0.0.1:8000
```

## How to Run Tests

From the refactored API folder:

```bash
cd module-08/after
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install pytest httpx
pytest -v
```

Expected result:

```text
14 tests passing
```

## Production Readiness

This repository is a training artifact, not a production service.

The production readiness review in `module-10/production-readiness-report.md` identifies expected gaps such as:

* no authentication;
* no authorization;
* in-memory storage only;
* limited observability;
* no production deployment configuration;
* no persistent data or backup strategy.

The appropriate interpretation is that the project is suitable for learning, demonstration, and portfolio discussion, but not for real production deployment without additional engineering work.

## Key Lessons Learned

The most useful patterns from this bootcamp were:

1. Use `CLAUDE.md` to give Claude Code stable project context.
2. Ask Claude to plan before implementation.
3. Keep work scoped to specific folders and files.
4. Use Git branches and commits to control AI-generated changes.
5. Generate more than one candidate solution when design decisions matter.
6. Test the real implementation, not copied or fake test logic.
7. Refactor only under explicit constraints.
8. Treat production readiness as a structured review, not a guess.

## Attribution

This repository is based on exercises from the Claude Code Bootcamp course materials by Luca Berton / Packt.

The completed module work, notes, tests, reports, and implementation choices in this repository reflect my own hands-on completion of the exercises.
