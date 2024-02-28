class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            print("Invalid task index")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
        else:
            print("Invalid task index")

    def display_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{index + 1}. {task['task']} - {status}")


def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. Complete Task\n3. Remove Task\n4. Display Tasks\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_index = int(input("Enter task index to complete: ")) - 1
            task_manager.complete_task(task_index)
        elif choice == '3':
            task_index = int(input("Enter task index to remove: ")) - 1
            task_manager.remove_task(task_index)
        elif choice == '4':
            task_manager.display_tasks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
