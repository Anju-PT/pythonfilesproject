#180-200 a+
#168-179 a
#148-159 b+

mark1=int(input("enter mark of sub 1"))
mark2=int(input("enter mark of sub 2"))
mark3=int(input("enter mark of sub 3"))
mark4=int(input("enter mark of sub 4"))
total=mark1+mark2+mark3+mark4
print("total mark:",total)
if(total>=180)&(total<=200):
    print("A+")
elif(total>=160)&(total<=179):
    print("A")
elif(total>=140)&(total<=159):
    print("B+")
elif(total>=120)&(total<=139):
    print("B")
elif(total>=100)&(total<=119):
    print("C+")
elif(total>=80)&(total<=99):
    print("c")
elif(total>=68)&(total<=79):
    print("D+")
else:
    print("fail")