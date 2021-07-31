from tkinter import *

#window--------------------=+
window = Tk()
window.title("Ха-ха")
window.geometry("500x500")
#Функции-------------------=+
def click():
    res = txt.get()
    lbl.configure(text=f"Привет, {res}")
#Элементы------------------=+
lbl = Label(window, 
            text="Привет",)
btn = Button(window,
            text="Не нажимать",
            command=click,)
txt = Entry(window,width=10, state="disabled")
#Grid----------------------=+
lbl.grid(column=0, row=0)
btn.grid(column=1, row=0)
txt.grid(column=2,row=0)




















window.mainloop()