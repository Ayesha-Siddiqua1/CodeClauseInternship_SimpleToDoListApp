import tkinter as tk
from tkinter import messagebox

# Main application class
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg='#947F67')

        self.tasks = []

        self.task_input = tk.Entry(self.root, width=60, font='50', border='10') #used to create a single-line text input field
        self.task_input.pack(pady=10) #to add widget

        self.add_button = tk.Button(self.root, text="Add Task", width=40, command=self.add_task, background='#92947E', border='5', font=('MV Boli', 12))
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, selectmode=tk.SINGLE, border='2', font=('MV Boli', 15))
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=40, command=self.delete_task, background='#92947E', border='5', font=('MV Boli', 12))
        self.delete_button.pack(pady=5)

        self.done_button = tk.Button(self.root, text="Mark as Done", width=40, command=self.mark_done, background='#92947E', border='5', font=('MV Boli', 12))
        self.done_button.pack(pady=5)

    def add_task(self):
        task = self.task_input.get()
        if task != "":            
            self.tasks.append(task)
            self.update_listbox()
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            del self.tasks[selected[0]]
            self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if selected:
            task = self.tasks[selected[0]]
            if not task.startswith("✔ "):
                self.tasks[selected[0]] = "✔ " + task
                self.update_listbox()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()