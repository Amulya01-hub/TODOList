class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task_description):
        task = {"task": task_description, "done": False}
        self.tasks.append(task)
        print(f"Task '{task_description}' added successfully!")
    def remove_task(self, task_name):
        for task in self.tasks:
            if task["task"] == task_name:
                self.tasks.remove(task)
                print(f"Task '{task_name}' removed successfully!")
                return
        print(f"Task '{task_name}' not found in the list.")
    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty!")
            return
        print("\nYour To-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task["done"] else "Not Done"
            print(f"{index}. {task['task']} - {status}")
    def mark_complete(self, task_number):
        try:
            task_index = task_number - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index]["done"] = True
                print(f"Task '{self.tasks[task_index]['task']}' marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Display all tasks")
        print("4. Mark a task as completed")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            task = input("Enter the task description: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task name to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            todo_list.display_tasks()
            if todo_list.tasks:
                try:
                    task_num = int(input("Enter the task number to mark as completed: "))
                    todo_list.mark_complete(task_num)
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "5":
            print("Thanks for using me!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
if __name__ == "__main__":
    main()