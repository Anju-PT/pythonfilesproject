#break
#used to exit from loop

for i in range(1,51):
    if(i==25):
        break
    print(i)
print("outside loop")
#1 to 24

#continue
#only skip the condition and control go again to loop
for i in range(1,51):
     if(i==25):
        continue
     print(i)
# #1 to 24 26 to 50
#
# #pass
# #do nothing
num=int(input("enter a number"))
if(num%2==0):
     print(num)
else:
     pass
