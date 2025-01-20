warehouse = {
    'Zone A': {
        'items': {
            'Laptop': {'quantity': 50, 'price': 1000, 'min_stock': 20, 'max_stock': 100, 'category': 'Electronics'},
            'Phone': {'quantity': 100, 'price': 500, 'min_stock': 30, 'max_stock': 150, 'category': 'Electronics'}
        }
    },
    'Zone B': {
        'items': {
            'Tablet': {'quantity': 75, 'price': 300, 'min_stock': 25, 'max_stock': 120, 'category': 'Electronics'},
            'Watch': {'quantity': 150, 'price': 200, 'min_stock': 50, 'max_stock': 200, 'category': 'Accessories'}
        }
    }
}

# Exercise 1: Category Analysis
# Let's break it into steps:
# 1. Create a dictionary for categories
categories = {'Electronics': {'total_items': 0, 'total_value': 0}, 
              'Accessories': {'total_items': 0, 'total_value': 0}}

for store in warehouse.keys():
    for item, details in warehouse[store]['items'].items():
        cat = details['category']
        # Add to total items for this category
        categories[cat]['total_items'] += details['quantity']
        # Add to total value (quantity * price)
        categories[cat]['total_value'] += details['quantity'] * details['price']

# Print results
for category, data in categories.items():
    print(f"\n{category}:")
    print(f"Total items: {data['total_items']}")
    print(f"Total value: ${data['total_value']}")


