# PR: Add GET /health endpoint to Notes API

## Summary

- Adds a `GET /health` endpoint that returns `{"status": "ok", "service": "notes-api"}`
- Adds a test (`test_health`) verifying the status code and response body
- Documents the endpoint in `README.md` under the Endpoints section

## Why

A health endpoint is the standard way for load balancers, container orchestrators,
and monitoring tools to verify a service is alive. Adding it now establishes the
pattern for future modules that involve deployment or observability.

## Test plan

- [ ] `pytest tests/test_notes_api.py -v` — all 14 tests pass
- [ ] `pytest tests/test_notes_api.py::test_health -v` — new test passes in isolation
- [ ] `curl -s http://localhost:8000/health` returns `{"status":"ok","service":"notes-api"}`

## Checklist

- [ ] Only `module-06/` files modified
- [ ] No new dependencies introduced
- [ ] README updated
