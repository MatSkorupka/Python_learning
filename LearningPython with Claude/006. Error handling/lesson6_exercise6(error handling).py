class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.on_loan = False  # Add this for loan tracking

    def get_info(self):
        return f'The {self.title} wrote by {self.author} has {self.pages} pages'

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        return f"{book.title} has been added to the library"
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return "Book not found"

class BookLoanError(Exception):
    pass

def loan_book(library, title, days):
    try:
        # Check if days is a valid number
        days = int(days)
        if days <= 0 or days > 30:
            raise ValueError("Days must be between 1 and 30")

        # Check if book exists in library
        book = library.find_book(title)
        if book == "Book not found":
            raise KeyError(f"Book {title} not found in library")
            
        # Check if book is already on loan
        if book.on_loan:
            raise BookLoanError(f"Book {title} is already on loan")
            
        # Process the loan
        book.on_loan = True
        return f"Book {title} loaned for {days} days"
        
    except ValueError as e:
        return f"Invalid loan period: {e}"
    except KeyError as e:
        return f"Book not found: {e}"
    except BookLoanError as e:
        return f"Loan error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

# Test the code
library = Library()
library.add_book(Book("Harry Potter", "J.K. Rowling", 300))

# Test cases
print(loan_book(library, "Harry Potter", 14))      # Should work
print(loan_book(library, "Harry Potter", 14))      # Already on loan
print(loan_book(library, "Lord of Rings", 14))     # Not found
print(loan_book(library, "Harry Potter", -5))      # Invalid days
print(loan_book(library, "Harry Potter", "abc"))   # Invalid input