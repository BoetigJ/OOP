class Student:
    def __init__(self):
        self.SID = ""
        self.stu_Name = ""
        self.stu_dob = ""
        self.gpa = ""
        self.major = ""
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
    def display_student(self):
        print("Stu ID: ", self.SID)
        print("Stu Name: ", self.stu_Name)
        print("Stu Date of Birth: ", self.stu_dob)
        print("Stu GPA: ", self.gpa)
        print("Stu Major: ", self.major)

s1 = Student()
s1.add_student()
s1.display_student()