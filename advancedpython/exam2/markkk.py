class Student:
    def __init__(self,name,rollno,dept,mark):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.mark=mark

    def print(self):
        print("Details of student with highest mark \n __________________________________")
        print("Name::",self.name)
        print("rollno::",self.rollno)
        print("dept::",self.dept)
        print("mark::",self.mark)
    def __str__(self):
        return self.name+","+str(self.rollno)+","+self.dept+","+str(self.mark)
lst=[["Anu",1,"BCA",200],["Rahul",2,"BBA",177],["Vinod",2,"BBA",187],["Ajay",4,"BCA",198],["Maya",5,"BBA",195]]


m=lst[0][3]
for i in lst:
    if(i[3]>m):
        m=i[3]
for i in lst:
    if(i[3]==m):
        name=i[0]
        rollno=i[1]
        dept=i[2]
        mark=i[3]

ob=Student(name,rollno,dept,mark)
ob.print()

#
# # print(lst)
# # print(s1)