class Student:
    school="St. Joseph's HSS"
    def setval(self,name,age,id,mark):
        self.name=name
        self.age=age
        self.id=id
        self.mark=mark
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.mark)
        print(Student.school)
s1=Student()
s1.setval("anju",15,1008,606)
s1.printval()