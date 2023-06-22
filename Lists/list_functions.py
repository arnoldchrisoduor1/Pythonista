mylist = ["apple", "mangoes", "cherry", "mellons", "grapes"]

if "apple" in mylist:
    print("Apples is present in the list of fruits")

#change the items in the list
print("Before the chnages: ",mylist)
mylist[0] = "carrots"
print("After changes: ",mylist)

#changing a group of values
print("\n")
print("Chnaging a group of list values")
print("Before making the changes: ",mylist)
mylist[1:3] = ["bananas", "pears"]
print("After making major changes: ",mylist)

#inserting an item without replacing
print("\n")
print("Inserting a new item into the list")
print("Before any changes: ", mylist)
mylist.insert(2,"watermelons")
print("After the changes: ",mylist)

#appending an item to the list
print("\n")
print("Appending an item to the list")
print("Initial : ",mylist)
mylist.append("oranges")
print("After : ",mylist)

#extending the list with items from another list
print("\n")
print("Extending the list with items from anothe list")
print("Initial : ",mylist)
vegies = ["kales","greens","cabbages"]
mylist.extend(vegies)
print("After : ",mylist)
#It can also extend tuples,sets, dictionaries etc.

#removing items from the list
print("\n")
print("Removing items from the list")
print("Initial : ",mylist)
mylist.remove("oranges")
print("After : ",mylist)

#pop function removes the last item or the specified index
print("\n")
print("Using the pop function")
print("Initial : ",mylist)
mylist.pop(1)
print("After : ",mylist)
#use del mylist to delete entire list
#clear() clears the entire list - exists with nothing in it.


