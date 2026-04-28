# Training-Claude-Code-Extended

> **Claude Code Extended: Build 10 Real-World Projects with Claude Code**
> A 5-hour live workshop by **Luca Berton** that turns Claude Code from an autocomplete tool into an AI development partner you can plan, build, test, refactor, document, and ship with.

[![Workshop](https://img.shields.io/badge/format-live%20workshop-blue)](#)
[![Duration](https://img.shields.io/badge/duration-5h-informational)](#)
[![Level](https://img.shields.io/badge/level-beginner→intermediate-success)](#)
[![Slides](https://img.shields.io/badge/slides-Marp-orange)](slides/README.md)

---

## Table of Contents

- [Overview](#overview)
- [Who This Is For](#who-this-is-for)
- [Prerequisites](#prerequisites)
- [Learning Outcomes](#learning-outcomes)
- [Workshop Schedule](#workshop-schedule)
- [The 10 Projects](#the-10-projects)
- [Repository Structure](#repository-structure)
- [Slide Decks](#slide-decks)
- [Build the Decks](#build-the-decks)
- [Assessment & Certification](#assessment--certification)
- [License](#license)

---

## Overview

Most developers use AI as an autocomplete engine. This workshop teaches you to use **Claude Code** as a teammate — one that plans, codes, tests, reviews, and documents alongside you.

Across **10 hands-on projects** you'll build CLI tools, REST APIs, dashboards, tests, documentation, Git workflows, reusable commands, and production readiness reviews. You'll leave with a **repeatable workflow**, a **personal command library**, and a **certificate of completion**.

**Tagline:** *Build faster, review smarter, and ship safer with Claude Code.*

---

## Who This Is For

- Beginner-to-intermediate developers
- Tech leads adopting AI-assisted workflows
- DevOps and automation engineers
- AI-first builders moving from prompts to shipped software

---

## Prerequisites

- Basic programming knowledge (any language)
- Git familiarity (clone, branch, commit, diff)
- **Claude Code** installed and authenticated
- A local development environment (Node.js or Python preferred)

---

## Learning Outcomes

By the end you will be able to:

1. Set up Claude Code for professional AI-assisted development
2. Use **big prompts** to delegate complete tasks instead of single snippets
3. Build and iterate on real applications end-to-end
4. Use Git branches, commits, and worktrees to make AI coding safe
5. Create and maintain `CLAUDE.md` project context files
6. Apply **Best-of-N** prompting to compare multiple solutions
7. Use Claude Code for testing, debugging, refactoring, documentation, and code review
8. Convert screenshots, sketches, and requirements into working code
9. Use reusable commands, hooks, subagents, and MCP-style workflows
10. Pass the final assessment and earn a certificate

---

## Workshop Schedule

| # | Part | Time | Deliverable |
|---|------|------|-------------|
| 1 | Welcome, Setup & AI-First Mindset | 20 min | AI Coding Workspace |
| 2 | Prompting Like a Tech Lead | 30 min | CLI Task Manager |
| 3 | Project Context with `CLAUDE.md` | 25 min | Project Brain |
| — | Break 1 | 10 min | — |
| 4 | Build Faster with Best-of-N | 35 min | Notes App API |
| 5 | Testing, Debugging & Self-Review | 35 min | Tests + Bug Fixes + Rubric |
| 6 | Git Workflows for Safe AI Dev | 30 min | Feature Branch + Clean History |
| — | Break 2 | 10 min | — |
| 7 | Multimodal: Screenshot to UI | 30 min | Dashboard from Wireframe |
| 8 | Refactoring & Documentation at Scale | 25 min | Refactor + Handoff Docs |
| 9 | Commands, Hooks & Reusable Workflows | 30 min | Personal Command Library |
| — | Break 3 | 10 min | — |
| 10 | Production Readiness | 30 min | Production Readiness Report |
| — | Final Q&A + Exam Briefing | 30 min | — |

**Total:** 4h instruction + 1h breaks/Q&A.

---

## The 10 Projects

1. **AI Coding Workspace** — clean repo + Claude Code session ready
2. **CLI Task Manager** — add/list/complete/delete with tests
3. **Project Brain** — a reusable `CLAUDE.md`
4. **Notes App API** — best of N backend designs
5. **Tests + Rubric for Notes API** — meaningful tests, real bugs found
6. **Feature Branch Workflow** — tagging/search added safely via PR-style review
7. **Dashboard UI** — built from a wireframe, multimodal prompts
8. **Refactor + Handoff Docs** — cleaner structure, onboarding-grade docs
9. **Command Library** — reusable `/review`, `/gen-tests`, `/docs`, `/refactor`, `/release-notes`
10. **Production Readiness Report** — security, deps, CI/CD, deployment

---

## Repository Structure

```
.
├── README.md                # this file
├── .gitignore
└── slides/
    ├── README.md            # slide deck index + render commands
    ├── deploy-pptx.sh       # build PPTX (and PDF/HTML) for all decks
    ├── part-01-setup-mindset.md
    ├── part-02-prompting.md
    ├── part-03-claude-md.md
    ├── part-04-best-of-n.md
    ├── part-05-testing-debugging.md
    ├── part-06-git-workflows.md
    ├── part-07-multimodal.md
    ├── part-08-refactor-docs.md
    ├── part-09-automation.md
    └── part-10-production.md
```

Build artifacts go to `slides/dist/` (gitignored).

---

## Slide Decks

Decks are **Marp-flavored Markdown**. Each deck enforces accountability with the same structure:

1. **Promise** — what learners will be able to do
2. **Topics** — concepts taught
3. **Mini Project** — the hands-on build
4. **Deliverable Checklist** — concrete artifacts to submit
5. **Definition of Done** — pass/fail acceptance criteria
6. **Review Checkpoint** — what the instructor verifies before moving on

Index and per-part links: [slides/README.md](slides/README.md).

---

## Build the Decks

### Quick start

```bash
cd slides
./deploy-pptx.sh           # PPTX only        -> dist/pptx/
./deploy-pptx.sh --pdf     # PPTX + PDF
./deploy-pptx.sh --html    # PPTX + HTML
./deploy-pptx.sh --all     # PPTX + PDF + HTML
./deploy-pptx.sh --clean   # wipe dist/ first
```

The script auto-detects a global `marp` binary; otherwise it falls back to `npx --yes @marp-team/marp-cli@latest`.

### Manual

```bash
npm i -g @marp-team/marp-cli
marp slides/part-01-setup-mindset.md --pdf
marp --input-dir slides --html
```

> **Note:** PPTX/PDF export requires Chromium. Marp downloads one on first run, or set `CHROME_PATH` to an existing Chrome/Edge install.

---

## Assessment & Certification

| Component | Format | Weight |
|---|---|---|
| Knowledge Quiz | Multiple choice / scenario | 40% |
| Practical Task | Mini-build / improvement | 40% |
| Code Review Reflection | Short written | 20% |

**Pass:** ≥ 70% overall.
**Awarded:** *Certificate of Completion — Claude Code Extended: Build 10 Real-World Projects with Claude Code.*

### Sample Assessment Topics

- Choosing the right prompt structure for a feature build
- Creating useful `CLAUDE.md` context
- Reviewing AI-generated code safely
- Using Git branches for Claude Code workflows
- Applying Best-of-N prompting
- Asking Claude Code to generate tests
- Identifying unsafe or incomplete AI output
- Refactoring with constraints
- Using multimodal inputs effectively
- Preparing a project for production review

---

## License

Workshop materials © Luca Berton. All rights reserved unless a `LICENSE` file is added later.
