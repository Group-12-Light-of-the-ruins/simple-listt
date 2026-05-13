import tkinter as tk
from tkinter import messagebox

# Main functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    selected = listbox.curselection()

    def execute_update():
        new_value = update_entry.get()

        if new_value != "":
            index = selected[0]
            listbox.delete(index)
            listbox.insert(index, new_value)
            update_pop.destroy()
        else:
            messagebox.showwarning("Blank", "Enter a task.")

    if selected:
        task = listbox.get(selected[0])

        update_pop = tk.Toplevel(root)
        update_pop.title(f"Updating '{task}' task.")
        update_pop.resizable(False, False)

        text_label = tk.Label(update_pop, text=f"Update '{task}' task:", font=("Arial", 10))
        update_entry = tk.Entry(update_pop, font=("Arial", 10), width=25)
        update_button = tk.Button(update_pop, text="Update", width=25, command=execute_update)
        close_button = tk.Button(update_pop, text="Cancel", width=25, command=update_pop.destroy)

        text_label.pack()
        update_entry.pack()
        update_button.pack()
        close_button.pack()

# Setup the main window
root = tk.Tk()
root.title("Simple listt")
root.geometry("400x450")

# Global variables
selected_index = -1


# Labels
label_guide1 = tk.Label(root, text="Enter task", font=("Arial", 13, "bold"))

# Buttons
add_button = tk.Button(root, text="Add Task", width=25, command=add_task)
delete_button = tk.Button(root, text="Delete Task", width=25, command=delete_task)
update_button = tk.Button(root, text="Update Task", width=25, command=update_task)

# (Listbox, Input fields stuffs)
entry = tk.Entry(root, font=("Arial", 14), width=50)
listbox = tk.Listbox(root, height=0, width=35, font=("Arial", 12))


# Packs (arrangement)
label_guide1.pack(pady=(10, 0))
entry.pack(pady=(0, 20))
add_button.pack(pady=5)
delete_button.pack(pady=5)
listbox.pack(pady=10, fill="both", expand=True, padx=60)
update_button.pack(pady=5)

# Behaviors
listbox.bind("<<ListboxSelect>>", lambda event: print("Selected a task"))

root.mainloop()
