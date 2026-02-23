#class is  the blue print or templete
# describes the state /behaviour of its object
#data is put in variable
#behaviour is put in function

class Students:

    #data or the properties
    stuName = "Shivanshu"
    stuId = 1685
    #self is used to access the attributes of the class we have defined
    #it is automatically loaded
    #self represents the instance of the class
    #create a fun to access the data
    def displyStu(self):
        print("Name ->  ",self.stuName)
        print("ID -> ",self.stuId)

#creating object of the class
a=Students()
a.displyStu()

#wap to create a clss for employee <id,name,address,empdepartment>, function
#write a program to create a class for an employee - with data - emp id , emp name , emp  dept and create function to display the data with 2 objects

class Employees:
    def getdata(self,empId,empName,empAdd,empDep):
        self.empId = empId
        self.empName = empName
        self.empAdd = empAdd
        self.empDep = empDep

    def displayData(self):
        print("Employee ID ->",self.empId,"\t|| Employee Name -> ",self.empName,"\t|| Employee Address-> ",self.empAdd,"\t|| Employee Department -> ",self.empDep)

emp1=Employees()
emp2 = Employees()

emp1.getdata(1001,"Shivanshu","Lucknow","IT")
emp2.getdata(1002,"Nitin","Delhi","HR")

emp1.displayData()
emp2.displayData()