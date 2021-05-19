lst=[2,3,5,6,7,8,9,10]
num=int(input("enter element to be searched"))
if(num in lst):
    print("element found")
else:
    print("not found")

flag=0
for i in lst:
    if(i==num):
        flag=1
        break
    else:
        pass
if(flag>0):
    print("element found")
else:
    print("element not found")
#linear search
#program complexity increases in linear search

#binary search
#-------------
