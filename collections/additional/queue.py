que=[]
s=int(input("enter the size of the queue::"))
top=0
def insert():
    global top,s,que
    if(top>=s):
        print("queue is full")
    else:
        p=int(input("enter num to inserted"))
        # que.append(p)
        que.insert(top,p)
        # top+=1
        for i in que:
            print(i)
        top+=1
def delete():
    global top,s,que
    if(top<=0):
        print("queue is empty")
    else:
        del que[0]
        # top-=1
        # print(que)
        top-=1
        for i in que:
            print(i)
while(True):
    print("enter the operation wants to perform")
    op=int(input("press: 1.insert 2.delete 3.exit"))
    if(op==1):
        insert()
    elif(op==2):
        delete()
    elif(op==3):
        break
    else:
        print("invalid operation")

# que=[]
# size=int(input("enter the size::"))
# front=0
# rear=0
# n=0
# def insert():
#     global front,rear,size,que
#     if(rear>=size):
#         print("queue is full")
#     else:
#         p=int(input("enter the element to inserted::"))
#         que.insert(rear,p)
#         rear+=1
#         for i in range(front,rear):
#             print(que[i])
# def delete():
#     global front,rear,size,que
#     if(rear<=0):
#         print("queue is empty")
#     else:
#         que.pop(front)
#         rear-=1
#         for i in range(front,rear):
#             print(que[i])
#         # print(que)
# while(True):
#     print("enter the operation wants to perform")
#     op=int(input("press: 1.insert 2.delete 3.exit"))
#     if(op==1):
#         insert()
#     elif(op==2):
#         delete()
#     elif(op==3):
#         break
#     else:
#         print("invalid operation")
