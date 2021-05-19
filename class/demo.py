# class MyClass:
#     x=5
# p1=MyClass()
# print(p1.x)
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # print(self.name)
        # print(self.age)
    def myfun(self):
        print(self.name," is",self.age,"years")
p1=Person("john",36)
# print(p1.name)
# print(p1.age)
p1.myfun()