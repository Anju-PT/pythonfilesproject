for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    # for k in range(0,i):
    #     print("*",end=" ")
    # print()

    for k in range(0,i):
        print(i,end=" ")
    print()
#output
#     1
#    2 2
#   3 3 3
#  4 4 4 4
# 5 5 5 5 5
