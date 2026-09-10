# s=[i*i for i in range(1,11)]
# print(s)

s = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# val=[2 ** i for i in range(1,6)]
# print(val)

# val2 = [i for i in  s if i%2==0 ]
# print(val2)

# squares ={x:x*x for x in range (1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

# how to read  multiple values from the keyboard in single line

# a,b = [int(x) for x in input("enter 2 numbers :").split()]
# print("product is :",a*b)

# a,b,c = [float(x)for x in input ("enter 3 float numbers :").split()]
# print("the sum is :",a+b+c)

# write a program to access each character of in forward and backward
# direction by using while loop

# s = "learning python is very easy!!!"
# n = len(s)
# print(n)
# i = 0
# print("forward direction \n ")
# while i<n:
#     print(s[i],end=' ')
#     i += 1

# print(" backward direction " )
# i = -1
# while i>=-n:
#     print(s[i],end=' ')
#     i = i - 1

# removing spaces from the string
#1. rstrip()===> to remove space at right side
#2. lstrip()===> to remove the space at left side
#3. strip()==> to remove spaces both sides

city = input("enter the city name")
scity = city.strip()
if scity == 'hydrabad':
    print("hello hyderbadi..adab")
elif scity == 'chennai':
    print("hello madrasi...vanakkam")
elif scity == 'bangalore':
    print("hello kannadiga..shubhodaya")
else:
    print("your entered city is invalid")

#replacing a string with another string
#s.replace(oldstring,newstring) inside s, every occurance of 
# ildstring will be replaced will be replaced with newstring.

s=""
s1=s.replace("difficult","easy")
print(s1)

s="abababababaab"
s1=s.replace("b","a")
print(s1)

v = ['a','e','i','o','u']
w = input ("enter the word where we will search the vowels")
found=[]
for i in w:
    if i in  v:
        if i not in found:
            found.append(i)
print('found vovels=',found)
print('unique vowels', len(found),'found the given word=',w)