def fact():
    f=1
    num=int(input("enter a num"))
    for i in range(1,num+1):

        f=f*i
        #i=i-1
    print(f)
def fact2(num):
    f=1
    for i in range(1,num+1):
        f=f*i

    print(f)
def fact3(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f
fact()
fact2(5)
d=fact3(5)
print(d)

