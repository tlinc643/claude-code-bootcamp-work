# Module 07 — Dashboard Web App

**Track A: Flask + Jinja templates**

## Run

```bash
pip install flask
python app.py
```

Then open http://localhost:8080 in your browser (optimised for 1280×720).

> On a machine with a broken system Python (e.g. 3.14 pyexpat), use uv instead:
> `uv run --with flask python app.py`

## Layout

| Zone | Description |
|------|-------------|
| Header | App title left, "Primary Action" button right |
| Main (left) | Data table — 8 hardcoded tasks with ID, title, status, assignee, due date |
| Main (right) | KPI panel — total tasks, completed, in-progress counts |
| Sidebar nav | Horizontal tab bar — Overview, Notes, Tasks, Reports, Settings |
| Footer | Centred version string |

## Design decisions

- Plain CSS only; no Tailwind or component libraries.
- Static in-memory data — no database, no auth.
- Status colour-coding: green (Done), amber (In Progress), grey (Todo).
