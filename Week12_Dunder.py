# Dunder Methods

class Book:
    """hello"""
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self): # explain why use __Str__
        return f"{self.title} by {self.author}"
    
    def __eq__(self, value) -> bool: #eq means equal
        return self.title == value.title or self.author == value.author

bookOne = Book("The Hobbit", "J.R.R. Tolkien", 320)
bookTwo = Book("Harry Potter and the Chamber of Secretrs", "J.K Rowling", 290)
bookThree = Book("Harry Potter and the Sorcerer's Stone", "J.K Rowling", 305)

print(bookTwo)
print(bookTwo == bookThree)