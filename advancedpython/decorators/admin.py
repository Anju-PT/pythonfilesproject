def admin_required(func):
    def wrapper(user,pin):
        if user!="admin":
            raise Exception("u are not allowed")
        else:
            return func(user,pin)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_account(user,accno):
    return str(accno)+"deleted"


print(change_pin("admin",1000))
try:
    print(delete_account("user",1000))
except Exception as e:
    print(e.args)
print(delete_account("admin",1000))
try:
    print(change_pin("user",1000))
except Exception as e:
    print(e.args)
