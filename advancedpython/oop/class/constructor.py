#constructor = to initialise instance variable

#constructor automatically invoke when creating object

# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printval(self):
#         print(self.name,self.age,self.gender)
# pe=Person("anju",26,"female")
# pe.printval()

class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def printval(self):
        print(self.name,self.id,self.salary)
e1=Employee("anju",1001,25000)
e1.printval()