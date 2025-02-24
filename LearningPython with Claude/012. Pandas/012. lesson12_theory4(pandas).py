import pandas as pd

# Create sample data
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob', 'Sarah', 'Mike', 'Lisa'],
    'department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'HR'],
    'salary': [75000, 65000, 80000, 70000, 65000, 85000, 72000, 68000],
    'experience': [3, 2, 5, 4, 3, 6, 4, 2]
}

df = pd.DataFrame(data)

# 1. Multiple Conditions
# IT employees with salary > 75000
it_high_salary = df[(df['department'] == 'IT') & (df['salary'] > 75000)]
print("IT employees with high salary:")
print(it_high_salary)

# 2. Complex Grouping
# Average salary and experience by department
dept_stats = df.groupby('department').agg({
    'salary': 'mean',
    'experience': 'mean'
})
print("\nDepartment Statistics:")
print(dept_stats)

# 3. Sort by multiple columns
# Sort by department and then by salary
sorted_multiple = df.sort_values(['department', 'salary'], ascending=[True, False])
print("\nSorted by department and salary:")
print(sorted_multiple)