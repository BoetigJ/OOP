class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_num = ""
        self.phone = ""
        self.emailID = ""
        self.balance = 0.0
        self.credit_card=[]
        self.debit_card=""

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
        print("The customer's debit card is ", self.debit_card)
        print("The customer's credit cards:")
        for card in self.credit_card:
            print(card)

class Card:
    def __init__(self):
        self.type = ""
        self.card_no=""
        self.cvv=""
        self.expriration_date=""
        self.card_balance=0.0

    def add_values_to_card(self, ty):
        self.type = ty
        self.card_no = input("What is the card number? ")
        self.cvv = input("What is the card's CVV? ")
        self.expriration_date = input("What is the card's expiration date? ")
        self.card_balance = float(input("What is the card's balance? "))

    def debit_from_card(self, debit):
        self.card_balance -= debit

    def credit_to_card(self, credit):
        self.card_balance += credit

    def display_card(self):
        print("This is a ",self.type, " card")
        print("The card number is ",self.card_no)
        print("The card's CVV is ",self.cvv)
        print("The card's expiration date is ",self.expriration_date)
        print("The card's balance is ",self.card_balance)

c1 = Customer()
c2 = Customer()

crd1 = Card()
crd2 = Card()

c1.add_values_to_customer()
print("")
c2.add_values_to_customer()
print("\n ------ \n")

crd1.add_values_to_card("credit")
print("")
crd2.add_values_to_card("debit")

crd1.display_card()
print("")
crd2.display_card()
print("\n ------ \n")

c1.credit_card.append(crd1)
c2.debit_card = crd2
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

import pickle

list_of_customers=[c1,c2]

with open ("lab4.dat", "wb") as file1:
    pickle.dump(list_of_customers, file1)
file1.close()

with open ("lab4.dat", "rb") as file2:
    information = pickle.load(file2)
file2.close()

print(information)