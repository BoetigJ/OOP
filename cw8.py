myStack = []

def stack():
    x = input("What do you want to add to the queue")
    myStack.append(x)
def destack():
    myStack.pop()

while 1:
    UI = input("A/R/D/Q: ")
    if UI == "A":
        stack()

    elif UI == "R":
        destack()

    elif UI == "D":
        print(myStack)

    elif UI == "Q":
        break


myQueue = []

def enqueue():
    x = input("What do you want to add to the queue")
    myQueue.append(x)
def dequeue():
    myQueue.remove(myQueue[0])

while 1:
    UI = input("A/R/D/Q: ")
    if UI == "A":
        enqueue()

    elif UI == "R":
        dequeue()

    elif UI == "D":
        print(myQueue)

    elif UI == "Q":
        break


def area_rectangle():
    l = int(input("Length: "))
    h = int(input("Hight: "))
    print("The area is ",l*h)

def volume_rectangle():
    l = int(input("Length: "))
    h = int(input("Hight: "))
    d = int(input("Depth"))
    print("The area is ",l * h * d)

def area_circle():
    r = int(input("radius: "))
    print("The area is ",r*r*3.14)

def volume_circle():
    r = int(input("radius: "))
    print("The area is ",r*2*3.14)

def volume_sphere():
    r = int(input("radius: "))
    print("The area is ",r*r*r*(4/3)*3.14)

while 1:
    UI = int(input("Rectangle: 1, Cube: 2, Area Circle:3, Circumference of Circle:4, Sphere: 5, Quit: 6 "))
    if UI == 1:
        area_rectangle()

    elif UI == 2:
        volume_rectangle()

    elif UI == 3:
        area_circle()

    elif UI == 4:
        volume_circle()

    elif UI == 5:
        volume_sphere()

    elif UI == 6:
        break


