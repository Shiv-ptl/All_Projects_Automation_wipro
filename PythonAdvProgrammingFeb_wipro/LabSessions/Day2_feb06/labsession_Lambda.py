# 1
from functools import reduce

from PythonPragramming.Lamda import square
from PythonPragramming.List import even_nums

nums = [1, 2, 3, 4, 5, 6]
#
# From a list of numbers:
# Filter even numbers
# Square them
# Find their sum

even_nums=list(filter(lambda x:x%2==0,nums))
print(even_nums)
square = list(map(lambda x:x*x,even_nums))
print(square)
sum = reduce(lambda x,y:x+y,square)
print(sum)


# 2.
salaries = [25000, 40000, 32000, 18000]
#
# From a list of salaries:
# Filter salaries > 30, 000
# Add 10 % hike
# Find the total payout
greaterSal = list(filter(lambda x:x>30000,salaries))
print("salaries greater than 30000 are : ",greaterSal)

hike10= list(map(lambda x:x+x/10,greaterSal))
print("after 10 % hike :",hike10)

total_payout= reduce(lambda x,y:x+y,hike10)
print("Total payout: " ,total_payout)
