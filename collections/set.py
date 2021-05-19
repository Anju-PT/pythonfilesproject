#set
#set={}#it creates dictionary not as set
#only using set function

st=set()
print(type(st))

st={2,5,7,8,10}
print(st)
st1={2,"anju",3.5,True,False}#it support hetrogenous data
print(st1)
#insertion order not preserved
st2={1,1,2,2,5,5,3,3,"luminar","luminar",True,True}
print(st2)#it not supported duplicates value
st3={True,False,1,0}
print(st3)
st4={10,9,8,7,6,5,4,3,2,1}
print(st4)
st4.remove(10)#set is mutable
print(st4)