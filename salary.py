rating = float(input())
salary = float(input())
increment = 0
if rating >= 1 and rating  <=3:
    increment = salary*10/100
elif rating >= 3.1 and rating <=4:
    increment = salary*20/100
elif rating >= 4.1 and rating <= 5:
    increment = salary*30/100
else:
    print("invalid rating")
print(salary)
print(rating)
print(increment)
print("increased salary",salary+increment)