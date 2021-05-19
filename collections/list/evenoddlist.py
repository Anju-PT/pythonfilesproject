lst=[]
for i in range(1,101):
    lst.append(i)
print(lst)
even=[]
odd=[]
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)