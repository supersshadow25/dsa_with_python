# instrance varible depends on object of a class


class Employee:
    def __init__(self):
        self.name = "sumeet"  # instrance varibale


obj1 = Employee()  # sumeet
obj2 = Employee()  # sumeet
obj3 = Employee()  # sumeet
print(obj1.name)
print(obj2.name)
print(obj3.name)
obj2.name = "singh"
obj3.name = "bca"
print(obj2.name)
print(obj3.name)
