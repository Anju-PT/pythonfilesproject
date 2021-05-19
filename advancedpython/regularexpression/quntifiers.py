#rule1
#_____
# import re
# x="a+" #a including group
# r="aaa abc aaaa bca"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule2
#_____
# import re
# x="a*" #count including 0 number of a
# r="aaa abc aaaa bca"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


#rule3
#_____
# import re
# x="a?" #count a as each including 0 number of a
# #count including 0 number of a without group
#
# r="aaa abc aaaa bca"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


#rule4
#_____
# import re
# x="a{2}" #no of position(only consider group of 2 a ie aa)
# r="aaa abc aaaa bca"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule5
#_____
# import re
# x="a{1,3}" #minimum 2 maximum 3 a
# r="aaa abc aaaa aa bca"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())

#rule6
#_____
# import re
# x="^a" # check string is starting with a
# r="aaa abc aaaa aa bca"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#rule7
#_____
# import re
# x="a$" #check ending with a
# r="aaa abc aaaa aa bca"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())


import re
x="a\s" #check ending with a
r="aaa abc aaaa aa bca"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())