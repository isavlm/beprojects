"""OOP Challenge: Requirements:
Create a book class with Title, Author, ISBN, Genre, Number of copies available.
Create an author class to represent an author with Aurthor's name, birthdate, nationality.
Library Catalog Class that can store a collection of books - methods should be add, remove, display and search for books based on title, author, genre. 
User interaction."""

#1 - Create a book class

class Book(object):
    def __init__(self, title, author, isbn, genre, copies): #no capilized letters for attributes. INIT should only be called once. 
        self.title = title
        self.author = author 
        self.isbn = isbn
        self.gender = genre
        self.copies = copies
   


#2 - Create an Author Class
class Author(Book):
    def __init__(self, name, birthday,nationality):
        self.name = name
        self.birthday = birthday
        self.nationality = nationality 

#3 - Create a Library Catalog Class

class LibraryCatalog_class(object): #should I have the word object or not? 
    books_count = 0 #I want to start a file or list so we can add the books.
    
    # initializing the consturctor method of LibraryCatalog
    def __init__(self, add, remove, display, search):
        self.add = input('Would you like to add a book? y/n')
        self.title = input("Enter the book's tittle: ")
        self.author = input("Enter the author's name: ")
        Book.books_count = += 1 

        
        


