import tkinter as tk
from tkinter import *

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        x = valueTxt.get(1.0, "end-1c")
        self.element.append(x)

    def dequeue(self):
        x = valueTxt.get(1.0, "end-1c")
        self.element.pop(0)

    def displayqueue(self):
        valueTxt.insert(tk.INSERT, "Elements in Queue")
        for i in self.element:
            valueTxt.insert(tk.INSERT, i)
    def clearQueue(self):
        valueTxt.delete(1.0, END)

top = Tk()
top.geometry("600x600")


valueTxt = Text(width=55, height=2)
valueTxt.place(x=100, y=100)
queue = Queue()
def show(x):
    try:
        if x == "create_queue":
            y = 1

        elif x == "display":
            queue.displayqueue()

        elif x == "enqueue":
            queue.enqueue()

        elif x == "dequeue":
            queue.dequeue()

        elif x == "clearQueue":
            queue.clearQueue()

    except:
        valueTxt.delete(1.0, END)
        valueTxt.insert(tk.INSERT, "Invalid")



display = Button(top, text="display", width=10, height=5, command=lambda: show("display"))
display.place(x=100, y=150)

enqueue = Button(top, text="enqueue", width=10, height=5, command=lambda: show("enqueue"))
enqueue.place(x=200, y=150)

dequeue = Button(top, text="dequeue", width=10, height=5, command=lambda: show("dequeue"))
dequeue.place(x=300, y=150)

create_queue = Button(top, text="create queue", width=10, height=5, command=lambda: show("create_queue"))
create_queue.place(x=100, y=250)

B5 = Button(top, text="clear queue", width=10, height=5, command=lambda: show("clearQueue"))
B5.place(x=200, y=250)


top.mainloop()