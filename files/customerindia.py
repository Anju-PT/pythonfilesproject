f=open("E:\customer","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    # print(data)
    # if(data[-1]=="india"):
    #     name=data[1]
    #     age=data[3]
    #     cou=data[5]
    #     print(name,",",age,",",cou)
    # if(int(data[3])>50):
    #     name=data[1]
    #     age=data[3]
    #     cou=data[-1]
    #     print(name,",",age,",",cou)
    if(data[4]=="Doctor"):
        name=data[1]
        age=data[3]
        pro=data[4]
        cou=data[-1]
        print(name, ",", age, ",",pro,",",cou)
