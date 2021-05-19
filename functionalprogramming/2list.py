lst1=[10,20,21,22,23]#check both are same
lst2=[20,21,10,22,23]
c=[]
# for i in lst1:
#     if i in lst2:
#         c.append(i)
#     else:
#         print("lists are different")
# if(c==lst1):
#     print("lists are same")
#--------------------------------------
# l1=sorted(lst1)
# l2=sorted(lst2)
# if(l1==l2):
#     print("same")
#--------------------------------
# if(len(lst1)==len(lst2)):
#     se=list([i if i in lst2 else print("different") for i in lst1])
#     if(se==lst1):
#         print("same")
# else:
#     print("different length")
#----------------------------------

[print("same") if sorted(lst1)==sorted(lst2) else print("different")]

