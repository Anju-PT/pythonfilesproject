lst=[1,2,3,4,5]
try:
    print(lst[0])
    print(lst[6])

except IndexError as e:
    print(e)
try:
    print(lst[1])
    print(lst['2'])
except TypeError as e:
    print(e)