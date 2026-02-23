#single inheritence
#parent ----> child class  properties from the parent class are aquired by child class

class Employee:     #parent class
    def __init__(self,name,empid):
        self.name=name
        self.empid=empid


    def empdetails(self):
        print(self.name,self.empid)

class Manager(Employee):        #child class
    def approve_leave(self):
        print("leave approved")

#creating the obj of child class to get inheritance in picture
m = Manager("Shivanshu Patel",1685)
m.empdetails() #from parent class
m.approve_leave()#from child class