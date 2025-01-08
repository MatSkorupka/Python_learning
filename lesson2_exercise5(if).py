# Advanced Dictionary Operations

inventory = {
    "electronics": {
        "laptop": {"price": 1200, "warranty": True, "rating": 4.5},
        "phone": {"price": 800, "warranty": False, "rating": 4.0},
        "tablet": {"price": 300, "warranty": True, "rating": 3.8}
    },
    "accessories": {
        "headphones": {"price": 100, "warranty": False, "rating": 4.2},
        "mouse": {"price": 50, "warranty": False, "rating": 4.7}
    }
}

sales_data = {
    "laptop": [5, 7, 3, 6],
    "phone": [12, 8, 9, 11],
    "tablet": [4, 6, 5, 3],
    "headphones": [8, 9, 7, 8],
    "mouse": [10, 12, 11, 9]
}

# Exercise 1: Category Analysis
# Print products from electronics category with:
# - Price > 500
# - Rating > 4.0

for key, value in inventory['electronics'].items():
    if value['price'] > 0 and value['rating'] > 4.0:
        print(f"{key}: Price={value['price']}, Rating={value['rating']}")

# Exercise 2: Sales Performance
# Calculate and print for each product:
# - Average sales
# - Total sales
# - Best month (highest sales)

for key, value in sales_data.items():
    print(f'Average sale for {key} is: {sum(value)/len(value)}')
    print(f'Sum of sales for {key} is: {sum(value)}')
    print(f'Best month for {key} is: {max(value)}')

# Exercise 3: Warranty Report
# Print all products with warranty and their prices

warranties = {k: v['price'] for category in inventory.values() 
             for k, v in category.items() 
             if v['warranty']}
print(warranties)