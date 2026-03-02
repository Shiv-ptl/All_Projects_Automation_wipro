import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:Shiv%40123@127.0.0.1:3306/school")

df = pd.read_sql("SELECT * FROM student", engine)

print(df)

# Average Marks
print("Average Marks:", df["marks"].mean())

# Highest Score
print("Topper:")
print(df[df['marks'] == df['marks'].max()])

# Subject-wise Average
print("Subject Wise Average:")
print(df.groupby('subject')['marks'].mean())
# import pandas as pd
# from sqlalchemy import create_engine
#
# engine = create_engine("mysql+pymysql://root:Shiv@123@127.0.0.1:3306/school")
#
# df = pd.read_sql("SELECT * FROM students",engine)
#
# print(df)
#
# #avg marks
#
# print(df["marks"].mean())
#
# #highest score
# print(df[df['marks']==df['marks'].max()])
#
# print(df.groupby('subject')['marks'].mean())