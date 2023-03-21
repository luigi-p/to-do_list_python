# import librieries
import  tkinter
from tkinter import *

root = Tk()

# visible title
root.title("To-Do List")

# define window size
root.geometry("400x600+400+100")

# disable resize
root.resizable(False, False)

task_list = []

# define function to add new tasks in the txt
def add_task():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

# define functon to remove the selected task from txt file
def delete_task():
    global task_list

    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        
        listbox.delete(ANCHOR)

# define function that open a text file and reads the content if present
def open_task_file():

    # try to open the file, if it doesn't exist, create a new one
    try:
        global task_list

        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if tasks != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    
    except:
        file=open("tasklist.txt", "w")
        file.close()

# window icon
window_icon = PhotoImage(file=r"icons\task.png")
root.iconphoto(False, window_icon)

# top bar icon
top_image = PhotoImage(file=r"icons\topbar.png")
Label(root, image=top_image).pack()

# dock icon
dock_image = PhotoImage(file=r"icons\dock.png")
Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

note_image = PhotoImage(file=r"icons\task.png")
Label(root, image=note_image, bg="#32405b").place(x=340, y=20)

# text in the header
heading = Label(root, text="TO-DO LIST", font="Arial 20 bold", fg="white", bg="#32405b")
heading.place(x=130, y=20)

# main
# create the white frame to add tasks
frame = Frame(root, width=400, height=50, bg="white")
frame.place(x=0, y=180)

# allow user to write in the frame just created
task = StringVar()
task_entry = Entry(frame, width=18, font="Arial 20", bd=0)
task_entry.place(x=10, y=7)

# highlight the frame where user can write down
task_entry.focus()

# add the button to add new tasks
button = Button(frame, text="ADD", font="Arial 20 bold", width=6, bg="#5a95ff", fg="#fff", bd=0, command=add_task)
button.place(x=300, y=0)

# create listbox
frame_1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame_1.pack(pady=(160, 0))

listbox = Listbox(frame_1, font=("Arial", 12), width=40, height=15, bg="#32405b", fg="white", cursor="hand2", selectbackground="#5a95ff")
listbox.pack(side=LEFT, fill=BOTH, padx=2)

# add a scrollbar into the listbox
scrollbar = Scrollbar(frame_1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# call the function
open_task_file()

# add delete button
delete_icon = PhotoImage(file=r"icons\delete.png")
Button(root, image=delete_icon, bd=0, command=delete_task).pack(side=BOTTOM)

# run app
root.mainloop()