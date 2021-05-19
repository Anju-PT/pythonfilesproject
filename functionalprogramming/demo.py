#functional programming

#to reduce length of a code

#lambda function
#map function
#filter
#list comprehension

#lamba functions are anonymous functions(nameless function)

# def add(num1,num2):
#     return(num1+num2)
# print(add(10,20))
# f=lambda num1,num2:num1+num2
# print(f(10,20))
# f=lambda num1,num2:num1-num2
# print(f(50,10))
# f=lambda num1,num2:num1*num2
# print(f(10,5))
# d=lambda num1,num2:num1/num2
# print(d(50,10))

#map
#we need operation on each objects
#each objects need corresponding output
#ls=[10,20,30,40] ==>f(x)  [100,400,900,1600]

#[ab,ae,cd,ae,fg]==>f(x) [AE,AE,CD,AE,FG]

#filter

#lst=[1,2,3,4,5,6,7,8,9] ==>f(x) [2,4,6,8]
#[ab,ae,cd,ae,fg] ==>f(x) [ab,ae,ae]


#syntax

# map(fn,iterable)
#
# filter(fn,iterable)
# lst=[1,2,3,4,5,6,7,8,9]
# # def sqr(num):
# #     return(num*num)
# # s=list(map(sqr,lst))
# # print(s)
# s=list(map(lambda num:num*num,lst))
# print(s)

#filter
# lst=[1,2,3,4,5,6,7,8,9,10]
# # def even(num):
# #     return num%2==0
# # ev=list(filter(even,lst))
# # print(ev)
# ev=list(filter(lambda num:num%2==0,lst))
# print(ev)


#list comperhension
# ls=[]
# def ele(num):
#     if(num>0):
#         ele(num-1)
#         ls.append(num)
# ele(50)
# print(ls)
# lst=[]
# for i in range(1,51):
#     lst.append(i)
# print(lst)

# lst=[i for i in range(1,51)]
# print(lst)
#print range condition


# lst=[i for i in range(1,51) if i%2==0]
# print(lst)
# lst=[i*i if i%2==0 else i*i*i for i in range(1,51)]
# print(lst)
#print condition range

lst=[(i,"even") if i%2==0 else (i,"odd") for i in range(1,51)]
print(lst)

