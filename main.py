from tkinter import *
from table import SimpleTable as Table

def init_col_names(tbl):
    rk = Label(tbl, text="Ranking")
    rk.pack()

    nm = Label(tbl, text="Name")
    nm.pack()

def textfield_parse(text):
    for line in text:
        label.config(text=line)

def calculate():
    matches = textfield_parse(text=t.get("1.0", END))

root = Tk()

label = Label(root, text="Football League Table")
label.grid(row=0)
label.pack()

t = Text(root)
t.pack()

calcBtn = Button(text="Calculate", command=calculate)
calcBtn.pack()

tbl = Table(root, 14, 9)
tbl.pack()

#init_col_names(tbl)

root.mainloop()