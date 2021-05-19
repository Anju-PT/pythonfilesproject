ls=[]
f=open("numbers","r")
for number in f:
    # ls.append(int(number))
    ls.append(int(number.rstrip("\n")))
    # print(number)
print(ls)
s=0
print(sum(ls))
for i in ls:
    s+=i
print("sum:",s)

#rstrip

#lstrip

s="hello\n"
s1=s.lstrip("h")
print(s1)



