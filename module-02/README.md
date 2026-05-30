# CLI Task Manager

A minimal task manager for the terminal. No dependencies — Python 3.11+ only.

## Install

No installation required. Just run with Python 3.11+:

```
python3 task.py <command>
```

Tasks are persisted to `tasks.json` in the current working directory.

## Commands

### add
Create a new task.
```
python3 task.py add "Write the spec"
```

### list
Print all tasks as a table.
```
python3 task.py list
```

### done
Mark a task as done by its ID.
```
python3 task.py done 1
```

### delete
Remove a task by its ID.
```
python3 task.py delete 1
```

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | User error (e.g. task ID not found) |
| 2 | Internal / I/O error |
