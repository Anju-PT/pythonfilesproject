a="hey"
b="hhello"
flag=0
print("\ncommon elements in a and b:",end=" ")
for i in a:
    # for j in b:
    #     if(i==j):
    #        print(i)
     if(i in b):
        print(i,end=" ")
print()
print('elements in a not in b:',end=" ")
for i in a:
    if(i not in b):
        print(i,end="")
     # if (i not in b):
     #     print(i)
         #in : used behalf of ==
         #not in:used behalf of !=
