f=open("datas","r")
f1=open("copy1","w")
for data in f:
    # data=lines.rstrip("\n")
    f1.write(data)
    f1.write("\n")
print(f1)
