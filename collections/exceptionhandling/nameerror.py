try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("something elsewent wrong")