# Given data
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

# Exercise 1: Create function to calculate profit margin
# Input: category and item name
# Output: profit margin as percentage (assume cost is 70% of price)

def margin(cat, item):
    cost = warehouse[cat][item]['price'] * 0.7
    revenue = warehouse[cat][item]['price']
    profit = revenue - cost
    margin = (profit / revenue) * 100
    return margin

#test
result = margin('Electronics', 'Laptop')
print(result)

# Exercise 2: Create function to find best selling item
# Input: warehouse data
# Output: item name and number of sales

def best_selling(data):
    best_item = ''
    highest_sales = 0
    
    for sector in data:
        for item, value in data[sector].items():
            if value['sales'] > highest_sales:
                highest_sales = value['sales']
                best_item = item
    
    return best_item, highest_sales

result = best_selling(warehouse)
print(f"Best selling item is {result[0]} with {result[1]} sales")

# Exercise 3: Create function that returns category performance
# Input: category name
# Output: dictionary with total sales, total value, average price

def returns_performance(cat):
    cnt = 0
    total_price = 0
    performance =  {
       'total_sales': 0,
       'total_value': 0,
       'avg_price': 0}
    for key, value in warehouse[cat].items():
        cnt += 1
        total_price += value['price']
        performance['total_sales'] += value['sales']
        performance['total_value'] += value['stock'] * value['sales']
        

    performance['avg_price'] = total_price / cnt
    return performance

result = returns_performance('Accessories')
print(result)