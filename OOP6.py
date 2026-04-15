from tkinter import *
from tkinter import ttk

win = Tk()
win.title("ООП практика 5")
win.geometry("500x1000")


style1 = ttk.Style()
style1.configure("1.TFrame", background="#EDE275")

frame1 = ttk.Frame(borderwidth = 2, style="1.TFrame", relief=SOLID, padding=[10,10], width=500, height=300)
frame1.grid()
frame1.grid_propagate(False)
frame1.columnconfigure(0, weight=1)


txt = Entry(frame1)
txt.grid(row=0, column=0)

check_var = BooleanVar()
check_var.set(False)

A = []

def F():
    if check_var.get():
        if not(txt.get()):
            p["text"] = "Ничего нет"
        else:
            p["text"] = txt.get()
            A.insert(END, txt.get())
    else:
        p["text"] = "Введите текст и нажмите галочку"

p = Label(frame1, text="")


A_var = Variable(value = A)
A = Listbox(frame1, listvariable = A_var)
A.grid(row=4, column=0)

chk = Checkbutton(frame1, text = "Click", variable=check_var, command = F)
chk.grid(row=1, column=0)
p.grid(row=2, column=0)



win.mainloop()
