from tkinter import *

def click():
    lbl.configure(text="Я жепросил")

window = Tk()
window.title("Ха-ха")
window.geometry("500x500")

lbl = Label(window, 
            text="qq",
            font=("Arial Bold",50))
lbl.grid(column=0, row=0)


btn = Button(window,
            text="Не нажимать",
            bg="green",
            fg="blue",
            command=click)
btn.grid(column=0, row=1)


window.mainloop()