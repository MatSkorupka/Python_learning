store_inventory = {
    'Week1': {
        'North': {
            'stock': [100, 150, 80],    # [Coffee, Tea, Snacks]
            'sold': [20, 30, 15]
        },
        'South': {
            'stock': [120, 140, 90],
            'sold': [25, 25, 20]
        }
    },
    'Week2': {
        'North': {
            'stock': [80, 120, 65],
            'sold': [30, 25, 10]
        },
        'South': {
            'stock': [95, 115, 70],
            'sold': [35, 20, 25]
        }
    }
}

items = ['Coffee', 'Tea', 'Snacks']

# store_inventory[week][store]['stock'][item_index]


# Exercise 1: Calculate remaining stock for each item in each store
# Result should show final stock after all weeks

# Initialize a nested dictionary structure:
# {'North': {'Coffee': 0, 'Tea': 0, 'Snacks': 0},
#  'South': {'Coffee': 0, 'Tea': 0, 'Snacks': 0}}
final_stocks = {
    'North': dict.fromkeys(items, 0),
    'South': dict.fromkeys(items, 0)
}

# Go through each store
for store in ['North', 'South']:
    # Go through each item using its index and name
    for item_index, item in enumerate(items):
        # Get the last week (Week2) since we want final stock
        last_week = list(store_inventory.keys())[-1]  # gets 'Week2'
        
        # Get the final stock by subtracting:
        # Final = Last week's stock - Last week's sold
        final_stock = (store_inventory[last_week][store]['stock'][item_index] - 
                      store_inventory[last_week][store]['sold'][item_index])
        
        # Store the result in our final_stocks dictionary
        final_stocks[store][item] = final_stock

print(final_stocks)

# Exercise 2: Find which store sold more of each item across all weeks

final_sales = {
    'North': dict.fromkeys(items, 0),
    'South': dict.fromkeys(items, 0)
}

for week in store_inventory:
    for store in ['North', 'South']:
        for item_index, item in enumerate(items):
            sales = store_inventory[week][store]['sold'][item_index]
            final_sales[store][item] += sales

print(final_sales)

best_store = {}
for item in items:
    if final_sales['North'][item] > final_sales['South'][item]:
        best_store[item] = 'North'
    else:
        best_store[item] = 'South'

print("\nBest selling store for each item:", best_store)


# Exercise 3: Calculate the percentage of stock sold for each item in each store
# Example: If North had 100 Coffee and sold 20, that's 20%

# Initialize dictionary for percentages
sold_percentages = {
    'North': dict.fromkeys(items, 0),
    'South': dict.fromkeys(items, 0)
}

# Calculate for last week
last_week = 'Week2'  # we can hardcode this since we know it's the last week

for store in ['North', 'South']:
    for item_index, item in enumerate(items):
        stock = store_inventory[last_week][store]['stock'][item_index]
        sold = store_inventory[last_week][store]['sold'][item_index]
        
        # Calculate percentage: (sold/stock) * 100
        percentage = (sold / stock) * 100
        sold_percentages[store][item] = percentage

# Print results in a readable format
for store in sold_percentages:
    print(f"\n{store} store:")
    for item in sold_percentages[store]:
        print(f"{item}: {sold_percentages[store][item]:.1f}%")