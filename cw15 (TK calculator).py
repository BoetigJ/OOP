#Calculator
import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("600x800")

answer = Text(width=55, height=2)
answer.place(x=100, y=100)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.insert(tk.INSERT, x)
            answer.insert(tk.INSERT, final_answer)

        elif x == "AC":
            answer.delete(1.0, END)

        elif x == "DEL":
            banana = x

        else:
            answer.insert(tk.INSERT, x)

    except:
        answer.delete(1.0, END)
        answer.insert(tk.INSERT, "Invalid Expression")


B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=100, y=150)

B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=150)

B3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
B3.place(x=300, y=150)

B4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
B4.place(x=100, y=250)

B5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
B5.place(x=200, y=250)

B6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
B6.place(x=300, y=250)

B7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
B7.place(x=100, y=350)

B8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
B8.place(x=200, y=350)

B9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
B9.place(x=300, y=350)

B0 = Button(top, text="0", width=10, height=5, command=lambda: show("0"))
B0.place(x=100, y=450)

Bminus = Button(top, text="-", width=10, height=5, command=lambda: show("-"))
Bminus.place(x=200, y=450)

Bplus = Button(top, text="+", width=10, height=5, command=lambda: show("+"))
Bplus.place(x=300, y=450)

Btimes = Button(top, text="*", width=10, height=5, command=lambda: show("*"))
Btimes.place(x=100, y=550)

Bdiv = Button(top, text="/", width=10, height=5, command=lambda: show("/"))
Bdiv.place(x=200, y=550)

Bequa = Button(top, text="=", width=10, height=5, command=lambda: show("="))
Bequa.place(x=300, y=550)

Period = Button(top, text=".", width=10, height=5, command=lambda: show("."))
Period.place(x=100, y=650)

AC = Button(top, text="AC", width=10, height=5, command=lambda: show("AC"))
AC.place(x=200, y=650)

DEL = Button(top, text="DEL", width=10, height=5, command=lambda: show("DEL"))
DEL.place(x=300, y=650)

top.mainloop()