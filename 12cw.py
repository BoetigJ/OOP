import pickle

class Product:
    def __init__(self):
        self.pid = ""
        self.pname = ""
        self.price = 0.0
        self.description = ""

    def get_product_details(self):
        self.pid = input("What is the product's ID? ")
        self.pname = input("What is the product's name? ")
        self.price = float(input("What is the product's price? "))
        self.description = input("What description does the product have? ")

    def display_product_info(self):
        print(self.pid)
        print(self.pname)
        print(self.price)
        print(self.description)

while 1:
    option = int(input("Enter your option: "))

    if option == 1:
        product_obj = Product()

    elif option == 2:
        product_obj.get_product_details()

    elif option == 3:
        product_obj.display_product_info()

    elif option == 4:
        f1 = open("product_inventory.dat", "ab")
        pickle.dump(product_obj, f1)
        f1.close()

    elif option == 5:
        f2 = open("product_inventory.dat", "rb")
        while 1:
            try:
                recieved_product = pickle.load(f2)
                recieved_product.display_product_info()
                print("--------")

            except EOFError:
                break
        f2.close()
    elif option == 6:
        break

print("Goodbye! ")



