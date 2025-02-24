import pandas as pd


# Create a simple DataFrame
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [28, 22, 35, 25],
    'city': ['New York', 'Paris', 'London', 'Berlin']
}

df = pd.DataFrame(data)

# Basic operations
print(df.head())        # View first rows
print(df.columns)       # Column names
print(df['age'].mean()) # Calculate mean age