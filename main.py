from tkinter import *

def click():
    res = txt.get()
    print(f"Привет, {res}")
    lbl.configure(text=f"Привет, {res}")

window = Tk()
window.title("Ха-ха")
window.geometry("500x500")

lbl = Label(window, 
            text="Привет",
            font=(10))
lbl.grid(column=0, row=0)


btn = Button(window,
            text="Не нажимать",
            command=click,
            )
btn.grid(column=1, row=0)

txt = Entry(window,width=10)
txt.grid(column=2,row=0)

window.mainloop()