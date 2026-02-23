# Create a Car class with attributes brand, model, price.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display(self):
        print(f"{self.brand} {self.model} costs ₹{self.price}")

# Create a Student class with method get_grade() based on marks.

class Student:
    def __init__(self, marks):
        self.marks = marks

    def get_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

# Create a BankAccount class with deposit() and withdraw() methods.
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

# Write a class Employee that initializes name, id, salary using __init__.
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

# Create a class that counts how many objects are created.
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

# Create a class Company with a class variable company_name.
class Company:
    company_name = "TechCorp"

# Implement a static method to validate email format.
import re

class Validator:
    @staticmethod
    def validate_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))

print(Validator.validate_email("pateladshiv@gmail.com"))
# True

print(Validator.validate_email("invalid@email"))
# False


# Inheritance Create a base class Vehicle and derived class Bike.
class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

# Create Person → Employee → Manager (multilevel inheritance).
class Person:
    def __init__(self, name):
        self.name = name

class Employee2(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee2):
    def __init__(self, name, emp_id, dept):
        super().__init__(name, emp_id)
        self.dept = dept

# Override a method in child class and call parent method using super().
class Animal:
    def speak(self):
        print("Animal make sound.")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog Barks")


# Encapsulation Create a class BankAccount with private balance.
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance   # private variable

    # Getter method
    def get_balance(self):
        return self.__balance

    # Setter method
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")


# acc = BankAccount(1000)
#
# acc.deposit(500)
# acc.withdraw(200)
#
# print("Balance:", acc.get_balance())
#
#
# #acc.set_balance(-500)   # invalid




# Use getter and setter methods to update balance safely.
# Prevent negative salary using property decorators.

# Polymorphism Create a Shape class with method area().
import math

class Shape:
    def area(self):
        pass

# Implement Circle and Rectangle.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Demonstrate method overloading using default arguments.
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Demonstrate operator overloading (__add__).
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

# Create Engine class and use it inside Car class.
class Engine:
    def start(self):
        print("Engine started")

class CarWithEngine:
    def __init__(self):
        self.engine = Engine()

    def start_car(self):
        self.engine.start()
        print("Car started")

# Create Team class that contains multiple Player objects
class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            print(p.name)




print("\n--- Car ---")
car1 = Car("Toyota", "Fortuner", 3500000)
car1.display()

print("\n--- Student ---")
student1 = Student(85)
print("Grade:", student1.get_grade())



print("\n--- Employee ---")
emp = Employee("Shivanshu", 101, 50000)
print(emp.name, emp.emp_id, emp.salary)

print("\n--- Counter ---")
c1 = Counter()
c2 = Counter()
c3 = Counter()
print("Objects created:", Counter.count)

print("\n--- Company ---")
print("Company Name:", Company.company_name)

print("\n--- Email Validator ---")
print(Validator.validate_email("test@gmail.com"))
print(Validator.validate_email("invalid@email"))

print("\n--- Vehicle & Bike ---")
bike = Bike()
bike.start()
bike.ride()

print("\n--- Multilevel Inheritance ---")
manager = Manager("Rahul", 201, "IT")
print(manager.name, manager.emp_id, manager.dept)

print("\n--- Method Override ---")
dog = Dog()
dog.speak()



print("\n--- Shapes ---")
circle = Circle(5)
rect = Rectangle(4, 6)
print("Circle Area:", circle.area())
print("Rectangle Area:", rect.area())

print("\n--- Calculator ---")
calc = Calculator()
print(calc.add(5))
print(calc.add(5, 3))
print(calc.add(5, 3, 2))

print("\n--- Operator Overloading ---")
n1 = Number(10)
n2 = Number(20)
n3 = n1 + n2
print("Sum:", n3.value)

print("\n--- Composition (Engine) ---")
car_engine = CarWithEngine()
car_engine.start_car()

print("\n--- Team & Players ---")
team = Team()
team.add_player(Player("Virat"))
team.add_player(Player("Rohit"))
team.add_player(Player("Gill"))
team.show_players()
