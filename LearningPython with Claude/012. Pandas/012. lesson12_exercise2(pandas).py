import pandas as pd

# Create more detailed sales data
data = {
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'store': ['North', 'North', 'South', 'South', 'East', 'East'],
    'price': [1200, 800, 300, 1200, 800, 300],
    'units_sold': [5, 10, 8, 4, 12, 6],
    'cost': [1000, 600, 200, 1000, 600, 200]
}

df = pd.DataFrame(data)
df['profit_margin'] = (df['price'] - df['cost']) / df['price'] * 100


# Exercises:

# 1. Calculate profit margin percentage for each product
# (price - cost) / price * 100

profit_margin = df.groupby('product')['profit_margin'].mean()
print("\nProfit margin by product:")
print(profit_margin)

# 2. Find daily revenue by store
# Group by date and store, sum revenue

df['revenue'] = df['price'] * df['units_sold']
daily_revenue = df.groupby(['date', 'store'])['revenue'].sum()
print("\nDaily revenue by product:")
print(daily_revenue)

# 3. Calculate what percentage of total revenue each store represents
# Store revenue / Total revenue * 100

total_revenue = df['revenue'].sum()
store_revenue = df.groupby('store')['revenue'].sum()
revenue_percentage = (store_revenue / total_revenue * 100).round(2)
print("\nRevenue percentage by store:")
print(revenue_percentage)
