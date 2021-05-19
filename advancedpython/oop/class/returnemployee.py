class Employee:
    def setval(self,name,id,comp,desig,sal):
        self.name=name
        self.id=id
        self.comp=comp
        self.desig=desig
        self.sal=sal
        print("Name::",self.name)
        print("Id::", self.id)
        print("company::", self.comp)
        print("Designation::", self.desig)
        print("Salary::", self.sal)
    def __str__(self):
        return self.name+str(self.id)

em=Employee()
em.setval("anu",1004,"Luminar","Python developer",25000)
print("Returned name::",em)