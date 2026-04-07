from tkinter import *
from tkinter import ttk

win = Tk()
win.title("ООП практика 5")
win.geometry("500x1000")

#1
style1 = ttk.Style()
style1.configure("1.TFrame", background="lightblue")

frame1 = ttk.Frame(borderwidth = 2, style="1.TFrame", relief=SOLID, padding=[10,10])
frame1.pack(fill=X, padx=5, pady=5)

txt = Entry(frame1, foreground = "blue")
txt.pack()

#2
style2 = ttk.Style()
style2.configure("2.TFrame", background="#EE82EE")


frame2 = ttk.Frame(borderwidth = 2, style="2.TFrame", relief=SOLID, padding=[10,10])
frame2.pack(fill=X, padx=5, pady=5)

def F():
    if chk_state.get():
        p.configure(text="1")
    else:
        p.configure(text="0")  

p = Label(frame2, text="")

chk_state = BooleanVar()
chk_state.set(True)
chk = Checkbutton(frame2, text = "Выбрать", var = chk_state, command = F)
chk.pack()
p.pack()

#3
style3 = ttk.Style()
style3.configure("3.TFrame", background="#FBB117")


frame3 = ttk.Frame(borderwidth = 2, style="3.TFrame", relief=SOLID, padding=[10,10])
frame3.pack(fill=X, padx=5, pady=5)


def T():
    if s.get() == 1:
        l.configure(text= " /⁠ᐠ⁠｡⁠ꞈ⁠｡⁠ᐟ⁠\ ")
    if s.get() == 2:
        l.configure(text=" U⁠ ⁠´⁠꓃⁠ ⁠`⁠ ⁠U ")
    if s.get() == 3:
        l.configure(text=" …⁠ᘛ⁠⁐̤⁠ᕐ⁠ᐷ ")    

l = Label(frame3, text = "")    
s = IntVar()    
rad1 = Radiobutton(frame3, text = "котость", value = 1, variable  = s, command=T)
rad2 = Radiobutton(frame3, text = "собакость", value = 2, variable  = s, command=T)
rad3 = Radiobutton(frame3, text = "рыбкость", value = 3, variable  = s, command=T)

rad1.pack()
rad2.pack()
rad3.pack()
l.pack()

#4

style4 = ttk.Style()
style4.configure("4.TFrame", background="#6C2DC7")


frame4 = ttk.Frame(borderwidth = 2, style="4.TFrame", relief=SOLID, padding=[10,10])
frame4.pack(fill=X, padx=5, pady=5)

CAT = ["коть","котики лучший","они самые милые","мяу~","котики правят миром!!"]
CAT_var = Variable(value=CAT)

cat = Listbox(frame4, listvariable = CAT_var)
cat.pack()

win.mainloop()