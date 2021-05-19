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
print("students with highest mark\n____________________________")
f=open("max","r")
details=[]
for lines in f:
    ln=lines.rstrip("\n").split(",")
    # print(ln)
    name=ln[0]
    rollno=int(ln[1])
    dept=ln[2]
    mark=int(ln[3])
    st=Student(name,rollno,dept,mark)
    details.append(st)
m=0
for i in details:
    if i.mark>m:
        m=i.mark
print(m)
for i in details:
    if(i.mark==m):
        print(i)


