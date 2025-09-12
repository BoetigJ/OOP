stu_name = ["Joe", "john", "mary", "sue", "larry"]
stu_age = [21,23,24,31,16]
print(stu_name)
print(stu_age)
while True:
    print("1. Add Student to the list")
    print("2. remove a specific student")
    print("3. replace a student in the list")
    print("5. Quit")
    option = input("Enter your choice: ")

    if option == "1":
        n = input("What is their name?: ")
        y = int(input("How old are they?: "))
        stu_age.append(y)
        stu_name.append(n)

    elif option == "3":
        x = int(input("what is the index of the element to be replaced"))
        new_name = input("The new value")
        stu_name[x] = new_name

        new_age = int(input("The new value"))
        stu_name[x] = new_age

    elif option == "2":

        z = int(input("Who do you want to remove?: "))
        for i in range(0,len(stu_name)):
            if stu_name[i] == z:

                stu_name.remove(z)
                stu_age.remove(stu_age[i])

    elif option == "6":
        break
    print(stu_name)
    print(stu_age)


























mylist = [1,5,7,8,98,67,10009,67,2,16]

while True:
    print("1. Add Element to the list")
    print("2. remove a specific element")
    print("3. replace and element in the list")
    print("4. Sort the list")
    print("5. Reverse the list")
    print("5. Quit")
    option = input("Enter your choice: ")

    if option == "1":
        y = int(input("What do you want to add?: "))
        mylist.append(y)

    elif option == "3":
        x = int(input("what is the index of the element to be replaced"))
        new_element = int(input("The new value"))
        mylist[x] = new_element

    elif option == "2":
        z = int(input("What do you want to remove?: "))
        mylist.remove(z)

    elif option == "4":
        mylist.sort()

    elif option == "5":
        mylist.reverse()


    elif option == "6":
        break
    print(mylist)

while True:
    print("1. Add Element to the list")
    print("2. remove a specific element")
    print("3. pop")
    print("4. Display list")
    print("5. Quit")
    option = input("Enter your choice: ")

    if option == "1":
        mylist.append(input("What do you want to add?: "))

    elif option == "3":
        mylist.pop()

    elif option == "2":
        print(mylist)
        mylist.remove(input("What do you want to remove?: "))

    elif option == "4":
        print(mylist)

    elif option == "5":
        print("Thank you for using this program")
        break

