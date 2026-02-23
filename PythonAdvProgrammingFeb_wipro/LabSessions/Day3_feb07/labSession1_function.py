# 1.Write a Python function to sum all the numbers in a list.
nums = [23,45,32,56,33,34,-12,0,66]

def sumele(a):
    return sum(a)

print(sumele(nums))

def sumlist(a):
    total=0
    for i in a:
        total+=i
    return total

print(sumlist(nums))


# 2.Write a Python function to find the maximum of three numbers.

def maxin3(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c

print(maxin3(-4,-2,-6))