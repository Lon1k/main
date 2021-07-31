from tkinter import *
from tkinter.ttk import Combobox, Checkbutton
#window--------------------=+
window = Tk()
window.title("Ха-ха")
window.geometry("500x500")
#Функции-------------------=+

#Элементы------------------=+
chk_state = IntVar()
chk_state.set(0)
chk = Checkbutton(window, text="Выбрать", var=chk_state)
chk.grid(column=0,row=0)
#Grid----------------------=+
window.mainloop()