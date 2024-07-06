from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector


# insert Data Function
def insertData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showwarning("Cannot Insert", "All the fields are required!")

    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Jeff032587!", database="employee"
        )
        myCur = myDB.cursor()
        myCur.execute(
            "INSERT INTO empDetails (empID, empName, empDept) VALUES(%s, %s, %s)",
            (id, name, dept),
        )
        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        show()  # Added call to show the data in Listbox

        messagebox.showinfo("Insert Status", "Data Inserted Sucessfully")
        myDB.close()


# update Data Function
def updateData():
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    if id == "" or name == "" or dept == "":
        messagebox.showwarning("Cannot Update", "All the fields are required!")
    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Jeff032587!", database="employee"
        )
        myCur = myDB.cursor()
        myCur.execute(
            "UPDATE empDetails SET empName=%s, empDept=%s WHERE empID=%s",
            (name, dept, id),
        )

        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        show()  # Added call to show the data in Listbox

        messagebox.showinfo("Update Status", "Data Updated Sucessfully")
        myDB.close()


def getData():
    if enterId.get() == "":
        messagebox.showwarning(
            "Fetch Status", "Please provide the Emp ID to fetch the data:"
        )
    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Jeff032587!", database="employee"
        )
        myCur = myDB.cursor()
        myCur.execute("SELECT * FROM empDetails WHERE empID=%s", (enterId.get(),))
        rows = myCur.fetchall()
        # No call required to show the data in Listbox as no changes happened

    for row in rows:
        enterName.insert(0, row[1])
        enterDept.insert(0, row[2])

    myDB.close()

    # delete Data function


def deleteData():
    if enterId.get() == "":
        messagebox.showwarning(
            "cannot delete", "plese provide the Emp ID to delete the data"
        )
    else:
        myDB = mysql.connector.connect(
            host="localhost", user="root", passwd="Jeff032587!", database="employee"
        )
        myCur = myDB.cursor()
        myCur.execute("DELETE FROM empDetails WHERE empID=%s", (enterId.get(),))
        myDB.commit()

        enterId.delete(0, "end")
        enterName.delete(0, "end")
        enterDept.delete(0, "end")

        show()

        messagebox.showinfo("Delete Status", "Data deleted sucessfully")
        myDB.close()


# show Method


def show():
    myDB = mysql.connector.connect(
        host="localhost", user="root", passwd="Jeff032587!", database="employee"
    )
    myCur = myDB.cursor()
    myCur.execute("SELECT * from empDetails")
    rows = myCur.fetchall()
    showData.delete(0, showData.size())

    for row in rows:
        addData = str(row[0]) + " " + row[1] + " " + row[2]
        showData.insert(showData.size() + 1, addData)

    myDB.close()


# Reset Fields Method


def resetFields():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")


# creating parent window

window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")

# create all the labels

empId = Label(window, text="Employee ID", font=("Serif", 12))
empId.place(x=20, y=30)

empName = Label(window, text="Employee Name", font=("Serif", 12))
empName.place(x=20, y=60)

empDept = Label(window, text="Employee Dept", font=("Serif", 12))
empDept.place(x=20, y=90)

# all entry boxes respective to labels

enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

# creating Entry boxes respective to the labels

insertBtn = Button(
    window, text="Insert", font=("Sans", 12), bg="white", command=insertData
)
insertBtn.place(x=20, y=160)

updateBtn = Button(
    window, text="Update", font=("Sans", 12), bg="white", command=updateData
)
updateBtn.place(x=80, y=160)

getBtn = Button(window, text="Fetch", font=("Sans", 12), bg="white", command=getData)
getBtn.place(x=150, y=160)

deleteBtn = Button(
    window, text="Delete", font=("Sans", 12), bg="white", command=deleteData
)
deleteBtn.place(x=210, y=160)

resetBtn = Button(
    window, text="Reset", font=("Sans", 12), bg="white", command=resetFields
)
resetBtn.place(x=20, y=210)

# creating the Listbox

showData = Listbox(window)
showData.place(x=330, y=30)

show()
# added call to show the data in Listbox after the box is created
window.mainloop()
