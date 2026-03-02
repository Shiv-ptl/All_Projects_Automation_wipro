import numpy as np
import  pandas as pd

data ={
    "Name":["Ram","Shyam","John","Sam"],
    "Age":[25,35,22,55],
    "Salary":[40000,50000,30000,70000]
}
df =pd.DataFrame(data)
print(df)

#selecting single data
print(df["Age"])

#select multiple data
print(df[["Age","Name"]])

print(df.loc[3:0:-1])

print(df.loc[0:2])#nth index

print(df.iloc[0:2])#n-1 index


#filter

df = pd.DataFrame(data)
print(df)

filtered = df[df["Salary"]>30000]
print(filtered)
filtered = df[df["Salary"]<=30000]
print(filtered)
print("Salery Greter than 40000 and age less than 25")
filtered = df[(df["Salary"]>=30000) & (df["Age"]<=25)]
print(filtered)

df["Bonus"]= df["Salary"]*0.15
print(df)

df["New_Salary"] = df["Salary"]+df["Bonus"]
print(df)

df["Age"]= df["Age"]+1
print(df)


df["Name"] = df["Name"]+" ptl"
print(df)
print(df["Name"])


#Sorting
print(df)

sorted_df = df.sort_values("Salary", ascending=True)
print(sorted_df)

sorted_df = df.sort_values("Salary", ascending=False)
print(sorted_df)

#handle missing values

data ={
    "Name":["Ram","Shyam",None],
    "Age":[25,np.nan,35]
}

print(data)

df = pd.DataFrame(data)
print(df)

print("Missing Values: \n")
print(df.isnull())

df_filled = df.fillna(0)
print(df_filled)

#Drop missing values
data = {
    'Name': ['Aman', 'Riya', 'Karan','Shiv'],
    'Age': [23, 21, 24,22],
    'City': ['Delhi', 'Mumbai', 'Pune',None]

}

df = pd.DataFrame(data)

print(df)
df = df.dropna()
print(df)

#groupBy and Aggregation
import pandas as pd

data = {
    'Department': ['IT', 'HR', 'IT', 'Finance', 'HR', 'Finance', 'IT'],
    'Employee': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'Salary': [50000, 40000, 60000, 45000, 42000, 47000, 55000],
    'Experience': [3, 2, 5, 4, 3, 6, 2]
}

df = pd.DataFrame(data)
print(df)

group = df.groupby('Department')
print(group)

print(df.groupby('Department')['Salary'].sum())


print(df.groupby('Department')['Salary'].mean())

print(df.groupby('Department')['Salary'].agg(['sum', 'mean', 'max', 'min']))

print(df.groupby(['Department', 'Experience'])['Salary'].sum())

print(df.groupby('Department').agg({
    'Salary': ['sum', 'mean'],
    'Experience': 'max'
}))

#mearging DataFrames
df1 = pd.DataFrame({
    "Id":[1,2,3,4],
    "Name":["A","B","C","D"]
})
df2 = pd.DataFrame({
    "Id":[3,4,7,8,9],
    "Name":["E","F","G","H","I"]
})

merged = pd.merge(df1,df2,on="Id",how="inner")
print(merged)

df1 = pd.DataFrame({
    "Id":[1,2,3,4],
    "Name":["A","B","A","D"]
})

print("Before removing duplicates: ")
print(df1)
df = df1.drop_duplicates(subset="Name")
print("after removing duplicates:\n")
print(df)
