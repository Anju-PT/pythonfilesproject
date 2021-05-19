class Employee:
    comp="Luminar technolab"#static variable
    def setval(self,name,age,id,desig,salary,exper):
        self.name=name
        # self.comp=comp
        self.age=age
        self.id=id
        self.desig=desig
        self.salary=salary
        self.exper=exper
    def printval(self):
        print("_______Employee Details_______")
        print("Employee Name:",self.name)
        print("Age:",self.age)
        print("company Name:", Employee.comp)
        print("Employee ID:", self.id)
        print("Designation:",self.desig)
        print("Salary:",self.salary)
        print("Experience:",self.exper)

e1=Employee()
e1.setval("Anju",26,10558,"Python Developer","25000","2 year")
e1.printval()

#two types of variables

#1.static variable=related to class ---- use class name to call

#2.instance variable=related to methods ----use self to call