def generate_inventory():
    """
    Generator that simulates book inventory changes:
    - Starts with initial stock
    - Each day randomly sells 0-5 books
    - Each week (every 7 days) receives new stock (10-20 books)
    - Tracks total books sold and current stock
    """
    current_stock = 100  # Initial stock
    total_sold = 0
    day = 1
   

    while current_stock > 0:  # Infinite generator
        change = random.randint(0, 5)
        current_stock -= change
        total_sold += change
        
        if day%7 == 0:
            current_stock += random.randint(10, 20)
        
        yield {
            'day': day,
            'stock': current_stock,
            'sold_today': change,
            'total_sold': total_sold
        }
        day += 1


    # Your code here:
    # - Use random.randint for sales and restocking
    # - Track day number (for weekly restocking)
    # - Yield dictionary with current status
    # - Continue until stock runs out


inventory = generate_inventory()


for _ in range(10):  # Get first 5 days
    print(next(inventory))


# Should return something like:
# {'day': 1, 'stock': 98, 'sold_today': 2, 'total_sold': 2}
# {'day': 2, 'stock': 95, 'sold_today': 3, 'total_sold': 5}