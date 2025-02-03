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

library = Library()
book1 = Book("Harry Potter", "J.K. Rowling", 300)
book2 = Book("Lord of the Rings", "Tolkien", 500)

library.add_book(book1)
library.add_book(book2)

print(library.get_all_books())
print(library.find_book("Harry Potter").get_info())


# Method to find all books by an author
# Method to find all books of a certain difficulty
# Method to get total reading time for all books



