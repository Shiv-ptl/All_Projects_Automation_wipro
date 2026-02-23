#1.Handle FileNotFoundError Exception When Opening a File
import json
try:

    with open("C://Users//LENOVO//PycharmProjects//PythonAdvProgrammingFeb_wipro//DataFormats//employee.json","r")as file:
        data = json.load(file)
    print(data)

except FileNotFoundError:
    print("Requested file not found!!!!")
else:
    print("File found successfully")

# 2.write a program to handle invalid user input
import math
try:
    a = int(input("enter a number to find its squareroot: "))
    if a < 0:
        print("Enter a non-negative integer only")
    else:
        sq=math.sqrt(a)
        print(sq)

except ValueError:
    print("Enter Integer only")
# 3.Write a Python program that generates random alphabetical characters, alphabetical strings, and alphabetical strings of a fixed length. Use random.choice()

import random
import string

char = random.choice(string.ascii_letters)
print("Random alphabetical character:", char)


import random
import string

length = random.randint(5, 10)   # random length
rand_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

print("Random alphabetical string:", rand_string)


import random
import string

def random_string_fixed_length(n):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

print("Fixed length string:", random_string_fixed_length(8))
