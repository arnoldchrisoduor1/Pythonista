mylist = ["cherry", "apples", "oranges", "grapes", "carrots"]

for x in mylist:
    print(x)

#looping through the range method
print("\n")
print("Looping through range")
for i in range(len(mylist)):
    print(mylist[i])

#looping through the while loop.
print("\n")
print("Looping the list using the while loop")
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

#using loop comprehensions
print("\n")
print("Printing using loop comprehensions")
[print(x) for x in mylist]

#apending using list comprehensions
print("\n")
print("Appending to new list with list comprehesions")
print("initial : ",mylist)
newlist = [x for x in mylist if "a" in x]
print(newlist)

#creating a new iterable
print("\n")
print("Creating a new iterable")
thislist = [x for x in range(10) if x < 5]
print(thislist)

#manipulating items before adding to list
print("\n")
print("Manipulating items before adding to list")
print("initial : ",mylist)
newlist.clear()
newlist = [x.upper() for x in mylist]
print(newlist)

#changing the value of all the items in the list to another item
print("\n")
print("Changing all the items in the list")
print("initial : ",mylist)
newlist = ['item' for x in mylist]
print(newlist)

#conditional expressions
print("\n")
print("Conditional expressions")
print(mylist)
thelist = [x if x != 'oranges' else 'mango' for x in mylist]
print(thelist)