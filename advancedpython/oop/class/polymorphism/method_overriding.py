#method overriding
#same methodname same parameters and child class method over ride parent class method
# class Parent:
#     def bride(self):
#         print("anju marry")
#     def marry(self):
#         print("Athul")
# class Child(Parent):
#     def marry(self):
#         print("akhil")
# ch=Child()
# ch.marry()

class Parent:
    def num(self,num):
        self.num=num
        print("inside parent class:",self.num)
class Child(Parent):
    def num(self,num):
        self.num=num
        print("inside child class:",self.num)
ch=Child()
ch.num(2)