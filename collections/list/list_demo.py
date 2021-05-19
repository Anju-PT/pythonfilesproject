# #list
# #------
#
# lst=[] #empty list
#
# print(type(lst))#which class
#
#
# #using list function
# #list
# #-----
#
# sa=list()
# print(type(sa))

#2support hetrogeneoud data

# lst=[1,10.5,"anju","luminar",True,False]
# print(lst)
#
ls=[10,1,15,28,108,0,8,1,10.5,35,20.8,"anju","luminar","python","course",True] #insertion order is preserved
# print(ls)

# lst=[10,10,20,20,30,25,10,20,"anju","anju",True,True]#support dupicates
# print(lst)

#index
#index range start from 0 to n-1
print(ls[0])
print(ls[11])

ls[2]=100
print(ls)
ls[11]="spark"
ls[0]="luminar"#list is mutable
print(ls)