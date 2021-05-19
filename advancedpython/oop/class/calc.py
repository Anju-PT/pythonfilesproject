class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Sum::",self.num1+self.num2)
    def sub(self):
        print("Difference::",self.num1-self.num2)
    def mul(self):
        print("Mul::",self.num1*self.num2)
    def div(self):
        return self.num1/self.num2

while(True):
    print("______CALCULATOR______")
    print("1.Addition\n2.Subtractiuon\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter a choice:"))
    if(ch==5):
        break
    elif(0<ch<5):
        num1=int(input("Enter 1st no:"))
        num2=int(input("Enter 2nd no:"))
        ca=Calculator(num1,num2)
        if(ch==1):
            ca.add()
        elif(ch==2):
            ca.sub()
        elif(ch==3):
            ca.mul()
        elif(ch==4):
            print("Div::",ca.div())


    else:
        print("enter correct choice")
