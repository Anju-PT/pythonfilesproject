employees={1000:{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
             1001:{"eid":1001,"name":"vjay","salary":22000,"designation":"developer"},
             1002:{"eid":1002,"name":"arun","salary":26000,"designation":"quality"},
             1003:{"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
             1004:{"eid":1004,"name":"ram","salary":20000,"designation":"marketing"}}
# def print_employee(**kwargs):
#     # print(kwargs)
#     for k,v in kwargs.items():
#         if v in employees:
#             s=v
#             print(employees[v]["name"])
#         for p,r in employees.items():
#             if(p==s):
#                 if v in r:
#                     print(v,"=>",r[v])
#
#
# print_employee(id=1002,no="eid",sal="salary",desi="designation")

def print_employee(**kwargs):
    id=kwargs["id"]
    prop=kwargs["prop"]
    # print(prop)
    if id in employees:
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("invalid id")

print_employee(id=1003,prop="salary")