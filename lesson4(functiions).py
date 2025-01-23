# Basic function structure
def calculate_revenue(quantity, price):
    return quantity * price

# More practical example with warehouse data
def calculate_total_value(stock, price):
    """
    Calculate total value of inventory
    stock: number of items
    price: price per item
    """
    total = stock * price
    return total

# Test our functions
test_stock = 50
test_price = 1000

total_value = calculate_total_value(test_stock, test_price)
print(f"Total value: ${total_value}")