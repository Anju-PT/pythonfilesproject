#protected member

# class Base:
#     def __init__(self):
#         self._a=2#protected member
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)#calling constructor of base class
#         print("calling protected member of Base class::",self._a)
# obj1=Base()
# obj2=Derived()
# print(obj2.a)

#private member
class Base:
    def __init__(self):
        self.a="anju"
        self.__c="Panakkal"
        self.__c
class Derived:
    def __init__(self):
        Base.__init__(self)
        print("Calling private member of Base class:",self.__c)
obj1=Base()
print(obj1.a)
obj2=Derived()
print(obj2.__c)