# Complex Data Structures Exercise

# Store data
stores = {
    'north': {
        'products': ['Laptop', 'Phone'],
        'prices': [1200, 800],
        'stock': [5, 10]
    },
    'south': {
        'products': ['Tablet', 'Watch'],
        'prices': [300, 250],
        'stock': [15, 8]
    }
}

# Customer data
customers = [
    ('John', ['Laptop', 'Phone'], 'Premium'),
    ('Alice', ['Watch'], 'Standard'),
    ('Bob', ['Tablet', 'Watch'], 'Budget')
]

# Discount rules
discount_rules = {
    'Premium': {'base': 0.1, 'multiple_items': 0.05},  # 10% base + 5% for multiple items
    'Standard': {'base': 0.05, 'multiple_items': 0.02},  # 5% base + 2% for multiple items
    'Budget': {'base': 0.02, 'multiple_items': 0.01}    # 2% base + 1% for multiple items
}

# Exercise 1: Store Analysis
# For each store:
# - Total value of inventory (price * stock)
# - Most expensive product
# - Average price of products

total_value = dict()
max_value = dict()
avg_value = dict()

for store_name, store_data in stores.items():
    prices = store_data['prices']
    stock = store_data['stock']
    
    # Calculate average - just once per store
    avg_value[store_name] = sum(prices) / len(prices)
    
    # Calculate max price - using max() function
    max_value[store_name] = max(prices)
    
    # Calculate total inventory value
    total_value[store_name] = 0  # Initialize
    for price, st in zip(prices, stock):
        total_value[store_name] += price * st

# Print results in a formatted way
for store in stores:
    print(f"\nStore: {store}")
    print(f"Total inventory value: {total_value[store]}")
    print(f"Most expensive product: {max_value[store]}")
    print(f"Average price: {avg_value[store]}")



# Exercise 2: Customer Orders
# For each customer:
# - Calculate total price of their products
# - Apply appropriate discounts
# - Print final price after all discounts


for customer_name, products, tier in customers:
    # Initialize total price
    total_price = 0
    
    # Find prices for products
    for store_data in stores.values():
        for product in products:
            if product in store_data['products']:
                # Get the price
                product_index = store_data['products'].index(product)
                total_price += store_data['prices'][product_index]
    
    # Apply discounts
    basic_discount = discount_rules[tier]['base']
    if len(products) > 1:
        total_discount = basic_discount + discount_rules[tier]['multiple_items']
    else:
        total_discount = basic_discount
        
    final_price = total_price * (1 - total_discount)
    
    # Print results
    print(f"\nCustomer: {customer_name}")
    print(f"Total price before discount: {total_price}")
    print(f"Final price after discount: {final_price}")


# Exercise 3: Combined Report
# Create a summary showing:
# - Which store can fulfill each customer's order
# - Total revenue if all customers bought from each store


for customer_name, customer_products, tier in customers:
    print(f"\nCustomer: {customer_name}")
    print("Can be fulfilled by:")
    
    # Check each store if they have all products
    for store_name, store_data in stores.items():
        can_fulfill = True
        total_cost = 0
        
        # Check if store has all products customer wants
        for product in customer_products:
            if product not in store_data['products']:
                can_fulfill = False
                break
                
        if can_fulfill:
            print(f"- {store_name} store")
            
            # Calculate total cost for this customer at this store
            for product in customer_products:
                product_index = store_data['products'].index(product)
                total_cost += store_data['prices'][product_index]
                
            # Apply discounts
            discount = discount_rules[tier]['base']
            if len(customer_products) > 1:
                discount += discount_rules[tier]['multiple_items']
                
            final_cost = total_cost * (1 - discount)
            print(f"  Total cost would be: {final_cost}")