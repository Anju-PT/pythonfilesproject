import re
x="[+][9][1]\d{10}"
f=open("phonenum","r")
f1=open("validphonenum","a")
for lines in f:
    ln=lines.rstrip("\n")
    match = re.fullmatch(x, str(ln))
    if match is not None:
        print(ln,"is valid-Indian no")
        f1.write(ln)
    else:
        print(ln,"is invalid")


