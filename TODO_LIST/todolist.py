# todolist.py

class ToDoList:
    def __init__(self, file_path="tasks.txt"):
        self.file_path = file_path
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file_path, "r") as file:
                tasks = file.read().splitlines()
            return tasks
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.file_path, "w") as file:
            file.write("\n".join(self.tasks))

    def show_tasks(self):
        if not self.tasks:
            return "No tasks found."
        else:
            result = "Tasks:\n"
            for i, task in enumerate(self.tasks, start=1):
                result += f"{i}. {task}\n"
            return result.strip()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added successfully.")

    def delete_task(self, task_index):
        try:
            task_index = int(task_index)
            deleted_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"Task '{deleted_task}' deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid task index.")

    def update_task(self, task_index, new_task):
        try:
            task_index = int(task_index)
            self.tasks[task_index - 1] = new_task
            self.save_tasks()
            print("Task updated successfully.")
        except (ValueError, IndexError):
            print("Invalid task index.")
