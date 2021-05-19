for i in range(0,5):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    for k in range(j+1,i+2):
        print(k,end=" ")
    print()

#output

# 1
# 2 1 2
# 3 2 1 2 3
# 4 3 2 1 2 3 4
# 5 4 3 2 1 2 3 4 5