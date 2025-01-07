# Dictionary + Conditional Practice

# Given data
products = {
    "laptop": {"price": 1200, "stock": 5},
    "phone": {"price": 800, "stock": 10},
    "tablet": {"price": 300, "stock": 0}
}

customer = {
    "tier": "gold",
    "points": 150,
    "history": ["laptop", "phone"]
}

discounts = {
    "gold": 0.1,    # 10% off
    "silver": 0.05  # 5% off
}

# Exercise 1: Check product availability
# Write code that checks if a product is available (stock > 0)
# Print appropriate message


for key, value in products.items():
    if value['stock'] > 0:
        print(f'{key} is available')



# Exercise 2: Calculate discounted price
# For a given product, apply discount based on customer tier
# Add 5% if customer has > 100 points

selected_product = "laptop"  # Example product

# Get base price
product_price = products[selected_product]["price"]

# Apply tier discount
tier_discount = discounts[customer["tier"]]
final_price = product_price * (1 - tier_discount)

# Apply points discount if eligible
if customer["points"] > 100:
    final_price *= (1 - 0.05)

print(f"Final price for {selected_product}: {final_price}")


# Exercise 3: Purchase eligibility
# Check if customer can buy product based on:
# - Product in stock
# - Price less than 1000 OR customer tier is gold
# - Customer hasn't bought this product before

example_product = 'laptop'

if products[example_product]['stock'] > 0 and (products[example_product]['price'] < 1000  or customer['tier'] == 'gold') and example_product in customer['history']:
    print('You can buy the item')
else:
    print('You can not buy the item')



# 