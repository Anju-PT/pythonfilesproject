numclass=int(input("enter the number of class held"))
attend=int(input("enter the number of class attend"))
percent=(attend/numclass)*100
print("Percentage is:",percent)
if(percent<75):
    print("student not allowed to attend exam")
else:
    print("student allowed to attend exam")