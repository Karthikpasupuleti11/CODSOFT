import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"{self.title} - {'Completed' if self.completed else 'Pending'}"

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        # Create a Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_listbox.pack(pady=20)

        # Create buttons for task management
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.update_task_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack(pady=5)

        self.mark_complete_button = tk.Button(self.root, text="Mark as Complete", command=self.mark_complete)
        self.mark_complete_button.pack(pady=5)

        self.load_tasks()
        self.update_task_listbox()

    def add_task(self):
        title = simpledialog.askstring("Task Title", "Enter task title:")
        if title:
            description = simpledialog.askstring("Task Description", "Enter task description:")
            if description is not None:  # Check if the user didn't cancel the dialog
                task = Task(title, description)
                self.tasks.append(task)
                self.update_task_listbox()
                self.save_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            title = simpledialog.askstring("Task Title", "Enter new task title:", initialvalue=self.tasks[index].title)
            if title:
                description = simpledialog.askstring("Task Description", "Enter new task description:", initialvalue=self.tasks[index].description)
                if description is not None:  # Check if the user didn't cancel the dialog
                    self.tasks[index].title = title
                    self.tasks[index].description = description
                    self.update_task_listbox()
                    self.save_tasks()
        else:
            messagebox.showwarning("Update Task", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.update_task_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index].completed = True
            self.update_task_listbox()
            self.save_tasks()
        else:
            messagebox.showwarning("Mark Complete", "Please select a task to mark as complete.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**task) for task in tasks_data]
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()