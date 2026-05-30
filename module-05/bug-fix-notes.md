# Module 05 Bug Fix Notes

## Issue Encountered

Initial pytest run failed during test collection with:

`ModuleNotFoundError: No module named 'app'`

## Cause

The test file imported the real application using:

`import app as notes_app`

but pytest was not automatically adding the module-05 folder to the Python import path.

## Fix

Created `pytest.ini` with:

```ini
[pytest]
pythonpath = .
testpaths = tests
