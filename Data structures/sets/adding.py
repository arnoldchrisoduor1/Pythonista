#using the add() method
print("Adding items using the add method")

myset = {"orange", "mango", "carrot"}
print("initial: ",myset)
myset.add("roots")
print("After: ",myset)

#using the update() method
print("\n")
print("Adding using the update method")
thisset = {"grapes", "kales", "cabbages"}
print("Initial: ",thisset)
thisset.update(myset)
print("After: ",thisset)
#this method can be used with lists, dictionaries 
#and other data types.
