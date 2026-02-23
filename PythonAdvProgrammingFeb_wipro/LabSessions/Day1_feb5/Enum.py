
#Q1 What is the output?

print(list(enumerate(['a', 'b', 'c'])))

#Q2 What is the output?

for i, v in enumerate([10, 20, 30]):
    print(i, v)

#Q3 Write code to print index + value from:Index should start from 1.

colors = ['red', 'green', 'blue']
for i, color in enumerate(colors, start=1):
    print(i, color)




#Q4 What is the output?

list(enumerate("PYTHON", start=1))


#Q5 Find the index of value 50 using enumerate():

nums = [10, 20, 30, 40, 50, 60]
for i, v in enumerate(nums):
    if v == 50:
        print(i)


#Q6 What is the output?

for i, n in enumerate(range(10, 60, 10)):
    print(i, n)

#Q7 Convert this into an enumerate() loop:

#for i in range(len(data)):
#   print(i, data[i])

#for i,value in enumerate(data):
#   print(i,value)

#Q8 What is printed?

items = ['a', 'b', 'c']

for i in enumerate(items):
    print(i)


#Q9 What is the output?

#list(enumerate([], start=5))  ---- []

#Q10 What is the output?

for i, v in enumerate([100, 200, 300], start=-1):
    print(i, v)

#Q11 What happens here?

#i, v = enumerate(['x', 'y', 'z'])

#Q12 Explain the difference:

#enumerate(data) ---- index start from 0

#enumerate(data, start=1) ---- index start form 1
