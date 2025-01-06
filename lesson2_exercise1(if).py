# Exercise Set: If/Elif/Else Practice

# Setup some variables for our exercises
price = 800
category = "Premium"
stock = 5
customer_type = "Regular"

# Exercise 1: Basic if/else
# Write code that:
# - If price > 1000, print "Expensive"
# - Otherwise print "Regular price"
if price > 1000:
    print("Expensive")
else:
    print("Regular price")

# Exercise 2: if/elif/else
# Write code that:
# - If price > 1000, print "High price"
# - If price > 500 but ≤ 1000, print "Medium price"
# - Otherwise print "Low price"
if price > 1000:
    print("High price")
elif price > 500 and price <= 1000:
    print("Medium price")
else:
    print("Low price")

# Exercise 3: Multiple conditions using and
# Write code that checks if:
# - Price is more than 500 AND category is "Premium"
# Then print appropriate message
if price > 500 and category == 'Premium':
    print("Great!")

# Exercise 4: Multiple conditions using or
# Write code that checks if:
# - Stock is 0 OR price is more than 1000
# Then print "Need attention"
if stock == 0 or price > 1000:
    print("Need attention")

# Exercise 5: Nested if statements
# Write code that:
# 1. First checks if item is "Premium"
# 2. If it is Premium:
#    - If price > 1000, apply 10% discount
#    - If price ≤ 1000, apply 5% discount
# 3. Print final price
if category == 'Premium':
    if price > 1000:
        final_price = price * 0.9
    else:
        final_price = price * 0.95
    print(final_price)
else:
    print(price)

