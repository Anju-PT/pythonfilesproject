# # for num in range(-2,-5,-1):
# #     print(num,end=" ")
#
#
#  x=0
# for i in range(10):
#     for j in range(-1,-10,-1):
#         x+=1
#         print(x)
#
# a,b=12,5
# if a+b:
#     print("true")
# else:
#     print("false")
#     # a+b is real number only false when 0
#
# for l in 'john':
#     if l=='o':
#         pass
#     print(l,end=" ")

#10
var=10
for i in range(10):
    for j in range(2,10,1):
        if(var%2==0):
            continue
            var+=1
    var+=1
else:
    var+=1
print(var)


#interview questions
#--------------------
# def ff(x):
#     x+=1
#
# x=1
# ff(x)
# print(x)

# a=5
# b=25/5
# if a is b:
#     print(a)
# else:
#     print(a is b)