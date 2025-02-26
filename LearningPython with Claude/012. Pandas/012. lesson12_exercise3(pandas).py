import pandas as pd

# Create detailed sales data
data = {
    'date': ['2024-01-01', '2024-01-01', '2024-01-01', 
             '2024-01-02', '2024-01-02', '2024-01-02',
             '2024-01-03', '2024-01-03', '2024-01-03',
             '2024-01-04', '2024-01-04', '2024-01-04'],
    'product': ['Laptop', 'Phone', 'Tablet', 
                'Laptop', 'Phone', 'Tablet',
                'Laptop', 'Phone', 'Tablet',
                'Laptop', 'Phone', 'Tablet'],
    'store': ['North', 'North', 'North', 
              'South', 'South', 'South',
              'East', 'East', 'East',
              'North', 'South', 'East'],
    'price': [1200, 800, 300, 
              1200, 800, 300,
              1200, 800, 300,
              1200, 800, 300],
    'units_sold': [5, 10, 8, 
                   4, 12, 6,
                   7, 9, 5,
                   6, 8, 7],
    'cost': [1000, 600, 200, 
             1000, 600, 200,
             1000, 600, 200,
             1000, 600, 200]
}


# Create detailed sales data and DataFrame
df = pd.DataFrame(data)

# Calculate revenue and profit
df['revenue'] = df['price'] * df['units_sold']
df['profit'] = df['revenue'] - (df['cost'] * df['units_sold'])
df['profit_margin'] = (df['price'] - df['cost']) / df['price'] * 100


# Using the same data, let's do more complex analyses:

# Exercise 1: Performance Analysis
# For each store calculate:
# - Total revenue
# - Average profit margin
# - Best selling product (by units)
# - Most profitable product (by total profit)

# Total revenue by store
total_revenue = df.groupby('store')['revenue'].sum()
print(f'Total revenue by store: \n{total_revenue}\n')

# Average profit margin by store
profit_margin = df.groupby('store')['profit_margin'].mean()
print(f"Average profit margin by store:\n{profit_margin}\n")

# Best selling product by units for each store
best_selling = df.groupby(['store', 'product'])['units_sold'].sum().reset_index()
for store in df['store'].unique():
    store_data = best_selling[best_selling['store'] == store]
    top_product = store_data.loc[store_data['units_sold'].idxmax()]
    print(f"Best selling product in {store}: {top_product['product']} ({top_product['units_sold']} units)")

# Most profitable product by total profit
most_profitable = df.groupby(['store', 'product'])['profit'].sum().reset_index()
for store in df['store'].unique():
    store_data = most_profitable[most_profitable['store'] == store]
    top_profit = store_data.loc[store_data['profit'].idxmax()]
    print(f"Most profitable product in {store}: {top_profit['product']} (${top_profit['profit']})")


# Exercise 2: Time Analysis
# For each date calculate:
# - Daily revenue
# - Compare to previous day (% change)
# - Best performing store
# - Worst performing store

# First, let's work on Exercise 2: Time Analysis
print("EXERCISE 2: TIME ANALYSIS")

# Calculate daily revenue
daily_revenue = df.groupby('date')['revenue'].sum()
print(f"\nDaily Revenue:\n{daily_revenue}")

# Calculate percentage change from previous day
daily_pct_change = daily_revenue.pct_change() * 100
print(f"\nPercentage Change from Previous Day:\n{daily_pct_change}")

# Best and worst performing store by date
store_daily_revenue = df.groupby(['date', 'store'])['revenue'].sum().reset_index()

for date in df['date'].unique():
    date_data = store_daily_revenue[store_daily_revenue['date'] == date]
    best_store = date_data.loc[date_data['revenue'].idxmax()]
    worst_store = date_data.loc[date_data['revenue'].idxmin()]
    
    print(f"\nDate: {date}")
    print(f"  Best store: {best_store['store']} (${best_store['revenue']})")
    print(f"  Worst store: {worst_store['store']} (${worst_store['revenue']})")


# Exercise 3: Product Analysis
# For each product calculate:
# - Total units sold
# - Average price
# - Total profit
# - Percentage of total company profit

# Now, Exercise 3: Product Analysis
print("\n\nEXERCISE 3: PRODUCT ANALYSIS")

# Total units sold by product
units_by_product = df.groupby('product')['units_sold'].sum()
print(f"\nTotal Units Sold by Product:\n{units_by_product}")

# Average price by product (should be the same in this dataset)
avg_price = df.groupby('product')['price'].mean()
print(f"\nAverage Price by Product:\n{avg_price}")

# Total profit by product
total_profit_by_product = df.groupby('product')['profit'].sum()
print(f"\nTotal Profit by Product:\n{total_profit_by_product}")

# Percentage of total company profit
company_profit = df['profit'].sum()
profit_percentage = (total_profit_by_product / company_profit * 100).round(2)