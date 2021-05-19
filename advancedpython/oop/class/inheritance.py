#inherirance: inheritance allow us to define a class that inherits
# all the methods and properties from another class

#parent class
#is the class being inherited from,also called base class/super class

#child class
#is the class that inherits from another class,also called derived class/sub class

#single inheritance:a class can be derived from one base class

# class Base=> class Derived(Base)

#multiple Inheritance:
# a class can be derived from more than one base class
# class Base1 => class Base2 =>class Derived(Base1,Base2)

#multilevel/hierarchical Inheritance:
# features of base class and derived class are inherited to
# the new derived class
# class Base => class Derived1(Base) =>class Derived2(Derived1)



#pass,classname.__init__,super()
class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name,self.age,self.gender)

class Student(Person):
    def __init__(self,name,age,gender,year):
        super().__init__(name,age,gender)
        self.year=year
        # Person.__init__(self,name,age,gender)
    def print(self):
        print(self.name,self.age,self.gender,self.year)


    # pass
p1=Student("anju",26,"female",2021)
p1.print()