list = [[100, 198, 333, 323],
[122, 232, 221, 111],
[223, 565, 245, 764]]

newList = []
for i in range(3):
    max = list[i][0]
    for j in range(4):
        c_max = list[i][j]
        if max < c_max:
            max = c_max
    newList.append(max) 
print(newList)