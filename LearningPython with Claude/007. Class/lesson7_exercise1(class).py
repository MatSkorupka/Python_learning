# Try creating a class Book with:
# - Attributes: title, author, pages
# - Method: get_info() that returns book details

# Example structure:


# After you create the class, we'll test it like this:
# book1 = Book("Harry Potter", "J.K. Rowling", 300)
# print(book1.get_info())



class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self):
        return f'The {self.title} wrote by {self.author} has {self.pages} pages'
    
    def is_long(self):
        if self.pages > 400:
            return True
        else:
            return False
    
    def how_much_time(self):
        total_minutes = self.pages / 2
        hours = int(total_minutes // 60)  
        minutes = int(total_minutes % 60)  
        return f'The {self.title} will take about {hours} hours and {minutes} minutes to read'
    
    def personalized_reading_time(self, pages_per_minute):
        total_minutes2 = self.pages / pages_per_minute
        hours = int(total_minutes2 // 60)  
        minutes = int(total_minutes2 % 60)  
        return f'The {self.title} will take about {hours} hours and {minutes} minutes to read on your speed'
    
    def get_difficulty(self):
        if self.pages < 200:
            return f'Book is Easy'
        elif self.pages > 400:
            return f'Book is Hard'
        else:
            return f'Book is Medium'
   

    def compare_with(self, other_book):
        page_diff = abs(self.pages - other_book.pages)  # abs for absolute value
        time_diff = abs((self.pages / 2) - (other_book.pages / 2))  # difference in minutes
        
        comparison = {
            'longer_book': self.title if self.pages > other_book.pages else other_book.title,
            'page_difference': page_diff,
            'time_difference_minutes': time_diff
        }
        
        return comparison


    


book1 = Book("Harry Potter", "J.K. Rowling", 300)
book2 = Book("Lord of the Rings", "Tolkien", 500)

print(book1.get_info())
print(f"Is Harry Potter a long book? {book1.is_long()}")
print(f"Is Lord of the Rings a long book? {book2.is_long()}")
print(book1.how_much_time())
print(book2.how_much_time())
print(book1.personalized_reading_time(2))
print(book2.personalized_reading_time(4))
print(book1.get_difficulty())
print(book2.get_difficulty())


# Test it:
print("\nComparison:")
result = book1.compare_with(book2)
print(f"Longer book: {result['longer_book']}")
print(f"Difference in pages: {result['page_difference']}")
print(f"Difference in reading time: {result['time_difference_minutes']} minutes")