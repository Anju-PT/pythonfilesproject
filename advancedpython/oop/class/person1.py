class Person():
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self,gender):
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)

p1=Person()
p1.setval("anju","26")
p1.printval("Female")

