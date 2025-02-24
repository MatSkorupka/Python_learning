import pandas as pd

# Create sample data
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob', 'Sarah', 'Mike', 'Lisa'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [75000, 65000, 80000, 70000, 65000, 85000, 72000, 68000],
    'experience': [3, 2, 5, 4, 3, 6, 4, 2]
}

df = pd.DataFrame(data)

# 1. Filtering
# Get all IT employees
it_employees = df[df['department'] == 'IT']
print("IT Employees:")
print(it_employees)

# Employees with salary > 70000
high_salary = df[df['salary'] > 70000]
print("\nHigh Salary Employees:")
print(high_salary)

# 2. Grouping
# Average salary by department
dept_salary = df.groupby('department')['salary'].mean()
print("\nAverage Salary by Department:")
print(dept_salary)

# 3. Sorting
# Sort by salary (descending)
sorted_by_salary = df.sort_values('salary', ascending=False)
print("\nSorted by Salary:")
print(sorted_by_salary)