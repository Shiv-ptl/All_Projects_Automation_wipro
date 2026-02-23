# 1.Write a Python program to sort a list of tuples using Lambda
data=[(1,3),(4,1),(2,2),(0,0)]
sorteddata = sorted(data,key = lambda x:x[1])
print(sorteddata)
sorteddata = sorted(data,key = lambda x:x[0])
print(sorteddata)
data=[(1,3,6),(4,1,7),(2,2,8),(0,0,9)]
sorteddata = sorted(data,key = lambda x:x[2])
print(sorteddata)


# 2.Write a Python program to extract year, month, date and time using Lambda.
from datetime import datetime

print(
    (lambda d: (d.year, d.month, d.day, d.strftime("%H:%M:%S")))(datetime.now())
)

# 3.Write a Python script to concatenate the following dictionaries to create a new one.
dict1 = {1: "A", 2: "B"}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

new_dict = {}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)

print("Concatenated Dictionary:", new_dict)

result = {**dict1,**dict2,**dict3}
print(result)



