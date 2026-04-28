---
marp: true
theme: default
paginate: true
header: "Claude Code Extended — Part 10"
footer: "Luca Berton · Production Readiness"
---

# Part 10
## Production Readiness: Security, CI & Deployment

**Duration:** 30 min · **Format:** Demo + guided checklist
**Deliverable:** A **Production Readiness Report** for one project

---

## Prototype ≠ Production

Prototype optimizes for **speed of learning**.
Production optimizes for **safety, reliability, observability**.

Most AI-generated code stops at prototype. Your job: take it the last mile.

---

## Security Review Prompts

> *"Audit this codebase for OWASP Top 10. For each finding: severity, file:line, exploit scenario, recommended fix. Do not change code yet."*

Specific frameworks beat vague *"is this secure?"*

---

## Dependency Review

- List all direct + transitive deps
- Flag unmaintained / abandoned packages
- Check licenses for compatibility
- `npm audit` / `pip-audit` / `cargo audit` baseline
- Pin versions; reproducible builds

---

## Environment & Secrets

- **Never** commit secrets — `.env` in `.gitignore`
- Validate required env vars on startup
- Distinguish dev / staging / prod configs
- Rotate credentials on a schedule
- Use a secret manager in prod

---

## CI/CD Checklist

- [ ] Lint
- [ ] Type-check
- [ ] Unit + integration tests
- [ ] Security scan (deps + code)
- [ ] Build artifact
- [ ] Smoke test on deploy
- [ ] Rollback plan documented

---

## GitHub Actions (Concept)

```yaml
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm audit --omit=dev
```

Ask Claude to generate a workflow tailored to your stack.

---

## Performance & Maintainability

- Profile **before** optimizing
- Add basic logging + metrics
- Document SLAs / SLOs informally
- Track **mean time to recovery**, not just uptime
- Keep a `RUNBOOK.md` for on-call

---

## When Human Judgment Is Essential

- Approving a destructive migration
- Reviewing auth/payment paths
- Accepting a security finding's risk
- Naming things that touch users
- Saying *"no, not yet"*

AI accelerates. **Engineers decide.**

---

## Mini Project 10 — Production Readiness Report

Pick **one** earlier project (Notes API or Dashboard).

Use Claude Code to produce:
1. Security audit
2. Dependency audit
3. CI/CD plan + sample workflow
4. Deployment readiness checklist
5. Performance / maintainability notes
6. List of items requiring **human judgment**

---

## Deliverable Checklist ✅

- [ ] `reports/production-readiness.md`
- [ ] Security findings table (severity, file:line, fix)
- [ ] Dependency audit output
- [ ] `.github/workflows/ci.yml` (or stack equiv.)
- [ ] Deployment checklist signed off
- [ ] "Human review required" section
- [ ] Final polish commit on chosen project

---

## Definition of Done

- Report is **actionable**, not generic
- Every finding has an owner and severity
- CI runs (or would run) on push
- Project has a credible path to staging
- You can defend each decision verbally

---

## Review Checkpoint 🔎

Pair-review:
- Read each other's readiness report
- Flag one finding that's **too vague**
- Flag one finding that's **already handled**.

---

## Final Q&A & Exam Briefing — 30 min

- Common Claude Code mistakes
- Prompting anti-patterns
- How to keep practicing
- Assessment format & passing criteria
- Open Q&A

---

## Assessment Recap

| Component | Format | Weight |
|---|---|---|
| Knowledge Quiz | Multiple choice / scenario | 40% |
| Practical Task | Mini-build / improvement | 40% |
| Code Review Reflection | Short written | 20% |

**Pass:** ≥ 70% overall → **Certificate of Completion**

---

## Closing

> Build faster, review smarter, ship safer with Claude Code.

You've shipped **10 real-world projects**.
You have a workflow, a command library, and a brain in `CLAUDE.md`.

Now go build something real. 🚀
