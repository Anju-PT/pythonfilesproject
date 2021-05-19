employees=[{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
             {"eid":1001,"name":"vjay","salary":22000,"designation":"developer"},
             {"eid":1002,"name":"arun","salary":26000,"designation":"quality"},
             {"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
             {"eid":1004,"name":"ram","salary":20000,"designation":"marketing"}]

# emp_name=list(map(lambda emp:emp["name"],employees))
# print(emp_name)
# emp_sal=list(map(lambda emp:emp["salary"],employees))
# print(emp_sal)
# emp_developer=list(filter(lambda emp:emp["designation"]is"developer",employees))
# print(emp_developer)
#name of developers
# developers=list(filter(lambda emp:emp["designation"]=="developer",employees ))
# #developer_name=list(map(lambda emp:emp["name"],developers))
# developer_name=list(map(lambda emp:emp["name"],list(filter(lambda emp:emp["designation"]=="developer",employees ))))
# print(developer_name)

#print employee names only
e_name=[emp["name"] for emp in employees]
print(e_name)
#developer details
d_details=[emp for emp in employees if emp["designation"]=="developer"]
print(d_details)
d_name=[emp["name"] for emp in employees if emp["designation"]=="developer"]
print(d_name)
highest_sal=max([emp["salary"] for emp in employees])
print(highest_sal)

