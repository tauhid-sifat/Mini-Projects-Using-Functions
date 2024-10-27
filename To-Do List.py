tasks= []
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")
def view_tasks():
    if tasks:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")


def main():
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Exiting To-Do List application.")
            break
        else:
            print("Invalid choice. Please select again.")


# Run the main function
if __name__ == "__main__":
    main()