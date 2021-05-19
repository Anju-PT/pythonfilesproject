# f=open("sample","r")#different location copy absolute path,
# for lines in f:
#     print(lines)
# f=open("C:\Users\user\Downloads\sample3")
# for lines in f:
#     print(lines)
fname="C:\Downloads\sample3"
# if os.path.isfile(fname):
#     print("found file '{}'".format(fname))
with open(fname,'r') as f:
    for line in f:
        print(line)