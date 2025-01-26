# Simple inventory exercise
products = ['Laptop', 'Phone', 'Tablet']
prices = [1200, 800, 300]
stock = [5, 10, 15]

# Exercise 1:
# Print each product with its price
# Example output: "Laptop costs 1200"

for product, price in zip(products, prices):
    print(f'{product} costs {price}')

# Exercise 2:
# Print only products that:
# - Cost less than 1000
# - Have more than 7 items in stock

for product, price, st in zip(products, prices, stock):
    if price < 1000 and st > 7:
        print(f'{product} costs {price}')

# Exercise 3:
# Create a simple dictionary where:
# - Products are keys
# - Prices are values

product_dict = dict()

for product, price in zip(products, prices):
    if product not in product_dict.keys():
        product_dict[product] = price

print(product_dict)