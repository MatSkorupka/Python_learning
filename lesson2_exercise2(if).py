# Advanced Conditional Exercises

product = "Laptop"
price = 1200
stock = 5
category = "Premium"
warranty = True
customer_points = 150

# Exercise 1: Multiple nested conditions
# Calculate final price with these rules:
# - Premium products get 10% discount
# - If customer has > 100 points, additional 5% off
# - If warranty included, add 100 to price
# - If stock < 3, add 50 rush fee
# Print final price

discount_category = 0.1
discount_points = 0.05
add_price = 100
add_price_stock = 50
final_price = price

# Apply discounts
if category == 'Premium':
    final_price = final_price * (1 - discount_category)  # Apply 10% discount

if customer_points > 100:
    final_price = final_price * (1 - discount_points)    # Apply additional 5%

# Add fees
if warranty:
    final_price = final_price + add_price               # Add warranty cost

if stock < 3:
    final_price = final_price + add_price_stock         # Add rush fee

print(final_price)



# Exercise 2: Complex eligibility check
# Check if product is eligible for express shipping:
# - Must be Premium category
# - Price must be > 1000
# - Stock must be > 0
# - No warranty items
# Print "Express eligible" or "Not eligible"

if category =='Premium' and price > 1000 and stock > 0 and warranty == False:
    print("Express eligible")
else:
    print("Not eligible")



# Exercise 3: Price tier with multiple conditions
# Determine price tier with these rules:
# - "Luxury": Premium + price > 1000 + warranty
# - "High": Premium + price > 1000 OR any product > 2000
# - "Medium": price 500-1000 OR Premium products < 500
# - "Basic": everything else
# Print the tier

if category == 'Premium' and price > 1000 and warranty == True:
    print('Luxury')
elif (category == 'Premium' and price > 1000) or price > 2000:
    print('High')
elif (price > 500 and price  <= 1000) or (category == 'Premium' and price < 500):
    print('Medium')
else:
    print('Basic')