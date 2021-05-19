cyear=int(input("enter current year"))
cmonth=int(input("enter current month"))
cdate=int(input("enter current date"))
byear=int(input("enter birth year"))
bmonth=int(input("enter birth month"))
bdate=int(input("enter birth date"))
dyear=cyear-byear
dmonth=cmonth-bmonth
ddate=cdate-bdate
if(dyear>=0):
    if(dmonth>=0):
        if(ddate>=0):
            print("age:",dyear,"years",dmonth,"months",ddate,"days")
        elif(dmonth==0)&(ddate<0):
            print("invalid")
        else:
            dmonth=dmonth-1
            ddate=31+ddate
            print("age:",dyear,"years",dmonth,"months",ddate,"days")
    elif(dmonth<0):
        if(ddate>=0):
            if(dyear==0)&(dmonth<0):
                print("invalid dob")
            else:
                dyear=dyear-1
                dmonth=12+dmonth
                ddate=ddate
                print("age:",dyear,"years",dmonth,"months",ddate,"days")
        elif(dmonth<0)&(ddate<0):
             print("INVALID")
        else:
            dyear=dyear-1
            dmonth=dmonth+1
            dmonth=12+dmonth
            ddate=31+ddate
            print("age:",dyear,"years",dmonth,"months",ddate,"days")
    else:
        print("error")
else:print("Invalid DOB")