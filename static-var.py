# depends on class itself if class ka name change toh poorra object 
#object ka name change..does not work on  object

class College:
    college_Name = "Sandip"  # static varible


obj1 = College()
obj2 = College()
obj3 = College()
print(obj1.college_Name)  # sandip
print(obj2.college_Name)
print(obj3.college_Name)
College.college_Name = "University"
print(obj1.college_Name)  # university
print(obj2.college_Name)
print(obj3.college_Name)
