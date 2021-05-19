#single inheritance
class Person:#parent class/base class/super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):#child class/derived class/sub class
    def det(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def prints(self):
        print(self.rollno)
        print(self.school)

per=Person()
per.details("anju",20,"female")
per.printval()
st=Student()
st.det(8,"St.joseph's HSS")
st.prints()
st.details("ammu",22,"male")
st.printval()