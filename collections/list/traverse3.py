lst=[1,2,3,4,5,6,7,8]
print(list(enumerate(lst)))
for e,i in enumerate(lst):
    print("n[{0}]={1}".format(e,i))