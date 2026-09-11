x,y,z = map(int, input().split())
mylist = []
for i in range(x):
    a = int(input())
    mylist.append(a)
for j in mylist:
    if j >= y and j <= z:
        print(j,end=' ')