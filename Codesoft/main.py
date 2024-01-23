# main.py
import tkinter as tk
from todolist import ToDoList

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.todo_list = ToDoList()

        # Create and set up the UI elements
        self.create_ui()

    def create_ui(self):
        # Entry for adding new tasks
        self.new_task_entry = tk.Entry(self.root, width=30)
        self.new_task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Buttons for actions
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.grid(row=0, column=1, padx=5)

        delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        delete_button.grid(row=1, column=1, padx=5)

        update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        update_button.grid(row=2, column=1, padx=5)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, height=10, width=40, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=10, rowspan=2)

        # Populate listbox with existing tasks
        self.update_task_listbox()

    def add_task(self):
        new_task = self.new_task_entry.get()
        if new_task:
            self.todo_list.add_task(new_task)
            self.update_task_listbox()
            self.new_task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.todo_list.delete_task(selected_task_index[0])
            self.update_task_listbox()

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        new_task = self.new_task_entry.get()
        if selected_task_index and new_task:
            self.todo_list.update_task(selected_task_index[0], new_task)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
