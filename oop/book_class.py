# A python script that defines a Book class which uses specific magic methods to enhance functionality. Attributes for the class include title, author and publication year.
class Book:
    '''Book class which uses specific magic methods to enhance functionality. Attributes for the class include title, author and publication year. '''
    def __init__(self, title, author, year):
        """Method to initialize the class
        title is a string containing title of the book.
        author is a string containing name of the author.
        year is an integer containing year the book was published."""
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"