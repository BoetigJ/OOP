"""
for number in range (1,2):
    print(number)
    if number%2 == 0:
        print("Even")
    else:
        print("Odd")

n = int(input("What number: "))
x = int(input("What number: "))

for T in range (1, x+1):
    print(T," x ", n, " = ", n*T)

"""


p = int(input("What is the Payment: "))
n = int(input("What is the number of months: "))
R = int(input("What intrest rate: "))

r = R/(12*100)

EMI = p*r*((1+r)**n)/((1+r)**n - 1)

for month in range (1, n+1):
    p = p-EMI
    print(EMI)
    print("EMI:", EMI)
    print("Balance: ", p)
    print(month)
