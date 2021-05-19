#multilevel Inheritance/hierarchial inheritance

# class Parent:
#     def m1(self):
#         print("inside Parent")
# class Child(Parent):
#     def m2(self):
#         print("inside Child")
# class Subchild(Child):
#     def m3(self):
#         print("inside subchild")
#
# su=Subchild()
# su.m3()
# su.m2()
# su.m1()
class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print("Name::",self.name)
        print("Age::",self.age)
        print("Gender::",self.gender)
class Clg(Person):
    def det(self,clgname,dept,cgpa):
        self.clgname=clgname
        self.dept=dept
        self.cgpa=cgpa
    def prints(self):
        print("Collage::",self.clgname)
        print("Department::",self.dept)
        print("CGPA::",self.cgpa)
class Placement(Clg):
    def dets(self,compname,desig,sal):
        self.compname=compname
        self.desig=desig
        self.sal=sal
    def print(self):
        print("Name::",self.name)
        print("Age::",self.age)
        print("Gender::",self.gender)
        print("Collage::",self.clgname)
        print("Department::",self.dept)
        print("CGPA::",self.cgpa)
        print("Company::",self.compname)
        print("Designametion::",self.desig)
        print("Salary::",self.sal)
pl=Placement()
pl.details("anju",23,"female")
pl.det("MCT","CSE",6.5)
pl.dets("Luminar","PythonDeveloper",25000)
# pl.printval()
# pl.prints()
pl.print()