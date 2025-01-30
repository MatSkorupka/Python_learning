inventory = {
    'Laptop': {'price': 1000, 'stock': 5},
    'Phone': {'price': 500, 'stock': 0},
    'Tablet': {'price': 300, 'stock': 3}
}

# Exercise 1: Create a function that safely divides stock value by price
# Handle potential division by zero and missing keys

def divide(item):
    try:
        return inventory[item]['price'] / inventory[item]['stock']
    except KeyError:
        return f"Item {item} not found in inventory"
    except ZeroDivisionError:
        return f'Cannot division by 0'

result = divide('Phone')
print(result)

# Exercise 2: Create a function that safely updates item stock
# Handle cases where:
# - Item doesn't exist
# - New stock value is not a number
# - New stock value is negative

def update_stock(item, new_stock):
    try:
        # Check if new_stock is negative
        if new_stock < 0:
            raise ValueError
            
        # Try to update the stock
        inventory[item]['stock'] = new_stock
        return f"Stock updated for {item}: {new_stock}"
        
    except KeyError:
        return f"Item {item} not found in inventory"
    except TypeError:
        return "Stock value must be a number"
    except ValueError:
        return "Stock value cannot be negative"

# Test cases
print(update_stock('Laptop', 10))       # Should work
print(update_stock('Camera', 5))        # KeyError (item doesn't exist)
print(update_stock('Phone', 'ten'))     # TypeError (not a number)
print(update_stock('Tablet', -3))       # ValueError (negative number)


