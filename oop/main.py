from book_class import Book

def main():
    # Creating a book instance
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)

    # Demonstrating the __repr__ method
    print(repr(my_book))

    # Deleting the book instance
    del my_book

if __name__ == "__main__":
    main()