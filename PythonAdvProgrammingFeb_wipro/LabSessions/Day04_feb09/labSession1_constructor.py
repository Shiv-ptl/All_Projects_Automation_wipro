# Create a class Book with attributes title and author.
# Create 3 different book objects and print all details.
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author= author

    def displayDetails(self):
        print(f"Book Title - '{self.title}' Author Name - '{self.author}'")

b1 = Book("Fairy Tail","Abc")
b2 = Book("Harry Potter","Xyz")
b3 = Book("Game of thrones","R.R.Martin")

b1.displayDetails()
b2.displayDetails()
b3.displayDetails()


# Create a class Rectangle with a constructor that takes length and width and stores area and perimeter as object attributes.
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
