#finally block is always executed after the try statement
a=[1,2,3,4]
r = int(input("enter the index"))
try:
    print(a[r])
except:
    print("index out of range")
finally:
    print("inside finally")