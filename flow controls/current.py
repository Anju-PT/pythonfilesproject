#year
#month
#date
#birth year
#month
#date
#print year
cyear=int(input("enter current year"))
cmonth=int(input("enter current month"))
cdate=int(input("enter current date"))
byear=int(input("enter birth year"))
bmonth=int(input("enter birth month"))
bdate=int(input("enter birth date"))
dyear=cyear-byear
dmonth=cmonth-bmonth
ddate=cdate-bdate
if(dyear>=1):
    if(dmonth>=0):
        if(ddate>=0):
            print("age:",dyear,"years",dmonth,"months",ddate,"days")
        else:
            dmonth=dmonth-1
            ddate=31+ddate
            print("age:",dyear,"years",dmonth,"months",ddate,"days")
    elif(dmonth<0):
        if(ddate>=0):
            dyear=dyear-1
            dmonth=12+dmonth
            #ddate=ddate
            print("age:",dyear,"years",dmonth,"months",ddate,"days")
        else:
            dyear=dyear-1
            dmonth-=1
            dmonth=12+dmonth
            ddate=31+ddate
            print("age:",dyear,"years",dmonth,"months",ddate,"days")

    else:
        print("error")
elif(dyear==0):
    if(dmonth<=0):
        if(ddate<=0):
            print("error")
        else:
            print(dyear,"years",dmonth,"months",ddate,"days old")
    elif(dmonth>0):
        if(ddate<=0):
            dmonth=dmonth-1
            ddate=31+ddate
            print(dyear,"years",dmonth,"months",ddate,"days")
        else:
            print(dyear,"years",dmonth,"months",ddate, "days")
    else:
        print("error")
else:
    print("invalid  date of birth")