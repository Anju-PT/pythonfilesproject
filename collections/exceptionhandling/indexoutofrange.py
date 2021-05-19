a=[1,2,3,4,5,6]
r = int(input("enter the index"))
try:
    print(a[r])
except:
    print("index out of range")
finally:
    print("inside finally")