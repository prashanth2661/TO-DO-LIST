import os

tasks = []

def load_tasks():
    if os.path.exists('tasks.txt'):
        with open('tasks.txt', 'r') as file:
            for line in file:
                title, description, completed = line.strip().split('|')
                tasks.append({'title': title, 'description': description, 'completed': completed == 'True'})

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(f"{task['title']}|{task['description']}|{task['completed']}\n")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({'title': title, 'description': description, 'completed': False})
    save_tasks()

def view_tasks():
    for i, task in enumerate(tasks):
        status = 'Completed' if task['completed'] else 'Pending'
        print(f"{i + 1}. {task['title']} - {task['description']} [{status}]")

def update_task():
    view_tasks()
    task_index = int(input("Enter task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['title'] = input("Enter new title: ")
        tasks[task_index]['description'] = input("Enter new description: ")
        save_tasks()

def delete_task():
    view_tasks()
    task_index = int(input("Enter task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks()

def mark_task_completed():
    view_tasks()
    task_index = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks()

def main():
    load_tasks()
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            mark_task_completed()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
