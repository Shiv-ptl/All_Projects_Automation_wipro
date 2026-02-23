

def sq(num):
    return num*num

print(sq(5))

#function pass
def func_pass():
    pass

func_pass()

def cal(a,b):
    return a-b, a+b,a*b

add,sub,mul = cal(10,5)
print(add,"\n",sub,"\n",mul)

def areaofrect(len,width):
    return len*width

def areaofsquare(side):
    return side*side

val = areaofrect(4,6)
print(val)

print(areaofsquare(val))


print(areaofsquare(areaofrect(2,4)))

#fun with a loop
def even(limit):
    for i in range (2,limit+1,2):
        print(i)

even(10)

#fun with if else condition
def even(limit):
    for i in range (1,limit+1):
        if i%2==0:
            print(i)
        else:
            print(0)

even(10)