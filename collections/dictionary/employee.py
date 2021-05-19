dic={"id":2001,"name":"anju","desig":"developer","salary":25000}
print("name:",dic["name"])
if("company" not in dic):
    dic["company"]="luminar"
print(dic)
dic["salary"]+=5000
for i in dic:
    print(i,":",dic[i])
