import os

TODO_FILE = "todo.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            for line in file:
                task, status = line.strip().rsplit(",", 1)
                tasks.append({"task": task, "done": status == "done"})
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for t in tasks:
            status = "done" if t["done"] else "todo"
            file.write(f"{t['task']},{status}\n")

def display_tasks(tasks):
    print("\n TODO ")
    pending = [t for t in tasks if not t["done"]]
    if not pending:
        print("No tasks to do!")
    else:
        for i, t in enumerate(pending, 1):
            print(f"{i}. {t['task']}")

    print("\n DONE ")
    completed = [t for t in tasks if t["done"]]
    if not completed:
        print("No completed tasks yet.")
    else:
        for i, t in enumerate(completed, 1):
            print(f"{i}. {t['task']}")

def main():
    tasks = load_tasks()

    while True:
        print("\n TO-DO MENU:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            task = input("Enter the new task: ").strip()
            if task:
                tasks.append({"task": task, "done": False})
                print("Task added.")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)
            to_remove = input("Enter exact task to remove: ").strip()
            original_len = len(tasks)
            tasks = [t for t in tasks if t["task"] != to_remove]
            if len(tasks) < original_len:
                print("Task removed.")
            else:
                print("Task not found.")

        elif choice == "3":
            display_tasks(tasks)
            to_mark = input("Enter exact task to mark as done: ").strip()
            for t in tasks:
                if t["task"] == to_mark:
                    t["done"] = True
                    print("Task marked as done.")
                    break
            else:
                print("Task not found.")

        elif choice == "4":
            display_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

main()
