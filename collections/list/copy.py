#import copy
l7=[]

lst=["anju","amru","athuu"]
l1=lst[:]
l2=list(lst)
# l3=copy(lst)
# l4=copy.copy(lst)
# l5=copy.deepcopy(lst)
l6=[e for e in lst]
l7.extend(lst)
print(l1)
print(l2)
# print(l3)
# print(l4)
# print(l5)
print(l6)
print(l7)