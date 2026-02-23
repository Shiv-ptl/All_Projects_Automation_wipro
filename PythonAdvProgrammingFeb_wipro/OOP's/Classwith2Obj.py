#constructor  - first func of the class called when an object of the class is created
#syntax    __init__()
#we can parameterise the constructers
#self is mendatory



class Student:
    def __init__(self):
        print("Constructor is called....")

    def addSum(self):
        print("Adding 2 numbers..")

s1 = Student()
s1.addSum()

#PARAMETERISED CONSTRUCTOR
#self.name is a instance variable or a global variable (belong to object )
#name is a local variable (exists inside the method)
#if we dont assign it to the self.name the obj will not remember the value

class Employee:
    def __init__(self,name,Salary):
        self.name=name
        self.salary= Salary

    def display(self):
        print(self.name,self.salary)

e1 = Employee("shiv", 54332)
e2 = Employee("abc",123432)

e1.display()
e2.display()

#using * args in constructors
#constructor overloading is supported by *args keyword
#we can use any number of parameters to the constructor using *args

class Numbers:
    def __init__(self,* args):
        self.values = args

    # def sum(self,values):
    #     self.total+=int(values)

n =Numbers(10,20,30)
print(n.values)

m=Numbers(3,4)
print(m.values)
#print(m.sum)

#parent and child constructor
#super keyward for accessing parent constructor

class Parent:
    def __init__(self):
        print("I am Parent Constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("I am child constructor")

c= Child()

class Child1(Child):
    def __init__(self):
        super().__init__()
        print("I am child constructor")

d= Child1()