num=int(input("enter a num"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag+=1

if(flag>0):
    print(num,"is not prime")
else:
    print(num,"is prime")