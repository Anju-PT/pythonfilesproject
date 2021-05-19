lst=[3,10,5,7,2,4,8,1,9]
#num=len(lst)
temp=0
for i in lst:
    if(i>i+1):
        temp=i
        i=j
        j=temp
print(lst)




# for i in range(num):
#     for j in range(i+1,num):
#         if(lst[i]>lst[j]):
#             temp=lst[i]
#             lst[i]=lst[j]
#             lst[j]=temp
# print(lst)