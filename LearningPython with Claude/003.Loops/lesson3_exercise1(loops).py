# Basic for loop structure
numbers = [1, 2, 3, 4, 5]

# Simple loop through a list
# for number in numbers:
#     print(number)

# Practice Exercise 1:
products = ['Laptop', 'Phone', 'Tablet', 'Watch']
prices = [1200, 800, 300, 250]

# Try to:
# 1. Print each product
for product in products:
    print(product)


# 2. Print each price
for price in prices:
    print(price)


# 3. Print product with its price
for product, price in zip(products, prices):
    print(f'{product}: {price}')

