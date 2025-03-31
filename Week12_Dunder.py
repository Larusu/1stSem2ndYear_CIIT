# Dunder Methods (Double Underscore Methods)

class Book:
    """A class representing a book with title, author, and number of pages."""
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    # One of the examples of dunderer methods
    def __str__(self): 
        """
        Returns a string representation of the Book object.
        This method is called when using str() or print() on an instance.
        It makes the object more readable by displaying the title and author.
        """
        return f"{self.title} by {self.author}"
    
    def __eq__(self, value) -> bool: #eq means equal
        """
        Compares two Book objects to determine equality.
        Two books are considered equal if they have the same title or the same author.
        """
        return self.title == value.title or self.author == value.author

# Creating Book Instances
bookOne = Book("The Hobbit", "J.R.R. Tolkien", 320)
bookTwo = Book("Harry Potter and the Chamber of Secrets", "J.K Rowling", 290)
bookThree = Book("Harry Potter and the Sorcerer's Stone", "J.K Rowling", 305)

print(bookTwo) # triggers the __str__ method
print(bookTwo == bookThree) # Checking equality between bookTwo and bookThree using the __eq__ method
