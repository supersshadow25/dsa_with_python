#Write a program to accept student name and marks from the keyboard and creat
#a disctinoary.also display student marks by taking student as input?

n = int(input("enter the number of the students"))
d = {}

for i in range(n):
    name=input("enter the student name ")
    marks=input("enter students marks ")
    d[name]=marks
while True:
    name=input("enter the student name to get marks")
    marks=d.get(name,-1)
    if marks == -1:
        print("student not found")
    else:
        print("the marks of",name ,"are",marks)
    option = input("Do you want to find another student marks [YES / NO]")
    if option == "NO":
        break
print("Thanks for using the application")