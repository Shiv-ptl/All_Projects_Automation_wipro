"""Create a dictionary with student roll number as key and name as value. Print the dictionary.
Access the value of a key that exists and one that does not exist
Update the value of an existing key in a dictionary.
Delete a key from a dictionary using:
del
pop()
Find the number of key–value pairs in a dictionary.
Print only:
keys
values
key–value pairs
 """
students={20:"Shivanshu",
          21:"Jatin",
          22:"Sutam",
          23:"Nitish",
          24:"shubham",
          25:"Abhinash"}
print(students)

print(students[25])
print(students.get(26))

students[23]="Shivam"
print(students)

del students[24]
print(students)

print(students.pop(25))


print(len(students))
print(students.keys())
print(students.values())
print(students)

for key,value in students.items():
    print(f"{key}:{value}")