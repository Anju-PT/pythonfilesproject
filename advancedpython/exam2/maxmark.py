class Student:
    def __init__(self,name,rollno,course,mark):

        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
        f1.write(self.name)
        f1.write(',')
        f1.write(str(self.rollno))
        f1.write(',')
        f1.write(self.course)
        f1.write(',')
        f1.write(str(self.mark))
        f1.write('\n')
    def maxmark(self):
         print("Details of student with highest mark")
         print("------------------------------------")
         print("Name::",self.name)
         print("Rollno::",self.rollno)
         print("Course::",self.course)
         print("Mark::",self.mark)
m=0
max=[]
f1=open("max","a")
s1=Student("Anu",1,"BCA",200)
s2=Student("Rahul",2,"BBA",177)
s3=Student("Rahul",2,"BBA",177)
s4=Student("Ajay",4,"BCA",198)
s5=Student("Maya",5,"BBA",195)
f=open("max","r")
details=[]
for lines in f:
    ln=lines.rstrip("\n").split(",")

    name=ln[0]
    rollno=int(ln[1])
    dept=ln[2]
    mark=int(ln[3])
    # st=Student(name,rollno,dept,mark)
    # details.append(st)

# m=0
# for i in details:
#     if i.mark>m:
#         m=i.mark
#     print(m)
