#1.Write a Python function to check whether a number falls within a given range.


#2. Write a Python function to Print even numbers from 1 to 50
def print_even_num():
    for i in range (2,51,2):
        print (i)

print_even_num()

#3. Write a Python function to Sum of numbers from 1 to 100
def sum1to100():
    total=0
    for i in range(1,101):
        total+=i
    return total
print(sum1to100())



#4. Print all numbers divisible by 5 between 1 and 100
for i in range(5,101,5):
    print(i)

#5.Create a list of numbers from 50 to 100 with a step of 5
numbers = list(range(50,101,5))
print(numbers)

#6. Print the square of each number from 1 to 10.
for i in range(1,11):
    print(i*i)


#7. Print numbers between -10 and 10.
for i in range(-10,11):
    print(i)