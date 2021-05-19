class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
class Dog(Animal):
    def __init__(self,name,type,breed,age):
        self.breed=breed
        self.age=age
        super().__init__(name,type)
    def printval(self):
        print("Name ::",self.name)
        print("Type ::",self.type)
        print("Breed::",self.breed)
        print("Age  ::",self.age)
d1=Dog("Dog","Domestic","German Sheperd",2)
d1.printval()