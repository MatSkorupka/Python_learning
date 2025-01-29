inventory = {
    'Laptop': {'price': 1000, 'stock': 5},
    'Phone': {'price': 500, 'stock': 0},
    'Tablet': {'price': 300, 'stock': 3},
    'Watch': {'price': 200, 'stock': 2}
}

# Exercise 1: Create a list of all items that are:
# - In stock (stock > 0)
# - Cost less than 400

item = [key for key, value in inventory.items() if value['price'] < 500 and value['stock'] > 0]

print(item)

# Exercise 2: Create a list of tuples with:
# (item_name, total_value)
# where total_value = price * stock

item_list = [(key, value['price'] * value['stock']) for key, value in inventory.items()]
print(item_list)

# Exercise 3: Create a list of dictionaries with:
# {'item': item_name, 'price': price} 
# but only for items in stock

item_dict = [{'item': key, 'price' : value['price'] } for key, value in inventory.items() if value['stock'] > 0]
print(item_dict)