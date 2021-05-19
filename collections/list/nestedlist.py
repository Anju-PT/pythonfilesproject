lst=[[1001,"arun",25,1000],
     [1002,"arjun",26,2000],
     [1003,"vimu",27,3000],
     [1004,"binu",28,4000]]
#l=len(lst)
# print(lst)
# for i in range(0,l):
#     print(lst[i])
# for i in lst:
#     print(i)
# for i in lst:
#     print(i[1])
# for i in lst:
#     if(i[3]>2000):
#         print(i[1])
sum=0
for i in lst:
    sum+=i[3]
print(sum)