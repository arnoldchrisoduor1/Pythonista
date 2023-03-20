#Take in a string
#Find the acronym
#convert them to uppercase

words = input("Give the words to create an acronym for : ")

print()

words = words.upper()

words = words.split()

for word in words:
    print(word[0],end="")
