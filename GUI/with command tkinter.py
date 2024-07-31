from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def gui():
    window = Tk()
    name = Label(
        window, text="PythonX - Learn Python", bg="white", fg="blue", font=("serif", 16)
    )
    img = Image.open("pic2.png")
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)

    frame = Frame(window, bg="green")
    username = Label(frame, text="Username", bg="red", font=("serif", 12))
    inputBox = Entry(frame)
    button = Button(window, text="Let's Start", command=showMessage)
    button.bind("<Button-1>", showMessage)
    greet = Label(window)

    username1 = inputBox.get()
    greet["text"] = "Welcome" + username1

    name.pack()
    image.pack()
    frame.pack()
    username.pack(side=LEFT)
    inputBox.pack(side=RIGHT)
    button.pack()
    greet.pack()
    window.mainloop()


"""def greetUser(event):
    username = inputBox.get()
    greet["text"] = "Welcome" + username"""

from tkinter import username1


def showMessage():
    messagebox.showinfo("PythonX-Learn python", "Welcome!", username1)


if __name__ == "__main__":
    gui()
