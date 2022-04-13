import tkinter.commondialog
import tkinter.filedialog
import tkinter.font
import tkinter.messagebox
from tkinter import *
import pyrebase
from tkinter import ttk
 
config = {
    "apiKey": "AIzaSyBjIWNb-UANzMtPujPZAkrgbop8BNxtrBY",
    "authDomain": "hostel9999.firebaseapp.com",
    "databaseURL": "https://hostel9999.firebaseio.com",
    "projectId": "hostel9999",
    "storageBucket": "hostel9999.appspot.com",
    "messagingSenderId": "434326247526",
    "appId": "1:434326247526:web:33330d79f6dcb828"
}
 
firebase = pyrebase.initialize_app(config)
db = firebase.database()
 
# ** making new window ***
root = Tk()
root.geometry("1260x600")
 
# root.tk.call('wm', 'icon', root._w,  PhotoImage(file="C:\\Users\\user\\Pictures/captain.jpg"))
root.title("Student Application")
 
 
 
def doNothing():
    student = Tk()
    student.title("students")
    student.geometry("400x400")
    name = Label(student, text="Name : ", fg="green")
    name.grid(row=0, stick=W)
    entry_name = Entry(student)
    entry_name.grid(row=0, column=1)
 
 
 
    branch = Label(student, text="Branch", fg="green")
    branch.grid(row=1, stick=W)
    entry_branch = Entry(student)
    entry_branch.grid(row=1, column=1)
    var = BooleanVar()
    var.set(True)
    c = Checkbutton(student, text="fresher", variable=var)
    c.grid(columnspan=2)
    k = var.get()
    def insert_it():
        db.child("names").push(entry_name.get())
        db.child("students").push(entry_branch.get())
        db.child("freshers").push(k)
        tkinter.messagebox.showinfo(title="registration info", message="your registration is successful..")
 
    button = Button(student, text="Register", bg="green", fg="white", width=7, command = insert_it)
    button.grid(row=4, columnspan=2)
 
 
def department_login():
    depart = Tk()
    depart.title("Departments...")
 
    label_1 = Label(depart, text="To get access ..", fg="black", font=("TIMES NEW ROMAN", 20, "bold"))
    label_1.grid(columnspan=3, row=0)
    depart.geometry("400x400")
    name = Label(depart, text="ID :", fg="green")
    name.grid(row=1, stick=W)
    entry_name = Entry(depart)
    entry_name.grid(row=1, column=1, pady=10)
 
    name = Label(depart, text="PASSWORD :", fg="green")
    name.grid(row=2, stick=W)
    password = Entry(depart, show='*')
    password.grid(row=2, column=1, pady=10)
 
    def log():
        db.child("department").push(entry_name.get())
        db.child("passwords").push(password.get())
        tkinter.messagebox.showinfo(title = "logging you in", message="login is successful for your department admin ..")
 
 
    login = Button(depart, text="login", fg="white", bg="green", command=log )
    login.grid(row=3, columnspan=10, padx=10, pady=10)
 
 
def message_box_warning():
    tkinter.messagebox.showwarning(title="registration info", message="your some information are conflicting terms and conditions..")
 
 
menu = Menu(root)
root.config(menu=menu)
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Student...", command=doNothing)
subMenu.add_command(label="New sem", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)
 
tools = Menu(menu)
menu.add_cascade(label="Setting", menu=tools)
tools.add_command(label="External Setting", command=doNothing)
tools.add_separator()
tools.add_command(label="appearance", command=doNothing)
tools.add_command(label="admin setting", command=doNothing)
 
tools = Menu(menu)
menu.add_cascade(label="tools", menu=tools)
tools.add_command(label="student - forms", command=doNothing)
 
tools.add_command(label="events", command=doNothing)
tools.add_separator()
tools.add_command(label="important dates", command=doNothing)
 
# **** ADD A TOOL BAR***
 
toolbar = Frame(root, bg="white")
insertButt = Button(toolbar, text="in.", bg="lightgray", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
 
insertButt = Button(toolbar, text="start", bg="lightgray", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
 
insertButt = Button(toolbar, text="list", bg="lightgray", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
 
insertButt = Button(toolbar, text="inf.", bg="lightgray", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
 
toolbar.pack(side=TOP, fill=X)
 
departments_1 = Frame(root, bg="green")
head = Label(departments_1, bg="blue", text="ADMIN", font=("TIMES NEW ROMAN", 20, "bold"))
head.pack(side=LEFT)
 
departments = Label(departments_1, text="Departments", font=("TIMES NEW ROMAN", 15, "bold"), fg="red")
departments.pack(side=LEFT)
departments_1.pack(side=TOP)
frame_1 = Frame(root )
cse = Label(frame_1, text="1. Computer Science", fg="maroon",font=("TIMES NEW ROMAN", 25, "bold"))
cse.grid(row=0, column=0, padx=10, stick=W, pady = 5)
btn_1 = Button(frame_1, text="CSE LOGIN", bg="green", fg="white", command=department_login)
btn_1.grid(row=0, column=1, padx=10, stick=W)
 
mec = Label(frame_1, text="2. Mechanical Engineering", fg="maroon", font=("TIMES NEW ROMAN", 25, "bold"))
mec.grid(row=1, column=0, padx=10, stick=W, pady = 5)
btn_2 = Button(frame_1, text="MEC LOGIN", bg="green", fg="white", command=department_login)
btn_2.grid(row=1, column=1, padx=10, stick=W)
 
civil = Label(frame_1, text="3. Civil Engineering", fg="maroon", font=("TIMES NEW ROMAN", 25, "bold"))
civil.grid(row=2, column=0, padx=10, stick=W, pady = 5)
btn_3 = Button(frame_1, text="CIV LOGIN", bg="green", fg="white", command=department_login)
btn_3.grid(row=2, column=1, padx=10, stick=W)
 
 
cse = Label(frame_1, text="4. Electrical Engineering", fg="maroon",font=("TIMES NEW ROMAN", 25, "bold"))
cse.grid(row=3, column=0, padx=10, stick=W, pady = 5)
btn_1 = Button(frame_1, text="EE LOGIN", bg="green", fg="white", command=department_login)
btn_1.grid(row=3, column=1, padx=10, stick=W)
 
mec = Label(frame_1, text="5. Chemical Engineering", fg="maroon", font=("TIMES NEW ROMAN", 25, "bold"))
mec.grid(row=4, column=0, padx=10, stick=W, pady = 5)
btn_2 = Button(frame_1, text="CHE LOGIN", bg="green", fg="white", command=department_login)
btn_2.grid(row=4, column=1, padx=10, stick=W)
 
civil = Label(frame_1, text="6. Other Engineering", fg="maroon", font=("TIMES NEW ROMAN", 25, "bold"))
civil.grid(row=5, column=0, padx=10, stick=W, pady = 5)
btn_3 = Button(frame_1, text="LOGIN...", bg="green", fg="white", command=department_login)
btn_3.grid(row=5, column=1, padx=10, stick=W)
 
 
 
frame_1.pack(padx=10, pady=10, side=TOP, anchor=W)
 
 
status_bar = Frame(root, bg="white")
label = Label(status_bar, text="showing your results ...")
label.pack(side=LEFT)
status_bar.pack(side=BOTTOM)
 
root.mainloop()