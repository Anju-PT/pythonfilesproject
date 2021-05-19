lst=[1,2,4,5,6,7,3,2,3,1,10]
s=[]
for i in lst:
    if i not in s:
        s.append(i)
print(s)
l=len(lst)

#output
#[1, 2, 4, 5, 6, 7, 3, 10]
