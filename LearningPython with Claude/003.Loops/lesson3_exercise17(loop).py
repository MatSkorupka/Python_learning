warehouse = {
    'Zone A': {
        'items': {
            'Laptop': {'quantity': 50, 'price': 1000, 'min_stock': 20, 'max_stock': 100, 'category': 'Electronics'},
            'Phone': {'quantity': 100, 'price': 500, 'min_stock': 30, 'max_stock': 150, 'category': 'Electronics'}
        }
    },
    'Zone B': {
        'items': {
            'Tablet': {'quantity': 75, 'price': 300, 'min_stock': 25, 'max_stock': 120, 'category': 'Electronics'},
            'Watch': {'quantity': 150, 'price': 200, 'min_stock': 50, 'max_stock': 200, 'category': 'Accessories'}
        }
    }
}

# Exercise 1: Category Analysis
# Let's break it into steps:
# 1. Create a dictionary for categories
categories = {'Electronics': {'total_items': 0, 'total_value': 0}, 
              'Accessories': {'total_items': 0, 'total_value': 0}}

for store in warehouse.keys():
    for item, details in warehouse[store]['items'].items():
        cat = details['category']
        # Add to total items for this category
        categories[cat]['total_items'] += details['quantity']
        # Add to total value (quantity * price)
        categories[cat]['total_value'] += details['quantity'] * details['price']

# Print results
for category, data in categories.items():
    print(f"\n{category}:")
    print(f"Total items: {data['total_items']}")
    print(f"Total value: ${data['total_value']}")


# Exercise 2: Stock Efficiency
# For each zone calculate storage efficiency:
# - Current storage use (current quantity / max_stock) as percentage
# - Print which zone is using space more efficiently


# We'll need to:
# 1. Sum up all current quantities in each zone
# 2. Sum up all maximum capacities in each zone
# 3. Calculate efficiency percentage
# 4. Compare which zone is more efficient

quantity = {'Zone A' : 0, 'Zone B' : 0}
capacity = {'Zone A' : 0, 'Zone B' : 0}

efficiency = {'Zone A' : 0, 'Zone B' : 0}


for store in warehouse.keys():
    for item, details in warehouse[store]['items'].items():
        quantity[store] += details['quantity']
        capacity[store] += details['max_stock']

efficiency['Zone A'] = quantity['Zone A'] / capacity['Zone A'] * 100
efficiency['Zone B'] = quantity['Zone B'] / capacity['Zone B'] * 100

print(f"Zone A efficiency: {efficiency['Zone A']:.1f}%")
print(f"Zone B efficiency: {efficiency['Zone B']:.1f}%")

if efficiency['Zone A'] > efficiency['Zone B']:
    print("Zone A is more efficient")
else:
    print("Zone B is more efficient")



# Exercise 3: Value Density
# Calculate value per item in each zone:
# - Total value / Total quantity
# Print which zone has higher value density

value = {'Zone A': 0, 'Zone B': 0}
quantity = {'Zone A': 0, 'Zone B': 0}
density = {'Zone A': 0, 'Zone B': 0}

# Now you need to:
# 1. Calculate total value (quantity * price) for each zone
# 2. Get total quantity for each zone
# 3. Calculate density (value/quantity)

for store in warehouse.keys():
    for item, details in warehouse[store]['items'].items():
        quantity[store] += details['quantity']
        value[store] += details['quantity'] * details['price']
        density[store] = value[store] / quantity[store]


print(f"Zone A value density: ${density['Zone A']:.2f} per item")
print(f"Zone B value density: ${density['Zone B']:.2f} per item")

if density['Zone A'] > density['Zone B']:
    print("Zone A has higher value density")
else:
    print("Zone B has higher value density")