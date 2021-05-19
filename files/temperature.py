f=open("E:\Temperature","r")
dic={}
ls=[]
# for lines in f:
#     data=lines.rstrip("\n").split(" ")
#     ls.append(data)
# # print(ls)
# for i in ls:
#     if(i[0] not in dic):
#         dic[i[0]]=i[1]
#     else:
#         if(int(i[1])>int(dic[i[0]])):
#              dic[i[0]]=i[1]
# for i in dic:
#     print(i,":",dic[i])

for lines in f:
    data=lines.rstrip("\n").split(" ")
    if(data[0] not in dic):
        year=data[0]
        dic[year]=data[1]
    else:
        year=data[0]
        temp=int(data[1])
        if(int(dic[year])<temp):
            dic[year]=str(temp)
for i in dic:
    print(i,":",dic[i])

