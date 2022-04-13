import sqlite3
from telnetlib import Telnet
import tkinter.commondialog
import tkinter.filedialog
import tkinter.font
import tkinter.messagebox
from tkinter import *
import pyrebase
from tkinter import ttk

#Initialize Firebase
firebaseConfig={
    "apiKey": "AIzaSyB3VCEN-9oN3CTOBTRMXSWKnQsuqDrTh9Y",
  "authDomain": "facerecognition-6f8c2.firebaseapp.com",
  "databaseURL": "https://facerecognition-6f8c2-default-rtdb.firebaseio.com",
  "projectId": "facerecognition-6f8c2",
  "storageBucket": "facerecognition-6f8c2.appspot.com",
  "messagingSenderId": "205807307757",
  "appId": "1:205807307757:web:024d89044d94de5e44f5e4",
  "measurementId": "G-0XSV5P29Q8"
  }

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

# ** making new window ***
root = Tk()
root.title("Face Recognition System")
root.geometry("1080x720")
my_tree = ttk.Treeview(root)
storeName = "Face Recognition System"

#my functions 

def reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup

    
    
def insert_user():
    itemId = str(entryId.get())
    itemName = str(entryName.get())
    itemLastName= str(entryLastName.get())
    itemBirthdate= str(entryBirthdate.get())
    itemAdresse= str(entryAdresse.get())
    itemTel= str(entryTel.get())
    itemMail= str(entryMail.get())
    if itemId == "" or itemName == " ":
        print("Error Inserting Id")
    if itemName == "" or itemName == " ":
        print("Error Inserting Name")
    if itemLastName == "" or itemLastName == " ":
        print("Error Inserting Lastname")    
    if  itemBirthdate == "" or  itemBirthdate == " ":
        print("Error Inserting Birthdate")
    if itemAdresse == "" or itemAdresse== " ":
        print("Error Inserting Adresse")
    if  itemTel == "" or  itemTel == " ":
        print("Error Inserting Tel")
    if itemMail == "" or itemMail== " ":
        print("Error Inserting Mail")     
    else:
        db.child("user").push({"Id":itemId,"Name":itemName,"LastName":itemLastName,"Birthdate":itemBirthdate,"Adresse":itemAdresse,"Tel":itemTel,"Mail":itemMail})
        tkinter.messagebox.showinfo(title="registration info", message="your registration is successful..")
        entryId.delete(0,END) 
        entryName.delete(0,END) 
        entryLastName.delete(0,END) 
        entryAdresse.delete(0,END) 
        entryBirthdate.delete(0,END) 
        entryMail.delete(0,END) 
        entryTel.delete(0,END)

def read():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS 
        inventory(itemId TEXT, itemName TEXT, itemPrice TEXT, itemQuantity TEXT)""")

    cursor.execute("SELECT * FROM inventory")
    results = cursor.fetchall()
    conn.commit()
    return results
def update_data():
    selected_item = my_tree.selection()[0]
    update_name = my_tree.item(selected_item)['values'][0]
    update(entryId.get(), entryName.get(), entryTel.get(), entryBirthdate.get(), update_name)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

def delete_data():
    selected_item = my_tree.selection()[0]
    deleteData = str(my_tree.item(selected_item)['values'][0])
    delete(deleteData)

    for data in my_tree.get_children():
        my_tree.delete(data)

    for result in reverse(read()):
        my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE')
    my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

titleLabel = Label(root, text=storeName, font=('Arial bold', 30), bd=2)
titleLabel.grid(row=0, column=0, columnspan=8, padx=20, pady=20)
#graphical GUI
idLabel = Label(root, text="ID", font=('Arial bold', 15))
nameLabel = Label(root, text="Name", font=('Arial bold', 15))
lastnameLabel = Label(root, text="LastName", font=('Arial bold', 15))
birthdateLabel=Label(root, text="Birthdate", font=('Arial bold', 15))
AdresseLabel=Label(root, text="Adresse", font=('Arial bold', 15))
TelLabel=Label(root, text="Tel", font=('Arial bold', 15))
MailLabel=Label(root, text="Mail", font=('Arial bold', 15))

idLabel.grid(row=1, column=0, padx=10, pady=10)
nameLabel.grid(row=2, column=0, padx=10, pady=10)
lastnameLabel.grid(row=3, column=0, padx=10, pady=10)
birthdateLabel.grid(row=4, column=0, padx=10, pady=10)
AdresseLabel.grid(row=5, column=0, padx=10, pady=10)
TelLabel.grid(row=6, column=0, padx=10, pady=10)
MailLabel.grid(row=7, column=0, padx=10, pady=10)


#graphical GUI 
entryId = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryName = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryLastName = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryAdresse = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryMail = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryBirthdate = Entry(root, width=25, bd=5, font=('Arial bold', 15))
entryTel = Entry(root, width=25, bd=5, font=('Arial bold', 15))


entryId.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
entryName.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
entryLastName.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
entryBirthdate.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
entryAdresse.grid(row=5, column=1, columnspan=3, padx=5, pady=5)
entryTel.grid(row=6, column=1, columnspan=3, padx=5, pady=5)
entryMail.grid(row=7, column=1, columnspan=3, padx=5, pady=5)


buttonEnter = Button(
    root, text="Add", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#0099ff", command=insert_user)
buttonEnter.grid(row=8, column=1, columnspan=1)

buttonUpdate = Button(
    root, text="Update", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#ffff00", command=update_data)
buttonUpdate.grid(row=8, column=2, columnspan=1)

buttonDelete = Button(
    root, text="Delete", padx=5, pady=5, width=5,
    bd=3, font=('Arial', 15), bg="#e62e00", command=delete_data)
buttonDelete.grid(row=8, column=3, columnspan=1)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial bold', 15))

my_tree['columns'] = ("ID", "Name", "Lastname","Birthdate","Adresse","Tel")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("ID", anchor=W, width=50)
my_tree.column("Name", anchor=W, width=100)
my_tree.column("Lastname", anchor=W, width=100)
my_tree.column("Birthdate", anchor=W, width=100)
my_tree.column("Adresse", anchor=W, width=100)
my_tree.column("Tel", anchor=W, width=100)



my_tree.heading("ID", text="ID", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Lastname", text="Lastname", anchor=W)
my_tree.heading("Birthdate", text="Birthdate", anchor=W)
my_tree.heading("Adresse", text="Adresse", anchor=W)
my_tree.heading("Tel", text="Tel", anchor=W)



for data in my_tree.get_children():
    my_tree.delete(data)

for result in reverse(read()):
    my_tree.insert(parent='', index='end', iid=0, text="", values=(result), tag="orow")

my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial bold', 15))
my_tree.grid(row=1, column=5, columnspan=4, rowspan=5, padx=10, pady=10)

root.mainloop()



