empty_list=[]
nums=[1,2,3,4,5,0,8,3]
mixdata=[1,"Shiv",3.14,"pie",85,0]
print(nums[1])

print(nums)
nums.insert(0,11)
print(nums)
nums.append("shiv")
print(nums)
nums.remove(5)
print(nums)

print(mixdata)

for i in mixdata:
    print(i)

for i,x in enumerate(mixdata):
    print(f"At index : {i}  ,value is {x}")

for i,x in enumerate(mixdata,start=1):
    print(f"At index : {i}  ,value is {x}")

nums.clear()
print(nums)

mylist=['a','b','c','d','e','f','g']
print(mylist)

print(mylist[2:5])
print(mylist[:4])

numbers=[1,3,5,7]
even_nums=[2,4,6,8,10]
numbers.extend(even_nums)
print(numbers)

a=[12,32,34,26,11,4,35]
print(a)
print("laegest num; ",max(a))  #largest value in a list

res=[]
for i in a:                     #remove even values from the list
    if i % 2 != 0:
        res.append(i)

print(res)

result=1
for i in a:
    result *= i                 #multiply each item of the list

print(result)


# 1. Which of the following data types allows duplicate elements?
# A. Set
# B. Dictionary keys
# C. List
# D. All of the above
#C
# 2. Which collection is unordered and does not allow duplicate values?
# A. List
# B. Tuple
# C. Dictionary
# D. Set
#D
# 3. What is the output type of {} in Python?
# A. List
# B. Set
# C. Dictionary
# D. Tuple
#C
# 4. Which of the following allows access using a key?
# A. List
# B. Set
# C. Dictionary
# D. Tuple
#C
# 5. Which operation is NOT supported by sets?
# A. Union
# B. Intersection
# C. Indexing
# D. Difference
#C
# 6. Which data structure is best suited for fast lookups?
# A. List
# B. Set
# C. Dictionary
# D. Tuple
#C
# 7. What will be the output?
# a = [1, 2, 2, 3]print(len(a))
# A. 3
# B. 4
# C. Error
# D. 2
#A
# 8. What will be the output?
# s = {1, 2, 2, 3}print(len(s))
# A. 4
# B. 3
# C. 2
# D. Error
#B
# 9. Which of the following is mutable?
# A. List
# B. Dictionary
# C. Set
# D. All of the above
#D
# 10. Which data type stores elements as key–value pairs?
# A. List
# B. Tuple
# C. Set
# D. Dictionary
#D