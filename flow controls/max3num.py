num1=int(input("enter 1st num"))
num2=int(input("enter 2nd num"))
num3=int(input("enter 3rd num"))
if((num1>num2)&(num1>num3)):
    print(num1,"is higher")
elif((num2>num1)&(num2>num3)):
    print(num2,"is higher")
elif((num3>num1)&(num3>num2)):
    print(num3,"is higher")
else:
    print("equal")