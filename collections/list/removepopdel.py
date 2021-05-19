#removed,pop,delete difference


list=[1,2,3,4,5]
list.remove(3)#removes the first value/object, does not do anything with indexing
print(list)
lst=[1,2,3,4,5]
del list[4]#remove the item at a specific index does not return anything
print(lst)
ls=[1,2,3,4,5]
s=list.pop(3)#remove the item at a specific index and return its value
print(s)
print(list)