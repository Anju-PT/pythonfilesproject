# def num(l,u):
#     if(l<u):
#         print(l)
#         l+=1
#         num(l,u)
#
# num(1,101)

def printno(u):
    if(u>0):
        printno(u-1)
        print(u)
        # printno(u-1)
printno(100)
