#operator polymorphism means that the same operator behave differently for diff data types or the objects

#+ add number
#+ joins the strings
#+ meerges the lists
#operator overloading in python
#python
'''
__add__()
__sub__()
__mul__()
__eg__()
__it__()
__gt__()
'''

class Number:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value+other.value

n1=Number(100)
n2=Number(5.5)
print(n1+n2)

class Demo:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return self.x == other.x

a = Demo(5)
b = Demo(5)

print(a == b)


class Demo:
    def __init__(self, x):
        self.x = x

    def __truediv__(self, other):
        return self.x / other.x

a = Demo(10)
b = Demo(2)

print(a / b)
