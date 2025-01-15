store_data = {
    'North': {
        'stock': [100, 150, 80],    # [Coffee, Tea, Snacks]
        'sold': [20, 30, 15]
    },
    'South': {
        'stock': [120, 140, 90],
        'sold': [25, 25, 20]
    }
}

items = ['Coffee', 'Tea', 'Snacks']

# Exercise 1: Total Sales
# Calculate total number of items sold by each store
# Example output: "North sold total of 65 items"

sold_North = sum(store_data['North']['sold'])
sold_South = sum(store_data['South']['sold'])
print(f'North sold total of {sold_North} items')
print(f'South sold total of {sold_South} items')


# Exercise 2: Best Selling Item
# Find which item was sold the most in each store
# Example output: "Best selling item in North was Tea (30 items)"

# Initialize dictionaries outside the loop
max_value_North = {'item': '', 'sales': 0}
max_value_South = {'item': '', 'sales': 0}


for item_index, item in enumerate(items):
    if store_data['North']['sold'][item_index] > max_value_North['sales']:
        max_value_North['sales'] = store_data['North']['sold'][item_index]
        max_value_North['item'] = item
    
    if store_data['South']['sold'][item_index] > max_value_South['sales']:
        max_value_South['sales'] = store_data['South']['sold'][item_index]
        max_value_South['item'] = item

print(f"Best selling item in North was {max_value_North['item']} ({max_value_North['sales']} items)")
print(f"Best selling item in South was {max_value_South['item']} ({max_value_South['sales']} items)")


# Exercise 3: Sales Percentage
# For each item in each store, calculate what percentage was sold
# Example: If North had 100 Coffee and sold 20, that's 20%



percentage_North = dict.fromkeys(items, 0)
percentage_South = dict.fromkeys(items, 0)

for item_index, item in enumerate(items):
    sales_N = store_data['North']['sold'][item_index]
    stock_N = store_data['North']['stock'][item_index]
    percentage_North[item] = (sales_N / stock_N) * 100


    sales_S = store_data['South']['sold'][item_index]
    stock_S = store_data['South']['stock'][item_index]
    percentage_South[item] = (sales_S / stock_S) * 100


for item in items:
    print(f"North sold {percentage_North[item]:.1f}% of {item}")
    print(f"South sold {percentage_South[item]:.1f}% of {item}")