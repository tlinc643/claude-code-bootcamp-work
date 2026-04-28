# Claude Code Extended — Workshop Slide Decks

**Instructor:** Luca Berton
**Duration:** 5 hours (4h instruction + 1h breaks/Q&A)
**Format:** Marp-flavored Markdown — render to HTML, PDF, or PPTX.

## Decks (one per Part)

| # | Part | Time | Deliverable |
|---|------|------|-------------|
| 1 | [Welcome, Setup & AI-First Mindset](part-01-setup-mindset.md) | 20 min | AI Coding Workspace |
| 2 | [Prompting Claude Code Like a Tech Lead](part-02-prompting.md) | 30 min | CLI Task Manager |
| 3 | [Project Context with CLAUDE.md](part-03-claude-md.md) | 25 min | Project Brain (CLAUDE.md) |
| 4 | [Build Real Apps Faster with Best-of-N](part-04-best-of-n.md) | 35 min | Notes App API |
| 5 | [Testing, Debugging & Self-Review](part-05-testing-debugging.md) | 35 min | Tests + Bug Fixes + Rubric |
| 6 | [Git Workflows for Safe AI Development](part-06-git-workflows.md) | 30 min | Feature Branch + Clean History |
| 7 | [Multimodal Prompting: Screenshot to UI](part-07-multimodal.md) | 30 min | Dashboard UI from Wireframe |
| 8 | [Refactoring & Documentation at Scale](part-08-refactor-docs.md) | 25 min | Refactor + Dev Handoff Docs |
| 9 | [Automation: Commands, Hooks, Workflows](part-09-automation.md) | 30 min | Personal Command Library |
| 10 | [Production Readiness: Security, CI, Deployment](part-10-production.md) | 30 min | Production Readiness Report |

## Render

```bash
# Install Marp CLI
npm i -g @marp-team/marp-cli

# Render a single deck to PDF
marp part-01-setup-mindset.md --pdf

# Render all decks to HTML
marp --input-dir . --html
```

### Build all decks to PPTX

```bash
./deploy-pptx.sh           # PPTX only -> dist/pptx/
./deploy-pptx.sh --all     # PPTX + PDF + HTML
./deploy-pptx.sh --clean   # wipe dist/ first
```

The script auto-detects `marp` or falls back to `npx @marp-team/marp-cli`.

## Accountability Model

Every deck contains:
1. **Promise** — what learners will be able to do
2. **Topics** — concepts taught
3. **Mini Project** — the hands-on build
4. **Deliverable Checklist** — concrete artifacts to submit
5. **Definition of Done** — pass/fail acceptance criteria
6. **Review Checkpoint** — what the instructor checks before moving on
