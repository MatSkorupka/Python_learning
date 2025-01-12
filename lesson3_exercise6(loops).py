products = ['Laptop', 'Phone', 'Tablet', 'Watch']
prices = [1200, 800, 300, 250]
categories = ['Premium', 'Standard', 'Budget', 'Budget']

# Exercise 1:
# Create a dictionary where:
# - Categories are keys
# - Values are lists of products in that category
# Example: {'Premium': ['Laptop'], 'Standard': ['Phone'], ...}

dictionary_1 = dict()

for prod, cat in zip(products, categories):
    if cat not in dictionary_1:
        dictionary_1[cat] = []
    dictionary_1[cat].append(prod)

print(dictionary_1)

# Exercise 2:
# Calculate average price for each category
# Print like: "Average price for Premium is 1200"

avg_value = dict()
price_sum = dict()
price_count = dict()

for price, cat in zip(prices, categories):
    if cat not in price_sum:
        price_sum[cat] = 0
        price_count[cat] = 0
    
    price_sum[cat] += price
    price_count[cat] += 1

for cat in price_sum:
    avg_value[cat] = price_sum[cat] / price_count[cat]

print(avg_value)

# Exercise 3:
# Create a dictionary where:
# - Categories are keys
# - Values are dictionaries containing:
#   - count: number of products
#   - total_value: sum of prices
# Example: {'Premium': {'count': 1, 'total_value': 1200}, ...}



result_dict = dict()

for price, cat in zip(prices, categories):
    if cat not in result_dict:
        result_dict[cat] = {'count': 0, 'total_value': 0}
    
    result_dict[cat]['count'] += 1
    result_dict[cat]['total_value'] += price

print(result_dict)
    