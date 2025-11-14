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
        valueTxt.insert(tk.INSERT, "Elements in Queue: ")
        for i in self.element:
            b = i + ", "
            valueTxt.insert(tk.INSERT, b)
    def clearQueue(self):
        valueTxt.delete(1.0, END)

s1 = Stack()
queue = Queue()

top = Tk()
top.geometry("600x600")


valueTxt = Text(width=55, height=2)
valueTxt.place(x=100, y=100)

#Loop for the queue
def show(x):
    try:
        if x == "create_queue":
            y = 1

        elif x == "display_queue":
            queue.clearQueue()
            queue.displayqueue()

        elif x == "enqueue":
            queue.enqueue()
            queue.clearQueue()

        elif x == "dequeue":
            queue.dequeue()

        elif x == "clearQueue":
            queue.clearQueue()

    except:
        valueTxt.delete(1.0, END)
        valueTxt.insert(tk.INSERT, "Invalid")


#Buttons for the Queue
display_queue = Button(top, text="display_queue", width=10, height=5, command=lambda: show("display_queue"))
display_queue.place(x=100, y=150)

enqueue = Button(top, text="enqueue", width=10, height=5, command=lambda: show("enqueue"))
enqueue.place(x=200, y=150)

dequeue = Button(top, text="dequeue", width=10, height=5, command=lambda: show("dequeue"))
dequeue.place(x=300, y=150)

B5 = Button(top, text="clear queue", width=10, height=5, command=lambda: show("clearQueue"))
B5.place(x=200, y=250)

text_Box = Text(width=55, height=2)
text_Box.place(x=100, y=350)

#Stack loop
def show_stack(a):
    try:

        if a == "display_stack":
            s1.clear()
            s1.displayStack()

        elif a == "push":
            s1.push()
            s1.clear()

        elif a == "pop":
            s1.pop()

        elif a == "clear_stack":
            s1.clear()


    except:
        text_Box.delete(1.0, END)
        text_Box.insert(tk.INSERT, "Invalid")


#Stack Buttons
display_stack = Button(top, text="display_stack", width=10, height=5, command=lambda: show_stack("display_stack"))
display_stack.place(x=100, y=450)

push = Button(top, text="push", width=10, height=5, command=lambda: show_stack("push"))
push.place(x=200, y=450)

pop = Button(top, text="pop", width=10, height=5, command=lambda: show_stack("pop"))
pop.place(x=300, y=450)

clear_stack = Button(top, text="clear_stack", width=10, height=5, command=lambda: show_stack("clear_stack"))
clear_stack.place(x=200, y=550)


top.mainloop()