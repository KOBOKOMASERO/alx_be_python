class Book:
    def __init__(self, title, author, year):
        """Constructor: initializes the book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """Informal string representation"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation (used for debugging)"""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: prints a message when the object is deleted"""
        print(f"Deleting {self.title}")
