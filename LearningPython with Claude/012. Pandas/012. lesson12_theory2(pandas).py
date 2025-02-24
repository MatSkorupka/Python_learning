import pandas as pd

# Create a DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'age': [28, 22, 35, 25, 30],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [75000, 65000, 80000, 70000, 65000]
}

df = pd.DataFrame(data)

# Basic operations to try:

# 1. View the data
print("First few rows:")
print(df.head())

# 2. Basic information about DataFrame
print("\nDataFrame info:")
print(df.info())

# 3. Basic statistics
print("\nBasic statistics:")
print(df.describe())

# 4. Select a single column
print("\nAges:")
print(df['age'])

# 5. Select multiple columns
print("\nName and Salary:")
print(df[['name', 'salary']])