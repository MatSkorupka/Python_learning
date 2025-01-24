warehouse = {
    'Electronics': {
        'Laptop': {'stock': 50, 'price': 1000, 'min_stock': 10},
        'Phone': {'stock': 100, 'price': 500, 'min_stock': 20}
    },
    'Accessories': {
        'Case': {'stock': 200, 'price': 20, 'min_stock': 50},
        'Charger': {'stock': 150, 'price': 30, 'min_stock': 40}
    }
}

# Exercise 1: Create function to check stock levels
# Input: warehouse data
# Output: list of items below minimum stock

def is_too_low(a):
    list_too_low = []
    for category in a.keys():
        for item, value in a[category].items():
            if value['stock'] < value['min_stock']:
                list_too_low.append(item)
    return list_too_low
            

result = is_too_low(warehouse)
print(result)

# Exercise 2: Create function to calculate total value
# Input: warehouse data and category
# Output: total value of inventory in that category

def total_value(data, categories):
    total_value = dict.fromkeys(categories, 0)
    for category in categories:  # Only iterate through requested categories
        for item, value in data[category].items():
            total_value[category] += value['stock'] * value['price']
    return total_value

result = total_value(warehouse, ['Electronics', 'Accessories'])
print(result)

# Exercise 3: Create function to find most expensive item
# Input: warehouse data
# Output: item name and price of most expensive product

def find_most_expensive_item(data):
    most_expensive_name = ''
    highest_price = 0
    
    for category in data:
        for item, details in data[category].items():
            if details['price'] > highest_price:
                highest_price = details['price']
                most_expensive_name = item
    
    return most_expensive_name, highest_price


item, price = find_most_expensive_item(warehouse)
print(f"Most expensive item is {item} (${price})")


