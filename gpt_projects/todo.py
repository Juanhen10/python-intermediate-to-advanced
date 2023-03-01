# Define an empty list to store tasks
tasks = []

# Function to add a task to the list


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to view all tasks in the list


def view_tasks():
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        print("Tasks:")
        for task in tasks:
            print("- " + task)


# Main loop of the program
while True:
    print("Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
