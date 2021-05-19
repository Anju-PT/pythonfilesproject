low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))
evensum=0
oddsum=0
for i in range(low,(upp+1)):
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i

print("sum of even nos:",evensum)
print("sum of odd nos:",oddsum)
