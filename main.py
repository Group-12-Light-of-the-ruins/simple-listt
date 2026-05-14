import tkinter as tk
from tkinter import Frame, messagebox

# DEFINITIONS
FILE_NAME = "tasks"
COLORS = {
    'background' : "#ffffff",
    'bg-items-1' : "#d4d4d4",
    'bg-items-2' : "#e8e8e8",
    'selected-bg-color': '#9cdb65',
    'text-color-1': "#363636",
}

# Main functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        task_list.append(task)
        end_index = listbox.size() - 1

        if end_index % 2 == 0:
            listbox.itemconfig(end_index, bg=COLORS['bg-items-1'], selectbackground=COLORS['selected-bg-color'])
        else:
            listbox.itemconfig(end_index, bg=COLORS['bg-items-2'], selectbackground=COLORS['selected-bg-color'])

        save_list()
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        task_list.pop(selected)
        save_list()
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
            task_list[index] = new_value
            save_list()
            update_pop.destroy()
        else:
            messagebox.showwarning("Warning", "Blank value input")

    if selected:
        task = listbox.get(selected[0])

        update_pop = tk.Toplevel(root)
        update_pop.title(f"Editing task.")
        update_pop.resizable(False, False)

        text_label = tk.Label(update_pop, text=f"Update task:", font=("Arial", 10))
        update_entry = tk.Entry(update_pop, font=("Arial", 12), width=25)
        update_button = tk.Button(update_pop, text="Update", width=25, command=execute_update)
        close_button = tk.Button(update_pop, text="Cancel", width=25, command=update_pop.destroy)
        update_entry.insert(0, task)

        text_label.pack()
        update_entry.pack()
        update_button.pack()
        close_button.pack()
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def save_list():
    fileExists = False

    try:
        with open(FILE_NAME, "x") as file:
            file.write("")

        fileExists = True
    except FileExistsError:
        fileExists = True

    if fileExists:
        with open(FILE_NAME, "w") as file:
            for task in task_list:
                file.write(f"{task}\n")
    else:
        print(f"There's an error creating and saving '{FILE_NAME}' the file.")

def load_list():
    global task_list
    try:
        with open(FILE_NAME, "r") as file:
            task_list = file.read().splitlines()

        for i,task in enumerate(task_list):
            listbox.insert(tk.END, task)
            if i % 2 == 0:
                listbox.itemconfig(i, bg=COLORS['bg-items-1'], selectbackground=COLORS['selected-bg-color'])
            else:
                listbox.itemconfig(i, bg=COLORS['bg-items-2'], selectbackground=COLORS['selected-bg-color'])
    except FileNotFoundError:
        print(f"The file '{FILE_NAME}' doesn't seem to exist.")


# Setup the main window
root = tk.Tk()
root.title("Simple listt")
root.geometry("1000x700")
root.configure(bg=COLORS['background'])
# root.resizable(False, False)
buttons_container = tk.Frame(root, background=COLORS['background'])

# Global variables
selected_index = -1
task_list = []


# Labels
label_guide1 = tk.Label(root, text="Tasks", font=("Arial", 32, "bold"), background=COLORS['background'], 
                        foreground=COLORS['text-color-1'])
label_tasks = tk.Label(buttons_container, text="Add Task: ", font=("Arial", 12), background=COLORS['background'], 
                       foreground=COLORS['text-color-1'])

# Buttons
add_button = tk.Button(buttons_container, text="Add Task", width=12, command=add_task)
delete_button = tk.Button(buttons_container, text="Delete Task", width=12, command=delete_task)
update_button = tk.Button(buttons_container, text="Edit Task", width=12, command=update_task)

# (Listbox, Input fields stuffs)
entry = tk.Entry(buttons_container, font=("Arial", 12), width=25, borderwidth=4)
listbox = tk.Listbox(root, height=0, width=35, font=("Arial", 20), borderwidth=0, 
                     highlightthickness=0, background=COLORS['background'], foreground=COLORS['text-color-1'])

# Packs (arrangement)
label_guide1.pack(pady=(10, 0), padx=(60, 0), anchor="w")
listbox.pack(pady=5, fill="both", expand=True, padx=60)
buttons_container.pack(side="right", pady=(0, 20), padx=(0, 20))
label_tasks.pack(side="left")
entry.pack(pady=(0, 0), padx=(0, 120), side="left")
add_button.pack(pady=5, padx=(8, 0), side="left", fill="x")
delete_button.pack(pady=5, padx=(8, 0), side="left")
update_button.pack(pady=5, padx=(8, 0), side="left")

# Behaviors
listbox.bind("<<ListboxSelect>>", lambda event: print("Selected a task"))

load_list()
root.mainloop()
