class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Name::",self.name)
        print("Age::",self.age)
        print("gender::",self.gender)
class Student(Person):
    def studset(self,clg,deptment,cgpa):
        self.clg=clg
        self.deptment=deptment
        self.cgpa=cgpa
        print("Collage Name::",self.clg)
        print("Department::",self.deptment)
        print("CGPA::",self.cgpa)
class Child:
    def chset(self,company,place):
        self.company=company
        self.place=place
        print("Company Name::",self.company)
        print("Place::",self.place)
class Employee(Person,Child):
    def empset(self,dept,salary):
        self.dept=dept
        self.salary=salary
        print("Department::",self.dept)
        print("Salary::",self.salary)
class Placement(Student):
    def plaset(self,comp,deptm,sal):
        self.comp=comp
        self.deptm=deptm
        self.sal=sal
        print("Company::",self.comp)
        print("Department::",self.deptm)
        print("Salary::",self.sal)


s1=Student()
s1.setval("Anju",24,"Female")
s1.studset("MCT","CSE",7.5)
e1=Employee()
e1.setval("Ammu",21,"Female")
e1.chset("Luminar","Kakkanad")
e1.empset("Python",30000)
p1=Placement()
p1.setval("Arjun",23,"Male")
p1.studset("Christ","IT",8.2)
p1.plaset("Infosys","PHP",35000)
