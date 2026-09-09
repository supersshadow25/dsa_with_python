word1 = input("enter word 1")
word2 = input("enter word 2")

if len(word1) != len(word2):
    print("not anagram")
else:
    for i in word1:
        if word1.count(i) != word2.count(i):
            print("not anagram")
            break
    else:
        print("anagram")
