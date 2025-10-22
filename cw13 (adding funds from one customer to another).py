class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_num = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0

    def add_values_to_customer(self):
        self.cid = input("What is the customer's ID? ")
        self.cname = input("What is the customer's name? ")
        self.acc_num = input("What is the customer's account number? ")
        self.phone = input("What is the customer's phone number? ")
        self.emailID = input("What is the customer's email ID? ")
        self.balance = float(input("What is the customer's account balance? "))

    def debit_from(self, debit):
        self.balance -= debit

    def credit_to(self, credit):
        self.balance += credit

    def display_customer(self):
        print("The customer's ID is ",self.cid)
        print("The customer's name is ",self.cname)
        print("The customer's account number is ",self.acc_num)
        print("The customer's phone number is ",self.phone)
        print("The customer's email ID is ",self.emailID)
        print("The customer's balance is $",self.balance)

c1 = Customer()
c2 = Customer()

c1.add_values_to_customer()
print("")
c2.add_values_to_customer()
print("\n ------ \n")

c1.display_customer()
print("")
c2.display_customer()
print("\n ------ \n")

transfer_amount = float(input("How much money do you wish to transfer? "))
print("")

c1.debit_from(transfer_amount)
c2.credit_to(transfer_amount)

c1.display_customer()
print("")
c2.display_customer()
print("\n ------ \n")