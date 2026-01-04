import os
import json

TODO_FILE = "/Users/work/Desktop/Python Projects/To-Dos/todo_list.json"

def load_list():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return {}
def save_todo_list(todo_list, task):
    with open(TODO_FILE, "w") as f:
        json.dump(todo_list, f)

def add_task(todo_list, task):
    task_id = str(len(todo_list) + 1)
    todo_list[task_id] = task
    save_todo_list(todo_list, task)
    print(f"Task added: [{task_id} {task}]")

def delete_task(todo_list, task_id):
    if task_id in todo_list:
        removed = todo_list.pop(task_id)
        save_todo_list(todo_list, removed)
        print(f"Take deleted: [{task_id} {removed}]")
    else:
        print("Invalid task ID.")

def main():
    todo_list = load_list()
    while True:
        print("\nTo-Do List:")
        for id, task in todo_list.items():
            print(f"[{id} {task}]")
        print("\nOptions: (1) Add (2) Delete (3) Exit")
        choice = input("Choose an option:")

        if choice == "1":
            task = input("Enter the new task:")
            add_task(todo_list, task)
        elif choice == "2":
            task_id = input("Enter the task ID to delete:")
            delete_task(todo_list, task_id)
        elif choice == "3":
            break
        else:
            print("Invalid input.")
    
if __name__ == "__main__":
    main()
