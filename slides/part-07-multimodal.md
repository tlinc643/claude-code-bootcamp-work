---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 7"
footer: "Luca Berton · Multimodal Prompting: From Screenshot to UI"
---

# Part 7
## Multimodal Prompting: Screenshot to UI

**Duration:** 30 min · **Format:** Visual prompt demo + hands-on build
**Deliverable:** A working **Dashboard UI** built from a wireframe

---

## Why Multimodal?

A picture is worth ~1,000 prompt tokens.

Sketches and screenshots convey:
- **Layout** — spatial intent
- **Hierarchy** — what's primary vs secondary
- **State** — empty, loading, error
- **Interaction** — what's clickable

---

## Inputs You Can Use

- Hand-drawn sketches (phone photo)
- Figma / wireframe screenshots
- Existing app screenshots ("clone this layout")
- Annotated images with arrows + notes

---

## Pasting Screenshots — Use **Ctrl+V**

In Claude Code's terminal UI:

- **Ctrl+V** → paste a screenshot from clipboard
- ⚠️ On macOS, **Cmd+V pastes the file path**, not the image

Workflow: capture → Ctrl+V → annotate intent in text.

---

## The Visual-to-Code Prompt

> *"Here is a wireframe of a dashboard. Build it as React + Tailwind. Infer spacing and hierarchy. List your assumptions before coding. Produce: components, routes, mock data, and a state diagram for empty/loading/error."*

Notice: ask for **assumptions** + **states** explicitly.

---

## Iterative Refinement

```
v0: Generate first pass
v1: Show running result → annotate screenshot → re-prompt
v2: Refine spacing, copy, states
v3: Polish — loading, empty, error
```

Each iteration: **update the prompt**, not the code by hand.

---

## When to Update the Prompt vs Edit Code

| Update prompt | Edit code |
|---|---|
| Layout-wide changes | One-off tweaks |
| Pattern repeats (theme, spacing) | Local fix |
| Re-architect | Rename a variable |
| Adding states | Typo fix |

If you'd want it next time → prompt it.

---

## Common Pitfalls

- Skipping the assumptions list → wrong layout, fast
- Not specifying the stack → random framework
- Forgetting empty/error states
- Pixel-perfect demands without enough source material

---

## Planning Mode — `Shift+Tab` ×2

For broad changes, toggle **Planning Mode**:

- Press **Shift+Tab twice** (once if already auto-accepting edits)
- Claude reads more files, drafts a plan, **waits for approval**
- You review and redirect *before* any code is written

Best for: multi-file refactors, new features, codebase-wide changes.

---

## Thinking Modes

Trigger more reasoning tokens by phrasing:

| Phrase | Reasoning budget |
|---|---|
| `think` | basic |
| `think more` | extended |
| `think a lot` | comprehensive |
| `think longer` | extended time |
| `ultrathink` | maximum |

Best for: hard logic, debugging, algorithm design.
**Planning ≠ Thinking** — combine for breadth + depth (costs tokens).

---

## Steering the Conversation

| Action | Shortcut / Cmd |
|---|---|
| Stop Claude mid-response | **Esc** |
| Rewind to an earlier message | **Esc Esc** |
| Add a memory while stopped | `#` |
| Summarize history, keep insights | `/compact` |
| Wipe history, fresh start | `/clear` |

`/compact` after deep learning · `/clear` when switching tasks.

---

## Mini Project 7 — Dashboard from Wireframe

**Source:** provided sketch (or your own).

Required regions:
- Top nav with user
- KPI cards row (4 cards)
- Chart panel
- Recent activity list

States: loading, empty, populated, error.

---

## Skills Practiced

- Multimodal prompting
- UI generation
- Component structure
- Iterative design refinement

---

## Deliverable Checklist ✅

- [ ] `03-dashboard/` runnable frontend
- [ ] All 4 regions present
- [ ] All 4 UI states implemented
- [ ] Componentized (not one big file)
- [ ] `prompts/` folder with **iteration history** (v0 → vN)
- [ ] Screenshot of final UI in repo

---

## Definition of Done

- `npm run dev` (or stack equiv.) boots
- Resizing the window doesn't break layout
- Loading/empty/error states are reachable
- Prompt history shows real iteration, not one-shot

---

## Review Checkpoint 🔎

Pair-demo:
- Show your wireframe **and** final UI
- Walk through your prompt iterations
- Each suggests **one** state or component you missed.

---

## Next Up

**Part 8 — Refactoring & Documentation at Scale**
You'll clean up the dashboard and document it for handoff.
