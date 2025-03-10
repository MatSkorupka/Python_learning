"""
Advanced Pandas Exercises

This file contains a series of exercises to practice advanced Pandas techniques
including time series analysis, MultiIndex, performance optimization, and advanced grouping.

Instructions:
1. Complete each exercise in the designated area
2. Run the code to verify your solution works
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time

# Generate sample data for our exercises
def generate_data():
    # Time series data - daily sales
    dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
    np.random.seed(42)  # For reproducibility
    
    # Create base sales with weekly seasonality and upward trend
    trend = np.linspace(100, 200, len(dates))
    seasonality = 20 * np.sin(np.arange(len(dates)) * (2 * np.pi / 7))
    noise = np.random.normal(0, 10, len(dates))
    sales = trend + seasonality + noise
    
    # Create daily sales dataframe
    daily_sales = pd.DataFrame({
        'date': dates,
        'sales': sales
    })
    
    # Create product sales dataframe with hierarchical structure
    products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor']
    categories = ['Electronics', 'Electronics', 'Electronics', 'Accessories', 'Electronics']
    regions = ['North', 'South', 'East', 'West']
    
    # Generate 1000 product sales records
    n_records = 1000
    product_sales = pd.DataFrame({
        'date': np.random.choice(dates, n_records),
        'product': np.random.choice(products, n_records),
        'category': np.random.choice(categories, n_records),
        'region': np.random.choice(regions, n_records),
        'quantity': np.random.randint(1, 10, n_records),
        'unit_price': np.random.uniform(50, 1000, n_records).round(2),
        'discount': np.random.choice([0, 5, 10, 15, 20], n_records)
    })
    
    # Calculate total price
    product_sales['total_price'] = (product_sales['unit_price'] * 
                                   product_sales['quantity'] * 
                                   (1 - product_sales['discount']/100)).round(2)
    
    # Sort by date
    product_sales = product_sales.sort_values('date')
    
    return daily_sales, product_sales

# Generate our datasets
daily_sales, product_sales = generate_data()

print("Daily Sales Dataset (first 5 rows):")
print(daily_sales.head())
print("\nProduct Sales Dataset (first 5 rows):")
print(product_sales.head())

# --------------------------------------------------------------------------------------
# EXERCISE 1: Time Series Analysis
# --------------------------------------------------------------------------------------
"""
In this exercise, you'll work with the daily_sales DataFrame to perform time series analysis.
"""

# 1.1 Convert the 'date' column to a datetime index
daily_sales.set_index('date', inplace=True)
print("DataFrame with datetime index:")
print(daily_sales.head())

# 1.2 Resample the data to get monthly total sales
monthly_sales = daily_sales.resample('M').sum()
print("Monthly total sales:")
print(monthly_sales.head())

# 1.3 Calculate a 7-day moving average of sales
daily_sales['sales_7d_avg'] = daily_sales['sales'].rolling(window=7).mean()
print("\nDaily sales with 7-day moving average:")
print(daily_sales.head(10))

# 1.4 Calculate the percentage change in daily sales compared to the previous day
daily_sales['pct_change'] = daily_sales['sales'].pct_change() * 100
print("\nPercentage change in daily sales:")
print(daily_sales.head(10))

# 1.5 Identify the day of the week with the highest average sales
daily_sales['day_of_week'] = daily_sales.index.day_name()
day_avg_sales = daily_sales.groupby('day_of_week')['sales'].mean().sort_values(ascending=False)
print("\nAverage sales by day of week:")
print(day_avg_sales)

# 1.6 Create a time series plot showing daily sales and the 7-day moving average
plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales['sales'], label='Daily Sales', alpha=0.5)
plt.plot(daily_sales.index, daily_sales['sales_7d_avg'], 
         label='7-day Moving Average', color='red', linewidth=2)
plt.title('Daily Sales with 7-day Moving Average')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# --------------------------------------------------------------------------------------
# EXERCISE 2: MultiIndex and Hierarchical Data
# --------------------------------------------------------------------------------------
"""
In this exercise, you'll work with the product_sales DataFrame to use MultiIndex features.
"""

# 2.1 Create a MultiIndex DataFrame by setting ['category', 'product', 'region'] as index
product_sales.set_index(['category', 'product', 'region'], inplace=True)
print("MultiIndex DataFrame:")
print(product_sales.head())

# 2.2 Calculate the total sales amount for each category-product combination
sales_by_region = product_sales.groupby(['category', 'product', 'region'])['total_price'].sum()
print(sales_by_region)

# 2.3 Unstack the region level to create a DataFrame with regions as columns
region_columns = sales_by_region.unstack(level='region')
print("Sales with regions as columns:")
print(region_columns.head())

# 2.4 Find the product with the highest sales in each region
highest_sales_by_region = product_sales.loc[product_sales.groupby('region')['total_price'].idxmax()]
print(highest_sales_by_region)

# 2.5 Use .xs() to extract all sales data for the 'Laptop' product across all regions
laptop_sales = product_sales.xs('Laptop', level='product')
print(laptop_sales)

# --------------------------------------------------------------------------------------
# EXERCISE 3: Performance Optimization
# --------------------------------------------------------------------------------------
"""
In this exercise, you'll practice optimizing Pandas operations for better performance.
"""

# 3.1 Check the memory usage of the product_sales DataFrame
memory_in_bytes = product_sales.memory_usage(deep=True).sum()
print(f"Memory usage: {memory_in_bytes / 1024**2:.2f} MB")

# 3.2 Convert the 'category', 'product', and 'region' columns to categorical data type 
# and measure the memory savings
# First, let's check the current memory usage
before_memory = product_sales.memory_usage(deep=True).sum()

# Convert specified columns to categorical data type
product_sales['category'] = product_sales['category'].astype('category')
product_sales['product'] = product_sales['product'].astype('category')
product_sales['region'] = product_sales['region'].astype('category')

# Check the memory usage after conversion
after_memory = product_sales.memory_usage(deep=True).sum()

# Calculate and display the memory savings
memory_saved = before_memory - after_memory
percent_saved = (memory_saved / before_memory) * 100

print(f"Memory before: {before_memory / 1024**2:.2f} MB")
print(f"Memory after: {after_memory / 1024**2:.2f} MB")
print(f"Memory saved: {memory_saved / 1024**2:.2f} MB ({percent_saved:.2f}%)")

# 3.3 Use vectorized operations to calculate the profit for each sale 
# (assume cost is 60% of unit_price)
# Calculate the cost (60% of unit_price)
product_sales['cost'] = product_sales['unit_price'] * 0.6

# Calculate the profit (unit_price - cost) * quantity
product_sales['profit'] = (product_sales['unit_price'] - product_sales['cost']) * product_sales['quantity']

# Display the first few rows to verify the calculation
product_sales[['unit_price', 'cost', 'quantity', 'profit']].head()
print(product_sales)

# 3.4 Compare the performance of iterrows() vs vectorized operations for a simple calculation
# (e.g., calculating the total value of each transaction including a 5% tax)
# Define both calculation methods
def using_iterrows(df):
    # Create a new column to store results
    df['total_with_tax_iterrows'] = 0.0
    
    # Start timer
    start_time = time.time()
    
    # Use iterrows to calculate total with tax
    for index, row in df.iterrows():
        df.at[index, 'total_with_tax_iterrows'] = row['unit_price'] * row['quantity'] * 1.05
    
    # Calculate execution time
    execution_time = time.time() - start_time
    return execution_time

def using_vectorized(df):
    # Start timer
    start_time = time.time()
    
    # Use vectorized operation to calculate total with tax
    df['total_with_tax_vectorized'] = df['unit_price'] * df['quantity'] * 1.05
    
    # Calculate execution time
    execution_time = time.time() - start_time
    return execution_time

# Run both methods and compare times
iterrows_time = using_iterrows(product_sales)
vectorized_time = using_vectorized(product_sales)

# Verify that both methods produce the same results
is_equal = product_sales['total_with_tax_iterrows'].equals(product_sales['total_with_tax_vectorized'])

# Print results
print(f"iterrows execution time: {iterrows_time:.6f} seconds")
print(f"Vectorized execution time: {vectorized_time:.6f} seconds")
print(f"Vectorized operations are {iterrows_time/vectorized_time:.1f}x faster")
print(f"Results are identical: {is_equal}")


# --------------------------------------------------------------------------------------
# EXERCISE 4: Advanced Grouping and Aggregation
# --------------------------------------------------------------------------------------
"""
In this exercise, you'll practice advanced grouping and aggregation techniques.
"""

# 4.1 Group by product and calculate multiple aggregations:
# - Total quantity sold
# - Average unit price
# - Minimum and maximum discount
# - Total sales amount

product_aggs = product_sales.groupby('product').agg({
    'quantity': 'sum',             # Total quantity sold
    'unit_price': 'mean',          # Average unit price
    'discount': ['min', 'max'],    # Min and max discount
    'total_price': 'sum'           # Total sales amount
})

print("Product aggregations:")
print(product_aggs)


# 4.2 Create a custom aggregation function to calculate the price range 
# (max price - min price) for each product, and include it in your aggregations
def price_range(x):
    return x.max() - x.min()

# Apply the function along with other aggregations
product_aggs = product_sales.groupby('product').agg({
    'quantity': 'sum',                          # Total quantity sold
    'unit_price': ['min', 'max', price_range],  # Min, max, and range
    'discount': ['min', 'max'],                 # Min and max discount
    'total_price': 'sum'                        # Total sales amount
})

print("Product aggregations with price range:")
print(product_aggs)

# 4.3 Use transform to add a column showing what percentage of the category's 
# total sales each product represents

# First, make sure we're working with the original DataFrame (not grouped)
if isinstance(product_sales.index, pd.MultiIndex):
    product_sales = product_sales.reset_index()

# Calculate the category totals using transform
category_totals = product_sales.groupby('category')['total_price'].transform('sum')

# Calculate each product's percentage of its category total
product_sales['category_percentage'] = (product_sales['total_price'] / category_totals) * 100

# View the results
print("Products with category percentage:")
print(product_sales[['category', 'product', 'total_price', 'category_percentage']].head(15))

# 4.4 Use filter to select only products that have more than 50 total units sold

# Group by product and filter based on total quantity
popular_products = product_sales.groupby('product').filter(lambda x: x['quantity'].sum() > 50)

# Check how many products were filtered
original_products = product_sales['product'].nunique()
filtered_products = popular_products['product'].nunique()

print(f"Original number of products: {original_products}")
print(f"Products with more than 50 units sold: {filtered_products}")

# View the filtered DataFrame
print("\nPopular products data:")
print(popular_products[['product', 'quantity']].head(10))

# 4.5 Calculate the cumulative sales amount for each product over time
# First, ensure the data is sorted by date
if isinstance(product_sales.index, pd.MultiIndex):
    product_sales = product_sales.reset_index()

# Convert 'date' to datetime if it's not already
product_sales['date'] = pd.to_datetime(product_sales['date'])

# Sort by product and date
product_sales_sorted = product_sales.sort_values(['product', 'date'])

# Group by product and calculate cumulative sum of total_price
product_sales_sorted['cumulative_sales'] = product_sales_sorted.groupby('product')['total_price'].cumsum()

# Display results
print("Cumulative sales by product over time:")
print(product_sales_sorted[['product', 'date', 'total_price', 'cumulative_sales']].head(15))

# To visualize the cumulative sales for specific products:
top_products = product_sales_sorted.groupby('product')['total_price'].sum().nlargest(3).index

plt.figure(figsize=(12, 6))
for product in top_products:
    product_data = product_sales_sorted[product_sales_sorted['product'] == product]
    plt.plot(product_data['date'], product_data['cumulative_sales'], label=product)

plt.title('Cumulative Sales for Top 3 Products')
plt.xlabel('Date')
plt.ylabel('Cumulative Sales ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# --------------------------------------------------------------------------------------
# EXERCISE 5: Combining Multiple Techniques for Analysis
# --------------------------------------------------------------------------------------
"""
In this final exercise, you'll combine multiple techniques to perform a comprehensive
sales analysis.
"""

# 5.1 For each product, find the region with the highest sales and the region 
# with the lowest sales
# First, calculate total sales for each product-region combination
product_region_sales = product_sales.groupby(['product', 'region'])['total_price'].sum().reset_index()

# Create a pivot table with products as rows and regions as columns
product_by_region = product_region_sales.pivot(index='product', columns='region', values='total_price')

# Find the region with highest and lowest sales for each product
product_region_analysis = pd.DataFrame(index=product_by_region.index)
product_region_analysis['highest_sales_region'] = product_by_region.idxmax(axis=1)
product_region_analysis['highest_sales_value'] = product_by_region.max(axis=1)
product_region_analysis['lowest_sales_region'] = product_by_region.idxmin(axis=1)
product_region_analysis['lowest_sales_value'] = product_by_region.min(axis=1)

print("Region analysis by product:")
print(product_region_analysis)

# 5.2 Create a pivot table showing monthly sales by product category
# YOUR CODE HERE

# 5.3 Calculate month-over-month growth rate for each product
# YOUR CODE HERE

# 5.4 Identify the top 3 selling products for each month
# YOUR CODE HERE

# 5.5 Create a DataFrame that shows the sales rank of each product within 
# its category, for each region
# YOUR CODE HERE