class Book:
    """Base class representing a generic book."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library using composition."""

    def __init__(self):
        self.books = []  # Holds Book, EBook, and PrintBook objects

    def add_book(self, book):
        """Adds a book instance to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Prints the details of all books in the library."""
        for book in self.books:
            print(book)
