"""
number1 = int(input("number 2: "))
number2 = int(input("number 2: "))
operator = input("+, -, *, / ")

if operator == "+":
    print("the Sum is: ", number1 + number2)

elif operator == "-":
    print("the subtratcion is: ", number1 - number2)

elif operator == "/":
    print("the divition is: ", number1 / number2)

elif operator == "*":
    print("the multiplication is: ", number1 * number2)

else:
    print("Folow intstructions next time")
"""

student_name = input("enter the student name: ")
course1 = int(input("emter the grade for course1: "))
course2 = int(input("emter the grade for course2: "))
course3 = int(input("emter the grade for course3: "))
course4 = int(input("emter the grade for course4: "))
course5 = int(input("emter the grade for course5: "))

total = (course1+course2+course3+course4+course5)/5

if total >= 90:
    print("Grade is an A")

elif total < 90 and total >= 80:
    print("Grade is an B")

elif total < 80 and total >= 70:
    print("Grade is an C")

elif total < 70 and total >= 60:
    print("Grade is an D")

else:
    print("Grade is an F")
