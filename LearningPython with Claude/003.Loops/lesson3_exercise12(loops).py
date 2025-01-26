store_data = {
    'North': {
        'stock': [100, 150, 80],    # [Coffee, Tea, Snacks]
        'sold': [20, 30, 15],
        'price': [5, 4, 3]          # Added prices
    },
    'South': {
        'stock': [120, 140, 90],
        'sold': [25, 25, 20],
        'price': [5, 4, 3]
    }
}

items = ['Coffee', 'Tea', 'Snacks']

# Exercise 1: Revenue Calculation
# Calculate total revenue for each store
# Remember: revenue = sold * price
# Example output: "North store revenue: $X"

revenue_North = dict.fromkeys(items, 0)
revenue_South = dict.fromkeys(items, 0)

for item_index, item in enumerate(items):
    sale_N = store_data['North']['sold'][item_index]
    price_N = store_data['North']['price'][item_index]
    revenue_North[item] = sale_N * price_N

for item_index, item in enumerate(items):
    sale_S = store_data['South']['sold'][item_index]
    price_S = store_data['South']['price'][item_index]
    revenue_South[item] = sale_S * price_S


total_revenue_North = sum(revenue_North.values())
total_revenue_South = sum(revenue_South.values())


print(f'North store revenue: ${total_revenue_North}')
print(f'South store revenue: ${total_revenue_South}')
print('\nRevenue breakdown:')
print(f'North: {revenue_North}')
print(f'South: {revenue_South}')


# Exercise 2: Most Profitable Item
# Find which item generated the most revenue in each store
# Example: "Most profitable item in North was X ($Y revenue)"

North = dict.fromkeys(items, 0)
South = dict.fromkeys(items, 0)

for item_index, item in enumerate(items):
    sale_N = store_data['North']['sold'][item_index]
    price_N = store_data['North']['price'][item_index]
    North[item] = sale_N * price_N

for item_index, item in enumerate(items):
    sale_S = store_data['South']['sold'][item_index]
    price_S = store_data['South']['price'][item_index]
    South[item] = sale_S * price_S


print("North store revenues:", North)
print("South store revenues:", South)

most_profitable_N = max(North, key=North.get)
most_profitable_S = max(South, key=South.get)

print(f'Most profitable item in North was {most_profitable_N} (${North[most_profitable_N]} revenue)')
print(f'Most profitable item in South was {most_profitable_S} (${South[most_profitable_S]} revenue)')

# Exercise 3: Stock Value
# Calculate the value of remaining stock in each store
# Remember: value = remaining_stock * price


North = dict.fromkeys(items, 0)
South = dict.fromkeys(items, 0)

for item_index, item in enumerate(items):
    sale_N = store_data['North']['sold'][item_index]
    price_N = store_data['North']['price'][item_index]
    stock_N = store_data['North']['stock'][item_index]
    North[item] = (stock_N - sale_N) * price_N

for item_index, item in enumerate(items):
    sale_S = store_data['South']['sold'][item_index]
    price_S = store_data['South']['price'][item_index]
    stock_S = store_data['South']['stock'][item_index]
    South[item] = (stock_S - sale_S) * price_S

print(f'Stock value on North is {North}')
print(f'Stock value on South is {South}')

