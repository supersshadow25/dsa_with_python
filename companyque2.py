# You are playing an online game. In the game, a list of N numbers is given. 
# The player has to arrange the numbers so that all the odd numbers of the list come after the even numbers. 
# Write an algorithm to arrange the given list such that all the odd numbers of the list come after the even numbers.

# Input

# The first line of the input consists of an integer num, 
# representing the size of the list (N).

# The second line of the input consists of N space-separated integers
# representing the values of the list.

# Output

# Print N space-separated integers such that all the odd numbers of
# the list come after the even numbers.

N = 8
mylist = []
for  i in range(N):
    val = int(input('enter the value'))
    mylist.append(val)
print(mylist)
A = []
B = []
for i in range (len(mylist)):
    if mylist[i]%2 == 0:
        A.append(mylist[i])
    else:
        B.append(mylist[i])
print(A+B)