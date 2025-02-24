import pandas as pd

# Create sample sales data
data = {
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'store': ['North', 'North', 'North', 'South', 'South', 'South', 'East', 'East'],
    'price': [1200, 800, 300, 1200, 800, 300, 1200, 800],
    'units_sold': [5, 10, 8, 4, 12, 6, 7, 9]
}

df = pd.DataFrame(data)


# First, calculate total revenue for each row
df['total_revenue'] = df['price'] * df['units_sold']

# 1. Calculate total revenue per product
product_revenue = df.groupby('product')['total_revenue'].sum()
print("Revenue by product:")
print(product_revenue)

# 2. Find store with highest revenue
store_revenue = df.groupby('store')['total_revenue'].sum()
print("\nRevenue by store:")
print(store_revenue.sort_values(ascending=False))

# 3. Average units sold per product
avg_units = df.groupby('product')['units_sold'].mean().sort_values(ascending=False)
print("\nAverage units sold by product:")
print(avg_units)

# Try these exercises! Remember:
# - For revenue: use price * units_sold
# - For grouping: use groupby()
# - For sorting: use sort_values()