class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # def printval(self):
    #     print("Name::",self.name)
    #     print("Age::",self.age)
class Student(Person):
    def __init__(self,name,age,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        super().__init__(name,age)
    def print(self):
        print("Name::", self.name)
        print("Age::", self.age)
        print("Rollno::",self.rollno)
        print("Mark::",self.mark)

st=Student("anju",23,8,87)
# st.printval()
st.print()
