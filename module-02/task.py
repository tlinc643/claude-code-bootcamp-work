#!/usr/bin/env python3
import argparse
import json
import os
import sys
from datetime import datetime, timezone

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error reading {TASKS_FILE}: {e}", file=sys.stderr)
        sys.exit(2)


def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
    except OSError as e:
        print(f"Error writing {TASKS_FILE}: {e}", file=sys.stderr)
        sys.exit(2)


def next_id(tasks):
    return max((t["id"] for t in tasks), default=0) + 1


def cmd_add(text):
    tasks = load_tasks()
    task = {
        "id": next_id(tasks),
        "status": "todo",
        "created_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task {task['id']}: {task['text']}")


def cmd_list():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    id_w = max(len(str(t["id"])) for t in tasks)
    id_w = max(id_w, 2)
    status_w = max(len(t["status"]) for t in tasks)
    status_w = max(status_w, 6)
    time_w = 19
    text_w = max(len(t["text"]) for t in tasks)
    text_w = max(text_w, 4)

    header = (
        f"{'ID':<{id_w}}  {'STATUS':<{status_w}}  {'CREATED AT':<{time_w}}  {'TEXT'}"
    )
    print(header)
    print("-" * len(header))
    for t in tasks:
        print(
            f"{t['id']:<{id_w}}  {t['status']:<{status_w}}  {t['created_at']:<{time_w}}  {t['text']}"
        )


def cmd_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            if t["status"] == "done":
                print(f"Task {task_id} is already done.")
                return
            t["status"] = "done"
            save_tasks(tasks)
            print(f"Marked task {task_id} as done.")
            return
    print(f"Error: task {task_id} not found.", file=sys.stderr)
    sys.exit(1)


def cmd_delete(task_id):
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Error: task {task_id} not found.", file=sys.stderr)
        sys.exit(1)
    save_tasks(new_tasks)
    print(f"Deleted task {task_id}.")


def main():
    parser = argparse.ArgumentParser(
        prog="task",
        description="A simple CLI task manager.",
    )
    sub = parser.add_subparsers(dest="command", metavar="COMMAND")
    sub.required = True

    add_p = sub.add_parser("add", help="Add a new task")
    add_p.add_argument("text", help="Task description")

    sub.add_parser("list", help="List all tasks")

    done_p = sub.add_parser("done", help="Mark a task as done")
    done_p.add_argument("id", type=int, metavar="ID", help="Task ID")

    del_p = sub.add_parser("delete", help="Delete a task")
    del_p.add_argument("id", type=int, metavar="ID", help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        cmd_add(args.text)
    elif args.command == "list":
        cmd_list()
    elif args.command == "done":
        cmd_done(args.id)
    elif args.command == "delete":
        cmd_delete(args.id)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as e:
        print(f"Internal error: {e}", file=sys.stderr)
        sys.exit(2)
