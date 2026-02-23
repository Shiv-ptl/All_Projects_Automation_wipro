#variable - used to store the data
#instance variable- global variable to the class
# local variable - scope inside the method only

#instance variable example
class Student:
    #class variable
    school = "St. Alosias School"

    def __init__(self,name,marks):
        self.name= name     #instance variable or global variable
        self.marks = marks  #instance variable or global variable

    def show(self):
        schoolcity= "Lucknow"   # local variable - scope inside the method only
        print(self.marks,self.name)
        print(schoolcity)
        print(self.school)

s1 = Student("Shivanshu",87)
s2 = Student("Jatin",79)
s1.show()
s2.show()

class Rectangle:
    def __init__(self,L,W):
        self.length = L
        self.width = W

    def Area(self):
        area= self.length*self.width
        Parameter = 2*(self.width+self.length)
        print(f"Area of rectangle of Length {self.length} and width {self.width} is ",area)
        print(f"Parameter of rectangle of Length {self.length} and width {self.width} is ", Parameter)


R1=Rectangle(5,6)
R1.Area()
R1=Rectangle(3.14,77.88)
R1.Area()
# a=[]
# for i in range(0,2,1):
#     a[i]= Rectangle(input("Enter the Length :"),input("Enter the width"))
#
# for i in range(0,2,1):
#     a[i].Area()
