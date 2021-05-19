# reduce() #cant use reduce() directly
#it is in functools module not in builtin
# lst=[2,4,6,8,10]
#
# res=list(map(lambda num:num**2,lst))
# print(res)


#only pass number values
import functools
list=[7,8,9,4,3,2]
#in map & filter ,lambda have 1 argument
#lambda 2 args
total=functools.reduce(lambda no1,no2:no1+no2,list)
print(total)
highest=functools.reduce(lambda no1,no2:no1 if no1>no2 else no2,list)
print(highest)




