import re
n= input("enter:")
x="([K][L][0-9]{2}[A-Z]{2}[0-9]{4}$)"
match=re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("valid")