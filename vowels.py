name = "apple"

vowels = ['a','e','i','o','u','A','E','I','O','U']
vowels_count = 0
consonent_count = 0
for i in name:
    if i in vowels:
        vowels_count+= 1
    else:
        consonent_count +=1
print( vowels_count)
print(consonent_count)
        