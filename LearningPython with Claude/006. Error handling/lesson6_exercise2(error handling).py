inventory = {
    'Laptop': {'price': 1000, 'stock': 5},
    'Phone': {'price': 500, 'stock': 0},
    'Tablet': {'price': 300, 'stock': '3'},  # Note: stock is a string
    'Watch': None  # Note: no price or stock
}

# Exercise 1: Create a function calculate_item_value() that:
# - Takes item_name as input
# - Returns price * stock
# Handle these potential errors:
# - Item doesn't exist
# - Item data is None
# - Stock is not a number
# - Any other unexpected errors

def calculate_item_value(item_name):
   try:
       if inventory[item_name] is None:
           raise TypeError("Item has no data")
           
       stock = int(inventory[item_name]['stock'])
       price = inventory[item_name]['price']
       
       return price * stock
       
   except KeyError:
       return f"Item {item_name} not found"
   except TypeError as e:
       return str(e)
   except ValueError:
       return "Stock must be a valid number"

# Test cases
print(calculate_item_value('Laptop'))    # Should work
print(calculate_item_value('Camera'))    # KeyError
print(calculate_item_value('Watch'))     # TypeError
print(calculate_item_value('Tablet'))    # Should convert string stock to int



# Exercise 2: Create a function process_order() that:
# - Takes item_name and quantity
# - Checks if enough stock
# - Updates stock if order is possible
# Handle all possible errors

def process_order(item_name, quantity):
   try:
       if inventory[item_name] is None:
           raise TypeError("Item has no data")
           
       # Convert stock to number if needed
       current_stock = int(inventory[item_name]['stock'])
       
       if quantity <= 0:
           raise ValueError("Order quantity must be positive")
           
       if current_stock < quantity:
           raise ValueError(f"Not enough stock. Available: {current_stock}")
           
       inventory[item_name]['stock'] = current_stock - quantity
       return f"Order processed: {quantity} {item_name}(s)"
       
   except KeyError:
       return f"Item {item_name} not found"
   except TypeError as e:
       return str(e)
   except ValueError as e:
       return str(e)


print(process_order('Laptop', 3))    # Should work
print(process_order('Camera', 1))    # Item not found
print(process_order('Watch', 1))     # No data
print(process_order('Laptop', 10))   # Not enough stock
print(process_order('Phone', -1))    # Invalid quantity