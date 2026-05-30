# scoring.md — worked example (reference)

> This is a **filled-in example** of the `scoring.md` you create during the lab.
> Copy this shape into your own `module-04/scoring.md` and replace the numbers
> and notes with your real results. Do not edit this reference file.

## Per-candidate scores

```text
Candidate: a
Correctness (0–3): 3   all 7 curls pass (201/200/200/200/200/204/404)
Simplicity   (0–3): 3   single app.py, readable in one glance, ~12 lines shorter
Fit          (0–3): 2   404 returns {"detail":{"error":"not found"}} — FastAPI wraps detail
Total: 8 / 9
Notes: Pragmatic single-file build. Only ding is the wrapped 404 body, which
       diverges from the spec's bare {"error":"not found"}.
```

```text
Candidate: b
Correctness (0–3): 3   all 7 curls pass
Simplicity   (0–3): 2   split across routes + persistence + schema (3 files to follow)
Fit          (0–3): 3   returns bare {"error":"not found"}; persistence isolated and testable
Total: 8 / 9
Notes: More structure than the scope strictly needs, but it caught the 404
       envelope mismatch and keeps persistence behind a seam.
```

## Side-by-side comparison

| Criterion (0–3) | Candidate A (single file) | Candidate B (split) |
|---|---|---|
| Correctness | 3 — all 7 curls pass | 3 — all 7 curls pass |
| Simplicity  | 3 — one readable file     | 2 — three files to follow |
| Fit         | 2 — 404 body is `{"detail":…}` | 3 — bare `{"error":"not found"}` |
| **Total**   | **8 / 9** | **8 / 9** |

## Decision

**Tie at 8 / 9.** Tie-breaker rule is "simpler source wins," which points to A.
But Fit matters more for a service that will grow, and B's correct 404 shape +
testable persistence seam win on that axis.

**Winner: B.** Justification: with Correctness tied, B's spec-accurate 404 body and
isolated persistence layer outweigh A's brevity for anything beyond a throwaway.
(Choosing A here would also be defensible — *if* the write-up names this exact
trade-off. A vague "B looks cleaner" would not.)
