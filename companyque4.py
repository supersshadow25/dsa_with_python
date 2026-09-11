# Choose two cards. To win the game, the product of the values of the two cards must be the
# maximum value possible for any pair of cards in the display. The winning amount will be the sum
# of the two cards chosen by the player.

# Write an algorithm to find the winning amount as the sum of the values of the two cards whose
# product value is maximum.

# Input

# The first line of the input consists of an integer numCards, representing the number of cards (N).
# The second line consists of N space-separated integers - val1, val2, ..., valN representing
# the values on the cards.

# Output

# Print an integer representing the sum of the values of the two cards whose product value is
# maximum.


mylist = [7,9,-3,8,-6,-7,8,10]
max2=0
large = 0
for i in  range (0,len(mylist)-1):
    max = mylist[i]
    for j in range (0,len(mylist)):
        max2 = max*mylist[j]
        if max2 > large:
            large = max2
            num1 = max
            num2 = mylist[j]
print(large)
print( num1 + num2)
