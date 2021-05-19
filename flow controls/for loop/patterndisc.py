for i in range(0,4):
    for j in range(1,4-i):
        print(end="  ")
    for k in range(0,i+4):
        print("*",end="   ")
    print()
for i in range(4,0,-1):
    for j in range(0,4-i):
        print(end="  ")
    for k in range(i+4,1,-1):
        print("*",end="   ")
    print()
