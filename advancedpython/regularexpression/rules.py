#Rules
#1 # x="[abc]" either a or b or c
#2 # x="[^abc]" not abc
#3 # x="[a-z]" #from a to z(lowercase only)
#4 # x="[A-Z]" #from A to Z(uppercase only)
#5 # x="[a-zA-Z]" #from a to z and A to Z(uppercase and lowecase only)
#6 # x="[0-9]" #from 0 to 9
#7 # x="[^a-zA-Z0-9]" #special symbols only
#8 # x="\s" #space
#9 # x="\d" #digits
#10# x="\D" #except digits
#11# x="\w" #only words
#12# x="\W" #except characters

#quantifiers

# x="a+" #a including group
# x="a*" #count including 0 number of a
# x="a?" #count a as each including 0 number of a
# x="a{2}" #no of position(only consider group of 2 a ie aa)
# x="a{1,3}" #minimum 2 maximum 3 a
# x="^a" # check string is starting with a
# x="a$" #check ending with a

