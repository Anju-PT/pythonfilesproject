line="hai hello hai hello hai"

#split
words=line.split(" ")
print(words)

dic={}
for i in words:
    if(i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
# for i in dic:
#     print
l=0
for i in dic:
    if(dic[i]>l):
        l=dic[i]
print(i,":",l)
s=0
s=len(dic)
print(s)
d=2
for i in dic:
    if(dic[i]<=d):
        d=dic[i]
print(i,":",d)

