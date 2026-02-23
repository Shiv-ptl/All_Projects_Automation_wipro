#many forms
#same method /fun name will behave differently depending on the
#object type
#input argments
#class implementation

#object type
print(len("python"))
print(len([1,2,3,4]))
print(len({1,2,3,4,5}))

#input arguments no of arguments/data type

class Cal:
    def add(self,a,b=0,c=0):
        return a+b+b

c = Cal()
print(c.add(5))
print(c.add(2,3))


#runtime poly.. is only supported
#achieved mathod overriding - child class method will override the parent class meethod

class Animal:

    def sound(self):
        print("Animal makes sound...")

class Dog(Animal):
    def sound(self):
        print("Dog Barks..")

a = Dog()
a.sound()