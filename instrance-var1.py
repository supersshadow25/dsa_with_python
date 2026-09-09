class Student:
    def __init__(self):
        self.s_name = input("enter the name of the student")#instrance
        self.s_rollno = 101
    
    def getdata(self):
        self.s_mb = 2823833#instrance
    
obj = Student()
obj.getdata()
obj.s_branch ="CS"
del obj.s_rollno
print(obj.__dict__)