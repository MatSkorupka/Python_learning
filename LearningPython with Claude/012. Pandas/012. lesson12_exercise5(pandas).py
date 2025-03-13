# Comprehensive Pandas Exercise: E-commerce Sales Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Generate sample data
def generate_ecommerce_data(n_records=5000):
    # Date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 12, 31)
    days_range = (end_date - start_date).days
    
    # Customer segments
    segments = ['New', 'Returning', 'Loyal', 'VIP']
    segment_weights = [0.4, 0.3, 0.2, 0.1]
    
    # Products and categories
    products = {
        'Electronics': ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Camera'],
        'Clothing': ['T-shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes'],
        'Home': ['Sofa', 'Lamp', 'Bed', 'Desk', 'Chair'],
        'Beauty': ['Perfume', 'Makeup', 'Skincare', 'Haircare', 'Nailcare']
    }
    
    # Regions
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    # Payment methods
    payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash on Delivery']
    
    # Generate data
    data = []
    for i in range(n_records):
        # Generate date with higher probability for recent months
        days_offset = int(np.random.beta(2, 5) * days_range)
        date = start_date + timedelta(days=days_offset)
        
        # Select category and product
        category = np.random.choice(list(products.keys()))
        product = np.random.choice(products[category])
        
        # Generate other fields
        region = np.random.choice(regions)
        segment = np.random.choice(segments, p=segment_weights)
        payment = np.random.choice(payment_methods)
        
        # Generate prices based on category
        if category == 'Electronics':
            base_price = np.random.uniform(300, 1500)
        elif category == 'Clothing':
            base_price = np.random.uniform(20, 200)
        elif category == 'Home':
            base_price = np.random.uniform(100, 800)
        else:  # Beauty
            base_price = np.random.uniform(15, 150)
        
        # Apply discount
        discount_pct = np.random.choice([0, 5, 10, 15, 20], p=[0.7, 0.1, 0.1, 0.05, 0.05])
        discount_amount = base_price * (discount_pct / 100)
        final_price = base_price - discount_amount
        
        # Quantity
        quantity = np.random.randint(1, 5)
        
        # Calculate total
        total_amount = final_price * quantity
        
        # Add a shipping cost
        shipping_cost = np.random.uniform(5, 25) if total_amount < 100 else 0
        
        # Add row to data
        data.append({
            'order_id': f'ORD-{i+1000}',
            'date': date,
            'customer_segment': segment,
            'region': region,
            'category': category,
            'product': product,
            'payment_method': payment,
            'base_price': round(base_price, 2),
            'discount_pct': discount_pct,
            'discount_amount': round(discount_amount, 2),
            'final_price': round(final_price, 2),
            'quantity': quantity,
            'shipping_cost': round(shipping_cost, 2),
            'total_amount': round(total_amount + shipping_cost, 2)
        })
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    return df

# Generate data
sales_data = generate_ecommerce_data()
print("Sample data generated:")
print(sales_data.head())

# EXERCISE: Comprehensive E-commerce Data Analysis
# Complete the following tasks to analyze the sales data

# Task 1: Time Series Analysis
# Convert date to datetime index
# Calculate monthly sales and visualize trend
# Identify which day of the week has the highest average sales

# Convert date to datetime index
sales_data['date'] = pd.to_datetime(sales_data['date'])
sales_ts = sales_data.set_index('date')

# Calculate monthly sales
monthly_sales = sales_ts.resample('M')['total_amount'].sum().reset_index()
monthly_sales['month'] = monthly_sales['date'].dt.strftime('%B %Y')

# Visualize the trend
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['date'], monthly_sales['total_amount'], marker='o', linestyle='-')
plt.title('Monthly Sales Trend (2023)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print monthly sales data
print("Monthly Sales Summary:")
print(monthly_sales[['month', 'total_amount']].set_index('month'))

# Identify which day of the week has the highest average sales
sales_data['day_of_week'] = sales_data['date'].dt.day_name()
day_of_week_sales = sales_data.groupby('day_of_week')['total_amount'].agg(['mean', 'sum', 'count'])

# Sort by mean sales
day_of_week_sales = day_of_week_sales.sort_values('mean', ascending=False)

# Set the order of days (optional)
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if day_of_week_sales.index.isin(days_order).all():
    day_of_week_sales = day_of_week_sales.reindex(days_order)

print("\nSales by Day of Week:")
print(day_of_week_sales)

# Visualize day of week analysis
plt.figure(figsize=(10, 6))
plt.bar(day_of_week_sales.index, day_of_week_sales['mean'], color='skyblue')
plt.title('Average Daily Sales by Day of Week', fontsize=14)
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Average Sales ($)', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()



# Task 2: Customer Segment Analysis
# Calculate average order value by customer segment
# Determine which segment contributes most to overall revenue
# Find which products are most popular with VIP customers

# Task 3: Product and Category Analysis
# Identify the top 3 products in each category by sales
# Calculate the profit margin for each category (assume 40% of base_price is cost)
# Find products with consistent month-over-month growth

# Task 4: Regional Analysis
# Create a pivot table showing category performance by region
# For each region, identify the best-selling and worst-selling product
# Calculate what percentage of total sales each region contributes

# Task 5: Discount Analysis
# Analyze the relationship between discount percentage and quantity sold
# Determine which product categories are most sensitive to discounts
# Calculate the average discount amount by customer segment

# Task 6: Payment Method Analysis
# Find the most popular payment method by region
# Calculate the average order value for each payment method
# Determine if certain customer segments prefer specific payment methods

# Task 7: Create a comprehensive dashboard
# Combine the key insights from your analysis into a set of visualizations
# Include a monthly sales trend, category distribution, regional comparison, and segment analysis