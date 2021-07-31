from tkinter import *

window = Tk()
window.title("Ха-ха")
window.geometry("500x500")

lbl = Label(window, 
            text="qq",
            font=("Arial Bold",50))
lbl.grid(column=0, row=0)

window.mainloop()