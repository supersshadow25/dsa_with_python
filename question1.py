# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a ', 'b')
# print(init_tuple_a == init_tuple_b)


# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
# print(init_tuple_a + init_tuple_b)

# l = [1,2,3]
# init_tuple = ('python',)*(l.__len__()-1[::-1][0])
# print(init_tuple)

# init_tuple = ('python',)*3 #if comma waas not present then it is a list
# print(type(init_tuple))

# init_tuple = (1,)*3
# init_tuple[0] = 2
# print(init_tuple)

# init_tuple = ((1, 2),) * 7
# print(len(init_tuple[3:8]))  # pairs count karna hai index nhi

sumeet*is*good*programmer

# word = 'sumeet*is*good*programmer'
# newword =''
# val =''
# for i in  word:
#     if i !='*':
#         newword += i
#     else:
#         val += i
#     print(newword)
#     print(str(val+newword))

word = 'aabbbbeeeeffggg'
newword = ''

count = 1

for i in range(len(word)):
    if i + 1 < len(word) and word[i] == word[i + 1]:
        count += 1
    else:
        newword += word[i] + str(count)
        count = 1

print(newword)
