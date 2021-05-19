s="Hello::{ wo;rld?>"
b=",./;'[]():<>?{}@#!$%^&*+-_"
c=""
for i in s:
    if i not in b:
        c+=i
print("string without punctuation:",c)