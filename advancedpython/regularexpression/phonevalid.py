num=input("enter a phone num")

import re
x="[+][9][1][789]\d{9}"
match=re.fullmatch(x,str(num))
if match is not None:
    print("valid-Indian no")
else:
    print("invalid")
