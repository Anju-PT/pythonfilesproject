import re
n=input("enter")
x="(^a+[\w0-9\W]*b$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")