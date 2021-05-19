lst=[10,20,30,40,50,60,70,80,90,100]

#len
#print(len(lst))
print("there are {0} items".format(len(lst)))

#sorted
ls=[6,7,3,9,10,5,4,2,1]
print(sorted(ls))
# ls=sorted(ls)
# st=0
# st=ls[::-1]
# print(st)

ls.sort(reverse=True)
print(ls)

words=["big","Blue","seven","glass","Green","anju","Antartica"]
print(sorted(words))
words.sort(key=str.lower)
print(words)

