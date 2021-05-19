def add(num1,num2):
    s=num1+num2
    print(num1,"+",num2,"=",s)

def sub(num1,num2):
    s=num1-num2
    print(num1,"-",num2,"=",s)
def mul(num1,num2):
    m=num1*num2
    print(num1,"*","num2","=",m)
def div(num1,num2):
    d=num1/num2
    print(num1,"/",num2,"=",d)
# def fdiv(num1,num2):
#     f=num1//num2
#     print(num1,"//",num2,"="f)

print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
while True:
    ch=int(input("enter choice"))
    num1=float(input("enter num1"))
    num2=float(input("enter num2"))
    if(ch>0):
        if(ch==1):
            add(num1,num2)
        elif(ch==2):
            sub(num1,num2)
        elif(ch==3):
            mul(num1,num2)
        elif(ch==4):
            div(num1,num2)
            break
        else:
            print("invalid choice")