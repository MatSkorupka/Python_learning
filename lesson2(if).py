# 1. If/Else statements
price = 100

if price > 1000:
    print("This is expensive")
elif price > 500:
    print("This is moderate")
else:
    print("This is cheap")

# 2. For loops
products = ['Laptop', 'Phone', 'Tablet', 'Watch']
for product in products:
    print(f"Product: {product}")

# 3. While loops
stock = 5
while stock > 0:
    print(f"Items in stock: {stock}")
    stock -= 1  # same as: stock = stock - 1