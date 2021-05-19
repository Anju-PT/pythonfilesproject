#multiple inheritance:2 parent and 1 child
# class Parent1():#parent
#     def m1(self):
#         print("Inside Parent1")
# class Parent2():#child
#     def m2(self):
#         print("Inside Parent2")
# class Child(Parent1,Parent2):#subchild
#     def m3(self):
#         print("Inside Child class")
#
# ch=Child()
# ch.m3()
# ch.m2()
# ch.m1()

# class Person:
#     def details(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def printval(self):
#         print("Name::",self.name)
#         print("Age::",self.age)
#         print("Gender::",self.gender)
# class Clg:
#     def det(self,clgname,dept,cgpa):
#         self.clgname=clgname
#         self.dept=dept
#         self.cgpa=cgpa
#     def prints(self):
#         print("Collage::",self.clgname)
#         print("Department::",self.dept)
#         print("CGPA::",self.cgpa)
# class Placement(Clg,Person):
#     def dets(self,compname,desig,sal):
#         self.compname=compname
#         self.desig=desig
#         self.sal=sal
#     def print(self):
#         print("Company::",self.compname)
#         print("Designametion::",self.desig)
#         print("Salary::",self.sal)
# pl=Placement()
# pl.details("anju",23,"female")
# pl.det("MCT","CSE",6.5)
# pl.dets("Luminar","PythonDeveloper",25000)
# pl.printval()
# pl.prints()
# pl.print()


class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

class Clg:
    def set(self,clgname,dept,cgpa):
        self.clgname=clgname
        self.dept=dept
        self.cgpa=cgpa

class Placement(Person,Clg):
    def se(self,compname,desig,sal):
        self.compname=compname
        self.desig=desig
        self.sal=sal
    def print(self):
        print("Name::",self.name)
        print("Age::",self.age)
        print("Gender::",self.gender)
        print("Collage::", self.clgname)
        print("Department::", self.dept)
        print("CGPA::", self.cgpa)
        print("Company::",self.compname)
        print("Designametion::",self.desig)
        print("Salary::",self.sal)
pl=Placement()
pl.setval("anju",23,"female")
pl.set("MCT","CSE",6.5)
pl.se("Luminar","PythonDeveloper",25000)
pl.print()