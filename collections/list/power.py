lst=[10,20,21,22,25,26,27,26]
s=len(lst)
c=1
#print(s)
res=0
# print(lst)

for i in lst:
    res=i**c
    c+=1
    print(res)
    # for j in range(1,s+1):
    #     res=i*j
    # print(res)
j=1
for i in range(0,s):
    res=lst[i]**j
    j+=1
    print(res)