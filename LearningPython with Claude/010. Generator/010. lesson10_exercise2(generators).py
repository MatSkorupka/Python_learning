import random

def generate_book_sales():
    """
    Generator that simulates daily book sales:
    - Starts with base sales
    - Each day changes by random amount
    - Also tracks total sales
    """
    daily_sales = 100  # Starting sales
    total_sales = 0
    day = 1
    
    while True:  # Infinite generator
        change = random.randint(-20, 20)
        daily_sales += change
        total_sales += daily_sales
        
        yield {
            'day': day,
            'sales': daily_sales,
            'change': change,
            'total': total_sales
        }
        day += 1

# Use it:
sales_gen = generate_book_sales()
for _ in range(5):  # Get first 5 days
    print(next(sales_gen))