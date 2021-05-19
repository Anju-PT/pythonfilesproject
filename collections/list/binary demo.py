ls=[3,6,7,8,4,9,2,1]
lst=sorted(ls)
# print(lst)
# count=0
# low=0
# upper=len(ls)-1
# mid=low+upper//2
# element=int(input("enter element be searched"))
# if(element>lst[mid]):
#     low=mid+1
#     for i in range(low,upper+1):
#         if(lst[i]==element):
#             count=1
#             break
# elif(element<lst[mid]):
#     upper=mid-1
#     for i in range(low,upper+1):
#         if(lst[i]==element):
#             count=1
#             break
# elif(element==lst[mid]):
#     count=1
#
# else:
#     pass
# if(count>0):
#     print("element found")
# else:
#     print("element  not found")

low=0
upp=len(lst)-1
flag=0
element=int(input("enter element to be searched"))

while(low<=upp):
    mid=(low+upp)//2

    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upp=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag>0):
    print("element found")
else:
    print("not found")

