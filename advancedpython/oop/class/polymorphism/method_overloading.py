#method overloading
#same method different parameters
class Student:
    def set(self,name,rollno,dept,mark):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.mark=mark
        print("Name      ::",self.name)
        print("Rollno    ::", self.rollno)
        print("Department::", self.dept)
        print("Mark      ::", self.mark)
class Child(Student):
    def set(self,sname,sage):
        self.sname=sname
        self.sage=sage
        print("Name:",self.sname,"\nAge",self.sage)
ch=Child()
ch.set("anju",23)#only it will work because currently in python method overloading is not working
#ch.set("anju",23,"python",230) ##it will show error becuase overloading is not working
st=Student()
st.set("anju",23,"python",230)