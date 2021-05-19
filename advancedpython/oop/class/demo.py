#class
#design pattern

#object
#real world entity


#reference
# name that refers a memory location of a object(temporary memory space)
# =to access class using object(unique references for each objects)

#class

#keyword class name must start capital letter
#syntax :: class Person:
# class Person:
#     def print(self):
#         print("inside print method")
# pe=Person()
# pe.print()

class Person:
    def print(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Details:",self.name,self.age,self.gender)
p1=Person()
p1.print("anju",26,"Female")

p2=Person()
p2.print("amru",26,"Female")
p3=Person()
p3.print("athu","28","Female")
