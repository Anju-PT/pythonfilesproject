f=open("E:\customer","r")
dic={}
ls=[]
for lines in f:
    data=lines.rstrip("\n").split(",")
    ls.append(data[4])
print(ls)
for i in ls:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    print(i,":",dic[i])