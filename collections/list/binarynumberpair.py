ls=[0,1,2,3,7,4,9,8,6,5]
lst=sorted(ls)
l=len(lst)
num=int(input("enter a number"))
s=0
for i in range(0,l//2-1):
    for j in ls:
        s=lst[i]+j
        if(s==num):
            print(lst[i],j)
        else:
            pass


