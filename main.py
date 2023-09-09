from to_do_list import ToDoList

tasks = ToDoList()
is_on = True

while is_on:
    choice = int(input("Welcome to the To-Do List Application:\n"
                       "Select an option number:\n"
                       "1. Add a new task\n"
                       "2. List all task\n"
                       "3. Mark a task as complete\n"
                       "4. Remove a task\n"
                       "5. List completed tasks\n"
                       "6. List incomplete tasks\n"
                       "7. Exit\n"))

    if 1 > choice > 7:
        print("You have entered a wrong choice. Please enter again.\n")
    elif choice == 1:
        tasks.item()
    elif choice == 2:
        tasks.display()
    elif choice == 3:
        task_num = int(input("Enter the task you that want to mark as complete: "))
        tasks.mark_complete(task_num)
    elif choice == 4:
        task_num = int(input("Enter the task you that want to mark as complete: "))
        tasks.remove_task(task_num)
    elif choice == 5:
        tasks.completed_task()
    elif choice == 6:
        tasks.incomplete_task()
    elif choice == 7:
        is_on = False
        print("Thank you for using the To-Do List Application! Goodbye.")
