#tuples

#1.define using paranthesis ()
# tp=()
# print(type(tp))
#
# #using function
# tp=tuple()

tp1=(1,10.5,'anju',True,False)#2.it support hetrogeneous data
print(tp1)
tp2=(1,2,3,10,5,7,10.5,5.5,"luminar","abcd",True)#3.insertion order preserved
print(tp2)
tp3=(1,1,2,2,3,3,True,True,"ancd","abcd")#4.support duplicates
print(tp3)
tp3(2)=10 #immutable can not update
print(tp3)