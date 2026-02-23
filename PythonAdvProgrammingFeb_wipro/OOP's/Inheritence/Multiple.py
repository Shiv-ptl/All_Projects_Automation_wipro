# parent class1     parent class2
#             \    /
#              \  /
#               \/
#          child class

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1 , Parent2):
    pass

class Father:
    def Drive(self):
        print("Father has skill to Drive a Car")

class Mother:
    def Cook(self):
        print("Mother has skill to cook")

class Child(Father ,Mother):
    def bothSkills(self):
        print("Child has the skill to play Drums...")
        print("Child has both skills of driving and cooking")

c = Child()
c.Drive()
c.Cook()
c.bothSkills()