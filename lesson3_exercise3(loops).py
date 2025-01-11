sales_data = {
    'products': ['Laptop', 'Phone', 'Tablet', 'Watch'],
    'prices': [1200, 800, 300, 250],
    'stock': [5, 10, 15, 8],
    'categories': ['Premium', 'Standard', 'Budget', 'Budget'],
    'discounts': {
        'Premium': 0.1,    # 10% discount
        'Standard': 0.05,  # 5% discount
        'Budget': 0.02     # 2% discount
    }
}

# Exercise 1: Discounted Prices
# For each product, calculate and print:
# - Original price
# - Discount percentage (based on category)
# - Final price after discount
# Format output nicely
discount = 0
final_price = 0

for product, category, price in zip(products, categories, prices):
    # print(f'Price for {product} is {price}')
    discount = sales_data['discounts'][category]
    final_price = price * (1 - discount)
    print(f'Price for {product} is {price}')
    print(f'Discount for {product} is {discount}')
    print(f'Final price for {product} is {final_price}')


# Exercise 2: Stock Value Analysis
# For each product, calculate and print:
# - Total value of stock (price * stock)
# - Total value after applying category discount
# Also calculate and print:
# - Total value of all Premium products
# - Total value of all Budget products

stock_value = 0
discount = 0
premium_value = 0
budget_value = 0
budget_value = 0


for product, category, price, st in zip(products, categories, prices, stock):
    discount = sales_data['discounts'][category]
    stock_value = price * st
    final_price = stock_value * (1 - discount)
    print(f'Stock value for {product} is {stock_value}')
    print(f'Stock value including discount for {product} is {final_price}')
    if category == 'Premium':
        premium_value += stock_value
    elif category == 'Budget':
        budget_value += stock_value

print(f'Total value for Premium is {premium_value}')
print(f'Total value for Budget is {budget_value}')


# Exercise 3: Inventory Report
# Create these summaries:
# - Number of products in each category
# - Average price by category
# - Total stock by category


prices = sales_data['prices']
stock = sales_data['stock']    # This is important!
categories = sales_data['categories']

nb_of_products = dict()
avg_price = dict()
total_stock = dict()


for price, st, category in zip(prices, stock, categories):
    if category not in nb_of_products.keys():
        nb_of_products[category] = 1
        avg_price[category] = price
        total_stock[category] = st
    else:
        nb_of_products[category] +=1
        avg_price[category] += price 
        total_stock[category] += st

    
for cat, nb in nb_of_products.items():
    print(f'Number of products in {cat} category is {nb}')
    price_avg = avg_price[cat] / nb
    stock_total = total_stock[cat]
    print(f'Average price of products in {cat} category is {price_avg}')
    print(f'Total stock of products in {cat} category is {stock_total}')


