#Dictionary
#------------
#how to define
# dic={}
# print(type(dic))

#key : value pairs

#name:luminar,loc:kakkanad,course:python

#key: name,loc,course

#value:luminar,kakkanad,python

#key:value
# dic={"name":"luminar","loc":"kakkand","course":"python","marks":250,"data":10.758}#supprort hetrogeneous data
# print(dic)

#insertion order is preserved
#
# dic={"name":"luminar","loc":"kakkanad","age":25,"age":30}#it does not support duplicate keys
# print(dic)

dic={"name":"luminar","loc":"kakkanad","age":25,"mark":25}
print(dic)#support duplicate value but not duplicate key
#
# print(dic["name"])#collect value using the key
# print(dic.get("name"))
# print(dic["loc"])
# for i in dic:
#     print(i,":",dic[i])

#mutable
# dic["age"]=30
# # print(dic)
#
# dic["mark"]+=25
# print(dic)

#
# #delete
# del dic["name"]
# print(dic)
# s=dic.pop("age")
# print(s)
# print(dic)

#total :150
print("total" in dic)
dic["total"]=150
print(dic)

