lst=[]
prime=[]
flag=0

for i in range(1,101):
    lst.append(i)
for i in lst:
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                flag+=1
                break
    else:
        continue

    if(flag==0):
        prime.append(i)
    flag=0
print(prime)







