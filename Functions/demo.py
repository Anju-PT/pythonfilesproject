# #functions
# #-----------
#
# #print
# #input
# #range
# #type
#
# #syntax
#
# #def functionname(argument1,argument2):
#     #funtion statement
#
# #call()  #using function name
#
# #1. function without argument and no return type
#
# #2.function with argument and no return type
#
# #3.function with arguments and return type
#
# #----------------------------------------
#
# #1. function without argument and no return type
#
# # def add():
# #     num1=int(input("enter num1"))
# #     num2=int(input("enter num2"))
# #     sum=num1+num2
# #     print(sum)
# # add()
#
# def mul():
#     num1=int(input("enter num1"))
#     num2=int(input("enter num2"))
#     mul=num1*num2
#     print(mul)
# mul()

#functional programming
#----------------------
#reduce the length of the program
#lambda
#map
#filter
#reduce
#list comperhension

#lambda : annonymous function :unknown function
# f=lambda num1,num2:num1+num2
# print(f(10,20))

#2.fun with argument no return type
#----------------------------------

# def sumn(num1,num2):
#     res=num1+num2
#     print(res)
# sumn(10,40)
#
# sumn(40,50)

# def div(num1,num2):
#     div=num1/num2
#     print(int(div))
# div(20,4)

#3. fun with argument and return type
#
# def sum(num1,num2):
#     res=num1+num2
#     return res
# data=sum(40,60)
# print(data)

def sub():
    num1=int(input("enter 1st num"))
    num2=int(input("enter 2nd num"))
    sub=num1-num2
    print(sub)

def sub2(num1,num2):
    sub=(num1-num2)
    print(sub)
def sub3(num1,num2):
    sub=num1-num2
    return sub

sub()
sub2(25,10)
s=sub3(25,10)
print(s)

