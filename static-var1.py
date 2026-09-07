class College:
    collegename= "Mordern College" #static varible
    def __init__(self):
        self.studentname = "sumeet" #instrace varibale (3 seperate memory)

principal = College()
teacher = College()
accountant = College()
print("principal=",principal.collegename,"....",principal.studentname)
print("teacher=",teacher.collegename,"....",teacher.studentname)
print("accountant=",accountant.collegename,"....",accountant.studentname)

College.collegename ="HBD" #second way to add static varible
principal.studentname ="singh"

print("principal",principal.collegename,"|",principal.studentname)
print("teacher",teacher.collegename,"|",teacher.studentname)
print("accountant",accountant.collegename,"|",teacher.studentname)