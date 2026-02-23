"""Lab 1: Method Overriding with Inheritance
Create a base class Employee with a method calculate_salary().
Create a subclass Manager that overrides calculate_salary() and adds a bonus.
Demonstrate runtime polymorphism using parent class reference."""

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print("Employee Salary:", self.salary)


class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    # Method Overriding
    def calculate_salary(self):
        total = self.salary + self.bonus
        print("Manager Total Salary (with bonus):", total)


emp = Manager(70000, 8000)
emp.calculate_salary()


""" 
Lab 2: Polymorphism Using Function Arguments
Create classes Dog, Cat, and Cow each with a method speak().
Write a function animal_sound(obj) that calls speak().
Pass different objects to the same function."""


class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

class Cow:
    def speak(self):
        print("Cow moos")


def animal_sound(obj):
    obj.speak()

d = Dog()
c = Cat()
cw = Cow()

animal_sound(d)
animal_sound(c)
animal_sound(cw)

"""
Lab 3: Multilevel Inheritance with Polymorphism
Create Vehicle → Car → ElectricCar.
Each class overrides the method fuel_type().
Call the method using different object references."""

class Vehicle:
    def fuel_type(self):
        print("Vehicle uses general fuel")


class Car(Vehicle):
    def fuel_type(self):
        print("Car uses Petrol/Diesel")

class ElectricCar(Car):
    def fuel_type(self):
        print("Electric Car uses Battery")

v = Vehicle()
c = Car()
e = ElectricCar()

v.fuel_type()
c.fuel_type()
e.fuel_type()



""" 
Lab 4: Operator Overloading
Create a class BankAccount with attribute balance.
Overload + to add balances and > to compare balances.
Demonstrate polymorphic behavior of operators.
"""



"""
Lab 6: Multiple Inheritance and MRO
Create classes A, B, C, and D (diamond structure).
Override the same method in B and C.
Call method using D object and observe MRO.
 
Lab 7: Polymorphism with Exception Handling
Create Calculator class with divide().
Create SafeCalculator that overrides divide() and handles ZeroDivisionError.
Demonstrate method overriding.
 
 
Lab 8: Real-Time Payment System
Create base class Payment with method pay().
Create CreditCard, UPI, and NetBanking subclasses.
Use a single function to process all payments.
"""



#MCQ 11/02/2026
# ==============================
# 1: Constructors in Python
# ==============================

# 1. What will be the output?
# class A:
#     def __init__(self):
#         print("A Constructor")
#
# class B(A):
#     pass
#
# obj = B()
#
# A) Error
# B) A Constructor
# C) Nothing
# D) B Constructor
#B


# 2. What happens if a class does not define __init__()?
#
# A) Compilation error
# B) Default constructor is provided automatically
# C) Object cannot be created
# D) It inherits __init__ only if explicitly called
#B


# 3. What is true about constructors in Python?
#
# A) Multiple constructors are allowed
# B) Constructor name can be anything
# C) Constructor is executed automatically when object is created
# D) Constructor must return a value
#C

# 4. What will be the output?
# class Test:
#     def __init__(self):
#         print("Hello")
#
#     def __init__(self):
#         print("World")
#
# t = Test()
#
# A) Hello
# B) World
# C) Hello World
# D) Error
#B


# 5. If a parent class has a parameterized constructor, what must child class do?
#
# A) Nothing
# B) Must override constructor
# C) Must explicitly call parent constructor
# D) Cannot inherit
#C

# ==============================
# 2: Inheritance
# ==============================

# 6. What type of inheritance is this?
# class A: pass
# class B(A): pass
# class C(B): pass
#
# A) Multiple
# B) Multilevel
# C) Hierarchical
# D) Hybrid
#B

# 7. What will be the output?
# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     def show(self):
#         print("B")
#
# obj = B()
# obj.show()
#
# A) A
# B) B
# C) Error
# D) A B
#B


# 8. Which method determines method lookup order?
#
# A) dir()
# B) mro()
# C) help()
# D) isinstance()
#B

# 9. What is the diamond problem related to?
#
# A) Constructor overloading
# B) Multiple inheritance
# C) Method overriding
# D) Encapsulation
#B

# 10. What will be the output?
# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     def show(self):
#         print("B")
#
# class C(A):
#     def show(self):
#         print("C")
#
# class D(B, C):
#     pass
#
# obj = D()
# obj.show()
#
# A) A
# B) B
# C) C
# D) Error
#B

# ==============================
# 3: Polymorphism
# ==============================

# 11. Polymorphism means:
#
# A) Same function name with different behavior
# B) Different function names
# C) Multiple classes
# D) Data hiding
#A


# 12. What type of polymorphism is this?
# print(len("Hello"))
# print(len([1,2,3]))
#
# A) Method overriding
# B) Operator overloading
# C) Function overloading
# D) Duck typing
#D


# 13. What will be the output?
# class Animal:
#     def speak(self):
#         print("Animal speaks")
#
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
#
# a = Animal()
# d = Dog()
#
# a.speak()
# d.speak()
#
# A) Animal speaks
#    Animal speaks
#
# B) Animal speaks
#    Dog barks
#
# C) Dog barks
#    Animal speaks
#
# D) Error
#B

# 14. What is duck typing?
#
# A) Type checking using isinstance()
# B) Behavior-based polymorphism
# C) Constructor chaining
# D) Operator overloading
#B


# 15. What will be the output?
# class X:
#     def add(self, a, b):
#         return a + b
#
# x = X()
# print(x.add(5, 3))
# print(x.add("5", "3"))
#
# A) 8 and 8
# B) 8 and 53
# C) Error
# D) 8 and Error
#B


# 16. Which of the following supports operator overloading?
#
# A) add()
# B) init()
# C) str()
# D) call()
#A


# 17. What will be the output?
# class A:
#     def __init__(self):
#         print("A")
#
# class B(A):
#     def __init__(self):
#         print("B")
#
# obj = B()
#
# A) A
# B) B
# C) A B
# D) Error
#B

# 18. How to call parent constructor inside child constructor?
#
# A) parent()
# B) A.__init__(self)
# C) super().__init__()
# D) Both B and C
#D


# 19. What is method overriding?
#
# A) Same method name in same class
# B) Same method name in parent and child class
# C) Same variable name
# D) Multiple constructors
#B

# 20. What will be the output?
# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     pass
#
# obj = B()
# obj.show()
#
# A) A
# B) B
# C) Error
# D) Nothing
#A
