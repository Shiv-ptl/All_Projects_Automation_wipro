import pandas as pd
import numpy as np

# 1. Create DataFrame with missing values
data = {
    'Name': ['Aman', 'Riya', 'Karan', 'Shiv'],
    'Age': [23, 21, 28, 30],
    'City': ['Delhi', 'Mumbai', None, 'Bangalore'],
    'Salary': [50000, None, 60000, 70000],
    'Department': ['IT', 'HR', 'IT', 'Finance']
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 2. Detect missing values
print("\nMissing Values:")
print(df.isnull())

# 3. Replace missing values with 0
df_filled = df.fillna(0)
print("\nAfter Replacing Missing Values with 0:")
print(df_filled)

# 4. Drop rows containing missing values
df_dropped = df.dropna()
print("\nAfter Dropping Missing Rows:")
print(df_dropped)

# 5. Sort by Age (Ascending)
print("\nSorted by Age:")
print(df.sort_values(by='Age'))

# 6. Sort by Salary (Descending)
print("\nSorted by Salary (Descending):")
print(df.sort_values(by='Salary', ascending=False))

# 7. Average Salary per Department
print("\nAverage Salary per Department:")
print(df.groupby('Department')['Salary'].mean())

# 8. Total Salary per Department
print("\nTotal Salary per Department:")
print(df.groupby('Department')['Salary'].sum())

# 9. Filter Age > 25 AND City = Bangalore
filtered = df[(df['Age'] > 25) & (df['City'] == 'Bangalore')]
print("\nFiltered Employees:")
print(filtered)

# 10. Create Tax Column (10% of Salary)
df['Tax'] = df['Salary']*0.10

print("\nDataFrame with Tax Column:")
print(df)