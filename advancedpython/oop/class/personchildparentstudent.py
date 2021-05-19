class Person:
    def persset(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print("Name::",self.name)
        print("Age::",self.age)
        print("Gender::",self.gender)

class Parent(Person):
    def pareset(self,job,place,salary):
        self.job=job
        self.place=place
        self.salary=salary
        print("Job::",self.job)
        print("Place::",self.place)
        print("Salary::",self.salary)

class Child(Person):
    def chilset(self,school):
        self.school=school
        print("School::", self.school)

class Student(Child):
    def studset(self,rollno):
        self.rollno=rollno
        print("Roll No::", self.rollno)

st=Student()
st.persset("anju",23,"female")

st.chilset("St.Joseph's")
st.studset("8")
pa=Parent()
pa.pareset("python","kakkanad",30000)
pa.persset("amru",23,"female")