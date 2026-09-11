# The garments company Apparel wishes to open outlets at various locations. 
# The company shortlisted several plots in these locations and wishes to select only plots that are square-shaped.

# Write an algorithm to help Apparel find the number of plots that it can select for its outlets.

# Input

# The first line of the input consists of an integer number of plots, representing 
# the number of plots shortlisted by the company for outlet N.

# The second line consists of N space-separated integers - area1, area2, ..., 
# areaN representing the area of the N plots selected for outlets


N = int(input())

mylist = []

for i in range(N):  
    a = int(input())
    mylist.append(a)

for i in range(1,N+1):
    square = i*i
    if square in mylist:

        print(square)