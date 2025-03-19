"""
# Pandas Practice for Data Engineers

This file contains data generation code and practice tasks for developing pandas skills,
organized from beginner to advanced level.

## How to use this file:
1. Run the data generation code to create sample datasets
2. Work through the tasks in order, implementing your own solutions
3. Use pandas documentation and other resources to help solve the challenges
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os
import datetime as dt

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# ----------------------------------------------------------------------------
# DATA GENERATION
# ----------------------------------------------------------------------------

def generate_sales_data(n_rows=5000):
    """Generate sample sales data for practice exercises."""
    # Date range
    start_date = datetime(2022, 1, 1)
    end_date = datetime(2023, 12, 31)
    days_range = (end_date - start_date).days
    
    # Products and categories
    categories = ['Electronics', 'Clothing', 'Home', 'Food', 'Beauty']
    products = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
        'Clothing': ['T-shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes'],
        'Home': ['Sofa', 'Lamp', 'Bed', 'Desk', 'Chair'],
        'Food': ['Bread', 'Milk', 'Eggs', 'Cheese', 'Fruit'],
        'Beauty': ['Perfume', 'Makeup', 'Skincare', 'Haircare', 'Nailcare']
    }
    
    # Regions and stores
    regions = ['North', 'South', 'East', 'West']
    stores = ['Store ' + str(i) for i in range(1, 6)]
    
    # Customer types
    customer_types = ['New', 'Returning', 'Loyal', 'VIP']
    
    # Generate data
    data = []
    for i in range(n_rows):
        # Select date
        random_days = random.randint(0, days_range)
        date = start_date + timedelta(days=random_days)
        
        # Select category and product
        category = random.choice(categories)
        product = random.choice(products[category])
        
        # Price and quantity
        base_price = round(random.uniform(10, 1000), 2)
        quantity = random.randint(1, 10)
        
        # Location
        region = random.choice(regions)
        store = random.choice(stores)
        
        # Customer
        customer_type = random.choice(customer_types)
        
        # Apply discount sometimes
        discount_pct = random.choice([0, 0, 0, 5, 10, 15, 20])
        discount_amount = round(base_price * (discount_pct / 100), 2)
        final_price = base_price - discount_amount
        
        # Total
        total = round(final_price * quantity, 2)
        
        # Create record
        data.append({
            'transaction_id': f'TX-{i+1000}',
            'date': date,
            'category': category,
            'product': product,
            'base_price': base_price,
            'discount_pct': discount_pct,
            'final_price': final_price,
            'quantity': quantity,
            'total_amount': total,
            'region': region,
            'store': store,
            'customer_type': customer_type
        })
    
    return pd.DataFrame(data)

def generate_customer_data(n_customers=200):
    """Generate sample customer data for practice exercises."""
    data = []
    for i in range(n_customers):
        customer_id = f'CUST-{i+1000}'
        join_date = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 730))
        age = random.randint(18, 80)
        gender = random.choice(['M', 'F', 'Other'])
        city = random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 
                             'Seattle', 'Boston', 'Denver', 'Atlanta', 'Dallas'])
        purchases = random.randint(1, 50)
        customer_type = random.choice(['New', 'Returning', 'Loyal', 'VIP'])
        
        data.append({
            'customer_id': customer_id,
            'join_date': join_date,
            'age': age,
            'gender': gender,
            'city': city,
            'total_purchases': purchases,
            'customer_type': customer_type
        })
    
    return pd.DataFrame(data)

def generate_product_data():
    """Generate sample product data for practice exercises."""
    data = []
    product_id = 1000
    
    categories = ['Electronics', 'Clothing', 'Home', 'Food', 'Beauty']
    products = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
        'Clothing': ['T-shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes'],
        'Home': ['Sofa', 'Lamp', 'Bed', 'Desk', 'Chair'],
        'Food': ['Bread', 'Milk', 'Eggs', 'Cheese', 'Fruit'],
        'Beauty': ['Perfume', 'Makeup', 'Skincare', 'Haircare', 'Nailcare']
    }
    
    for category in categories:
        for product in products[category]:
            base_price = round(random.uniform(10, 1000), 2)
            cost = round(base_price * 0.6, 2)  # 60% of base price
            weight = round(random.uniform(0.1, 50), 1)
            in_stock = random.choice([True, True, True, False])
            
            data.append({
                'product_id': f'PROD-{product_id}',
                'product_name': product,
                'category': category,
                'base_price': base_price,
                'cost': cost,
                'weight_kg': weight,
                'in_stock': in_stock,
                'date_added': datetime(2022, 1, 1) + timedelta(days=random.randint(0, 365))
            })
            product_id += 1
    
    return pd.DataFrame(data)

# Create a data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Generate and save the data
print("Generating sample data...")
sales_df = generate_sales_data(5000)
customer_df = generate_customer_data(200)
product_df = generate_product_data()

# Save the data to CSV files
sales_df.to_csv('data/sales_data.csv', index=False)
customer_df.to_csv('data/customer_data.csv', index=False)
product_df.to_csv('data/product_data.csv', index=False)

print("Sample data generated successfully")
print(f"Sales data: {sales_df.shape[0]} rows, {sales_df.shape[1]} columns")
print(f"Customer data: {customer_df.shape[0]} rows, {customer_df.shape[1]} columns")
print(f"Product data: {product_df.shape[0]} rows, {product_df.shape[1]} columns")

# ----------------------------------------------------------------------------
# PRACTICE TASKS
# ----------------------------------------------------------------------------

"""
### Beginner Tasks ###

Task 1: Data Loading and Basic Exploration
1. Load the sales data from CSV file
2. Display the first 10 rows and the last 5 rows
3. Get the shape (number of rows and columns) of the DataFrame
4. List all column names and their data types
5. Check for missing values in each column
6. Generate basic descriptive statistics for numeric columns
"""
sales_df = pd.read_csv('data/sales_data.csv')
sales_df.head(10)
sales_df.tail(5)
sales_df.shape
sales_df.dtypes
sales_df.info()
sales_df.isna().sum()
sales_df.describe()

"""
Task 2: Data Cleaning
1. Convert the 'date' column to datetime format
2. Handle any missing values in numeric columns (replace with mean or median)
3. Ensure all categorical columns are consistent (correct capitalization, remove extra spaces)
4. Create a new boolean column 'has_discount' based on whether discount_pct > 0
5. Remove any duplicate transactions (if they exist)
6. Create a clean version of the dataset with all transformations applied
"""

#1
sales_df['date'] = pd.to_datetime(sales_df['date'])

#2
missing_values = sales_df.isna().sum()
# No missing valuses so it is not necessery to fillup

#3
not_numeric_cols = sales_df.select_dtypes(include=['object']).columns
for x in not_numeric_cols:
    sales_df[x] = sales_df[x].str.upper().str.strip()

#4
sales_df['has_discount'] = (sales_df['discount_pct'] > 0).astype(int)


#5
sales_df.drop_duplicates(inplace = True)

#6
print(sales_df)
sales_df.to_csv('data/sales_data_cleaned.csv', index=False)



"""
Task 3: Data Transformation
1. Extract year, month, and day from the date column into separate columns
2. Add a column for day of week (Monday, Tuesday, etc.)
3. Add a column for 'weekend' (True if Saturday or Sunday)
4. Convert 'category', 'product', 'region', and 'store' columns to categorical data type
5. Create a 'price_range' column with bins for 'Low', 'Medium', 'High' based on final_price
6. Calculate the discount amount in dollars and add as a new column
"""


#1
sales_df['year'] = sales_df['date'].dt.year
sales_df['month'] = sales_df['date'].dt.month
sales_df['day'] = sales_df['date'].dt.day

#2
sales_df['day_of_week'] = sales_df['date'].dt.day_name()

#3
sales_df['is_weekend'] = sales_df['date'].dt.dayofweek > 4


#4
sales_df[['category', 'product', 'region', 'store']] = sales_df[['category', 'product', 'region', 'store']].astype('category')

#5
final_price = sales_df['final_price']
final_price.describe()

#based on describe Over 75% = High, over 50% = Medium
sales_df['price_range'] = 'Low'
sales_df.loc[sales_df['final_price'] > 458, 'price_range'] = 'Medium'
sales_df.loc[sales_df['final_price'] > 681, 'price_range'] = 'High'

#6
sales_df['discount_amount'] = (sales_df['discount_pct'] / 100) * sales_df['base_price'] 


### Intermediate Tasks ###

"""
Task 4: Aggregation and Grouping
1. Calculate total sales, average order value, and number of transactions by category
2. Find the top 5 best-selling products by total quantity sold
3. Calculate the average discount percentage by product category
4. Group data by region and store, calculating total sales for each combination
5. Find the average transaction value by customer type
6. Create a cross-tabulation (pivot table) of categories vs. regions showing total sales
"""

#1
product_aggs = sales_df.groupby('category').agg({
    'total_amount': ['sum', 'mean'],         # Total sales, average order value
    'transaction_id': 'count'                # Number of transactions by category
})

#2
top_5 = sales_df.groupby('product')['quantity'].sum().sort_values(ascending=False).head(5)

#3
avg_discount = sales_df.groupby('category')['discount_pct'].mean().sort_values(ascending=False)

#4
region_store_amount = sales_df.groupby(['region', 'store'])['total_amount'].sum().sort_values(ascending=False)

#5
avg_per_customer = sales_df.groupby('customer_type')['total_amount'].mean().sort_values(ascending=False)

#6
pivot_table = pd.pivot_table(sales_df, values='total_amount', index='category', columns='region', aggfunc='sum')



# Using the sales_df DataFrame:

# 1. Create a new column 'month_year' that combines the month and year (format: 'YYYY-MM')
sales_df['month_year'] = sales_df['date'].dt.strftime('%Y-%m')
print(sales_df)

# 2. For each month_year and customer_type combination, calculate:
#    - Total revenue
#    - Average order value
#    - Number of transactions
#    - Total quantity sold
#    - Average discount percentage

sales_agg2 = sales_df.groupby(['month_year', 'customer_type']).agg({
    'total_amount' : ['sum', 'mean'],
    'transaction_id' : 'count',
    'quantity' : 'sum',
    'discount_pct' : 'mean'
})

# 3. Identify the top-performing customer segment for each month (by total revenue)
# Hint: This requires groupby, then another operation to find the maximum

monthly_segment_sales = sales_df.groupby(['month_year', 'customer_type'])['total_amount'].sum().reset_index()

top_segment_by_month = monthly_segment_sales.loc[
    monthly_segment_sales.groupby('month_year')['total_amount'].idxmax()
]

print(top_segment_by_month[['month_year', 'customer_type', 'total_amount']])


# 4. Calculate the percentage contribution of each customer segment to the total revenue for each month
# Hint: You'll need to calculate monthly totals, then join or merge back

# Get total sales by month
monthly_totals = sales_df.groupby('month_year')['total_amount'].sum().reset_index()
monthly_totals.rename(columns={'total_amount': 'month_total'}, inplace=True)

# Merge with segment sales
segment_contribution = monthly_segment_sales.merge(monthly_totals, on='month_year')

# Calculate percentage
segment_contribution['contribution_pct'] = (segment_contribution['total_amount'] / 
                                           segment_contribution['month_total'] * 100)

print(segment_contribution[['month_year', 'customer_type', 'total_amount', 
                            'month_total', 'contribution_pct']])

# 5. Find months where VIP customers contributed more than 30% of the total revenue
vip_months = segment_contribution[
    (segment_contribution['customer_type'] == 'VIP') & 
    (segment_contribution['contribution_pct'] > 30)
]

print("Months where VIP customers contributed more than 30% of revenue:")
print(vip_months[['month_year', 'contribution_pct']])


# Assuming you have sales_df loaded with date as datetime

# 1. First, create a new DataFrame that contains the daily sales by product
# Hint: Use groupby with date and product, then sum of quantity and total_amount
daily_sales = sales_df.groupby(['date', 'product'])[['quantity', 'total_amount']].sum()
daily_sales_reset = daily_sales.reset_index()
print(daily_sales)

# 2. Calculate the cumulative sum of quantity sold for each product over time
# This will show the running total of units sold for each product

# Sort data by date
daily_sales_reset = daily_sales_reset.sort_values('date')

# Calculate cumulative sum of quantity for each product over time
product_cumulative_sales = daily_sales_reset.groupby('product')['quantity'].cumsum()

# Add this as a new column to your DataFrame
daily_sales_reset['cumulative_quantity'] = product_cumulative_sales
print(daily_sales_reset)

# 3. Calculate a 7-day rolling average of sales for each product
# This will smooth out daily fluctuations and show trends

daily_sales_reset = daily_sales_reset.sort_values(['product', 'date'])

# Set up a MultiIndex
daily_sales_indexed = daily_sales_reset.set_index(['product', 'date'])

# Calculate the 7-day rolling average for each product
seven_day_rolling = daily_sales_indexed.groupby(level='product')['total_amount'].rolling(window=7).mean()

# First convert to DataFrame
seven_day_rolling_df = seven_day_rolling.to_frame(name='rolling_7day_avg')

# Rename the column
seven_day_rolling_df = seven_day_rolling_df.rename(columns={'total_amount': 'rolling_7day_avg'})

print(seven_day_rolling_df.head(10))

# 4. For each product, calculate:
#    - The percentage change in sales compared to the previous day
#    - The maximum single-day sales
#    - The day with the highest sales


# 5. Create a 'product_performance' metric that ranks products by:
#    - Total revenue (50% weight)
#    - Sales growth (30% weight) - using the slope of a linear fit to daily sales
#    - Consistency (20% weight) - inverse of the coefficient of variation
# Hint: You may need to use apply() with a custom fu



"""
Task 5: Time Series Analysis
1. Resample the data to get daily, weekly, and monthly total sales
2. Calculate the month-over-month percentage change in sales
3. Create a 7-day moving average of daily sales
4. Find the day of week with the highest average sales
5. Group data by month and calculate year-over-year growth for months that appear in both years
6. Identify seasonal patterns by analyzing monthly sales data

Task 6: Data Joins and Merges
1. Merge the sales data with product data to get cost information
2. Calculate the profit margin for each transaction (total_amount - cost * quantity)
3. Join customer data with sales data based on customer_type
4. Create a complete dataset that includes all information from sales, products, and customers
5. Identify any transactions where the product is out of stock (from product data)
6. Calculate the average age of customers by product category

### Advanced Tasks ###

Task 7: Performance Optimization
1. Measure the memory usage of the sales DataFrame
2. Convert appropriate columns to categorical data type and measure the reduction in memory usage
3. Implement a function to process the sales data in chunks of 1000 rows at a time
4. Compare the performance of vectorized operations vs. using an apply() function to calculate profit margin
5. Create a function that efficiently identifies outliers in the sales data
6. Profile the memory and time performance of different operations

Task 8: ETL Pipeline Simulation
1. Create a function to extract data from the three CSV files
2. Transform the data: clean, join, and add calculated fields
3. Create aggregated tables for sales by category, region, and time period
4. Load the processed data to different file formats (CSV, Parquet, JSON)
5. Implement logging to track the ETL process
6. Add error handling for potential issues (missing files, data type errors)

Task 9: Data Quality Assessment
1. Check for referential integrity between sales and product data
2. Validate that all discount percentages are within a valid range (0-100%)
3. Ensure all dates are within the expected time period
4. Verify that quantities and prices are positive values
5. Create a data quality report showing the percentage of records that pass or fail each check
6. Implement automated data validation rules that can be applied to new data

Task 10: Advanced Analysis Tasks
1. Perform a cohort analysis of customers based on their join date
2. Calculate customer lifetime value (CLV) based on their purchase history
3. Implement a simple product recommendation algorithm based on purchasing patterns
4. Create a function to forecast future sales using historical data
5. Build a price elasticity model to understand how discounts affect purchase quantity
6. Identify statistically significant correlations between different variables in the dataset

### Challenge Projects ###

Project 1: Sales Analytics Dashboard
Create a comprehensive sales analytics solution that:
1. Processes and cleans the raw data
2. Creates summary tables for different dimensions (product, region, time)
3. Calculates KPIs (revenue, profit, growth, discount effectiveness)
4. Exports data for visualization

Project 2: Data Pipeline for Daily Sales Updates
Design a pipeline that simulates processing daily sales updates:
1. Split the data by date to simulate daily batches
2. Process each batch, performing necessary transformations
3. Update master datasets with new information
4. Create daily, weekly, and monthly summary reports
5. Implement monitoring for data quality issues

Project 3: Customer Segmentation System
Build a customer segmentation system that:
1. Analyzes purchase history, frequency, recency, and monetary value
2. Groups customers into segments
3. Creates profiles for each segment
4. Recommends marketing strategies based on segment characteristics
5. Tracks segment changes over time
"""