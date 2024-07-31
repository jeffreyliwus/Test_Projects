from tkinter import *

window = Tk()

lbl = Label(window, text="choose your fav prog languages:")
frame = Frame(window)
python = Checkbutton(frame, text="Python")
java = Checkbutton(frame, text="Java")
js = Checkbutton(frame, text="Js")
cpp = Checkbutton(frame, text="c++")


lbl.pack()
frame.pack()
python.pack()
java.pack()
js.pack()
cpp.pack()
window.mainloop()
