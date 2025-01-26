# Sales Data
products = ['Coffee', 'Tea', 'Juice', 'Water']
prices = [5, 4, 6, 2]
sales_data = {
    'Monday': [10, 15, 8, 20],
    'Tuesday': [8, 12, 10, 15],
    'Wednesday': [12, 18, 5, 25]
}

# Exercise 1: Basic Reports
# Create a dictionary showing total sales for each product
# Example output: {'Coffee': 30, 'Tea': 45, ...}

total_sales = dict.fromkeys(products, 0)

for product_index, product in enumerate(products):
    for day in sales_data:
        total_sales[product] += sales_data[day][product_index]

print(total_sales)


# Exercise 2: Daily Revenue
# Calculate total revenue for each day
# Remember: revenue = price * quantity
# Print like: "Monday revenue: $X"


for day, quantities in sales_data.items():
    daily_revenue = 0
    for price, quantity in zip(prices, quantities):
        daily_revenue += price * quantity
    print(f'{day} revenue: ${daily_revenue}')


# Exercise 3: Product Performance
# Create a dictionary with:
# - Product names as keys
# - Dictionary as values containing:
#   - 'total_sales': total quantity sold
#   - 'total_revenue': total money made
#   - 'average_daily_sales': average sales per day


total_sales = dict.fromkeys(products, 0)
total_revenue = dict.fromkeys(products, 0)
day_counts = dict.fromkeys(products, 0)
average_sales = dict.fromkeys(products, 0)


for product_index, product in enumerate(products):
    for day in sales_data:
        total_sales[product] += sales_data[day][product_index]
        total_revenue[product] += (sales_data[day][product_index] * prices[product_index])
        day_counts[product] += 1
    

    average_sales[product] = total_sales[product] / day_counts[product]


print("Total Sales:", total_sales)
print("Total Revenue:", total_revenue)
print("Days with Sales:", day_counts)
print("Average Sales:", average_sales)