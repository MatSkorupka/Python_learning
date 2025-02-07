import pandas as pd

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, this is a text file')

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)



def save_book(book):
    # Write book info in format: title,author,pages
    with open('books.txt', 'a') as file:  # 'a' for append mode
        book_info = f"{book.title},{book.author},{book.pages}\n"
        file.write(book_info)

def read_books():
    books = []
    with open('books.txt', 'r') as file:
        for line in file:
            # Split line into title, author, pages
            title, author, pages = line.strip().split(',')
            # Create new Book object
            book = Book(title, author, int(pages))
            books.append(book)
    return books

# Test
book1 = Book("Harry Potter", "J.K. Rowling", 300)
book2 = Book("Lord of the Rings", "Tolkien", 500)

# Save books
save_book(book1)
save_book(book2)

# Read books
loaded_books = read_books()
for book in loaded_books:
    print(book.get_info())