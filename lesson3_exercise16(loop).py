store_data = {
    'Electronics': {
        'Laptop': {'stock': 50, 'price': 1000},
        'Phone': {'stock': 100, 'price': 500}
    },
    'Accessories': {
        'Case': {'stock': 200, 'price': 20},
        'Charger': {'stock': 150, 'price': 30}
    }
}

# Exercise 1: Calculate for each category (Electronics and Accessories):
# - Total number of items in stock
# - Total value (stock * price)

# Initialize dictionaries with starting values for each category
total_nb = {'Electronics': 0, 'Accessories': 0}
total_vl = {'Electronics': 0, 'Accessories': 0}

for cat, value in store_data.items():
    for item, v in value.items():
        total_nb[cat] += v['stock']
        total_vl[cat] += v['stock'] * v['price']  

print("Total items in each category:", total_nb)
print("Total value in each category:", total_vl)

# Exercise 2: Print which category has more total items

# First part - your code to calculate totals
total_nb = {'Electronics': 0, 'Accessories': 0}

for cat, value in store_data.items():
    for item, v in value.items():
        total_nb[cat] += v['stock']

# Now compare totals
if total_nb['Electronics'] > total_nb['Accessories']:
    print(f"Electronics has more items: {total_nb['Electronics']}")
else:
    print(f"Accessories has more items: {total_nb['Accessories']}")

print(f"\nFull breakdown:")
print(f"Electronics: {total_nb['Electronics']} items")
print(f"Accessories: {total_nb['Accessories']} items")




# Exercise 3: Print which category has higher total value

total_value = {'Electronics': 0, 'Accessories': 0}

for cat, value in store_data.items():
    for item, v in value.items():
        total_value[cat] += v['stock'] * v['price']

# Compare values
if total_value['Electronics'] > total_value['Accessories']:
    print(f"Electronics has higher value: ${total_value['Electronics']}")
else:
    print(f"Accessories has higher value: ${total_value['Accessories']}")

print(f"\nFull breakdown:")
print(f"Electronics: ${total_value['Electronics']}")
print(f"Accessories: ${total_value['Accessories']}")

