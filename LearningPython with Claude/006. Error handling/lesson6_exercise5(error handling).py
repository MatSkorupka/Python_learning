def process_book_data(title, author, pages):
    try:
        # Check if title and author are strings
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not isinstance(author, str):
            raise TypeError("Author must be a string")
            
        # Convert pages to int and check if positive
        pages = int(pages)
        if pages <= 0:
            raise ValueError("Pages must be a positive number")
            
        # Create and return book object
        return Book(title, author, pages)
        
    except ValueError as e:
        return f"Invalid number: {e}"
    except TypeError as e:
        return f"Invalid data type: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"

# Test cases
print(process_book_data("Harry Potter", "J.K. Rowling", "abc"))  # ValueError
print(process_book_data(123, "J.K. Rowling", 300))              # TypeError
print(process_book_data("Harry Potter", "J.K. Rowling", -100))  # ValueError
print(process_book_data("Harry Potter", "J.K. Rowling", 300))   # Should work