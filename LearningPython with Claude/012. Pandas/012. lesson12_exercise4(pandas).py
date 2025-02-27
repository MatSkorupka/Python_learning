import pandas as pd
import numpy as np

# Creating a more complex dataset with some missing values and dates
data = {
    'date': pd.date_range(start='2024-01-01', periods=10),
    'product': ['Laptop', 'Phone', None, 'Tablet', 'Laptop', 'Phone', 'Tablet', None, 'Laptop', 'Phone'],
    'category': ['Electronics']*10,
    'store': ['North', 'North', 'South', 'South', 'East', 'East', 'North', 'South', 'East', 'North'],
    'price': [1200, 800, 300, np.nan, 1200, 800, 300, 1200, 800, 300],
    'units_sold': [5, 10, 8, 4, np.nan, 12, 6, 7, 9, 5]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df.head())

# Common data engineering operations:

# 1. Handling missing values
print("\n1. Missing values per column:")
print(df.isna().sum())

# Fill missing values
df_filled = df.copy()
df_filled['product'] = df_filled['product'].fillna('Unknown')
df_filled['price'] = df_filled['price'].fillna(df_filled['price'].mean())
df_filled['units_sold'] = df_filled['units_sold'].fillna(0)
print("\nAfter filling missing values:")
print(df_filled.isna().sum())

# 2. Date operations
df_filled['month'] = df_filled['date'].dt.month
df_filled['day'] = df_filled['date'].dt.day
df_filled['day_of_week'] = df_filled['date'].dt.day_name()
print("\nDate operations:")
print(df_filled[['date', 'month', 'day', 'day_of_week']].head())

# 3. Data transformations
# Create revenue column
df_filled['revenue'] = df_filled['price'] * df_filled['units_sold']