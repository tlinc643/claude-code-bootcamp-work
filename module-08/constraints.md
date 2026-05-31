# Module 08 Refactoring Constraints

## Goal

Refactor the Notes API from Module 06 to improve readability and maintainability without changing external behavior.

## Hard Constraints

- Do not change API endpoint paths.
- Do not change request or response shapes.
- Do not remove the `/health` endpoint.
- Do not add a database.
- Do not add authentication.
- Do not add unnecessary dependencies.
- Do not modify files outside `module-08`.
- Preserve existing test behavior.
- Keep the app simple and readable.
- Public behavior must remain the same before and after refactoring.

## Allowed Changes

- Improve function names.
- Improve code organization.
- Add helper functions if useful.
- Improve comments or docstrings.
- Improve README or documentation.
- Move the refactored result into `module-08/after`.

## Success Criteria

- Tests pass after refactoring.
- Code is easier to read.
- No external API behavior changes.
