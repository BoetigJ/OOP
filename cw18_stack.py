import tkinter as tk
from tkinter import *

class Stack:
    def __init__(self):
        self.element = []
    def push(self):
        self.element.append((text_Box.get(1.0,"end-1c")))
    def pop(self):
        self.element.pop()
    def displayStack(self):
        text_Box.insert(tk.INSERT, "Elements in stack: ")
        for i in self.element:
            g = i + ", "
            text_Box.insert(tk.INSERT, g)
    def clear(self):
        text_Box.delete(1.0, END)


s1 = Stack()

top = Tk()
top.geometry("600x600")



text_Box = Text(width=55, height=2)
text_Box.place(x=100, y=100)
def show(x):
    try:
        if x == "create_stack":
            y = 1

        elif x == "display":
            s1.clear()
            s1.displayStack()

        elif x == "push":
            s1.push()
            s1.clear()

        elif x == "pop":
            s1.pop()

        elif x == "clear":
            s1.clear()


    except:
        text_Box.delete(1.0, END)
        text_Box.insert(tk.INSERT, "Invalid")



display = Button(top, text="display", width=10, height=5, command=lambda: show("display"))
display.place(x=100, y=150)

push = Button(top, text="push", width=10, height=5, command=lambda: show("push"))
push.place(x=200, y=150)

pop = Button(top, text="pop", width=10, height=5, command=lambda: show("pop"))
pop.place(x=300, y=150)

"""create_stack = Button(top, text="create stack", width=10, height=5, command=lambda: show("create_stack"))
create_stack.place(x=100, y=250)"""

clear = Button(top, text="clear", width=10, height=5, command=lambda: show("clear"))
clear.place(x=200, y=250)


top.mainloop()