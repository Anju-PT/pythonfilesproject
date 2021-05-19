#regular expression
#patternmatching
#re package is used
#
# import re
#
# count=0
# matcher=re.finditer("ab","abbabaab")
# #print(matcher)
# for match in matcher:
#     count+=1
# print("count=",count)

#start() :position
#group(): which group or onject find match

import re

count=0
matcher=re.finditer("ab","abbabaab")
#print(matcher)
for match in matcher:
    print("match available at:",match.start())#return position
    print("group:",match.group())#return the object searched
    count+=1
print("count=",count)