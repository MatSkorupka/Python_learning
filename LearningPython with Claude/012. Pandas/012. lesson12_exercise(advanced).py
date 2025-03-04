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
# YOUR CODE HERE

# 2.2 Calculate the total sales amount for each category-product combination
# YOUR CODE HERE

# 2.3 Unstack the region level to create a DataFrame with regions as columns
# YOUR CODE HERE

# 2.4 Find the product with the highest sales in each region
# YOUR CODE HERE

# 2.5 Use .xs() to extract all sales data for the 'Laptop' product across all regions
# YOUR CODE HERE


# --------------------------------------------------------------------------------------
# EXERCISE 3: Performance Optimization
# --------------------------------------------------------------------------------------
"""
In this exercise, you'll practice optimizing Pandas operations for better performance.
"""

# 3.1 Check the memory usage of the product_sales DataFrame
# YOUR CODE HERE

# 3.2 Convert the 'category', 'product', and 'region' columns to categorical data type 
# and measure the memory savings
# YOUR CODE HERE

# 3.3 Use vectorized operations to calculate the profit for each sale 
# (assume cost is 60% of unit_price)
# YOUR CODE HERE

# 3.4 Compare the performance of iterrows() vs vectorized operations for a simple calculation
# (e.g., calculating the total value of each transaction including a 5% tax)
# YOUR CODE HERE


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
# YOUR CODE HERE

# 4.2 Create a custom aggregation function to calculate the price range 
# (max price - min price) for each product, and include it in your aggregations
# YOUR CODE HERE

# 4.3 Use transform to add a column showing what percentage of the category's 
# total sales each product represents
# YOUR CODE HERE

# 4.4 Use filter to select only products that have more than 50 total units sold
# YOUR CODE HERE

# 4.5 Calculate the cumulative sales amount for each product over time
# YOUR CODE HERE


# --------------------------------------------------------------------------------------
# EXERCISE 5: Combining Multiple Techniques for Analysis
# --------------------------------------------------------------------------------------
"""
In this final exercise, you'll combine multiple techniques to perform a comprehensive
sales analysis.
"""

# 5.1 For each product, find the region with the highest sales and the region 
# with the lowest sales
# YOUR CODE HERE

# 5.2 Create a pivot table showing monthly sales by product category
# YOUR CODE HERE

# 5.3 Calculate month-over-month growth rate for each product
# YOUR CODE HERE

# 5.4 Identify the top 3 selling products for each month
# YOUR CODE HERE

# 5.5 Create a DataFrame that shows the sales rank of each product within 
# its category, for each region
# YOUR CODE HERE