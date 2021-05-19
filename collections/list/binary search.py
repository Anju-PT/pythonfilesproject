#Binary search

#lst=[2,4,7,1,5]

#1.sort the given array
#lst=[1,2,4,5,7]

#2.declare 2 variable lower & upper

#low=0

#upper=len(lst-1)

#3.calculate mid
#mid=low+upper//2 (0+4//2=2)

#3 conditions

#if element to be serched greater than change low as mid+1
#if(elemet>lst[mid])
#1.low=mid+1

#.if element is less than mid then upper chaged to mid-1
#if(elemnt<lst[mid])
#2.upper=mid-1

#if the element is equal to mid print elemnt found
#if(elemnt==lst[mid])
#3element=lst[mid] print("element found")



