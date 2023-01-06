class Person:
    # Constructor for Person class
    def __init__(self, name, age):
        self.__name = name # property name of the person
        self.__age = age # property age of the person
    
    # Accessors to get the values of the properties
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age

class BookAuthor(Person):
    # Constructor for BookAuthor class
    def __init__(self, name, age, books):
        Person.__init__(self, name, age) # inherits the properties from Person class
        self.__books = books # property for list of books
    
    # Accessor to get the list of books
    def getBooks(self):
        return self.__books
    
class Book:
    # Constructor for Book class
    def __init__(self, title, stock, price):
        self.__title = title # property title of the book
        self.__stock = stock # property number of books in stock
        self.__price = price # property price of book
    
    # Accessors to get the values of the properties
    def getTitle(self):
        return self.__title
    
    def getStock(self):
        return self.__stock
    
    def getPrice(self):
        return self.__price

# Function to print the values of the BookAuthor
def print_BookAuthor_values(author):
    print("Name: {}".format(author.getName()))
    print("Age: {}".format(author.getAge()))
    for book in author.getBooks(): # looping through the list of books retrieved by the accessor
        print("Book Title: {}".format(book.getTitle()))
        print("Number in Stock: {}".format(book.getStock()))
        print("Price: {}".format(book.getPrice()))

# Creating two book objects
book1 = Book("The Lightning Thief", 10, 6.99)
book2 = Book("The Sea of Monsters", 5, 7.99)

# Creating a BookAuthor object
author = BookAuthor("Rick Riordan", 58, [book1, book2])

# Calling the print_BookAuthor_values function to print out the values
print_BookAuthor_values(author)
