class Swift:
    def start(self):
        print("Swift car starts")

    def accelerate(self):
        print("Swift car accelerating functionally")

    def breaks(self):
        print("Swift car break method")

    def stop(self):
        print("Swift car stopping")

class Seltos:
    def start(self):
        print("Seltos car starts")

    def accelerate(self):
        print("Seltos car accelerating functionally")

    def breaks(self):
        print("Seltos car break method")

    def stop(self):
        print("Seltos car stopping")

class Person:
    def drive(self,car):
        car.start()
        car.accelerate()
        car.breaks()
        car.stop()
pe=Person()
sw=Swift()
se=Seltos()
pe.drive(sw)
pe.drive(se)