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

# Reset index if needed to work with a regular DataFrame
if isinstance(daily_sales_indexed, pd.DataFrame) and daily_sales_indexed.index.nlevels > 1:
    analysis_df = daily_sales_indexed.reset_index()
else:
    analysis_df = daily_sales_reset.copy()

# Sort by product and date
analysis_df = analysis_df.sort_values(['product', 'date'])

# Calculate percentage change compared to previous day
analysis_df['pct_change'] = analysis_df.groupby('product')['total_amount'].pct_change() * 100

# Find maximum sales and best day for each product
product_stats = analysis_df.groupby('product').agg(
    max_daily_sales=('total_amount', 'max'),
    total_revenue=('total_amount', 'sum')
)

# Find the day with highest sales for each product
best_days = analysis_df.loc[analysis_df.groupby('product')['total_amount'].idxmax()]
best_days = best_days[['product', 'date', 'total_amount']]
best_days = best_days.rename(columns={'date': 'best_day', 'total_amount': 'best_day_sales'})

# Merge the stats
product_stats = product_stats.merge(best_days[['product', 'best_day']], on='product')

print("Product statistics:")
print(product_stats)

# 5. Create a 'product_performance' metric that ranks products by:
#    - Total revenue (50% weight)
#    - Sales growth (30% weight) - using the slope of a linear fit to daily sales
#    - Consistency (20% weight) - inverse of the coefficient of variation
# Hint: You may need to use apply() with a custom fu


# First, calculate consistency (coefficient of variation)
product_cv = analysis_df.groupby('product')['total_amount'].agg(
    lambda x: x.std() / x.mean() if x.mean() > 0 else float('inf')
)
product_cv = product_cv.reset_index()
product_cv = product_cv.rename(columns={'total_amount': 'cv'})
product_stats = product_stats.merge(product_cv, on='product')
product_stats['consistency'] = 1 / product_stats['cv']  # Inverse of CV so higher is better

# Calculate growth trend using pandas
def calculate_growth_trend(group):
    # Add a numeric x-axis
    group = group.copy()
    group['x'] = range(len(group))
    
    # Calculate covariance and variance for the slope
    if len(group) <= 1:
        return 0
    
    cov = group['x'].cov(group['total_amount'])
    var = group['x'].var()
    
    # Return slope (0 if variance is 0 to avoid division by zero)
    return cov / var if var > 0 else 0

# Apply the growth trend calculation to each product group
growth_trends = analysis_df.groupby('product').apply(calculate_growth_trend)
growth_trends = growth_trends.reset_index()
growth_trends = growth_trends.rename(columns={0: 'growth_slope'})
product_stats = product_stats.merge(growth_trends, on='product')

# Normalize metrics to 0-1 scale
product_stats['norm_revenue'] = product_stats['total_revenue'] / product_stats['total_revenue'].max() if product_stats['total_revenue'].max() > 0 else 0

# For growth, handle case where all products have same growth
if product_stats['growth_slope'].max() != product_stats['growth_slope'].min():
    product_stats['norm_growth'] = (product_stats['growth_slope'] - product_stats['growth_slope'].min()) / (product_stats['growth_slope'].max() - product_stats['growth_slope'].min())
else:
    product_stats['norm_growth'] = 1  # All products have same growth

# For consistency, handle case where all products have same consistency
product_stats['norm_consistency'] = product_stats['consistency'] / product_stats['consistency'].max() if product_stats['consistency'].max() > 0 else 0

# Calculate weighted score
product_stats['performance_score'] = (
    0.5 * product_stats['norm_revenue'] + 
    0.3 * product_stats['norm_growth'] + 
    0.2 * product_stats['norm_consistency']
)

# Rank products
product_stats['rank'] = product_stats['performance_score'].rank(ascending=False)
product_stats = product_stats.sort_values('performance_score', ascending=False)

print("\nProduct Performance Ranking:")
print(product_stats[['product', 'performance_score', 'rank', 'norm_revenue', 'norm_growth', 'norm_consistency']])



"""
Task 5: Time Series Analysis
1. Resample the data to get daily, weekly, and monthly total sales
2. Calculate the month-over-month percentage change in sales
3. Create a 7-day moving average of daily sales
4. Find the day of week with the highest average sales
5. Group data by month and calculate year-over-year growth for months that appear in both years
6. Identify seasonal patterns by analyzing monthly sales data
"""
#1

sales_with_date_index = sales_df.set_index('date')

daily_sales = sales_with_date_index.resample('D')['total_amount'].sum().reset_index()
print(daily_sales.head())

weekly_sales = sales_with_date_index.resample('W-MON')['total_amount'].sum().reset_index()
print(weekly_sales.head())

monthly_sales = sales_with_date_index.resample('M')['total_amount'].sum().reset_index()
print(monthly_sales.head())


#2
monthly_sales['mom_pct_change'] = monthly_sales['total_amount'].pct_change() * 100
print("\nMonth-over-Month Percentage Change:")
print(monthly_sales[['date', 'total_amount', 'mom_pct_change']])


#3
sales_with_date_index = sales_df.set_index('date')  # Make sure date is the index
moving_avg_7d = sales_with_date_index['total_amount'].rolling(window=7).mean()
moving_avg_df = moving_avg_7d.reset_index()
moving_avg_df.columns = ['date', 'moving_avg_7d']

print("\n7-Day Moving Average of Sales (first 5 rows):")
print(moving_avg_df.head())

combined_df = pd.merge(daily_sales, moving_avg_df, on='date', how='left')
print("\nDaily Sales with 7-Day Moving Average (first 5 rows):")
print(combined_df.head())



"""
Task 6: Data Joins and Merges
1. Merge the sales data with product data to get cost information
2. Calculate the profit margin for each transaction (total_amount - cost * quantity)
3. Join customer data with sales data based on customer_type
4. Create a complete dataset that includes all information from sales, products, and customers
5. Identify any transactions where the product is out of stock (from product data)
6. Calculate the average age of customers by product category
"""

#1
sales_df['date'] = pd.to_datetime(sales_df['date'])
product_df['date_added'] = pd.to_datetime(product_df['date_added'])

print("Sales DataFrame product column name:", sales_df['product'].name)
print("Product DataFrame product column name:", product_df['product_name'].name)

sales_with_cost = sales_df.merge(
    product_df[['product_name', 'cost']],
    left_on='product',
    right_on='product_name',
    how='left'
)

print("\nMerged DataFrame (first 5 rows):")
print(sales_with_cost.head())

missing_cost = sales_with_cost[sales_with_cost['cost'].isna()]
if len(missing_cost) > 0:
    print(f"\nWarning: {len(missing_cost)} transactions have missing cost information.")
    print("Unique products with missing cost:", missing_cost['product'].unique())


# 2. Calculate the profit margin for each transaction (total_amount - cost * quantity)

# Calculate profit
sales_with_cost['profit'] = sales_with_cost['total_amount'] - (sales_with_cost['cost'] * sales_with_cost['quantity'])

# Calculate profit margin percentage
sales_with_cost['profit_margin_pct'] = (sales_with_cost['profit'] / sales_with_cost['total_amount']) * 100

# Display results
print("\nSales with Profit Information (first 5 rows):")
print(sales_with_cost[['transaction_id', 'product', 'total_amount', 'cost', 'quantity', 'profit', 'profit_margin_pct']].head())

# Aggregate profit by product
product_profit = sales_with_cost.groupby('product').agg({
    'total_amount': 'sum',
    'profit': 'sum',
    'profit_margin_pct': 'mean',
    'transaction_id': 'count'
}).rename(columns={'transaction_id': 'num_transactions'}).sort_values('profit', ascending=False)

print("\nProfit by Product (top 10):")
print(product_profit.head(10))

#3
# First, let's load our customer dataset if it's not already loaded
# customer_df = pd.read_csv('data/customer_data.csv')

# Ensure join_date is in datetime format
customer_df['join_date'] = pd.to_datetime(customer_df['join_date'])

# Check the key columns we'll join on
print("Sales DataFrame customer type column:", sales_df['customer_type'].name)
print("Customer DataFrame customer type column:", customer_df['customer_type'].name)

# Join sales data with customer data
# We'll join the sales data that already has product costs
sales_with_customer = sales_with_cost.merge(
    customer_df,
    on='customer_type',  # Join on customer_type which exists in both DataFrames
    how='left'
)

# Check to make sure the merge worked
print("\nSales with Customer Information (first 5 rows):")
print(sales_with_customer.head())

# Check if any customer types didn't match
missing_customer = sales_with_customer[sales_with_customer['customer_id'].isna()]
if len(missing_customer) > 0:
    print(f"\nWarning: {len(missing_customer)} transactions have missing customer information.")
    print("Unique customer types with missing info:", missing_customer['customer_type'].unique())

# Create a summary of sales by customer type
customer_summary = sales_with_customer.groupby('customer_type').agg({
    'total_amount': 'sum',
    'profit': 'sum',
    'age': 'mean',
    'transaction_id': 'count'
}).rename(columns={'transaction_id': 'num_transactions'})

print("\nSales Summary by Customer Type:")
print(customer_summary)

# Analyze average order value by customer type
customer_summary['avg_order_value'] = customer_summary['total_amount'] / customer_summary['num_transactions']
print("\nAverage Order Value by Customer Type:")
print(customer_summary[['avg_order_value']])

# Optional: Analyze sales by customer demographics (e.g., age groups)
if 'age' in sales_with_customer.columns:
    # Create age groups
    bins = [0, 25, 35, 50, 65, 100]
    labels = ['18-25', '26-35', '36-50', '51-65', '65+']
    sales_with_customer['age_group'] = pd.cut(sales_with_customer['age'], bins=bins, labels=labels)
    
    # Analyze sales by age group
    age_group_summary = sales_with_customer.groupby('age_group').agg({
        'total_amount': 'sum',
        'profit': 'sum',
        'transaction_id': 'count'
    }).rename(columns={'transaction_id': 'num_transactions'})
    
    print("\nSales by Age Group:")
    print(age_group_summary)

### Advanced Tasks ###
"""
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