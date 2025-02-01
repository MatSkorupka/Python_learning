inventory = {
    'Laptop': {'price': 1000, 'stock': 5, 'warranty': '1 year'},
    'Phone': {'price': 500, 'stock': 0, 'warranty': None},
    'Tablet': {'price': 300, 'stock': '3', 'warranty': '6 months'},
    'Watch': None
}

# Exercise 1: Create a function that:
# - Checks item availability
# - Validates warranty
# - Calculates total price with warranty
# Handle all possible errors (nested try/except)

def check_item(item_name):
   try:
       if inventory[item_name] is None:
           raise TypeError("Item has no data")
           
       try:
           warranty = inventory[item_name]['warranty']
           if warranty is None:
               raise ValueError("No warranty available")
               
           price = inventory[item_name]['price']
           stock = int(inventory[item_name]['stock'])
           
           if stock <= 0:
               raise ValueError("Item out of stock")
               
           return {
               'item': item_name,
               'price': price,
               'warranty': warranty,
               'stock': stock
           }
           
       except ValueError as e:
           return str(e)
       except TypeError:
           return "Invalid stock value"
           
   except KeyError:
       return f"Item {item_name} not found"
   except TypeError as e:
       return str(e)

# Test cases
print(check_item('Laptop'))    # Should work
print(check_item('Phone'))     # Out of stock
print(check_item('Watch'))     # No data
print(check_item('Camera'))    # Not found
    
    
# Exercise 2: Create a function that:
# - Processes a list of orders
# - Continues processing if one order fails
# - Returns list of successful and failed orders

def process_orders(order_list):
    successful_orders = []
    failed_orders = []
    
    for order in order_list:
        try:
            item_name = order['item']
            quantity = order['quantity']
            
            if inventory[item_name] is None:
                raise TypeError(f"No data for {item_name}")
                
            stock = int(inventory[item_name]['stock'])
            if stock < quantity:
                raise ValueError(f"Not enough stock for {item_name}")
                
            successful_orders.append({
                'item': item_name,
                'quantity': quantity,
                'status': 'success'
            })
            
        except (KeyError, TypeError, ValueError) as e:
            failed_orders.append({
                'item': item_name,
                'status': 'failed',
                'reason': str(e)
            })
            continue  
            
    return {'successful': successful_orders, 'failed': failed_orders}


test_orders = [
    {'item': 'Laptop', 'quantity': 1},    # Should succeed
    {'item': 'Phone', 'quantity': 1},     # Should fail (out of stock)
    {'item': 'Camera', 'quantity': 1},    # Should fail (doesn't exist)
    {'item': 'Tablet', 'quantity': 2}     # Should succeed
]

result = process_orders(test_orders)
print("\nSuccessful orders:", result['successful'])
print("\nFailed orders:", result['failed'])