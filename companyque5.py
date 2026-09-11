# A company wishes to provide cab service for their N employees. The employees have distance
# ranging from 0 to N-1. The company has calculated the total distance from an employee's
# residence to the company, considering the path to be followed by the cab is a straight path. The
# distance of the company from itself is 0. The distance for the employees who live to the left side
# of the company is represented with a negative sign. The distance for the employees who live to
# the right side of the company is represented with a positive sign. The cab will be allotted a range
# of distance. The company wishes to find the distance for the employees who live within the
# particular distance range.

# Write an algorithm to find the distance for the employees who live within the distance range.

# Input

# The first line of the input consists of three space-separated integers - num, start and end
# representing the size of the list (N), the starting value of the range, and the ending value of the
# range respectively. The second line of the input consists of N space-separated integers
# representing the distances of the employees from the company.

# Output

# Print space-separated integers representing the distance for employees whose distance lies
# within the given range. Else return -1.

# C



x, y, z = map(int, input().split())

mylist = []

for i in range(x):
    a = int(input())
    mylist.append(a)


for j in mylist:
    if j >= y and j <= z:
        print(j, end=' ')

