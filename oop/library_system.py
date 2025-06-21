# Objective: this script aims to deepen knowledge of ionheritance and composition by creating a system that models a library with different types of books.
# Create a base class Book and two child Ebook anf PrintBook.
# A library class to demonstrate composition by managing collection of books.
class Book:
    ''' Base class for the library system.
    title: string containing book title.
    author: string containing'''
    def __init__(self, title, author):
        """Method to initialize book attributes"""
        self.title = title
        self.author = author
    
class EBook(Book):
    ''' child class to book class'''
    def __init__(self, title, author, file_size):
        self.file_size = file_size
        super().__init__(title, author)
    
class PrintBook(Book):
    ''' Another child class that inherits from book class '''
    def __init__(self, title, author, page_count):
        self.page_count = page_count
        super().__init__(title, author)

class Library:
    ''' Class that demonstrates composition'''
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        '''Method that adds a Book, EBook or PrintBook to the library'''
        self.books.append(book)
    
    def list_books(self):
        '''Method that prints details of each book in the library'''
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                if isinstance(book, EBook):
                    print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
                elif isinstance(book, PrintBook):
                    print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
                else:
                    print(f"Book: {book.title} by {book.author}")
    
    
