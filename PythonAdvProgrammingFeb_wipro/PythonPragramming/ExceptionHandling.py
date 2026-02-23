#Exceptions- run time errors which will disrupt the normal program flow
#benifits:-
#helps in debugging
#prevent programing crashing
#handling errors and exceptions in the code more efficiently

#try except
#try- code to be executed
#except - exceptions details catching
#else - if the exception does not occur then else part will be exicuted
#finally - mandated code
#custom exceptions

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second numver : "))
    print(a/b)
except ZeroDivisionError:
    print("Can not divide by zero")
except ValueError:
    print("Please enter valid number")

#generic exception
try:
    a= 10/2
except Exception as e:
    print(e)
#runs only if no exception occurs
else:
    print("Division Successful")
#mandatory code
finally:
    print("Close the browser")

#custom exp
age = int(input("Enter the age: "))
if age<18:
    raise ValueError("Age must be 18 or above")