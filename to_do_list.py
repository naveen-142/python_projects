from tkinter import *

class ToDoList:
    def __init__(self, root):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self.root)
        self.entry = Entry(self.root)
        self.addButton = Button(self.root, text="Add Task", command=self.add_task)
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task)
        self.updateButton = Button(self.root, text="Update Task", command=self.update_task)
        self.clearButton = Button(self.root, text="Clear List", command=self.clear_list)

        # GUI Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()
        self.updateButton.pack()
        self.clearButton.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.listbox.insert(END, task)
            self.entry.delete(0, END)

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            self.listbox.delete(task_index)
        except IndexError:
            pass

    def update_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            new_task = self.entry.get()
            if new_task != "":
                self.listbox.delete(task_index)
                self.listbox.insert(task_index, new_task)
                self.entry.delete(0, END)
        except IndexError:
            pass

    def clear_list(self):
        self.listbox.delete(0, END)

root = Tk()
root.title("Python To-Do List")
root.geometry("300x400") # Set the window size
to_do_list = ToDoList(root)
root.mainloop()
