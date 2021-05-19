class Vehicle:
    def setval(self,name,type,manufact,year):
        self.name=name
        self.type=type
        self.manufact=manufact
        self.year=year
    def printval(self):
        print("Vehicle Name         ::",self.name)
        print("Vehicle Type         ::",self.type)
        print("Manufacturer         ::",self.manufact)
        print("Year of Manufacturing::",self.year)
class Bus(Vehicle):
    def set(self,regnum,owner):
        self.regnum=regnum
        self.owner=owner
    def print(self):
        print("Registration number::",self.regnum)
        print("Owner Nwme         ::",self.owner)

b1=Bus()
b1.setval("Bus","Heavy","TATA",2020)
b1.printval()
b1.set("KL7AT2567","Anju P.T")
b1.print()