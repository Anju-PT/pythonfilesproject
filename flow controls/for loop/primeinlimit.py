limit=int(input("enter a limit"))
flag=0
for num in range(1,(limit+1)):
    if(num>1):
       for i in range(2,num):
            if(num % i)==0:
                flag+=1
            else:
                flag+=0

       if(flag==0):
            print(num)
       flag=0



