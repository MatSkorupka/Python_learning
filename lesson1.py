# First, we import pandas - a powerful library for data manipulation
import pandas as pd

# Creating sample data (similar to what you might have in a SQL table)
data = {
    'customer_id': [1, 2, 3, 4, 5],
    'product': ['Laptop', 'Phone', 'Laptop', 'Tablet', 'Phone'],
    'amount': [1200, 800, 1500, 300, 600]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Let's look at our data
print("All data:")
print(df)

# Let's add more operations to our script:

# 1. Filtering (like WHERE in SQL)
# SQL: SELECT * FROM sales WHERE product = 'Laptop'
laptops = df[df['product'] == 'Laptop']
print("\nOnly Laptops:")
print(laptops)

# 2. Grouping and aggregation (like GROUP BY)
# SQL: SELECT product, SUM(amount) as total_amount 
# FROM sales GROUP BY product
sales_by_product = df.groupby('product')['amount'].sum()
print("\nTotal sales by product:")
print(sales_by_product)

# 3. Sorting (like ORDER BY)
# SQL: SELECT * FROM sales ORDER BY amount DESC
sorted_sales = df.sort_values('amount', ascending=False)
print("\nAll sales sorted by amount (descending):")
print(sorted_sales)