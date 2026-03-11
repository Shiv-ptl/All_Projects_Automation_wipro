'''
You are a data analyst at a retail company. You receive a CSV file:
Columns:
OrderID, Date, Region, Product, Category, Quantity, Price

Your Tasks
Step 1: Data Cleaning
Load data using pandas.
Convert Date to datetime.
Create a new column:
Check for null values and handle them.
Step 2: Analysis Questions
Which region generates the highest total revenue?
What is the monthly sales trend?
Which category performs best?
What are the top 5 products by revenue?
Step 3: Visualizations (Matplotlib only)
Create:
Bar chart → Revenue by Region
Line plot → Monthly Revenue Trend
Pie chart → Category Contribution
Horizontal bar chart → Top 5 Products
Revenue = Quantity * Price
'''

import pandas as pd

data = [
    [1001,"2024-01-05","North","Laptop","Electronics",2,55000],
    [1002,"2024-01-10","South","Mobile","Electronics",5,20000],
    [1003,"2024-01-15","East","Sofa","Furniture",1,30000],
    [1004,"2024-02-02","West","T-Shirt","Clothing",10,800],
    [1005,"2024-02-10","North","Refrigerator","Electronics",1,40000],
    [1006,"2024-02-18","South","Jeans","Clothing",6,1500],
    [1007,"2024-03-05","East","Dining Table","Furniture",2,25000],
    [1008,"2024-03-12","West","Headphones","Electronics",8,2500],
    [1009,"2024-03-20","North","Shirt","Clothing",7,1200],
    [1010,"2024-04-01","South","Washing Machine","Electronics",1,35000],
    [1011,"2024-04-10","East","Bed","Furniture",1,45000],
    [1012,"2024-04-18","West","Jacket","Clothing",4,3000],
    [1013,"2024-05-03","North","Tablet","Electronics",3,18000],
    [1014,"2024-05-12","South","Chair","Furniture",5,4000],
    [1015,"2024-05-25","East","Sneakers","Clothing",6,3500],
    [1016,"2024-06-02","West","TV","Electronics",2,60000],
    [1017,"2024-06-15","North","Almirah","Furniture",1,28000],
    [1018,"2024-06-20","South","Cap","Clothing",12,500],
    [1019,"2024-07-05","East","Smartwatch","Electronics",4,15000],
    [1020,"2024-07-18","West","Bookshelf","Furniture",3,7000],
    [1021,"2024-03-12","West","Headphones",None,8,2500],
    [1022,"2024-03-20","North","Shirt","Clothing",None,1200]
]

columns = ["OrderID","Date","Region","Product","Category","Quantity","Price"]

df = pd.DataFrame(data, columns=columns)

df.to_csv("retail_data.csv", index=False)

print("CSV file created successfully!")

import matplotlib.pyplot as plt

df =pd.read_csv("retail_data.csv")
print(df)

#Data Cleaning:
df['Date'] = pd.to_datetime(df['Date'],errors='coerce')

#print(df)

print("Null values before cleaning:")
print(df.isnull().sum())

# Drop invalid dates
df = df.dropna(subset=['Date'])

df['Quantity'] = df['Quantity'].fillna(0)
df['Price'] = df['Price'].fillna(0)
df['Region'] = df['Region'].fillna("Unknown")
df['Category'] = df['Category'].fillna("Unknown")
df['Product'] = df['Product'].fillna("Unknown")


df['Revenue'] = df['Quantity'] * df['Price']

print("\nNull values after cleaning:")
print(df.isnull().sum())


#Region with highest revenue
region_revenue = df.groupby('Region')['Revenue'].sum().sort_values(ascending=False)
print("\nRevenue by Region:")
print(region_revenue)

#Monthly Sales Trend
df['Month'] = df['Date'].dt.to_period('M')
monthly_revenue = df.groupby('Month')['Revenue'].sum()

print("\nMonthly Revenue Trend:")
print(monthly_revenue)

#Best Performing Category
category_revenue = df.groupby('Category')['Revenue'].sum().sort_values(ascending=False)
print("\nRevenue by Category:")
print(category_revenue)

#Top 5 Products by Revenue
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)



plt.figure()
region_revenue.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure()
monthly_revenue.plot(kind='line')
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure()
category_revenue.plot(kind='pie', autopct='%1.1f%%')
plt.title("Category Contribution")
plt.ylabel("")
plt.tight_layout()
plt.show()


plt.figure()
top_products.sort_values().plot(kind='barh')
plt.title("Top 5 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.tight_layout()
plt.show()







'''
Student Performance Dataset
Scenario
You have exam data:
StudentID, Gender, Math, Science, English, Attendance

Your Tasks
Step 1: Feature Engineering
Create Average_Marks
Create Result column:
Pass if Average >= 40
Fail otherwise
Step 2: Analysis
What is the average score per subject?
Does attendance correlate with performance?
Compare performance by gender.
How many students passed vs failed?
Step 3: Visualizations
Bar chart → Average subject scores
Scatter plot → Attendance vs Average Marks
Boxplot → Marks distribution by Gender
Pie chart → Pass vs Fail

'''