class Person:
    def __init__(self, nn, dd, gg):
        self.name = nn
        self.dob = dd
        self.gender = gg

    def display(self):
        print("Person_Name: ", self.name)
        print("Person_DOB: ", self.dob)
        print("Person_Gender: ", self.gender)
        return ""

class Student(Person):
    def __init__(self,x,y,z,a,b):
        Person.__init__(self, x, y, z)
        self.dept = a
        self.id = b

    def display(self):
        print(Person.display(self))
        print("Stu_Dept: ", self.dept)
        print("Stu_ID: ", self.id)

class Faculty(Person):
    def __init__(self,x,y,z,a="",b="", c="", ):
        Person.__init__(self, x, y, z)
        self.dept = a
        self.id = b
        self.salary = c


    def display(self):
        print(Person.display(self))
        if self.dept != "":
            print("Prof_Dept: ", self.dept)
        if self.id != "":
            print("Prof_ID: ", self.id)
        if self.salary != "":
            print("Prof_Salary: ", self.salary)

s1 = Student("Jim", "2004", "Male", "CS", "123")
s1.display()

p1 = Faculty("Bob", "1776", "Male",)
p2 = Faculty("Bob", "1776", "Male", "Batman studies", c="$1,000,000,000,000,000,000")
p3 = Faculty("Bob", "1776", "Male", "Batman Studies", "67", "$200,000,000,000,000,000,000,000")

p1.display()
p2.display()
p3.display()

