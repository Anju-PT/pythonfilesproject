class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print("sum:",self.num1+self.num2)
a1=Addition()
a=int(input("enter num1"))
b=int(input("enter num2"))
a1.add(a,b)