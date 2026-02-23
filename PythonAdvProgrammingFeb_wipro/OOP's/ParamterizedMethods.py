#default methods - builtin methods , user defined methods - method name,method body

#parametrized methods-

class Calculator:
    def add(self,a,b):
        print(a+b)

c = Calculator()
c.add(10,20)
c.add("Shivnshu"," Patel")
c.add(10,20)


#default parameters
class Test:
    def run(self,browser="chrome"):
        print("Running on....",browser)

t = Test()
t.run()
t.run("Firefox")

# * args parameterized methods
class Addition:
    def add(self,* args):
        print(sum(args))

s = Addition()
s.add(10,20,30)
s.add(10)

# class Action:
#     a=[12,10]
#     def Show(self,* args):
#         print(self.a.append(args))
#
# s = Action()
# s.Show(10,20,30)
# s.Show(10)

