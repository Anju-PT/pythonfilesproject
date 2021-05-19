num1=int(input("Enter 1st num"))
num2=int(input("enter 2nd num"))
num3=int(input("enter 3rd num"))
# if(num1<num2<num3)|(num3<num2<num1):
#     print("second largest num is",num2)
# elif(num2<num1<num3)|(num3<num1<num2):
#      print("second largest num is", num1)
# elif (num1<num3<num2)|(num2<num3<num1):
#      print("second largest num is", num3)
# else:
#     print("same numbers")

#nested if

if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2,"second largest")
    else:
        print(num3,"second largest")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print(num1,"second largest")
    else:
        print(num3,"second largest")
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print(num1,"second largest")
    else:
        print(num2,"second largest")
else:
    print("same numbers")