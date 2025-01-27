inventory = {
    'Warehouse_A': {
        'Electronics': {
            'Laptop': {'stock': 50, 'price': 1000, 'min_stock': 10, 'location': 'A1'},
            'Phone': {'stock': 100, 'price': 500, 'min_stock': 20, 'location': 'A2'}
        },
        'capacity': 1000,
        'current_usage': 150
    },
    'Warehouse_B': {
        'Electronics': {
            'Tablet': {'stock': 75, 'price': 300, 'min_stock': 15, 'location': 'B1'},
            'Watch': {'stock': 150, 'price': 200, 'min_stock': 25, 'location': 'B2'}
        },
        'capacity': 800,
        'current_usage': 225
    }
}

# Exercise 1: Create a function that:
# - Takes warehouse name and new item details as parameters
# - Checks if warehouse has enough capacity
# - Returns True/False and remaining capacity

def check_capacity(warehouse_name, new_item_quantity):
    warehouse = inventory[warehouse_name]
    capacity = warehouse['capacity']
    current_usage = warehouse['current_usage']
    remaining = capacity - current_usage
    
    if remaining >= new_item_quantity:
        return True, remaining
    else:
        return False, remaining

test_quantity = 100
has_space, remaining_space = check_capacity('Warehouse_A', test_quantity)

if has_space:
    print(f"Can add item. Remaining space: {remaining_space}")
else:
    print(f"Not enough space. Only {remaining_space} spaces available")


# Exercise 2: Create a function that:
# - Takes warehouse name and category
# - Returns total value and space utilization percentage

def sum_up(warehouse_name, category):
    warehouse = inventory[warehouse_name]

    space_utilization = (warehouse['current_usage'] / warehouse['capacity']) * 100
    
    total_value = 0
    for item, details in warehouse[category].items():
        total_value += details['stock'] * details['price']
    
    return total_value, space_utilization

value, utilization = sum_up('Warehouse_A', 'Electronics')
print(f"Total value: ${value}")
print(f"Space utilization: {utilization:.1f}%")


# Exercise 3: Create a function that:
# - Takes an item name
# - Searches all warehouses for that item
# - Returns warehouse name and location if found

def find_location(item_name):
    for warehouse in inventory:
        for category in inventory[warehouse]:
            if isinstance(inventory[warehouse][category], dict):
                if item_name in inventory[warehouse][category]:
                    location = inventory[warehouse][category][item_name]['location']
                    return warehouse, location
    return None, None

warehouse, location = find_location('Laptop')
if warehouse:
    print(f"Item found in {warehouse} at location {location}")
else:
    print("Item not found")
