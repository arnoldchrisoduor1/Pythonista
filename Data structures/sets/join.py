#joining sets using union.
print("Joining sets to create new using 'union'")
set1 = {"Oranges", "mangoes", "grapes"}
set2 = {1, 2, 3, 4}
print("set1: ",set1)
print("set2: ",set2)
set3 = set1.union(set2)
print("set3 : ",set3)

#using the update method also works.
#both the union and the update method ignore duplicate,
#items.

#keeping only the duplicate items.
print("\n")
print("Keeping only the duplicate items")
x = {"mangoes", "grapes", "onions", 3, 9}
y = {3, "onions", "lettuce"}
print("x: ",x)
print("y: ",y)
x.intersection_update(y)
print("After: ",x)
#intersection_update() updates the sets.
#intersection() creates a new set.

#Keeping all but not the updates
print("\n")
print("Keeping all but not the updates")
sett1 = {"onions", "grapes", "carrots", "stick", 4, 6}
sett2 = {1, 4, "grapes", "lettuce", "onions"}
print("sett1: ",sett1)
print("sett2: ",sett2)
sett1.symmetric_difference_update(sett2)
print("After: ",sett1)
#symmetric difference creates a new set.