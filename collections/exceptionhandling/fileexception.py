try:
    f=open("demofile1")
    f.write("anju")
    print(f)
except:
    print("something went wrong when writing to the file")
finally:
    f.close()