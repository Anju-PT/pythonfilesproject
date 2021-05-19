# #data structures
#
# #used to store data
#
# #stack
#
# #push =add element
# #pop=remove element
# l=int(input("enter the size of the stack"))
# lst=[]
# def pushs(num):
#     lst.append(num)
#     print(lst)
# def pops():
#     lst.pop()
#     print(lst)
# while(True):
#     print("---enter the operation wants to perform----")
#     p=int(input("press:1.Push 2.Pop"))
#     if(p==1):
#         if(len(lst)<l):
#             num1=int(input("enter the number to push"))
#             pushs(num1)
#         else:
#             print("list limit reached")
#     elif(p==2):
#         if(len(lst)==0):
#             print("list empty")
#         else:
#             pops()
#     else:
#         print("invalid operation")

stk=[]
size=int(input("enter size of stack"))
top=0
n=0
def push():
    global top,size
    if(top>=size):
        print("stack is full")
    else:
        p=int(input("enter num to pop"))
        stk.append(p)
        top+=1
        print(stk)
def pop():
    global top,size
    if(top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top-=1
        print(stk)
while(n!=1):
    print("enter the operation wants to perform")
    op=int(input("press: 1.Push 2.Pop 3.exit"))
    if(op==1):
        push()
    elif(op==2):
        pop()
    elif(op==3):
        break
    else:
        print("invalid operation")



