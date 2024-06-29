class Base:
    def method(self):
        print("Base class method called")


class Derived(Base):
    def method(self):
        print("Derived class method called")


obj1 = Derived()
obj1.method()
