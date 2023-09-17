import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        task_list.delete(selected_task_index)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def edit_task():
    selected_task_index = task_list.curselection()
    if selected_task_index:
        edited_task = entry.get()
        if edited_task:
            task_list.delete(selected_task_index)
            task_list.insert(selected_task_index, edited_task)
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter an edited task!")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit!")

def clear_tasks():
    task_list.delete(0, tk.END)

#Create a main tkinter window
root = tk.Tk()
root.title("To-Do List")

#Create a label with a black background
label = tk.Label(root, text="To-Do List", font=("Arial", 16), bg="black", fg='white')
label.pack(pady=10, fill=tk.X)

#Create an entry widget
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10, fill=tk.X)

#Create a frame for the listbox and buttons
frame = tk.Frame(root)
frame.pack(padx=10, pady=5)

#Create listbox to display tasks
task_list = tk.Listbox(frame, selectmode=tk.SINGLE, font=("Arial", 12), height=10, width=40)
task_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#Create scrollbar for the listbox
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=task_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list.config(yscrollcommand=scrollbar.set)

#Create buttons for adding, editing, deleting, clearing tasks
add_button = tk.Button(root, text="Add Task", bg='black', fg='white', font=("Arial", 12), command=add_task)
edit_button = tk.Button(root, text="Edit Task", bg='black', fg='white', font=("Arial", 12), command=edit_task)
delete_button = tk.Button(root, text="Delete Task", bg='black', fg='white', font=("Arial", 12), command=delete_task)
clear_button = tk.Button(root, text="Clear Task", bg='black', fg='white', font=("Arial", 12), command=clear_tasks)  # Added Clear Task button

add_button.pack(pady=5)
edit_button.pack(pady=5)
delete_button.pack(pady=5)
clear_button.pack(pady=5)

#Start the tkinter main loop
root.mainloop()
