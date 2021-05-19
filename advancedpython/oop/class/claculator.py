class Calc:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    # def setval(self,num1,num2):
    #     self.num1 = num1
    #     self.num2 = num2
    def add(self):
        print("sun=",self.num1+self.num2)
    def sub(self):
        print("sub=",self.num1-self.num2)
    def mul(self):
        print("mul=",self.num1*self.num2)
    def div(self):
        print("div=",self.num1/self.num2)
    def floor(self):
        print("floordiv=",self.num1//self.num2)
    def expo(self):
        self.s=1
        for i in range(0,self.num2):
            self.s=self.s*self.num1
        print("exponent=",self.s)
# c1=Calc()
while(True):
    print("\n---------CALCULATOR__________")
    print(" 1.Adiition\n","2.Subtraction\n","3.Multiplication\n","4.Division\n","5.Floor Division\n","6Exponent\n","7.Exit")
    ch=int(input("select choice::"))

    if(ch==7):
        break
    elif(0<ch<=7):

        a=int(input("Enter num1:"))
        b=int(input("Enter num2:"))
        c1=Calc(a,b)
        if(ch==1):
            c1.add()
        elif(ch==2):
            c1.sub()
        elif(ch==3):
            c1.mul()
        elif(ch==4):
            c1.div()
        elif(ch==5):
            c1.floor()
        elif(ch==6):
            c1.expo()
    elif(ch>7):
        print("Invalid choice")
    else:

            print("please enter a positive num")

#
# a=int(input("Enter num1:"))
# b=int(input("Enter num2:"))
# c1=Calc()
# c1.setval(a,b)
# c1.add()
# c1.sub()