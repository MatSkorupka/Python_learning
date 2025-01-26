import pandas as pd

# Creating a more complex dataset
data = {
    'product': ['Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop', 'Phone', 'Tablet', 'Laptop'],
    'price': [1200, 800, 300, 1500, 900, 350, 1100, 750, 400, 1300],
    'stock': [5, 10, 15, 3, 8, 20, 4, 12, 8, 6],
    'category': ['Premium', 'Standard', 'Budget', 'Premium', 'Premium', 'Budget', 'Standard', 'Standard', 'Budget', 'Premium'],
    'region': ['North', 'South', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'],
    'last_sale_date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', 
                       '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-05', '2024-01-05']
}

df = pd.DataFrame(data)

# Try these more complex filters:

# 1. Find all products that:

#    - Are in North or South region
#    - AND have price between 700 and 1200 (inclusive)
#    - AND are not Budget category
df2 = df[(df['region'].isin(['North','South']) & 
          (df['price'].between(700, 1200)) & 
          (df['category']!='Budget')
        )]
print(df2)


# 2. Find all products where:
#    - Stock is less than 10
#    - OR (price is more than 1000 AND category is Premium)
df3 = df[(df['stock'] < 10) |
          ((df['price'] > 1000) &
           (df['category'] == 'Premium'))
          ]
print(df3)


# 3. Find all products that:
#    - Are either Laptop or Phone
#    - AND were sold after '2024-01-02'
#    - AND have stock more than 5
df4 = df[(df['product'].isin(['Laptop','Phone']) &
          (df['last_sale_date'] > '2024-01-02') &
          (df['stock'] > 5)
        )]
print(df4)