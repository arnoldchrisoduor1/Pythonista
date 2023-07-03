#Reg Ex is a sequence of characters that form a search pattern.
import re

#searching for "the"
print()
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

#The findall() shows all occurrances of  the item.
print()
print("Using the 'findall()' function.")
txt = "This is the biggest rain that's ever rained in Spain"
y = re.findall("ai", txt)
print(y)
print()

#Searching for the first white space character in a string.
print("Searching for the first wite space character.")
bxb = "This is the text to be tested."
b = re.search("\s", bxb)
print("The first white space is at position: ",b.start())
print()

#the split() function returns a ist where the string,
#has been splait at each match.
print()
print("Using the 'split()' method.")
cxc = "This is another text that has to be tested"
c = re.split("\s", cxc)
print(c)
print()

#sub() to replace the matches with the text of your choice.
print()
print("Using the 'sub()' function")
nxn = "It rains in spain"
n = re.sub("\s","--", nxn)
#n = re.sub("\s","--", nxn,2) to replace the first 2 ocuurances.
print(n)

#Using the span() method to get a tuple for the start,
#and end of the part containing the match.
print()
print("Using the 'span()' method")
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
print("Printing the string passed into the function: ")
print(x.string)

#The group method to return part of the string where there was a match.
print()
print("Part of the string where there was a match.")
axa = "The rain is realy heavy in Spain."
a = re.search(r"\bS\w+", axa)
print(x.group())
print()