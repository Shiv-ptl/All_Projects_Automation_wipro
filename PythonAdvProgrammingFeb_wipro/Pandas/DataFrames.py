import pandas as pd

data = [
    {"Name":"Ram","Age":25},
{"Name":"Shyam","Age":35},
{"Name":"Krishna","Age":45},
]

df = pd.DataFrame(data)
print(df)

#Create DataFrames fron dictionary of series
s1= pd.Series([1,2,3])
s2= pd.Series([4,5,6])
df = pd.DataFrame({"A":s1,"B":s2})
print(df)


#Create DataFrame from Numpy Array
import numpy as np

arr = np.array([[1,2],[3,4],[5,6]])
df = pd.DataFrame(arr,columns=["A","B"])
print(df)

#create dataframe using csv file

df = pd.read_csv("data.csv")
print(df)

#Create empty df
df = pd.DataFrame()
print(df)


data ={
    "Name":["Ram","Shyam"],
    "Age":[25,35]
}
df = pd.DataFrame(data,index=["Emp1","Emp2"])
print(df)
