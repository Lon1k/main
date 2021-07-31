from tkinter import *
from tkinter.ttk import Combobox
#window--------------------=+
window = Tk()
window.title("Ха-ха")
window.geometry("500x500")
#Функции-------------------=+

#Элементы------------------=+
combo = Combobox(window)
combo["values"]=(1,2,3,4,5,"text")
combo.current(0)
combo.grid(column=0, row=0)
#Grid----------------------=+



















window.mainloop()