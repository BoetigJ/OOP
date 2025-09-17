"""mystudent = {"s1":"Justus", "s2":"Jemi"}
mystudent.update({"s3":"melba"})
print(mystudent)

del mystudent["s2"]

print(mystudent)"""

myStudents = {"s1":
    {
        "name":"Bob",
        "major":"Theater",
        "year": "Freshman",
        "TCredits": 15,
        "gpa": 0.0
    },
"s2":
    {
        "name":"Bess",
        "major":"CS",
        "year": "Senior",
        "TCredits": 36,
        "gpa": 3.6
    },
"s3":
    {
        "name":"Billy",
        "major":"Enginering",
        "year": "Graduate",
        "TCredits": 80,
        "gpa": 4.0
    }
}

while 1:
    yn = input("y/n/p/d/r")
    if yn == "y":
        sid = input("Enter student ID")
        nname = input("Enter student name")
        mmajor = input("Enter student major")
        yyear = input("Enter student year")
        ttc = int(input("Enter student's total credit "))
        ggpa = int(input("Enter studen's GPA"))

        myStudents.update({sid:{
                           "name":nname,
                            "major":mmajor,
                            "year":yyear,
                           "Total Credit":ttc,
                            "GPA":ggpa
            }
        })
    elif yn == "n":
        break

    elif yn == "p":
        for student_record in myStudents.items():
            print(student_record)
            print("-------------------------------------------")

    elif yn == "d":
        x = input("What student ID do you want to remove?: ")
        del myStudents[x]

    elif yn == "r":
        a = input("Which student do you want to replace (use their ID) ")

        sid = input("Enter student ID")
        nname = input("Enter student name")
        mmajor = input("Enter student major")
        yyear = input("Enter student year")
        ttc = int(input("Enter student's total credit "))
        ggpa = int(input("Enter studen's GPA"))

       for b in myStudents[a]:
           break
