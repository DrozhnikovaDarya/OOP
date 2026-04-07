from tkinter import *
from tkinter.ttk import *

a = Tk()
a.title("Для ООП 4 практика")
a.geometry("500x500")

#1

txt = Entry(a, width = 30)
txt.grid(column = 1, row = 1)

#2

def F():
    if chk_state.get():
        p.configure(text="1")
    else:
        p.configure(text="0")  

p = Label(a, text="")

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(a, text = "Выбрать", var = chk_state, command = F)
chk.grid(column = 0, row = 3)
p.grid(column = 0, row = 2)

#3
def T():
    if s.get() == 1:
        l.configure(text= " /⁠ᐠ⁠｡⁠ꞈ⁠｡⁠ᐟ⁠\ ")
    if s.get() == 2:
        l.configure(text=" U⁠ ⁠´⁠꓃⁠ ⁠`⁠ ⁠U ")
    if s.get() == 3:
        l.configure(text=" …⁠ᘛ⁠⁐̤⁠ᕐ⁠ᐷ ")    

l = Label(a, text = "")    
s = IntVar()    
rad1 = Radiobutton(a, text = "котость", value = 1, variable  = s, command=T)
rad2 = Radiobutton(a, text = "собакость", value = 2, variable  = s, command=T)
rad3 = Radiobutton(a, text = "рыбкость", value = 3, variable  = s, command=T)

rad1.grid(column = 0, row = 4)
rad2.grid(column = 1, row = 4)
rad3.grid(column = 2, row = 4)
l.grid(column = 0, row = 5)

#4

CAT = ["коть","котики лучший","они самые милые","мяу~","котики правят миром!!"]
CAT_var = Variable(value=CAT)

cat = Listbox(listvariable = CAT_var)
cat.grid(column = 1, row = 6)
    

    


a.mainloop()