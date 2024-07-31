from tkinter import *
from PIL import ImageTk, Image

window = Tk()

name = Label(
    window, text="PythonX - Learn Python", bg="white", fg="blue", font=("Serif", 16)
)
img = Image.open("pic2.png")

logo = ImageTk.PhotoImage(img)
image = Label(window, image=logo, width=250, height=200)
button = Button(window, text="Lets Start")
username = Label(window, text="Username", font=("Serif", 12))
inputBox = Entry(window)

name.pack()
image.pack()
username.place(x=20, y=180)
inputBox.place(x=100, y=180)
button.place(x=100, y=200)
window.mainloop()
