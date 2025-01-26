# Simple store data
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

# Exercise 1:
# Print how much of each item was sold in North store
# Example output: "North sold 20 Coffee"

for item_index, item in enumerate(items):
    soldn = store_data['North']['sold'][item_index]
    solds = store_data['South']['sold'][item_index]
    print(f"North sold {soldn} {item}")
    print(f"South sold {solds} {item}")


# Exercise 2:
# Calculate remaining stock for each item in South store
# Example: If stock was 120 and sold 25, remaining is 95

for item_index, item in enumerate(items):
    stock = store_data['South']['stock'][item_index] - store_data['South']['sold'][item_index]
    print(f'Stock for {item} in South store is {stock}')

# Exercise 3:
# Print which store sold more Coffee

for item_index, item in enumerate(items):
    if item =='Coffee':
        soldn = store_data['North']['sold'][item_index]
        solds = store_data['South']['sold'][item_index]
        if soldn > solds:
            print(f'North store sold more coffee {soldn}')
        elif soldn < solds:
            print(f'South store sold more coffee {soldn}')
        else:
            print(f'Both stores sold the same amount of coffee')

