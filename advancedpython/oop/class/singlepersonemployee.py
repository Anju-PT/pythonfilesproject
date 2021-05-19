class Person:
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print("Name::",self.name)
        print("Age::",self.age)
        print("Gender::",self.gender)
class Employee(Person):
    def det(self,id,comp,desig,sal):
        self.id=id
        self.comp=comp
        self.desig=desig
        self.sal=sal
    def prints(self):
        print("Employee id::",self.id)
        print("Company:: ",self.comp)
        print("Designation",self.desig)
        print("Salary::",self.sal)
# pe=Person()
# pe.details("anju",22,"female")
# pe.printval()
em=Employee()
em.det(1002,"Luminar","Python Developer",25000)
em.details("athu",23,"female")
em.printval()
em.prints()