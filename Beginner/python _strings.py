#Printing multiple strings
a = """
This is the first line of the text.
This is the second line of the text
This is the third line of the text.
This is the fourth line of the text.
"""

print(a)

#looping through a string
print("Lets loop through a string")

for x in "Banana":
    print(x)


#lets find the length of a string
print("Finding the length of a string")
x = "Findinglength"

print(len(x))

#Lets find a word in a string
print("Finding words in a string")
ntxt = "Good fruits are free, better fruits are paid for."

if "free" in ntxt:
    print("Yes, there is a free variety")

if "expensive" not in ntxt:
    print("There are no expensive fruits in the collection")

print("\n")
print("Removing white space from a string")
mtxt = " Hellow world."
print("Initial: ",mtxt)
print("Updated: ",mtxt.strip())

#splitting words by detecting a separator
print("\n")
print("Splitting a string")
stxt = "Hello, world!"
print("Initial: ",stxt)
print("Updated: ",stxt.split())

#text formatting
print("\n")
print("String formatting")
item = "Meat"
weight = 9
dtxt = "I want {} pounds of {} to go!"
print(dtxt.format(weight, item))