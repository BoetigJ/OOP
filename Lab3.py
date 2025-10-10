class User():
    def __init__(self):
        self.user_id = ""
        self.user_name = ""
        self.user_password = ""
        self.user_address = ""
        self.user_phone = ""
        self.user_email_id = ""
        self.books_borrowed = []

    def add_user(self):
         self.user_id = input("What is the user's ID? ")
         self.user_name = input("What is the user's name? ")
         self.user_password = input("What is the user's password? ")
         self.user_address = input("What is the user's address? ")
         self.user_phone = input("What is the user's phone number? ")
         self.user_email_id = input("What is the user's email address? ")

    def display_user(self):
        print(self.user_id)
        print(self.user_name)
        print(self.user_password)
        print(self.user_address)
        print(self.user_phone)
        print(self.user_email_id)

    def edit_user(self):
         self.user_id = input("What is the user's ID? ")
         self.user_name = input("What is the user's name? ")
         self.user_password = input("What is the user's password? ")
         self.user_address = input("What is the user's address? ")
         self.user_phone = input("What is the user's phone number? ")
         self.user_email_id = input("What is the user's email address? ")

    def borrow_book(self, book_borrowed):
        self.books_borrowed.append(book_borrowed)
        print(book_borrowed, " is borrowed.")

    def display_borrowed_books(self):
        for book in self.books_borrowed:
            print(book)

    def return_book(self, returned_book):
        self.books_borrowed.remove(returned_book)
        print(returned_book, " is returned.")


class Book():
    def __init__(self):
        self.book_id = ""
        self.book_title =""
        self.book_author_id = ""
        self.book_publisher = ""
        self.book_year_of_publication = ""

    def add_book(self):
        self.book_id = input("What is the book's ID? ")
        self.book_title = input("What is the book's name? ")
        self.book_author_id = input("What is the ID of the author of the book's name? ")
        self.book_publisher = input("What was the book's publisher? ")
        self.book_year_of_publication = input("What year was the book published? ")

    def edit_book(self):
        self.book_id = input("What is the book's ID? ")
        self.book_title = input("What is the book's name? ")
        self.book_author_id = input("What is the author of the book's name? ")
        self.book_publisher = input("What was the book's publisher? ")
        self.book_year_of_publication = input("What year was the book published? ")

    def display_book(self):
        print("The book's ID is ", self.book_id)
        print("The book's title is ", self.book_title)
        print("The author's ID is ", self.book_author_id)
        print("The book's publisher is ", self.book_publisher)
        print("The books was published in ", self.book_year_of_publication)

    
class Author():
    def __init__(self):
        self.author_id = ""
        self.author_name = ""
        self.author_affiliation = ""
        self.author_country = ""
        self.author_phone = ""
        self.author_email_id = ""

    def add_author(self):
        