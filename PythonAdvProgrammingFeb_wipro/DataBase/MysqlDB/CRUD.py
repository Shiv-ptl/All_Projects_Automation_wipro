import mysql.connector

# Step 1: Connect to MySQL Server
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shiv@123",
    port=3306
)

cursor = connection.cursor()
print("Connected Successfully")

# Step 2: Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
connection.commit()

# Step 3: Reconnect WITH database
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shiv@123",
    database="school",
    port=3306
)

cursor = connection.cursor()
print("Connected to school DB")

# Step 4: Create Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student(
        studentid INT AUTO_INCREMENT PRIMARY KEY,
        studentname VARCHAR(50),
        subject VARCHAR(30),
        marks INT
    )
''')
connection.commit()

# Step 5: Insert Data
query = "INSERT INTO student(studentname, subject, marks) VALUES (%s, %s, %s)"
values  = ("John","Math",85)

cursor.execute(query, values)
connection.commit()

# Step 6: Insert Multiple
student_data = [
    ("Sneha","English",90),
    ("Shiv","Hindi",99),
    ("Vinay","Math",84)
]

cursor.executemany(query, student_data)
connection.commit()

# Step 7: Read Data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

print("Students:")
for row in rows:
    print(row)

# Step 8: Update
cursor.execute("UPDATE student SET marks=95 WHERE studentname='John'")
connection.commit()

# Step 9: Delete
cursor.execute("DELETE FROM student WHERE studentname='Sneha'")
connection.commit()
# import mysql.connector
# from sqlalchemy.sql.ddl import CreateTable
#
# #create the connection to my sql data base
# connection = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="Shiv@123",
#     port=3306
# )
#
# cursor = connection.cursor()
# print("Connected Successfully")
# #create Database
# cursor.execute("CREATE DATABASE IF NOT EXISTS school")
# connection.commit()
#
# #Now reconnect with database:
# connection = mysql.connector.connect(
# host="127.0.0.1",
#     user="root",
#     password="Shiv@123",
#     port=3306
#
# )
#
# cursor = connection.cursor()
# print("connected Successfully")
#
# #create table
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS student(
#     studentid INT AUTO_INCREMENT PRIMARY KEY,
#     studentname VARCHAR(50),
#     subject VARCHAR(30),
#     marks INT
#
# )
# ''')
# connection.commit()
#
# #insert data into the table
# query = "INSERT INTO TABLE students(studentname,subject,marks) VALUES (%S ,%S,%S)"
# values  = ("John","Math",85)
#
# cursor.execute(query,values)
# connection.commit()
#
# student_data = [
#     ("Sneha","English",90),
# ("Shiv","Hindi",99),
# ("Vinay","Math",84)
# ]
# cursor.executemany(query,student_data)
# connection.commit()
#
# #read data
# cursor.execute("SELECT * FROM students")
# rows = cursor.fetchall()
#
# #update the data
#
# cursor.execute("UPDATE students SET marks=95 WHERE studentname='John'")
# connection.commit()
#
# #delete data
# cursor.execute("DELETE FROM students WHERE studentname='Sneha'")
# connection.commit()
#
#
