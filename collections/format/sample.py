quantity=3
itemno=567
price=49
# txt="the price is {} dollars"
# txt="the price is {:.2f} dollars"
# myorder="I want {} pieces of item number{} for {:.2f} dollars"
myorder="I want {0} pieces of item number {1} for {2:.2f} dollars"
# print(txt.format(price))
print(myorder.format(quantity,itemno,price))