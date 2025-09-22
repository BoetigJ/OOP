Projects = {}

while 1:
    preference = input("What do you want to do? Initiate, Close, Update, Print Specific, Print All : ")
    if preference == "i":
        pid = input("What is the ID of the project")
        name = input("What is the name of the project? ")
        number_Mangers = int(input("How many managers are there? "))
        mngr = []
        for m in range(0, number_Mangers):
            mng = input("Manager name: ")
            mngr.append(mng)
        sDate = input("What is the starting date of the project? ")
        eDate = input("What is the ending date of the project? ")
        spon = input("Who is the sponsor for the project? ")
        bdgt = int(input("What is the budget for the project? "))
        tech = []
        tk = int(input("How many technologies are being used? "))
        for t in range(0, tk):
            x = input("What technology are you using? ")
            tech.append(x)
        team = []
        team_number = int(input("How many team members are there? "))
        for tx in range(0, team_number):
            y = input("What is the team member's name? ")
            team.append(y)

        Projects.update( pid:{
            "Project Title": name,
            "managers": mngr,

        })
