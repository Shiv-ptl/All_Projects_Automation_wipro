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
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
np.random.seed(1)

data = {
    'StudentID': range(1,31),
    'Gender': np.random.choice(['Male','Female'], 30),
    'Math': np.random.randint(20, 100, 30),
    'Science': np.random.randint(20, 100, 30),
    'English': np.random.randint(20, 100, 30),
    'Attendance': np.random.randint(60, 100, 30)
}

df = pd.DataFrame(data)


print("Original Data:\n", df)
df['Average_Marks'] = (df['Math'] + df['Science'] + df['English']) / 3
df['Result'] = df['Average_Marks'].apply(lambda x: "Pass" if x >= 40 else "Fail")
print(df.head())

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shiv@123",
    port=3306
)

cursor = conn.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
cursor.execute("USE school_db")


cursor.execute("""
CREATE TABLE IF NOT EXISTS StudentInfo (
    StudentID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Math INT,
    Science INT,
    English INT,
    Attendance INT,
    Average_Marks FLOAT,
    Result VARCHAR(10)
)
""")


cursor.execute("DELETE FROM StudentInfo")

insert_query = """
INSERT INTO StudentInfo 
(StudentID, Gender, Math, Science, English, Attendance, Average_Marks, Result)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
"""

records = df.values.tolist()
cursor.executemany(insert_query, records)
conn.commit()

print("Data inserted into MySQL successfully!")


df = pd.read_sql("SELECT * FROM StudentINFO", conn)

print("Fetched Data:\n", df.head(10))







print("\nAfter Feature Engineering:\n", df)



#Average score per subject
subject_avg = df[['Math','Science','English']].mean()
print("\nAverage Score per Subject:\n", subject_avg)

#Attendance correlation with performance
correlation = df['Attendance'].corr(df['Average_Marks'])
print("\nCorrelation between Attendance and Average Marks:", correlation)

#Performance by Gender
gender_performance = df.groupby('Gender')['Average_Marks'].mean()
print("\nAverage Performance by Gender:\n", gender_performance)

#Pass vs Fail count
result_count = df['Result'].value_counts()
print("\nPass vs Fail Count:\n", result_count)

#Bar Chart → Average subject scores
plt.figure()
subject_avg.plot(kind='bar')
plt.title("Average Subject Scores")
plt.ylabel("Average Marks")
plt.show()

#Scatter plot → Attendance vs Average Marks
plt.figure()
plt.scatter(df['Attendance'], df['Average_Marks'])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()

# Boxplot → Marks distribution by Gender
plt.figure()
df.boxplot(column='Average_Marks', by='Gender')
plt.title("Marks Distribution by Gender")
# plt.suptitle("")
plt.show()



#Pie chart → Pass vs Fail

result_count.plot(kind='pie', autopct='%1.1f%%')
plt.title("Pass vs Fail Distribution")

plt.show()

plt.figure()

plt.plot(df['StudentID'], df['Attendance'], label='Attendance')
plt.plot(df['StudentID'], df['Average_Marks'], label='Average Marks')

plt.title("Attendance & Average Marks per Student")
plt.xlabel("Student ID")
plt.ylabel("Value")
plt.legend()

plt.show()