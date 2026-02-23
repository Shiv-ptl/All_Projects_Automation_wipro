#descriptors- control the access of the objrct attributs
#_get_()
#_set_()
#_delete()

class Desc:
    def __get__(self, instance, owner):
        print("Getting the value")
        return 10

class Test:
    x = Desc()

t = Test()
print(t.x)
#this is called non-data descriptor - uses only the __get__ descriptor

#data desc uses both get and set method

class myDes:
    def __get__(self, instance, owner):
        return instance._Value

    def __set__(self, instance, value):
        print("Setting the value..")
        instance._Value=value

class Test:
    x = myDes()

t = Test()
t.x = 100
print(t.x)

class Name:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        instance._name = value

    def __delete__(self, instance):
        print("Deleting the value.")
        del instance._name

class Person:
    name = Name()

p = Person()
p.name = "Shivanshu Patel"
del p.name
