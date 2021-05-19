# class Student:
#     def setval(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
#
# st=Student()
# f=open("student","r")
# for lines in f:
#     ln=lines.rstrip("\n").split(",")
#     st.setval(ln[0],ln[1])

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("Name",self.name)
        print("Age", self.age)
    def __str__(self):
        return self.name


f=open("student","r")
for lines in f:
    ln=lines.rstrip("\n").split(",")
    name=ln[0]
    age=ln[1]
    st=Student(name,age)
    print(st)
    st.printval()