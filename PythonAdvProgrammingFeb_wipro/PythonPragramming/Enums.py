#Enumareters- returns index and value as a pair
# enumarates(intrables,start=0)
#loop over iterable and get both index and the value at the same index


fruits = ["orange","cherry","kiwi"]

for index,fruit in enumerate(fruits):
    print(index,fruit)

#enumerate with start value change
for index,fruit in enumerate(fruits,start=1):
    print(index,fruit)

word= "python"
for i,ch in enumerate(word):
    print(i,ch)

word= "Shivanshu"
for i,ch in enumerate(word,start=2):
    print(i,ch)

fruits = ("orange","cherry","kiwi")
for index,fruit in enumerate(fruits):
    print(index,fruit)

#real time scenario
teat_cases=["login","signup","checkout"]
for case_no,test in enumerate(teat_cases,start=1):
    print(f"Executing Testcase {case_no}: {test}")

a=['God','is','Grate']
b = enumerate(a)
nxt_val=next(b)
print(nxt_val)

#duplicaate ditection using enumerate
characters =["Krillin", "Goku", "Goku", "Gohan", "Piccolo",
             "Krillin", "Goku", "Vegeta", "Gohan", "Piccolo",
             "Piccolo", "Goku", "Vegeta", "Goku","Piccolo"]
character_map = {character: [] for character in set(characters)}

for index,character in enumerate(characters):
    character_map[character].append(index)

print(character_map)


# 1. What is the main purpose of enumerate() in Python?
# A. To generate random numbers
# B. To iterate with both index and value
# C. To sort elements
# D. To filter values
#B

# 2. Which of the following does enumerate() return?
# A. List
# B. Tuple
# C. enumerate object
# D. Dictionary
#C

# 3. What is the default starting index of enumerate()?
# A. 1
# B. -1
# C. None
# D. 0
#0

# 4. Which syntax is correct for enumerate()?
# A. enumerate(start, iterable)
# B. enumerate(iterable, start)
# C. enumerate(iterable)
# D. Both B and C
#D

# 5. Which of the following iterables can be used with enumerate()?
# A. List
# B. Tuple
# C. String
# D. All of the above
#D

# 6. What will list(enumerate(['a', 'b'])) produce?
# A. List of strings
# B. List of indexes
# C. List of tuples
# D. Dictionary
#C

# 7. Which of the following is the most Pythonic way to loop with index?
# A. for i in range(len(data))
# B. for i, v in enumerate(data)
# C. for i in data
# D. for v in index(data)
#B

# 8. Can enumerate() be used with files?
# A. No
# B. Only with lists
# C. Only with tuples
# D. Yes
#D

# 9. What is the type of each item produced by enumerate()?
# A. List
# B. Dictionary
# C. Tuple
# D. Set
#C

# 10. Which keyword is commonly used to unpack enumerate() values?
# A. key, value
# B. index, value
# C. count, element
# D. All of the above
#D

# 11. What does the start parameter in enumerate() do?
# A. Stops iteration
# B. Changes step size
# C. Sets the starting index
# D. Limits the range
#C

# 12. Which of the following is TRUE about enumerate()?
# A. It modifies the original iterable
# B. It consumes high memory
# C. It provides index automatically
# D. It works only on lists
#C

# 13. What happens if start is set to 5 in enumerate()?
# A. Indexing starts from 0
# B. Indexing starts from 5
# C. It raises an error
# D. It skips first 5 elements
#B

# 14. Which loop is best for printing line numbers from a file?
# A. for line in file
# B. for i in range(file)
# C. for i, line in enumerate(file)
# D. for i in len(file)
#C

# 15. enumerate() is mainly used to replace which pattern?
# A. for x in list
# B. for i in range(len(list))
# C. while loop
# D. recursion
#B