import sys

"""OOP Challenge: Requirements:
Create a book class with Title, Author, ISBN, Genre, Number of copies available.
Create an author class to represent an author with Aurthor's name, birthdate, nationality.
Library Catalog Class that can store a collection of books - methods should be add, remove, display and search for books based on title, author, genre. 
User interaction."""

#1 - Create a book class

class Book():
    def __init__(self, title, author, isbn, genre, num_copies): #no capilized letters for attributes. INIT should only be called once. 
        self.title = title
        self.author = author 
        self.isbn = isbn
        self.genrer = genre
        self.copies = num_copies
   


#2 - Create an Author Class
class Author():
    def __init__(self, name, birthday,nationality):
        self.name = name
        self.birthday = birthday
        self.nationality = nationality 

#3 - Create a Library Catalog Class

class LibraryCatalog_class(): 

    # initializing the constructor method of LibraryCatalog
    def __init__(self):
        self.books = {} #this is a dict. We need to create a dict before anything else. 


    def add_book(self, book): #Aha! Using book so I don't have to write all the paramethers again, since we already know what they are based on the book class! 
        #because I am using a dict, I need to add keys to it  
        self.books[book.title] = {
            "author": book.author.name,
            "isbn": book.isbn,
            "genre":book.genre,
            "num_copies": book.num_copies
        }

    

    def remove_book(self, title):
        #Removing book based on the title
        for book in self.books:
            if title in self.books: #remember that self.book is a dictionary
                del self.books[title]
                print(f"Book '{title} removed successfully")
            else:
                print(f"Book '{title}' not found.")

            
    def display_all_books(self):
        #learning a new method. the if not!
        if not self.books:
            print("No books available.")
        else:
            print("Books in the catalog: ")
            for title, book_info in self.books.items():
                print(f"Title: {title}")
                print(f"Author: {book_info['author']}")
                print(f"ISBN: {book_info['isbn']}")
                print(f"Genre: {book_info['genre']}")
                print(f"Number of Copies: {book_info['num_copies']}")

    def search_for_books(self):
            #I don't need a for loop here, since I don't really need to loop
            if title in self.books: #I don't know why it is says that title hasnt been defined when we did that all the way back in Books...
                print("Here is your book: {title}")
            else:
                print("This book is not in the catalog")

#I know JOseph said no input. But I can't think of this program without user input or UI. 

class user_menu():
    def __init__(self):
        self.catalog = LibraryCatalog()

    def start(self):
        while True:
            print("Menu: ")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Display all books")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")
            if choice == "1":
                self.add_new_book()#calling the method

            elif choice == "2":
                self.remove_book()
            
            elif choice == "3":
                self.display_all_books
            
            elif choice == "4":
                print(Thank you using this catalog.)
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

    #inputs inputs inputs
    def add_new_book(self):
        title = input("Enter the title: ")
        author_name = input("Enter the author's name: ")
        birthday = input("Enter the author's birthday:")
        nationality = input("Enter the author's nationality: ")
        isbn = input("Enter the ISBN: ")
        genre = input("Enter the genre: ")
        num_copies = input("Enter the number of copies available: ")
        self.catalog.add_book(book)
        print("Book added successfully.")

    def remove_book(self):

        #INCOMPLETE CODE> Waiting for review.  






        

        
        

