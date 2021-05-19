# import re
# n="hello"
# x="\w*[^0-9]"
# match=re.fullmatch(x,n)# take the full string
# if match is not None:
#     print("Valid")
# else:
#     print("Invalid")

import re
n="45kg"
x="\d{2}[a-z]{2}"
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")