import json

TASK_FILE_NAME = "Task.json"


def Load():
    try:
        with open(TASK_FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def Save(Task):
    with open(TASK_FILE_NAME, 'w') as file:
        json.dump(Task, file, indent=4)

def Display(Task):
    if not Task:
        print("No Task found.")
        return
    for i, task in enumerate(Task, start=1):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i}. {task['title']} [{status}]")
        if task.get('description'):
            print(f"   Description: {task['description']}")
        if task.get('due_date'):
            print(f"   Due Date: {task['due_date']}")


def Add(Task):
    title = input("Enter task title: ").strip()
    if not title:
        print("Task title cannot be empty!")
        return
    description = input("Enter task description (optional): ").strip()
    due_date = input("Enter due date (optional): ").strip()
    Task.append({
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    })
    Save(Task)
    print(f"Task '{title}' added successfully!")


def mark(Task):
    Display(Task)
    if not Task:
        return
    try:
        index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= index < len(Task):
            Task[index]['completed'] = True
            Save(Task)
            print(f"Task '{Task[index]['title']}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def Delete(Task):
    Display(Task)
    if not Task:
        return
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(Task):
            removed_task = Task.pop(index)
            Save(Task)
            print(f"Task '{removed_task['title']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    Task = Load()
    while True:
        print("\nTo-Do List")
        print("1. View Task")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        Option = input("Choose an option: ").strip()
        if Option == '1':
            Display(Task)
        elif Option == '2':
            Add(Task)
        elif Option == '3':
            mark(Task)
        elif Option == '4':
            Delete(Task)
        elif Option == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Option. Please try again.")

if __name__ == "__main__":
    main()
