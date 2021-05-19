age=int(input("enter ur age"))
sex=input("enter sex(M/F)")
status=input("enter marrital status(Y/N)")
if(sex=="F")&(20<=age<=60):
    print("Work only in urban areas")
elif(sex=="M")&(20<=age<=40):
    print("work in anywhere")
elif(sex=="M")&(40<age<=60):
    print("Work only in urban areas")
else:
    print("error")

