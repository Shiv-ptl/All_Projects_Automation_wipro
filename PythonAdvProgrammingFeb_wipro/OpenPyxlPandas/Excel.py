import pandas as pd

#read excel sheet

df =pd.read_excel("students.xlsx",engine="openpyxl")
print(df)


#writing excel

data = {
    "Name":["Shiv","Ram","Ravi"],
    "Age":[20,21,25],
    "Marks":[89,78,99]
}
df = pd.DataFrame(data)
df.to_excel("output.xlsx",index=False,engine="openpyxl")
print(df)
#read a specific column
df = pd.read_excel("output.xlsx",usecols=["Name"],engine="openpyxl")
print(df)

#read a perticular sheet
df = pd.read_excel("students.xlsx",
                   sheet_name="Sheet1",
                   engine="openpyxl")
print(df)
#read all sheets

df = pd.read_excel("students.xlsx",
                   sheet_name=None
                   )
print(df)

#writing Multiple Sheets

data1 = {
    "City":["Delhi","Mumbai"],
    "Sales":[10,20]
}

data2 = {
"City":["Delhi","Mumbai"],
"Customers":[200,242]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
with pd.ExcelWriter("report.xlsx",engine="openpyxl") as writer:
    df1.to_excel(writer,sheet_name="Sales")
    df2.to_excel(writer,sheet_name="Customers")


df = pd.read_excel("report.xlsx",
                   sheet_name=None,
                   engine="openpyxl"
                   )
print(df)