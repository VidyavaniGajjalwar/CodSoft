# To-Do List in Python

# Create an empty list to store tasks
to_do_list = []

# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

# Function to add a new task
def add_task():
    task = input("Enter the task: ")
    to_do_list.append({"task": task, "completed": False})
    print(f"Task '{task}' added successfully!")

# Function to view all tasks
def view_tasks():
    if len(to_do_list) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, item in enumerate(to_do_list, 1):
            status = "Completed" if item["completed"] else "Not Completed"
            print(f"{idx}. {item['task']} - {status}")

# Function to mark a task as completed
def mark_completed():
    view_tasks()
    if len(to_do_list) > 0:
        task_num = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_num <= len(to_do_list):
            to_do_list[task_num - 1]["completed"] = True
            print(f"Task {task_num} marked as completed!")
        else:
            print("Invalid task number.")

# Function to delete a task
def delete_task():
    view_tasks()
    if len(to_do_list) > 0:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(to_do_list):
            removed_task = to_do_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted successfully!")
        else:
            print("Invalid task number.")

# Main loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 5.")