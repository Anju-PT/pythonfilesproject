num=int(input("enter  num"))
rev=0
digit=0
while(num!=0):
     digit=num%10
     rev=(rev*10)+digit
     num=num//10
print(rev)
