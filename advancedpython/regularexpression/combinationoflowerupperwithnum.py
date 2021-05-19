import re
n=input("enter:")
x="[a-zA-Z]+\d{1}$"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")