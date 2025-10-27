"""
import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height=500, width=500)

shapel = myCanvas.create_oval(0, 0, 100, 100, fill="blue")

bob = myCanvas.create_rectangle(10, 150, 500, 100, fill="black")

myCanvas.pack()
root.mainloop()
"""

import tkinter

root = tkinter.Tk()
root.resizable(False, False)

myCanvas = tkinter.Canvas(root, bg="white", height=600, width=800)

shape1 = myCanvas.create_oval(20, 20, 100, 100, fill="blue")

#initialize the constants xx, yy
xx =yy = 3

def move_shape():
    global xx, yy
    #move the shape with the constanct xx, yy
    myCanvas.move(shape1, xx, yy)
    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape1)
    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        xx = -xx*.5
    if y1 <= 0 or y2 >= 600:
        yy = -yy*.5
    #call the function recursively
    myCanvas.after(30, move_shape)

#in the main program call the function move_shape()
myCanvas.after(10,move_shape())

shape2 = myCanvas.create_oval(50, 50, 100, 100, fill="red")

#initialize the constants xx, yy
xxx =yyy = -3

def move_shape():
    global xxx, yyy
    #move the shape with the constanct xx, yy
    myCanvas.move(shape2, xxx, yyy)
    #get the current coordinates of the shape
    (x1, y1, x2, y2) = myCanvas.coords(shape2)
    #check the boundaries of the coordinates and change the constants xx, yy
    if x1 <= 0 or x2 >= 800:
        xxx = -xxx
    if y1 <= 0 or y2 >= 600:
        yyy = -yyy
    #call the function recursively
    myCanvas.after(30, move_shape)

#in the main program call the function move_shape()
myCanvas.after(10,move_shape())

myCanvas.pack()
root.mainloop()

"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10",])
y = np.array([80, 100, 62, 76, 100, 89, 10, 74, 45, 98,])

print(np.mean(y))
print(np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("Grades")

plt.plot(x, y)
plt.show()

mylabels = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10"]
plt.pie(y, labels = mylabels)
plt.show()

x = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
y = [21,19,24,17,16,25,24,22,21,21]

plt.xlabel("Year")
plt.ylabel("Average number of bananas that teens consumed in a month")
plt.plot(x,y)
plt.show()

plt.pie(y, labels=x)
plt.show()

plt.scatter(y, x)
plt.show()
"""





