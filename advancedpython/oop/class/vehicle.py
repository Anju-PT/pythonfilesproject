class Vehicle:
    def name(self,name,type):
         self.name=name
         self.type=type
         print("vehicle Details:",self.name,",",self.type)

p1=Vehicle()
p1.name("Bus","Heavy")
p2=Vehicle()
p2.name("Car","4 WHLR")
p3=Vehicle()
p3.name("Bike","2WHLR")
p4=Vehicle()
p4.name("Lorry","Heavy")