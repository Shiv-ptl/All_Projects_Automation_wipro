# lambda function- anonymous(nameless)function ,one linen, used for simole operations

#function- function name , arguments,return type,code

# lambda arguments:expression
#rules:-
# it can have any num of arguments
#must have only one expression
#the expression is automatically returned

#normal fun to add two numbers
def add(a,b):
    return a+b

print(add(5,7.8))

sum= lambda a, b,c: print(a + b+c)
sum(5,7.8,-2)

check_even_odd = lambda x: print("Even") if x % 2 == 0 else print("Odd")
check_even_odd(5)
check_even_odd(6)

max = lambda a,b: a if a>b else b
print(max(12,23))

#important inbuilt fun in lambda - filter,map,reduce
#filter - select data - filter the data
#map- transform the data
#reduce- aggregate the data

#filter

numbers= [1,2,3,4,5,6,7,8,9,10]
even_nums= list(filter(lambda x:x%2==0,numbers))
print(even_nums)

nums = [-5, 10, -3, 7, 0, 2]
positive_nums=list(filter(lambda x:x>=0,nums))
print(positive_nums)

data = ["hello", "", "world", "", "python"]
non_empty=list(filter(lambda x:x!="",data))
print(non_empty)


#reduce - aggrigate (combining many values to a one single result

from functools import reduce
nums = [-5, 10, -3, 7, 1, 2, 50]
print(reduce(lambda x,y: x+y,nums))
#multiply
print(reduce(lambda x,y:x*y,nums))
#max value
print(reduce(lambda x,y: x if x>y else y,nums))
#min value
print(reduce(lambda x,y: x if x<y else y,nums))

#MAP - transform the data - the fun is applied to every element
nums = [-5, 10, -3, 7, 1, 2, 50]
square= list(map(lambda x:x*x,nums))
print(square)

#sorting in lambda

data=[(1,3),(4,1),(2,2),(0,0)]
sorteddata = sorted(data,key = lambda x:x[1])
print(sorteddata)

marks= {"A": 75,"B":90,"C":60}
sorted_marks= dict(sorted(marks.items(),key=lambda x:x[1]))
print(sorted_marks)

# 1.
# What
# will
# be
# the
# output
# of
# the
# following
# code?
#
# print(list(map(lambda x: x + x, [1, 2, 3])))
#
# A.[1, 2, 3]
#
# B.[2, 4, 6]
#
# C.[1, 4, 9]
#
# D.Error
#

#B
# 2.
# What
# does
# the
# following
# code
# return?
#
# print(list(filter(lambda x: x, [0, 1, False, True, 2])))
#
# A.[0, 1, False, True, 2]
#
# B.[1, True, 2]
#
# C.[0, False]
#
# D.Error
#
#B
# 3.
# Which
# of
# the
# following
# lambda functions is INVALID?
#
# A.
# lambda x: x * 2
#
# B.
# lambda x, y: x + y
#
# C.
# lambda x: x if x > 0 else -x
#
# D.
# lambda x:
# return x * 2
#
#D

# 4.
# What
# will
# be
# the
# output?
#
# nums = [1, 2, 3, 4]
#
# print(list(map(lambda x: x % 2 == 0, nums)))
#
# A.[2, 4]
#
# B.[False, True, False, True]
#
# C.[True, False]
#
# D.Error
#
#B

# 5.
# What happens if filter() receives a lambda that returns non - boolean values?
#
# A.Raises TypeError
#
# B.Only True is allowed
#
# C.Non - zero / non - empty values are treated as True
#
# D.Code will not execute
#
#C


# 6.
# What
# will
# be
# printed?
#
# from functools import reduce
#
# print(reduce(lambda x, y: x * y, [1, 2, 3, 4], 2))
#
# A.
# 24
#
# B.
# 48
#
# C.
# 12
#
# D.Error
#
#B
# 7.
# What is the
# output?
#
# print(list(filter(lambda x: x > 2, map(lambda x: x + 1, [1, 2, 3]))))
#
# A.[2, 3, 4]
#
# B.[3, 4]
#
# C.[4]
#
# D.[]
#
#B
# 8.
# Which
# statement
# about
# map() and filter() is TRUE?
#
# A.They
# return lists
# by
# default
#
# B.They
# modify
# the
# original
# iterable
#
# C.They
# return iterator
# objects
#
# D.They
# work
# only
# with lambda
#
#B
#         9. What will be the output?
#
#         print(list(map( lambda x: x.upper(), filter(lambda x: x.islower(), "PyThOn"))))
#
# A.['P', 'Y', 'T', 'H', 'O', 'N']
#
# B.['y', 'h', 'n']
#
# C.['Y', 'H', 'N']
#
# D.Error
#
#C
# 10.
# Which
# of
# the
# following
# best
# describes
# reduce()?
#
# A.Filters
# values
#
# B.Maps
# one - to - one
#
# C.Aggregates
# iterable
# into
# single
# value
#
# D.Sorts
# elements
#
#C
# 11.
# What
# will
# be
# the
# output?
#
# print(list(map(lambda x: x[0], ["python", "java", "c++"])))
#
# A.['p', 'j', 'c']
#
# B.['python', 'java', 'c++']
#
# C.['n', 'a', '+']
#
# D.Error
#
#A
# 12.
# Which
# scenario is BEST
# suited
# for filter()?
#
# A.Doubling
# all
# values
#
# B.Converting
# data
# types
#
# C.Selecting
# values
# based
# on condition
#
# D.Merging
# elements
#
#C
# 13.
# What is the
# output?
#
# nums = [1, 2, 3]
#
# f = map(lambda x: x * 2, nums)
#
# nums.append(4)
#
# print(list(f))
#
# A.[2, 4, 6]
#
# B.[2, 4, 6, 8]
#
# C.Error
#
# D.[2, 4]
#
#B
# 14.
# Which
# of
# the
# following is NOT
# a
# valid
# use
# case
# for lambda ?
#
#            A.Sorting keys
#
#            B.Complex multi-line logic
#
#            C.Short one-time functions
#
#            D.Inline transformations
#
#B
#            15. What will be the output?
#
#            print(list(filter(None, [0, "", None, 5, "Hi"])))
#
#
#            A.[0, "", None]
#
#            B.[5, 'Hi']
#
#            C.['', 'Hi']
#
#            D.Error

#B