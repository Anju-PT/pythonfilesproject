import re


user=input("Enter a username  ::")
x="[A-Z][a-z]{7}"
match=re.fullmatch(x,user)
f=open("username_password","a")
if match is not None:
    # print("valid username")
    user2=input("Confirm Username  ::")
    if(user==user2):
        passw=input("Enter the Password::")
        y="[a-zA-Z][0-9]{7}[^a-zA-Z]"
        mat=re.fullmatch(y,passw)
        if mat is not None:
            passw2=input("Confirm Password  ::")
            if (passw==passw2):
                f.write("\n")
                f.write(user2)
                f.write(",")
                f.write(passw2)
            else:
                print("enter same password as above")

        else:
            print("invalid password")


    else:
        print("enter the same username as above")
else:
    print("Invalid user name")
