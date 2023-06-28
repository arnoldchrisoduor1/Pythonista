#getting the model
thisdict = {
    "model" : "Mustang",
    "brand" : "ford",
    "year" : 1998
}
x = thisdict["model"]
print(x)

#using the get method
print("\n")
print("Using the get method")
n = thisdict.get("brand")
print(x)

#returning all the keys
print("\n")
print("Getting all the keys")
m = thisdict.keys()
print(m)

#adding item to the dictionary
print("\n")
print("Adding a new key to the dictionary")
b = thisdict.keys()
print(b)
thisdict["color"] = "white"
d = thisdict.keys()
print(d)

#getting the value
print("\n")
print("Adding the value")
b = thisdict.values()
print("Initial: ",b)
thisdict["Repairs"] = "None"
d = thisdict.values()
print("After: ",d)

#items() method will return each item in the dictionary,
#as list of tuples
print("\n")
print("items method to get items in dict")
thisdict["color"] = "Green", "red"
v = thisdict.items()
print(v)

#updating items in the dictionary
print("\n")
print("Updating items in the dictionaries")
print("Initial: ",thisdict)
thisdict.update({"year": 2020})
print("After:", thisdict)
#this can also be used to add items into the dictionary.