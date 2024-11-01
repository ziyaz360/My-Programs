def add_task(tasks, task):
    tasks.append({"task": task, "done": False})
def view_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['task']} - {status}")
def mark_done(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
    else:
        print("Invalid task number")
def remove_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
    else:
        print("Invalid task number")
tasks = []

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Enter task number to mark as done: "))
            mark_done(tasks, task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to remove: "))
            remove_task(tasks, task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()

void main()
