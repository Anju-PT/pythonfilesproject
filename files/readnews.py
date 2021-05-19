f=open("newscutting","r")
ls=[]
dic={}
# s=f.split(" ")
# for lines in f:
#     s=lines.rstrip("\n").split(" ")
#     print(s)
#     ls.append(s)
# print(ls)
for word in f:
    s=word

   # ls.append(word)
ls=s.split(" ")
print(s)
print(ls)
for i in ls:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
for i in dic:
    print(i,":",dic[i])
# print(dic.items())
for k,v in dic.items():#items() method with out loop
    print(k,",",v)