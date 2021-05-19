#Rules
#x="[abc]" either a or b or c
#x="[^abc]" not abc

#rule1
#------
# import re
#
# x="[abc]" #either a or b or c
# matcher=re.finditer(x,"ab yca845>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule2
#------
# import re
#
# x="[^abc]" #neither a or b or c
# matcher=re.finditer(x,"ab yca845>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule3
#------
# import re
#
# x="[a-z]" #from a to z(lowercase only)
# matcher=re.finditer(x,"ab yca845A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule4
#------
# import re
#
# x="[A-Z]" #from A to Z(uppercase only)
# matcher=re.finditer(x,"ab ySca845A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule5
#------
# import re
#
# x="[a-zA-Z]" #from a to z and A to Z(uppercase and lowecase only)
# matcher=re.finditer(x,"ab ySca845A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
#rule6
#------
# import re
#
# x="[0-9]" #from 0 to 9
# matcher=re.finditer(x,"ab ySca845A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule7
#------
# import re
#
# x="[^a-zA-Z0-9]" #special symbols only
# matcher=re.finditer(x,"ab ySca8@45A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule8
#------
# import re
#
# x="\s" #space
# matcher=re.finditer(x,"ab ySca8@45A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule9
#------
# import re
# x="\d" #digits
# matcher=re.finditer(x,"ab ySca8@45A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule10
#------
# import re
# x="\D" #except digits
# matcher=re.finditer(x,"ab ySca8@45A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())


#rule11
#------
import re
x="\w" #only words
matcher=re.finditer(x,"ab ySca8@45A>")
for match in matcher:
    print(match.start())
    print(match.group())

# #rule12
# #------
# import re
# x="\W" #except characters
# matcher=re.finditer(x,"ab ySca8@45A>")
# for match in matcher:
#     print(match.start())
#     print(match.group())