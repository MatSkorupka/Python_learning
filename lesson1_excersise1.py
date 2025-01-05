import pandas as pd

# Creating a more realistic dataset
sales_data = {
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', 
             '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-05', '2024-01-05'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 
                'Laptop', 'Tablet', 'Phone', 'Laptop', 'Phone'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics',
                 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'amount': [1200, 800, 300, 1500, 700, 
               1300, 400, 900, 1600, 750],
    'customer_region': ['North', 'South', 'North', 'South', 'East',
                       'West', 'North', 'South', 'East', 'West']
}

df = pd.DataFrame(sales_data)
print(df)

# Exercise 1: Get all sales where amount > 1000
# SQL equivalent: SELECT * FROM sales WHERE amount > 1000

df2 = df[df['amount'] > 1000]
print(df2)

# Exercise 2: Calculate total sales by region, sorted by total amount descending
# SQL equivalent: 
# SELECT customer_region, SUM(amount) as total_sales 
# FROM sales 
# GROUP BY customer_region 
# ORDER BY total_sales DESC

df3 = df.groupby('customer_region')['amount'].sum().rename('total_sales').sort_values(ascending=False)
print(df3)


# Exercise 3: Find average amount for each product, but only show products with avg price > 800
# SQL equivalent:
# SELECT product, AVG(amount) as avg_amount 
# FROM sales 
# GROUP BY product 
# HAVING avg_amount > 800

df4 = df.groupby('product')['amount'].mean().rename('avg_amount').sort_values(ascending=False)
df4 = df4[df4 > 800]
# df4 = df4[df4[['avg_amount'] > 800]]
print(df4)