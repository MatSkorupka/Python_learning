import pandas as pd

# Creating test data
data = {
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop'],
    'price': [1200, 800, 300, 1500, 900, 350, 1100, 750, 400, 1300],
    'stock': [5, 10, 15, 3, 8, 20, 4, 12, 8, 6],
    'category': ['Premium', 'Standard', 'Budget', 'Premium', 'Premium', 'Budget', 'Standard', 'Standard', 'Budget', 'Premium'],
    'region': ['North', 'South', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West']
}

df = pd.DataFrame(data)

# Try these filtering exercises:

# 1. Find all Premium laptops (products that are both Premium AND Laptop)
df2 = df[(df['product'] == 'Laptop') & (df['category'] == 'Premium')]
print(df2)

# 2. Find all products that are either Premium OR have price > 1000
df3 = df[(df['category'] == 'Premium') | (df['price'] > 1000)]
print(df3)

# 3. Find all products from North or South region that have stock less than 10
df4 = df[(df['region'].isin(['North', 'South'])) & (df['stock'] < 10)]
print(df4)

# 4. Find all Budget or Standard products that cost less than 500
df5 = df[(df['category'].isin(['Budget', 'Standard'])) & (df['price'] < 500)]
print(df5)

# 5. Find all products that are:
#    - Premium category
#    - AND cost more than 1000
#    - AND have stock less than 5
df6 = df[(df['category'] == 'Premium') & (df['price'] > 1000) & (df['stock'] < 5)]
print(df6)