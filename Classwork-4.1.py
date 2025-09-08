mylist = []

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