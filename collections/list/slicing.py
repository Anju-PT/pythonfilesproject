#slicing

lst=[10,25,30,35,40,45,50,60]
print(lst[1])
print(lst[4])
print(lst[1:4])#only execute up to upperlimit-1(n-1)


print(lst[2:7])#
print(lst[3:5])#35 40
print(lst[2:])# 2 to end of list
print(lst[:5])#0 t0 upper-1

print(lst[:])#full list

print(lst[-1])#60
print(lst[-3])#50
print(lst[0]+lst[-2])#10+50=60
print(lst[-3:-1])
print(lst[-1:-4])#error
print(lst[-3:])
print(lst[:-3])

#linear search
#binary search