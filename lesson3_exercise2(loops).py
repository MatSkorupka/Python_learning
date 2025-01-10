products = ['Laptop', 'Phone', 'Tablet', 'Watch']
prices = [1200, 800, 300, 250]
stock = [5, 10, 15, 8]
categories = ['Premium', 'Standard', 'Budget', 'Budget']

# Exercise 1: Enhanced Product Information
# Print each product with its price, stock, and category in a formatted way
# Example output: "Laptop (Premium) - Price: $1200, Stock: 5"

for product, price, st, cat in zip(products, prices, stock, categories):
    print(f'{product} {cat} - Price: {price}, Stock: {st}')


# Exercise 2: Premium Products
# Print only products that are:
# - In Premium category AND price > 1000
# OR
# - Stock > 10

for product, price, st, cat in zip(products, prices, stock, categories):
    if (cat == 'Premium' and price > 1000) or st > 10:
        print(product)

# Exercise 3: Inventory Value
# Calculate and print:
# - Total value of inventory (price * stock) for each product
# - Total value of all inventory combined
total_value_list = []
value = 0

for product, price, st in zip(products, prices, stock):
    print(f'Value of {product} is {price * st}')
    total_value = price * st
    total_value_list.append(total_value)

for i in total_value_list:
    value += i
    
    
print(f'Total value {value}')
