class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f'The {self.title} wrote by {self.author} has {self.pages} pages'
    
    def is_long(self):
        return self.pages > 400
    
    def how_much_time(self):
        total_minutes = self.pages / 2
        hours = int(total_minutes // 60)  
        minutes = int(total_minutes % 60)  
        return f'The {self.title} will take about {hours} hours and {minutes} minutes to read'
    
    def get_difficulty(self):
        if self.pages < 200:
            return "Book is Easy"
        elif self.pages > 400:
            return "Book is Hard"
        return "Book is Medium"

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
    
    def get_all_books(self):
        return [book.title for book in self.books]

    def find_by_author(self, author_name):
        matching_books = []
        for book in self.books:
            if book.author == author_name:
                matching_books.append(book.title)
        return matching_books if matching_books else "No books found by this author"

    def find_by_difficulty(self, difficulty):
        matching_books = []
        for book in self.books:
            if book.get_difficulty() == f"Book is {difficulty}":
                matching_books.append(book.title)
        return matching_books if matching_books else f"No {difficulty} books found"

    def total_reading_time(self):
        total_minutes = sum(book.pages / 2 for book in self.books)
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        return f"Total reading time: {hours} hours and {minutes} minutes"

# Test
library = Library()
library.add_book(Book("Harry Potter", "J.K. Rowling", 300))
library.add_book(Book("Chamber of Secrets", "J.K. Rowling", 350))
library.add_book(Book("Lord of the Rings", "Tolkien", 500))

print(library.total_reading_time())
print(library.find_by_author("J.K. Rowling"))
print(library.find_by_difficulty("Medium"))