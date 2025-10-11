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
        print("Book borrowed successfully!")

    def display_borrowed_books(self):
        for book in self.books_borrowed:
            print(book.book_title)

    def return_book(self, returned_book):
        self.books_borrowed.remove(returned_book)
        print("Book returned successfully!")

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
        self.book_author_id = input("What is the ID of the author of the book's ID? ")
        self.book_publisher = input("What was the book's publisher? ")
        self.book_year_of_publication = input("What year was the book published? ")

    def edit_book(self):
        self.book_id = input("What is the book's ID? ")
        self.book_title = input("What is the book's name? ")
        self.book_author_id = input("What is the author of the book's ID? ")
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
        self.author_id = input("What is the author's ID? ")
        self.author_name = input("What is the author's name? ")
        self.author_affiliation = input("What is the author's affiliation? ")
        self.author_country = input("What is the author's country? ")
        self.author_phone = input("What is the author's phone? ")
        self.author_email_id = input("What is the author's email address? ")

    def display_author(self):
        print("The author's ID is ", self.author_id)
        print("The author's name is ", self.author_name)
        print("The author's affiliation is ", self.author_affiliation)
        print("The author's country is ", self.author_country)
        print("The author's phone is ", self.author_phone)
        print("The author's email id is ", self.author_email_id)

    def edit_author(self):
        self.author_id = input("What is the author's ID? ")
        self.author_name = input("What is the author's name? ")
        self.author_affiliation = input("What is the author's affiliation? ")
        self.author_country = input("What is the author's country? ")
        self.author_phone = input("What is the author's phone? ")
        self.author_email_id = input("What is the author's email address? ")

print("Welcome to the Book App")

book_collection = []
author_collection = []
user_collection = []

while 1:
    print("Main Menu")
    task = input("What do you want to edit? (Book, User, Author) Enter 'Quit' to quit. ")

    if task == "Book":
        while 1:
            book_task = input("What do you want to do? Add, Edit, Display Book, Display all Books, Return to Menu: ")
            if book_task == "Add":
                b = Book()
                b.add_book()
                book_collection.append(b)

            elif book_task == "Edit":
                id = input("What is the book's ID? ")
                for book in book_collection:
                    if id == book.book_id:
                        book.edit_book()
                        break

            elif book_task == "Display all Books":
                for book in book_collection:
                    book.display_book()
                    print("--------------")

            elif book_task == "Display Book":
                id = input("What is the book's ID? ")
                for book in book_collection:
                    if id == book.book_id:
                        book.display_book()
                        break
            elif book_task == "Return to Menu":
                break

    elif task == "User":
        while 1:
            user_task = input("What do you want to do? Add, Edit, Display User, Display all Users, Borrow a Book, Display Borrowed Books, Return to Menu: ")
            if user_task == "Add":
                u = User()
                u.add_user()
                user_collection.append(u)

            elif user_task == "Edit":
                id = input("What is the user's ID? ")
                for user in user_collection:
                    if id == user.user_id:
                        user.edit_user()
                        break

            elif user_task == "Display all Users":
                for user in user_collection:
                    user.display_user()
                    print("--------------")

            elif user_task == "Display User":
                id = input("What is the user's ID? ")
                for user in user_collection:
                    if id == user.user_id:
                        user.display_user()
                        break

            elif user_task == "Borrow a Book":
                id = input("What is the user's ID? ")
                for user in user_collection:
                    if id == user.user_id:
                        bid = input("What is the book's ID? ")
                        for book in book_collection:
                            if book.book_id == bid:
                                user.borrow_book(book)
                                print("yes?")
                                break
                        break

            elif user_task == "Return Book":
                id = input("What is the user's ID? ")
                for user in user_collection:
                    if id == user.user_id:
                        bid = input("What is the book's ID? ")
                        for book in user.books_borrowed:
                            if book.book_id == bid:
                                user.return_book(book)
                                print("yes?")
                                break
                        break

            elif user_task == "Display Borrowed Books":
                id = input("What is the user's ID? ")
                for user in user_collection:
                    if id == user.user_id:
                        user.display_borrowed_books()
                        break

            elif user_task == "Return to Menu":
                break

    elif task == "Author":
        while 1:
            author_task = input("What do you want to do? Add, Edit, Display Author, Display all Authors, Print Author's Book Return to Menu: ")
            if author_task == "Add":
                a = Author()
                a.add_author()
                author_collection.append(a)

            elif author_task == "Edit":
                id = input("What is the author's ID? ")
                for author in author_collection:
                    if id == author.author_id:
                        author.edit_author()
                        break

            elif author_task == "Display all Authors":
                for author in author_collection:
                    author.display_author()
                    print("--------------")

            elif author_task == "Display Author":
                id = input("What is the author's ID? ")
                for author in author_collection:
                    if id == author.author_id:
                        author.display_author()
                        break

            elif author_task == "Print Author's Books":
                aid = input("What is the author's ID? ")
                for book in book_collection:
                    book.display_book()
                    print("--------------")

            elif author_task == "Return to Menu":
                break

    elif task == "Quit":
        break