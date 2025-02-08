# First, create a logging decorator
def log_operation(func):
    def wrapper(*args, **kwargs):
        print(f"Starting operation: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Operation completed: {func.__name__}")
        return result
    return wrapper

# Use it with our Book class
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @log_operation
    def get_info(self):
        return f'The {self.title} wrote by {self.author} has {self.pages} pages'
    
    @log_operation
    def is_long(self):
        return self.pages > 400

# Test it
book = Book("Harry Potter", "J.K. Rowling", 300)
print(book.get_info())
print(book.is_long())