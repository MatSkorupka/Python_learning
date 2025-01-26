import pandas as pd

# Creating a larger dataset
data = {
    'date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02',
             '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-03', '2024-01-03'],
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone',
                'Laptop', 'Tablet', 'Phone', 'Laptop', 'Tablet'],
    'category': ['Premium', 'Standard', 'Standard', 'Premium', 'Premium',
                 'Standard', 'Standard', 'Premium', 'Standard', 'Premium'],
    'amount': [2000, 800, 500, 1800, 1200,
               1000, 600, 1500, 1100, 550],
    'region': ['North', 'South', 'North', 'South', 'East',
               'West', 'North', 'South', 'East', 'West']
}

df = pd.DataFrame(data)

# Practice exercises - try to write these queries:

# 1. Basic filtering: 
# Find all Premium category products with amount greater than 1000
df2 = df[(df['category']=='Premium') & (df['amount'] > 1000)]
print(df2)

# 2. Grouping and counting:
# Count how many sales we have for each product
df3 = df.groupby('product').count('amount')
print(df3)

# 3. Multiple conditions:
# Find all sales from North or South region where amount is less than 1000
df4 = df[df['region'].isin(['North','South']) & (df['amount'] < 1000)]
print(df4)

# 4. Grouping with multiple aggregations:
# For each region, calculate total amount and number of sales
df5 = df.groupby('region').agg({
    'amount': ['sum', 'count']
}).rename(columns={'sum' : 'total amount', 'count' : 'number of sales'})
print(df5)


# 5. Filter and group:
# First filter only Premium products, then calculate average amount by region
df6 = df[df['category']=='Premium'].groupby('region')['amount'].mean()
print(df6)


