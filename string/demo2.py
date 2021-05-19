a="hello world"
l=input("enter a alphabet")
flag=0
for st in a:
    if(st==l):
       flag+=1

if(flag>0):
    print("present")
else:
    print("not present")