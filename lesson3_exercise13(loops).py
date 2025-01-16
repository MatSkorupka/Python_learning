# Warehouse inventory data
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

# Exercise 1: Available Stock
# Calculate available quantity (quantity - reserved) for each item in each zone
# Print like: "Zone A - Laptop: 40 available"

Zone_A = dict()
Zone_B = dict()

for store in warehouse.keys():
    for item, dic in warehouse[store]['items'].items():
        if store == 'Zone A':
            Zone_A[item] = dic['quantity'] - dic['reserved']
        if store == 'Zone B':
            Zone_B[item] = dic['quantity'] - dic['reserved']           

for item, available in Zone_A.items():
    print(f"Zone A - {item}: {available} available")
for item, available in Zone_B.items():
    print(f"Zone B - {item}: {available} available")



# Exercise 2: Zone Value
# Calculate total value of available items in each zone
# Remember: value = available_quantity * price

Zone_A = dict()
Zone_B = dict()

for store in warehouse.keys():
    for item, dic in warehouse[store]['items'].items():
        if store == 'Zone A':
            Zone_A[item] = (dic['quantity'] - dic['reserved']) * dic['price']
        if store == 'Zone B':
            Zone_B[item] = (dic['quantity'] - dic['reserved']) * dic['price']           

for item, available in Zone_A.items():
    print(f"Zone A - {item}: {available} value")
for item, available in Zone_B.items():
    print(f"Zone B - {item}: {available} value")

total_value_A = sum(Zone_A.values())
total_value_B = sum(Zone_B.values())

print("Item values:")
for item, value in Zone_A.items():
    print(f"Zone A - {item}: ${value}")
for item, value in Zone_B.items():
    print(f"Zone B - {item}: ${value}")

print(f"\nTotal Values:")
print(f"Zone A total value: ${total_value_A}")
print(f"Zone B total value: ${total_value_B}")

# Exercise 3: Reservation Percentage
# For each item, calculate what percentage is reserved
# Example: if 10 reserved out of 50 total, that's 20%

Zone_A = dict()
Zone_B = dict()

for store in warehouse.keys():
    for item, dic in warehouse[store]['items'].items():
        if store == 'Zone A':
            Zone_A[item] = (dic['reserved'] / dic['quantity']) * 100
        if store == 'Zone B':
            Zone_B[item] = (dic['reserved'] / dic['quantity']) * 100


for item, percentage in Zone_A.items():
    print(f"Zone A - {item}: {percentage:.1f}% reserved")
for item, percentage in Zone_B.items():
    print(f"Zone B - {item}: {percentage:.1f}% reserved")