#add
#
# def add(num1,num2):#parameter1,parameter2
#     return num1+num2
#
# res=add(10,20)
# print(res)
#
# def add_three(num1,num2,num3):
#     return num1+num2+num3
#
# def add_four(num1,num2,num3,num4):


#snake notation name_length

#camlin notation nameLength

# def add(*args):
#     # print(args)
#     # print(type(args)) #it takes arguments as tuple
#     res=0
#     for num in args:
#         res+=num
#     return res
#
# print(add(10,20))


# def print_employee(**kwargs):
#     print(kwargs)
#     for k,v in kwargs.items():
#         print(k,"=>",v)
#
# print_employee(id=200,name="anju",loc="kakkanad",sal=30000)


arr=[3,11,8,10,12]
# arr.sort # method
# print(arr)
# arr.sort(reverse=True)
# print(arr)
se=sorted(arr) #function
print(se)
se=sorted(arr,reverse=True)
print(se)