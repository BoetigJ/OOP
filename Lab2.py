myEmployees = {
    "eid1":{
        "Name": "Ferdinand",
        "BasicPay":10000,
        "allowance":20,
        "Deductions":0,
        "Taxes":100,
        "NetPay": 10020,
        "GrossPay": 99900
    },
    "eid2":{
        "Name": "Rebecca",
        "BasicPay":10000,
        "allowance":20,
        "Deductions":0,
        "Taxes":100,
        "NetPay": 10020,
        "GrossPay": 99900
    },
    "eid3":{
        "Name": "John",
        "BasicPay":10000,
        "allowance":20,
        "Deductions":0,
        "Taxes":100,
        "NetPay": 10020,
        "GrossPay": 99900
    },
    "eid4":{
        "Name": "Molly",
        "BasicPay":10000,
        "allowance":20,
        "Deductions":0,
        "Taxes":100,
        "NetPay": 10020,
        "GrossPay": 99900
    },
    "eid5":{
        "Name": "Bruce",
        "BasicPay":10000,
        "allowance":20,
        "Deductions":0,
        "Taxes":100,
        "NetPay": 10020,
        "GrossPay": 99900
    },
}

while 1:
    yn = input("add/quit/print/delete/replace")
    if yn == "add":
        eid = input("Enter Employee ID")
        Name = input("Enter Employee name")
        BasicPay = int(input("What is the Employee's basic pay"))
        Allowance = int(input("What is the Employee's allowance"))
        Deductions = int(input("What is the Employee's deductions"))
        Taxes = int(input("What is the Employee's taxes"))
        NetPay = BasicPay + Allowance
        GrossPay = BasicPay - (Deductions+Taxes)



        myEmployees.update({eid:{
            "Name":Name,
            "BasicPay":BasicPay,
            "Allowance":Allowance,
            "Deductions":Deductions,
            "Taxes":Taxes,
            "NetPay":NetPay,
            "GrossPay":GrossPay,
            }
        })

    elif yn == "quit":
        break

    elif yn == "print":
        for employee_record in myEmployees.items():
            print(employee_record)
            print("-------------------------------------------")

    elif yn == "delete":
        x = input("What Employee ID do you want to remove?: ")
        del myEmployees[x]

    elif yn == "replace":
        a = input("Which employee do you want to replace (use their ID) ")

        eid = input("Enter Employee ID")
        Name = input("Enter Employee name")
        BasicPay = int(input("What is the Employee's basic pay"))
        Allowance = int(input("What is the Employee's allowance"))
        Deductions = int(input("What is the Employee's deductions"))
        Taxes = int(input("What is the Employee's taxes"))
        NetPay = BasicPay + Allowance
        GrossPay = BasicPay - (Deductions + Taxes)

        myEmployees[eid].update( {
            "Name": Name,
            "BasicPay": BasicPay,
            "Allowance": Allowance,
            "Deductions": Deductions,
            "Taxes": Taxes,
            "NetPay": NetPay,
            "GrossPay": GrossPay,

        })