import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My To-Do App")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#f2f4f7")

        # Title
        title = tk.Label(
            root,
            text="My To-Do List",
            font=("Arial", 24, "bold"),
            bg="#f2f4f7",
            fg="#222222"
        )
        title.pack(pady=20)

        # Input frame
        input_frame = tk.Frame(root, bg="#f2f4f7")
        input_frame.pack(pady=5)

        self.task_entry = tk.Entry(
            input_frame,
            width=32,
            font=("Arial", 14)
        )
        self.task_entry.grid(row=0, column=0, padx=5)

        add_button = tk.Button(
            input_frame,
            text="Add",
            width=8,
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            command=self.add_task
        )
        add_button.grid(row=0, column=1, padx=5)

        # Listbox
        list_frame = tk.Frame(root)
        list_frame.pack(pady=20)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_list = tk.Listbox(
            list_frame,
            width=45,
            height=15,
            font=("Arial", 13),
            selectmode=tk.SINGLE,
            yscrollcommand=scrollbar.set
        )
        self.task_list.pack(side=tk.LEFT)

        scrollbar.config(command=self.task_list.yview)

        # Buttons
        button_frame = tk.Frame(root, bg="#f2f4f7")
        button_frame.pack(pady=10)

        delete_button = tk.Button(
            button_frame,
            text="Delete",
            width=12,
            font=("Arial", 11, "bold"),
            bg="#dc3545",
            fg="white",
            command=self.delete_task
        )
        delete_button.grid(row=0, column=0, padx=5)

        complete_button = tk.Button(
            button_frame,
            text="Complete",
            width=12,
            font=("Arial", 11, "bold"),
            bg="#007bff",
            fg="white",
            command=self.complete_task
        )
        complete_button.grid(row=0, column=1, padx=5)

        clear_button = tk.Button(
            button_frame,
            text="Clear All",
            width=12,
            font=("Arial", 11, "bold"),
            bg="#6c757d",
            fg="white",
            command=self.clear_tasks
        )
        clear_button.grid(row=0, column=2, padx=5)

        # Enter key
        self.task_entry.bind("<Return>", lambda event: self.add_task())

    def add_task(self):
        task = self.task_entry.get().strip()

        if task == "":
            messagebox.showwarning(
                "Warning",
                "Please enter a task."
            )
            return

        self.task_list.insert(tk.END, "☐ " + task)
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a task."
            )
            return

        self.task_list.delete(selected[0])

    def complete_task(self):
        selected = self.task_list.curselection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Please select a task."
            )
            return

        index = selected[0]
        task = self.task_list.get(index)

        if task.startswith("☐ "):
            task = "☑ " + task[2:]
            self.task_list.delete(index)
            self.task_list.insert(index, task)
            self.task_list.selection_set(index)

    def clear_tasks(self):
        if self.task_list.size() == 0:
            return

        answer = messagebox.askyesno(
            "Confirm",
            "Are you sure you want to delete all tasks?"
        )

        if answer:
            self.task_list.delete(0, tk.END)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
