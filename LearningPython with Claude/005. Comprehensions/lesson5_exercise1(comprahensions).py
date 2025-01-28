# Regular way with for loop
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num * num)

# Same thing with list comprehension
squared = [num * num for num in numbers]
# Let's practice with some exercises:
prices = [100, 200, 300, 400, 500]
names = ['laptop', 'phone', 'tablet', 'watch']
stock = [5, 0, 3, 0]

# Exercise 1: Create a list of prices with 10% discount
discount = [price * 0.9 for price in prices]
print(discount)

# Exercise 2: Create a list of items that are in stock (stock > 0)
items_in_stock =[nm for nm, st in zip(names, stock) if st > 0 ]
print(items_in_stock)

# Exercise 3: Create a list of tuples with (item, price) but only for items under $400
result = [(name, price) for name, price in zip(names, prices) if price < 400]

print(result)