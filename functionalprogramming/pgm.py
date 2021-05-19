lst1=[7,8,9,4,3,1]#if num>5 print num+1 else num-1
# l=len(lst1)
# for i in range(0,l):
#     if(lst1[i]>5):
#         lst1[i]+=1
#     else:
#         lst1[i]-=1
# print(lst1)

lst=[(i+1) if i>5 else (i-1) for i in lst1]
print(lst)
op=list(map(lambda num:num+1 if num>5 else num-1,lst1 ))
print(op)