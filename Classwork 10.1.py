class Student:
    def __init__(self):
        self.SID = ""
        self.stu_Name = ""
        self.stu_dob = ""
        self.gpa = ""
        self.major = ""
        self.courses = []
    def add_student(self):
        self.SID = input("Enter the ID of the student: ")
        self.stu_Name = input("Enter the student's name: ")
        self.stu_dob = input("Input the student's date of birth (MM/DD/YYYY): ")
        self.gpa = input("Input student's GPA: ")
        self.major = input("Enter the student's major: ")
    def edit_student(self):
        self.SID = input("Enter the ID of the student: ")
        self.stu_Name = input("Enter the student's name: ")
        self.stu_dob = input("Input the student's date of birth (MM/DD/YYYY): ")
        self.gpa = input("Input student's GPA: ")
        self.major = input("Enter the student's major: ")

    def register_courses(self, cc1):
        self.courses.append(cc1)

    def display_student(self):
        print("Stu ID: ", self.SID)
        print("Stu Name: ", self.stu_Name)
        print("Stu Date of Birth: ", self.stu_dob)
        print("Stu GPA: ", self.gpa)
        print("Stu Major: ", self.major)
        for x in self.courses:
            print("courses: ", x.cname)
        print("Stu courses: ", self.courses)

class Course:
    def __init__(self):
        self.cid = ""
        self.cname = ""

    def add_course(self):
        self.cid = input("What is the course ID")
        self.cname = input("What is the course name")

students = []

while True:
    print(students)
    which_student = input("which student do you want to edit? ")
    for student in students:
        what_to_do = input("")

s1 = Student()
s1.add_student()
s1.display_student()
c1 = Course()
c1.add_course()
s1.register_courses(c1)
s1.edit_student()
s1.display_student()
