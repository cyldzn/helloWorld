"""Simple command-line to-do list manager."""
import json
from pathlib import Path

TASKS_FILE = Path("tasks.json")

def load_tasks():
    if TASKS_FILE.exists():
        with TASKS_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task.get("done") else "✖"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def complete_task(tasks, index):
    try:
        tasks[index]["done"] = True
        save_tasks(tasks)
    except IndexError:
        print("Invalid task number")

def main():
    tasks = load_tasks()
    while True:
        cmd = input("(a)dd, (c)omplete, (l)ist, (q)uit: ").strip().lower()
        if cmd == 'a':
            title = input("Task title: ")
            add_task(tasks, title)
        elif cmd == 'c':
            num = int(input("Task number to complete: ") or 0) - 1
            complete_task(tasks, num)
        elif cmd == 'l':
            list_tasks(tasks)
        elif cmd == 'q':
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
