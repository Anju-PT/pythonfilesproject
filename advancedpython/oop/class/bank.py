class Bank:
    bankname="Federal bank"


    def account(self,name,place,address,idno):
        self.name=name
        self.place=place
        self.address=address
        self.idno=idno
        self.minbalance=5000
        self.balance=self.minbalance
        # self.accno=1000
        print("---Account holder details--")
        print("",Bank.bankname,"\n",self.name,"\n",self.place,"\n",self.address,"\n",self.idno,"\n",self.balance,"\n")



    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        self.accno+=1
        print("your",Bank.bankname,"credited with amount",self.amount)
        print("ur current balance is",self.balance)



    def withdraw(self,amt):
        self.amt=amt
        if(self.amt>self.balance):
            print("insufficient balance")
        else:
            self.balance-=self.amt
            print("your", Bank.bankname, "debited with amount", self.amt)
            print("current balance :",self.balance)


b1=Bank()
b1.account("anju","Ernakulam","panakkal house","WHL1234")
b1.deposit(12000)
b1.withdraw(3000)
b2=Bank()
b2.account("anjus","Ernakulam","panakkal house","WHL234")
b2.deposit(1000)
b2.withdraw(4000)