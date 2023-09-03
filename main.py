import customtkinter, tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# Load images
# file_path = os.path.dirname(os.path.realpath(__file__))
# image_1 = customtkinter.CTkImage(
#    Image.open(file_path + "/delete_transparent.jpg"), size=(60, 60)
# )


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("To Do List - By Nagyadi")
app.geometry("400x650")


# Add task def
def add_task():
    task = task_get.get()
    if task:
        tasks_list.insert(0, task)
        task_get.delete(0, END)
        save_tasks()
    else:
        messagebox.showerror("Error", "Enter a task.")


# Remove a task def
def remove_task():
    selected = tasks_list.curselection()
    if selected:
        tasks_list.delete(selected[0])
        save_tasks()
    else:
        messagebox.showerror("Error", "Choose a task to delete.")


# Creating the savings of tasks
def save_tasks():
    with open("tasks.txt", "w") as f:
        tasks = tasks_list.get(0, END)
        for task in tasks:
            f.write(task + "\n")


# Loading the tasks
def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                tasks_list.insert(0, task.strip())
    except FileNotFoundError:
        pass


# font definition
main_font = customtkinter.CTkFont(family="Helvetica", size=30)

# Frame
frame = customtkinter.CTkFrame(master=app, width=360, height=610, bg_color="gray")
frame.place(relx=0.05, rely=0.03)

# head name
label = customtkinter.CTkLabel(
    master=frame, width=350, height=60, text="To-Do-List", font=main_font, anchor=CENTER
)
label.place(relx=0.03, rely=0.05)

# Entry box
task_get = customtkinter.CTkEntry(
    master=frame, font=main_font, width=300, height=60, bg_color="white"
)
task_get.place(relx=0.1, rely=0.15)

# Add button
button_add = customtkinter.CTkButton(
    master=frame,
    command=add_task,
    width=100,
    height=40,
    text="Add Task",
    font=main_font,
    text_color="black",
    fg_color="green",
)
button_add.place(relx=0.28, rely=0.25)

# Remove button
button_remove = customtkinter.CTkButton(
    master=frame,
    command=remove_task,
    #   image=image_1,
    width=200,
    height=80,
    text="Remove Task",
    font=main_font,
    text_color="lightgray",
    fg_color="red",
    border_spacing=10,
)
button_remove.place(
    relx=0.12,
    rely=0.85,
)

# Task display

tasks_list = Listbox(
    master=frame, width=17, height=8, font=main_font, background="gray"
)
tasks_list.place(relx=0.1, rely=0.35)

load_tasks()

app.mainloop()
