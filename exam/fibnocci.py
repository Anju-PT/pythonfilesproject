s=0
l=1
c=2
n=0
limit=int(input("enter limit"))
if(limit<=0):
    print("incorrect input")
elif(limit==1):
    print(s,end=" ")
    #print(l,end=" ")
else:
    print(s, l,end=" ")
    while(c<limit):
        n=s+l
        print(n,end=" ")
        s=l
        l=n
        c+=1




