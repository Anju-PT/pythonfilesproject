# class Student:
#     def __init__(self,name,rollno,dept,mark):
#         self.name=name
#         self.rollno=rollno
#         self.dept=dept
#         self.mark=mark
#     def printval(self):
#         print("Name      ::",self.name)
#         print("Rollno    ::", self.rollno)
#         print("Department::", self.dept)
#         print("Mark      ::", self.mark)
#         print()
# print("Details of student with mark above 190\n______________________________________")
# f=open("studdetails","r")
# for lines in f:
#     ln=lines.rstrip("\n").split(",")
#     if(int(ln[3])>190):
#         name=ln[0]
#         rollno=ln[1]
#         dept=ln[2]
#         mark=ln[3]
#         st=Student(name,rollno,dept,mark)
#         st.printval()


class Student:
    def __init__(self,name,rollno,dept,mark):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.mark=mark
    def printval(self):
        print("Name      ::",self.name)
        print("Rollno    ::", self.rollno)
        print("Department::", self.dept)
        print("Mark      ::", self.mark)
        print()
    def __str__(self):
        return self.name
print("students with mark above 190\n____________________________")
f=open("studdetails","r")
details=[]
for lines in f:
    ln=lines.rstrip("\n").split(",")
    name=ln[0]
    rollno=int(ln[1])
    dept=ln[2]
    mark=int(ln[3])
    st=Student(name,rollno,dept,mark)
    details.append(st)
for i in details:
    if i.mark>190:
        print(i)