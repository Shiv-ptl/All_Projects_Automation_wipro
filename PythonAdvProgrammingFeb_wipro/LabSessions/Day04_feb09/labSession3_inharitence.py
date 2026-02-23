# 1.Write a Python program to create a class representing a
# Circle. Include methods to calculate its area and perimeter

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        self.area = 3.14*self.radius*self.radius
        print("Area of circle ->",self.area)

    def Parameter(self):
        self.Par = 3.14*2*self.radius
        print("Parameter of circle ->",self.Par)

c = Circle(5)
c.area()
c.Parameter()


# 2.Write a Python program to create a person class. Include
# attributes like name, country and date of birth. Implement
# a method to determine the person's age.
from  datetime import date
class Person:
    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob  # YYYY,MM,DD

    def Cal_Age(self):
        today = date.today()
        age = today.year - self.dob.year
        if (today.month, today.day) <(self.dob.month,self.dob.day):
            age -=1
        return age

    def display(self):
        print(f"Name : {self.name} ,Country : {self.country} , Date of Birth : {self.dob}, Age : {self.Cal_Age()}")

a = Person("Shivanshu Patel","India",date(2003,3,12))
print(a.Cal_Age())
a.display()


# 3.Write a Python program to create a class that represents
# a shape. Include methods to calculate its area and perimeter.
# Implement subclasses for different shapes like circle, triangle,
# and square.
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print("Circle Area =", math.pi * self.r * self.r)

    def perimeter(self):
        print("Circle Perimeter =", 2 * math.pi * self.r)


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print("Square Area =", self.side * self.side)

    def perimeter(self):
        print("Square Perimeter =", 4 * self.side)

c = Circle(5)
c.area()
c.perimeter()

s = Square(4)
s.area()
s.perimeter()
# 4.Write a python program to create a child class Bus that will
# inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display(self):
        print("Vehicle Name:", self.name)
        print("Max Speed:", self.max_speed)
        print("Mileage:", self.mileage)


class Bus(Vehicle):
    pass   # Inherits everything from Vehicle

b1 = Bus("Tata", 80, 6)

b1.display()

# 5.Write a python program to create  a Vehicle class without
# any variables and methods
class Vehicle:
    pass

v1 = Vehicle()

print("Vehicale class")
