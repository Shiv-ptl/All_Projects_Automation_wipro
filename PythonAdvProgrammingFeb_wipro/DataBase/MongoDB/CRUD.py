#pip install pymongo pandas
from pymongo import MongoClient

# Connect
client = MongoClient("mongodb://localhost:27017/")
print("Connected Successfully")

# Create DB
db = client["school"]

# Create Collection
collection = db["students"]

# CREATE
collection.insert_one({
    "name": "Shiv",
    "subject": "Math",
    "marks": 95
})

students = [
    {"name": "Sneha", "subject": "English", "marks": 90},
    {"name": "Vinay", "subject": "Hindi", "marks": 85}
]

collection.insert_many(students)

print("Inserted Data")

# READ
print("All Students:")
for student in collection.find():
    print(student)


# UPDATE
collection.update_one(
    {"name": "Vinay"},
    {"$set": {"marks": 88}}
)

print("Updated Vinay")

# DELETE
collection.delete_one({"name": "Sneha"})
print("Deleted Sneha")


students = [
    {"name": "Sameer", "subject": "English", "marks": 80},
    {"name": "Sam", "subject": "Science", "marks": 75}
]

collection.insert_many(students)

print("Inserted Data")

# READ
print("All Students:")
for student in collection.find():
    print(student)

import pandas as pd

data = list(collection.find())
df = pd.DataFrame(data)

print(df)

print(df['marks'].mean())

print(df[df['marks']==df['marks'].max()])

print(df.groupby('subject')['marks'].mean())