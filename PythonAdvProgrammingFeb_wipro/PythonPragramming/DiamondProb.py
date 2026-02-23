class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show()
print(D.mro())


#using super()
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(A):
    def show(self):
        super().show()
        print("Class C")

class D(B, C):
    def show(self):
        super().show()
        print("Class D")

obj = D()
obj.show()


