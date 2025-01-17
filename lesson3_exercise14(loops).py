warehouse = {
    'Zone A': {
        'items': {
            'Laptop': {'quantity': 50, 'price': 1000, 'reserved': 10},
            'Phone': {'quantity': 100, 'price': 500, 'reserved': 15}
        },
        'temperature': 20,
        'status': 'active'
    },
    'Zone B': {
        'items': {
            'Tablet': {'quantity': 75, 'price': 300, 'reserved': 5},
            'Watch': {'quantity': 150, 'price': 200, 'reserved': 20}
        },
        'temperature': 22,
        'status': 'active'
    }
}

# Exercise 1: Low Stock Alert
# Find items where available stock (quantity - reserved) is less than 50
# Print like: "Low stock alert: Laptop in Zone A (40 available)"

Zone_A = dict()
Zone_B = dict()

for store in warehouse.keys():
    for item, dic in warehouse[store]['items'].items():
        if store == 'Zone A':
            Zone_A[item] = dic['quantity'] - dic['reserved']
        if store == 'Zone B':
            Zone_B[item] = dic['quantity'] - dic['reserved']           

for item, available in Zone_A.items():
    if available < 50:
        print(f"Low stock alert: {item} in Zone A ({available} available)")
for item, available in Zone_B.items():
    if available < 50:
        print(f"Low stock alert: {item} in Zone B ({available} available)")

# Exercise 2: High Value Items
# Find items worth more than $20,000 in total value (quantity * price)
# Print like: "High value item: Laptop in Zone A ($50,000)"

Zone_A = dict()
Zone_B = dict()

for store in warehouse.keys():
    for item, dic in warehouse[store]['items'].items():
        if store == 'Zone A':
            Zone_A[item] = dic['quantity'] * dic['price']
        if store == 'Zone B':
            Zone_B[item] = dic['quantity'] * dic['price']           

for item, value in Zone_A.items():
    if value > 20000:
        print(f"Zone A - {item}: {value} value")
for item, value in Zone_B.items():
    if value > 20000:
        print(f"Zone B - {item}: {value} value")



# Exercise 3: Inventory Status
# For each zone print:
# - Number of different items
# - Total items (sum of quantities)
# - Average price of items

Zone_A = {'nb_of_items': 0, 'sum_of_quantities': 0, 'total_price': 0}
Zone_B = {'nb_of_items': 0, 'sum_of_quantities': 0, 'total_price': 0}

for store in warehouse.keys():
    for item, dic in warehouse[store]['items'].items():
        if store == 'Zone A':
            Zone_A['nb_of_items'] += 1
            Zone_A['sum_of_quantities'] += dic['quantity']
            Zone_A['total_price'] += dic['price']
        if store == 'Zone B':
            Zone_B['nb_of_items'] += 1
            Zone_B['sum_of_quantities'] += dic['quantity']
            Zone_B['total_price'] += dic['price']

avg_price_A = Zone_A['total_price'] / Zone_A['nb_of_items']
avg_price_B = Zone_B['total_price'] / Zone_B['nb_of_items']

print(f"Zone A:")
print(f"- Number of different items: {Zone_A['nb_of_items']}")
print(f"- Total items: {Zone_A['sum_of_quantities']}")
print(f"- Average price: ${avg_price_A:.2f}")

print(f"\nZone B:")
print(f"- Number of different items: {Zone_B['nb_of_items']}")
print(f"- Total items: {Zone_B['sum_of_quantities']}")
print(f"- Average price: ${avg_price_B:.2f}")
