from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def showMessage(username):
    messagebox.showinfo("PythonX - Learn Python", f"Welcome {username}")


def gui():
    window = Tk()
    window.title("PythonX - Learn Python")

    name = Label(
        window, text="PythonX - Learn Python", bg="white", fg="blue", font=("serif", 16)
    )
    name.pack()

    img = Image.open("pic2.png")
    logo = ImageTk.PhotoImage(img)
    image = Label(window, image=logo)
    image.pack()

    frame = Frame(window, bg="green")
    frame.pack()

    username_label = Label(frame, text="Username", bg="red", font=("serif", 12))
    username_label.pack(side=LEFT)

    inputBox = Entry(frame)
    inputBox.pack(side=RIGHT)

    def on_button_click():
        username1 = inputBox.get()
        showMessage(username1)
        greet["text"] = "Welcome " + username1

    button = Button(window, text="Let's Start", command=on_button_click)
    button.pack()

    greet = Label(window)
    greet.pack()

    window.mainloop()


if __name__ == "__main__":
    gui()
