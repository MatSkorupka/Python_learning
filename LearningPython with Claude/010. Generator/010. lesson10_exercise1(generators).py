# Exercise 1: Create a generator that yields book titles
def book_titles():
    books = ["Harry Potter", "Lord of the Rings", "The Hobbit", "Dune"]
    for book in books:
        yield book


# Example usage:
titles = book_titles()
print(next(titles))  # "Harry Potter"
print(next(titles))  # "Lord of the Rings"

# Exercise 2: Create a generator that yields book details
def book_details():
    books = [
        {"title": "Harry Potter", "pages": 300},
        {"title": "Lord of the Rings", "pages": 500},
        {"title": "The Hobbit", "pages": 400}
    ]
    for book in books:
        yield f"{book['title']} - {book['pages']} pages"


titles2 = book_details()
print(next(titles2))  # "Harry Potter"
print(next(titles2))  # "Lord of the Rings"