# Encode as Number

# Description

# A company wants to encode its data. The data is in the form of a number. They wish to encode
# the data with respect to a specific digit. They wish to count the number of times the specific digit
# occurs and so give data so that they can encode the data accordingly. Write an algorithm to
# find the number of the specific digit in the given data.

# Input

# The first line consists of two space-separated integers, data and d, representing the data to be
# encoded and the digit to be counted in the data.

# Output

# Print the number of times the digit d is present in the given data.

mylist = [5,7,2,3,7,8,2,3,3]
newdict={}

for i in range(len(mylist)):
    count = 0
    key = mylist[i]
    j = 1
    while j < len (mylist):
        if key == mylist[j]:
            count += 1
        j = j+1
    if count > 1:
        newdict[key] = count
        
max = newdict
print(max)