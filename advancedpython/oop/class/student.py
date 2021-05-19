class Student():
    def setval(self,name,course,branch,regno,percentage):
        self.name=name
        self.branch=branch
        self.course=course
        self.regno=regno
        self.percentage=percentage
    def printval(self):
        print("Name:",self.name)
        print("course:",self.course)
        print("Branch:",self.branch)
        print("Register No:",self.regno)
        print("Percentage:",self.percentage)
p1=Student()
p1.setval("anju","Btech","CSE",110558,70)
p1.printval()