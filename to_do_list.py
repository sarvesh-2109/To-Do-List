class ToDoList:

    def __init__(self):
        self.task_list = []

    def item(self):
        name = input("Enter the task title: ")
        description = input("Enter the task description: ")
        date = input("Enter due date (DD-MM-YYYY): ")

        task = {
            "Name": name,
            "Description": description,
            "Date": date,
            "Complete": False
        }

        self.task_list.append(task)
        print("Task added successfully!\n")

    def display(self):
        task_number = 1

        for task in self.task_list:
            name = task["Name"]
            description = task["Description"]
            date = task["Date"]
            status = "Complete" if task["Complete"] else "Incomplete"
            print(
                f"{task_number}. Task: {name}\n   Description: {description}\n   Due Date: {date}\n   Status: {status}")
            print()
            task_number += 1

    def mark_complete(self, task_number):
        if 1 <= task_number <= len(self.task_list):
            self.task_list[task_number - 1]["Complete"] = True
            print(f"Task {task_number} marked as complete.")
            print()
        else:
            print("Invalid task number. Please enter a correct task number.")
            print()

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.task_list):
            self.task_list.remove(self.task_list[task_number - 1])
            print("Task removed successfully.")
            print()
        else:
            print("Invalid task number. Please enter a correct task number.")
            print()

    def completed_task(self):
        counter = 1

        for task in self.task_list:
            if task["Complete"]:
                name = task["Name"]
                description = task["Description"]
                date = task["Date"]
                print(f"{counter}. Task: {name}\n   Description: {description}\n   Due Date: {date}")
                print()
                counter += 1

    def incomplete_task(self):
        counter = 1

        for task in self.task_list:
            if not task["Complete"]:
                name = task["Name"]
                description = task["Description"]
                date = task["Date"]
                print(f"{counter}. Task: {name}\n   Description: {description}\n   Due Date: {date}")
                print()
                counter += 1
