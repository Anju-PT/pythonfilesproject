pattern="ABCABC"
dic={}
for char in pattern:
    if(char not in dic):
        dic[char]=1
    else:
        print("first recursive character",char)
        break: