
warehouse = {
    'Electronics': {
        'Laptop': {'stock': 50, 'price': 1000, 'min_stock': 10, 'sales': 20},
        'Phone': {'stock': 100, 'price': 500, 'min_stock': 20, 'sales': 45}
    },
    'Accessories': {
        'Case': {'stock': 200, 'price': 20, 'min_stock': 50, 'sales': 100},
        'Charger': {'stock': 150, 'price': 30, 'min_stock': 40, 'sales': 80}
    }
}

# Exercise 1: Create two functions
# 1. Function to get category statistics (reuse your previous function)
# 2. Function that compares two categories and returns which is performing better
#    (based on total sales value - sales * price)

def get_category_performance(data, category):
    total_value = 0
    for item, details in data[category].items():
        total_value += details['sales'] * details['price']
    return total_value

def compare_categories(data, cat1, cat2):
    perf1 = get_category_performance(data, cat1)
    perf2 = get_category_performance(data, cat2)
    
    if perf1 > perf2:
        return f"{cat1} performs better (${perf1} vs ${perf2})"
    else:
        return f"{cat2} performs better (${perf2} vs ${perf1})"

# Test
result = compare_categories(warehouse, 'Electronics', 'Accessories')
print(result)


# Exercise 2: Create two functions
# 1. Function to check if item needs restocking
# 2. Function that uses first function to create restock report for all categories

def is_restock_needed(data):
    restock_needed = []
    for key in data.keys():
        for item, value in data[key].items():
            if value['stock'] < value['min_stock']:
                restock_needed.append(item)  # Fixed typo: apeend -> append
    return restock_needed

def create_restock_report(data):
    items = is_restock_needed(data)
    for item in items:
        for cat in data:
            if item in data[cat]:
                current = data[cat][item]['stock']
                minimum = data[cat][item]['min_stock']
                print(f"Restock needed: {item} in {cat} (Current: {current}, Minimum: {minimum})")

result = create_restock_report(warehouse)
print(result)

