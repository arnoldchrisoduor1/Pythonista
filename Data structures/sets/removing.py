#removing items from a set, the remove() method
print("Removing items from a set")
myset = {"mangoes", "grapes", "apples"}
print("Initial: ",myset)
myset.remove("grapes")
print("After:", myset)
#if items do not exist the remove will raise an error.

#using the discard() function.
print("\n")
print("Using the discard function")
thisset = {"audi", "mercedes", "bmw"}
print("initial : ",thisset)
thisset.discard("bmw")
print("After: ",thisset)
#This will NOT raise an error if not present.

#using pop
print("\n")
print("Pop removes a random item")
nset = {"ugali", "chapo", "beans"}
print("Initial set: ",nset)
x = nset.pop()
print("Popped value: ", x)
print("New set: ",nset)

#clear method to empty the set.
print("\n")
print("using the clear method to empty the set")
mset = {"chair", "table", "seats", "desk"}
print("Initial: ",mset)
mset.clear()
print("After: ",mset)

#del deletes the set completely.
print("\n")
print("Deleting the entire set")
jset = {"great", "excellent", "honorary"}
print("Initial: ",jset)
del jset
print("After: jset is not defined")