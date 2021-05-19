class Max:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark
        print("Name::",self.name)
        print("Rollno::", self.rollno)
        print("Course::", self.course)
        print("Mark::", self.mark)
dic={}
c=0
f=open("stud","r")
for lines in f:
    ln=lines.rstrip("\n").split(",")
    dic[c]=ln
    c+=1
# print(dic)
m=dic[0][3]
d=0
# print(m)
for k,v in dic.items():
    if(v[3]>m):
        m=v[3]
        d=k
    else:
        pass

name=dic[d][0]
roll=dic[d][1]
cour=dic[d][2]
mar=dic[d][3]
print("Details of student with highest mark\n----------------------------")
ob=Max(name,roll,cour,mar)

