l=int(input("enter limit"))

for i in range(0,l):
    for j in range(1,l-i):
        print(end=" ")
    for k in range(0,i):
        print("*",end=" ")
    print()
#output
#enter limit:3
#   *
#  * *
# * * *